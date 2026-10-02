# 🗄️ SQL Server

The application logs say `SQL timeout`, so SQL deserves inspection.

CPU is normal. Memory pressure is normal. Storage latency is normal. Replication is current. There is no obvious sign of a database under stress.

There are, however, far more connections from `WEB-01` than usual.

---

## What do you do?

- **[Inspect sessions](connections.md)**
- **[Check blocking](blocking.md)**
- **[Look at the normal metrics more closely](../observability/database-normal.md)**
- **[Restart SQL](restart-sql.md)**
