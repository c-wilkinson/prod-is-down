# 🧪 Hypothesis: SQL Failed

The SQL timeout errors are real, but the timeline places them *after* `WEB-02` disappeared.

If SQL were the initiating failure, you would expect both web nodes to struggle before one of them vanished.

You can test the hypothesis rather than arguing about it.

---

## What do you do?

- **[Check SQL health](../observability/database-normal.md)**
- **[Ask Carol Query](../people/dba.md)**
- **[Restart SQL and find out dramatically](../database/restart-sql.md)**
