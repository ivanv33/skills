# Inventory Sync v2 — design

## Architecture

Here's the overall architecture:

```mermaid
flowchart LR
    A[Store App] --> B[API]
    B --> C[(DB)]
    B --> D[InventoryManager.java]
    D --> E[Redis]
    B --> F[Warehouse System]
    F --> B
    G[Ops Team] --> H[k8s cluster prod-eu-1]
    H --> B
    B --> I[Kafka]
    I --> J[Reconciler]
    J --> C
    J --> K[Datadog]
    B --> K
    D --> L[StockLevelDTO]
    style D fill:#f9f
    style J fill:#f9f
```

The Reconciler is new. It fixes the drift we see between our DB and the warehouse every night. It uses Kafka. Everything else already exists.

## Rollout
Enable per region behind a flag.
