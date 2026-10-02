# 🧯 Controlled Recovery

You have enough evidence to fix the problem without gambling.

The recovery plan is straightforward:

1. Restore production logging to `INFO`.
2. Preserve the incident-relevant logs.
3. Free space on `WEB-02`.
4. Restart its application.
5. Return it to the load balancer.
6. Validate both nodes and the customer path.

---

## What do you do?

- **[Fix the configuration first](../infrastructure/set-info.md)**
- **[Free disk space first](../infrastructure/clear-logs.md)**
- **[Bring WEB-02 back after cleanup](../infrastructure/add-web02-back.md)**
