# 🧵 Trace a Request

A traced request through `WEB-01` eventually succeeds.

Most of the time is spent waiting for an application database connection. When one becomes available, the SQL query itself completes quickly.

So the database call is *waiting before it reaches the database*.

That is a useful distinction.

---

## What do you do?

- **[Inspect WEB-01](web01.md)**
- **[Inspect its connection pool](../database/pool.md)**
