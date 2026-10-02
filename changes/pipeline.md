# 🔧 Pipeline Targeting

The pipeline uses an environment selector supplied by a variable group.

Today's run resolved the selector to:

```text
APP-*
```

The test environments are named `APP-DEV`, `APP-TEST`, and `APP-PREPROD`.

Unfortunately, production is named `APP-PROD`.

Wildcards remain undefeated.

---

## What do you do?

- **[Inspect the selector logic](selector.md)**
- **[Run the config again with the right target](../infrastructure/set-info.md)**
- **[Open the war room](../people/war-room.md)**
