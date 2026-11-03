# Mermaid starter snippets

Each snippet already carries a title, a legend, typed elements and verb-labelled arrows with protocols. Copy, rename, and delete what you don't need. Mermaid has no native legend, so the legend is a small subgraph (structural diagrams) or a `Note` (sequence diagrams). Keep it whenever the diagram uses colour, dashed lines or dashed borders to mean something; drop it from a plain sequence diagram that uses only ordinary request and reply lines.

Syntax gotchas (verified with mermaid-cli 11): sequence-diagram participant aliases cannot contain square brackets, and semicolons inside labels or notes are read as statement separators, so use parentheses and commas there.

Conventions used throughout:
- Solid arrow `-->` = synchronous call, initiated by the source.
- Dashed arrow `-.->` = asynchronous message or event.
- Dashed border (`stroke-dasharray`) = proposed / new in this design.
- In **sequence diagrams** Mermaid itself draws replies dashed (`-->>`), so "dashed = async" does not hold there. State the sequence-diagram convention separately in its note: solid = request, dashed = reply, `-)` = async fire-and-forget message.
- Grey fill = external or existing, out of scope for the change.

## System Context (C4 level 1) as a flowchart

```mermaid
---
title: "System Context diagram: Checkout system (proposed)"
---
flowchart LR
    shopper["Shopper<br/>[Person]<br/>Buys products on the web store"]
    checkout["Checkout System<br/>[Software System]<br/>Takes orders and payments"]
    psp["Payment Provider<br/>[External System]<br/>Authorises and captures card payments"]
    erp["ERP<br/>[External System]<br/>Fulfils orders and holds stock"]

    shopper -->|"places orders using<br/>[HTTPS]"| checkout
    checkout -->|"authorises payments via<br/>[HTTPS/JSON]"| psp
    checkout -.->|"publishes OrderPlaced to<br/>[Kafka: orders.v1]"| erp

    subgraph legend["Legend"]
        l1["In scope (this design)"]
        l2["External / existing"]
        l1 ~~~ l2
    end

    classDef scope fill:#dbe9ff,stroke:#1f4e99,color:#000
    classDef ext fill:#e6e6e6,stroke:#666,color:#000
    class checkout,l1 scope
    class psp,erp,l2 ext
```

## Container (C4 level 2) as a flowchart

```mermaid
---
title: "Container diagram: Checkout system (proposed)"
---
flowchart TB
    shopper["Shopper<br/>[Person]"]

    subgraph checkout["Checkout System"]
        web["Web App<br/>[Container: React]<br/>Checkout UI"]
        api["Checkout API<br/>[Container: Go, gRPC]<br/>Validates and persists orders"]
        refunds["Refund Worker<br/>[Container: Go]<br/>Processes refunds asynchronously"]
        db[("Orders DB<br/>[Container: PostgreSQL]<br/>Orders and payment state")]
        q[["orders.v1<br/>[Kafka topic]"]]
    end

    psp["Payment Provider<br/>[External System]"]

    shopper -->|"uses checkout UI<br/>[HTTPS]"| web
    web -->|"submits orders to<br/>[gRPC]"| api
    api -->|"reads/writes orders<br/>[SQL]"| db
    api -->|"authorises payment via<br/>[HTTPS/JSON]"| psp
    api -.->|"publishes OrderPlaced to"| q
    q -.->|"consumes RefundRequested from"| refunds
    refunds -->|"issues refund via<br/>[HTTPS/JSON]"| psp

    subgraph legend["Legend"]
        direction LR
        l1["Existing container"]
        l2["Proposed (new in this design)"]
        l3["External system"]
        l4[("Data store")]
        l5[["Queue / topic"]]
        l1 ~~~ l2 ~~~ l3 ~~~ l4 ~~~ l5
    end

    classDef existing fill:#dbe9ff,stroke:#1f4e99,color:#000
    classDef proposed fill:#dbe9ff,stroke:#1f4e99,stroke-dasharray:6 4,color:#000
    classDef ext fill:#e6e6e6,stroke:#666,color:#000
    class web,api,db,q,l1 existing
    class refunds,l2 proposed
    class psp,l3 ext
```

Legend text should also state: "solid arrow = synchronous call in the direction of the initiator; dashed arrow = asynchronous message." Every shape the diagram uses (cylinder for data stores, double-bracket for queues) gets a legend entry, as above.

## Sequence diagram (one scenario, including the failure path)

```mermaid
---
title: "Sequence diagram: refund when the payment provider times out"
---
sequenceDiagram
    autonumber
    participant W as Refund Worker (Container)
    participant P as Payment Provider (External)
    participant D as Orders DB (Container)

    Note over W,D: Audience: payments on-call. Question: what happens when the provider times out?<br/>Solid = request, dashed = reply, idempotency key = order_id
    W->>D: mark refund PENDING [SQL]
    W->>P: POST /refunds (Idempotency-Key: order_id) [HTTPS]
    P--xW: timeout 5 s
    loop up to 3 retries, exponential backoff
        W->>P: POST /refunds (same Idempotency-Key)
        P-->>W: 200 refund re_123 (replayed)
    end
    W->>D: mark refund COMPLETE
```

## State machine

```mermaid
---
title: "State diagram: Refund lifecycle"
---
stateDiagram-v2
    [*] --> Requested : customer requests refund
    Requested --> Pending : worker picks up job
    Pending --> Complete : provider confirms [HTTP 200]
    Pending --> Pending : provider timeout / retry (max 3)
    Pending --> Failed : retries exhausted
    Failed --> Pending : operator retries manually
    Complete --> [*]
    note right of Pending : Legend — "event [guard]" on each transition
```

## Deployment (nested nodes)

```mermaid
---
title: "Deployment diagram: Checkout system, Production, us-east-1"
---
flowchart TB
    subgraph region["AWS us-east-1 [Region]"]
        subgraph az1["us-east-1a [Availability Zone]"]
            api1["Checkout API ×2<br/>[EKS pods]"]
            db1[("Orders DB primary<br/>[RDS PostgreSQL]")]
        end
        subgraph az2["us-east-1b [Availability Zone]"]
            api2["Checkout API ×2<br/>[EKS pods]"]
            db2[("Orders DB standby<br/>[RDS PostgreSQL, sync replica]")]
        end
        kafka[["orders.v1<br/>[MSK, regional, 3 brokers]"]]
    end
    api1 -->|"reads/writes [SQL]"| db1
    api2 -->|"reads/writes [SQL]"| db1
    db1 -.->|"replicates to [PostgreSQL streaming]"| db2
    api1 -.->|"publishes to"| kafka
    api2 -.->|"publishes to"| kafka

    subgraph legend["Legend"]
        direction LR
        l1["Nested box = failure domain"]
        l2["×N = replica count"]
        l1 ~~~ l2
    end
```

Pair the deployment diagram with a "what happens when X fails" table in prose (AZ loss, DB primary loss, broker loss).
