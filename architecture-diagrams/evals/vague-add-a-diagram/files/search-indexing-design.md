# Design: Incremental search indexing

**Author:** Tomas · **Status:** draft

## Background
Our product search runs on an Elasticsearch cluster that is rebuilt from scratch every night by a cron job in the `catalog` monolith. The full rebuild takes ~4 hours, so price and stock changes made during the day are invisible in search until the next morning. Merchandising has asked for changes to appear within 5 minutes.

## Proposal
Keep the nightly full rebuild as a safety net, and add an incremental path:

- The `catalog` monolith already emits `ProductUpdated` events to a RabbitMQ exchange (used today by the recommendations team).
- A new `search-indexer` service (Python) subscribes to that exchange, fetches the full product document from the catalog's internal REST API, transforms it into the search document shape, and writes it to Elasticsearch with `op_type=index` keyed on product id, so repeated events for the same product are safe.
- Indexing errors go to a dead-letter queue; an on-call runbook describes replaying it.
- The storefront keeps querying Elasticsearch through the existing `search-api` (Go) unchanged.

Events can arrive out of order when the monolith retries; we handle that by including the product's `updated_at` as the document version and letting Elasticsearch reject stale writes (`version_type=external`).

## Open questions
- Should `search-indexer` be part of the `search-api` deployment or its own?
- How do we backfill if the service is down for more than the exchange's TTL (24h)?
