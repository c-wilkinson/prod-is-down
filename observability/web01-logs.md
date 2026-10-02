# 📜 WEB-01 Application Logs

The logs are noisy enough to qualify as literature.

Most errors are database timeouts: threads are waiting for connections and eventually giving up. Between the errors are an extraordinary number of `DEBUG` messages containing request details that you do not remember seeing before.

SQL looks guilty. The logging looks suspicious.

---

## What do you do?

- **[Investigate SQL](../database/sql.md)**
- **[Inspect the connection pool](../database/pool.md)**
- **[Investigate the DEBUG logging](debug-logs.md)**
