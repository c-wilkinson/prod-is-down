# 📊 Ann O'Maly's Monitoring Dashboard

**Ann O'Maly** has already highlighted the interesting bits.

The overview is aggressively red in several places, which is not the same as being useful.

HTTP `503`s started at **16:46**. Application latency rose at almost the same time. SQL timeout errors followed seconds later. The load balancer says one backend is unhealthy.

The database dashboard, irritatingly, looks mostly normal.

---

## What do you do?

- **[Check the public HTTP endpoint](front-door.md)**
- **[Inspect the load balancer](load-balancer.md)**
- **[Look at the web servers](web01.md)**
- **[Go straight to SQL](../database/sql.md)**
- **[Silence Ann's noisy alert](../infrastructure/disable-alert.md)**
