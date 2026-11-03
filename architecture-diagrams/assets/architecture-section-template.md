# Template: Architecture section of a design doc

Copy into the design doc and replace the placeholders. Delete subsections that don't apply (e.g., Deployment when infrastructure doesn't change) rather than leaving them empty.

```markdown
## Architecture

### Context and scope
<!-- 2–4 sentences: what system, what changes, who uses it. -->

**Figure 1 – System Context diagram for <System Name> (<current|proposed>)**
<!-- Audience: <e.g., all reviewers incl. product>. Question: <what does this system interact with?> -->
‹embed/link to rendered diagram; source: docs/architecture/<file>.dsl|.mmd›

<1 paragraph walkthrough: users, external systems, what's new (dashed).>

### Structure

**Figure 2 – Container diagram for <System Name> (<proposed>)**
<!-- Audience: <engineers on X, Y teams>. Question: <what runs where and how do they talk?> -->
‹embed diagram›

| Element catalog (keep narrow) |
|---|
| **<Container A>** – <responsibility>; <tech>; owner: <team> |
| **<Container B>** – <responsibility>; <tech>; owner: <team> |

Data ownership: <which container owns which data>.

### Key runtime scenarios

**Figure 3 – Dynamic/sequence diagram: <happy-path scenario>**
‹embed diagram›
<Numbered walkthrough; latency budget per hop if relevant.>

**Figure 4 – Dynamic/sequence diagram: <failure scenario, e.g., provider timeout>**
‹embed diagram›
<Retries, idempotency, compensation, user-visible outcome.>

### Deployment (include only if infra changes)

**Figure 5 – Deployment diagram: <environment, e.g., Production, us-east-1>**
‹embed diagram›
<Mapping of containers → nodes; replicas; zones; failure domains.>

### Quality attributes
- **Latency:** When <stimulus> under <environment>, <artifact> responds within <measure>. Addressed by <tactic> in <Figure N>.
- **Availability:** …
- **Security:** <trust boundaries, authn/z points, data classification>.
- **Scalability / modifiability:** …

### Decisions and alternatives considered
- **Decision:** <one sentence>. **Drivers:** <QA scenarios/constraints>.
  **Alternatives:** <Alt 1 – rejected because…>; <Alt 2 – rejected because…>.
  **Consequences/risks:** <…>. **ADR:** <link>

### Diagram maintenance
Owner: <team/person> · Last verified: <YYYY-MM-DD> · Source: <repo path> · Status after launch: <promote to docs/architecture | mark historical>
```
