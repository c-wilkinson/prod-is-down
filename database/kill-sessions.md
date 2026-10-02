# ✂️ Kill Application Sessions

You kill a batch of connections from `WEB-01`.

For several seconds the session count drops.

Then the application reconnects and recreates them all, because the demand has not changed.

You have treated the queue, not the reason the queue exists.

---

## What do you do?

- **[Inspect the application pool](pool.md)**
- **[Restart SQL to really clear them](restart-sql.md)**
- **[Inspect WEB-01 load](../observability/web01.md)**
