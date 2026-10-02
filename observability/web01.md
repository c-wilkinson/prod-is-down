# 🖥️ WEB-01

`WEB-01` is alive and doing the work of two servers.

CPU is hovering around **94%**. Request queues are climbing. Its application connection pool is nearly exhausted, and the log volume is much higher than usual.

**Cash Miss** from Performance points out that the cache hit rate is actually fine, which is both useful and disappointing given the name.

Nothing here explains why its sibling disappeared.

---

## What do you do?

- **[Read the application logs](web01-logs.md)**
- **[Add capacity](../infrastructure/scale-out.md)**
- **[Reboot WEB-01](../infrastructure/reboot-web.md)**
