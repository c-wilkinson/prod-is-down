# 🕒 Build the Timeline

You line up the evidence:

- **16:41** configuration automation completes.
- **16:41** DEBUG logging begins.
- **16:46** `WEB-02` application stops.
- **16:46** load balancer removes `WEB-02`.
- **16:47** `WEB-01` saturates.
- **16:47** application starts reporting SQL connection timeouts.

The order matters.

---

## What do you do?

- **[Investigate the 16:41 configuration change](hypothesis-config.md)**
- **[Focus on WEB-02 failing first](hypothesis-web.md)**
- **[Assume SQL is the root cause](hypothesis-db.md)**
