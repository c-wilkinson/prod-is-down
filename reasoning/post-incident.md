# 🧠 Never Waste an Incident

The technical root cause is clear:

A broad environment selector allowed a test-only DEBUG setting into production. High log volume filled `WEB-02`, removing it from rotation and overloading `WEB-01`. The resulting connection-pool exhaustion looked like a database outage.

The recovery is complete. The question now is whether this can happen again.

---

## What do you do?

- **[Add a production targeting guardrail](../meta/config-test.md)**
- **[Improve detection](../meta/alerting.md)**
- **[Fix the runbook](../meta/documentation.md)**
- **[Do all of it](../endings/never-waste-incident.md)**
