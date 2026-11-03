# Design: Notification Service

**Author:** Priya (Growth Platform team) · **Status:** draft · **Reviewers:** Growth Platform, Mobile, SRE

## Problem
Today each product team sends push and email notifications directly from its own service using the SendGrid and Firebase Cloud Messaging (FCM) SDKs. There is no rate limiting per user, no quiet-hours handling, and no unified opt-out. Marketing wants campaign sends of up to 2M messages in under 30 minutes; Support wants a single place to see what a user was sent.

## Proposal
Introduce a Notification Service owned by Growth Platform. Product services (Orders, Billing, Social) call it over gRPC with a `SendNotification` request (user id, template id, payload). The service:

- looks up the user's channel preferences and quiet hours in a new Preferences store (PostgreSQL);
- enqueues the message on a Kafka topic `notifications.v1` and returns immediately with a notification id;
- a pool of Delivery Workers consume the topic, render the template, and call FCM or SendGrid;
- delivery results are written to a Delivery Log (PostgreSQL, partitioned by month) and exposed to Support through an internal admin UI (React) via the existing Admin Gateway.

Campaign sends come from the Marketing team's existing Campaign Tool, which will call the same gRPC API in batches of 1,000.

Idempotency: callers pass an idempotency key; duplicates within 24h are dropped.
Retries: FCM/SendGrid failures retry 3 times with exponential backoff; after that the message is marked FAILED and an alert fires if the failure rate exceeds 2% over 5 minutes.

## Non-goals
SMS, in-app inbox, A/B testing of templates.

## Architecture
TODO — diagrams go here. Priya said "I'll add some boxes and arrows".

## Rollout
Shadow mode for Orders first, then Billing, then Social. Marketing campaigns last.
