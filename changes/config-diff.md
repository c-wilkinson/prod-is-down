# 🧾 Configuration Diff

There is exactly one production difference:

```diff
- log_level: INFO
+ log_level: DEBUG
```

Nothing else changed.

The diff is small enough to look harmless and timed well enough to look extremely suspicious.

---

## What do you do?

- **[Inspect the commit](commit.md)**
- **[Roll the setting back](rollback-config.md)**
- **[Compare with log growth](../observability/debug-logs.md)**
