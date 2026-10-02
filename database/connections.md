# 🔌 Database Sessions

`WEB-01` has a large number of open sessions.

Most are idle or executing quickly. The database is accepting them happily. The application is simply asking one server to handle far more concurrent requests than usual.

That raises a better question: **why is only WEB-01 doing the work?**

---

## What do you do?

- **[Inspect the application connection pool](pool.md)**
- **[Kill the sessions](kill-sessions.md)**
- **[Check the load balancer](../observability/load-balancer.md)**
