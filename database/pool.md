# 🏊 Connection Pool

`WEB-01`'s application pool is exhausted.

Requests are waiting for a free connection and eventually timing out before they ever execute SQL. Increasing the pool might delay the symptom, but it would not explain why one web server suddenly has twice the normal traffic.

---

## What do you do?

- **[Ask why only WEB-01 is busy](../observability/load-balancer.md)**
- **[Increase the pool limit](../endings/scale-it-away.md)**
- **[Inspect WEB-01 metrics](../observability/web01.md)**
