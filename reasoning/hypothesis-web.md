# 🧪 Hypothesis: A Web Node Failed First

The evidence fits a simpler chain:

`WEB-02` fails → load balancer sends everything to `WEB-01` → `WEB-01` exhausts its connection pool → users see timeouts.

That explains the SQL-shaped symptoms without requiring SQL itself to be broken.

Now you need to explain why `WEB-02` failed.

---

## What do you do?

- **[Inspect WEB-02](../observability/web02.md)**
- **[Inspect the load balancer](../observability/load-balancer.md)**
- **[Check recent changes](../changes/recent.md)**
