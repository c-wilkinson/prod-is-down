# 🔧 Restore INFO Logging

You set the production logging level back to `INFO`.

The configuration applies cleanly. Log growth returns to normal almost immediately.

Before recovery continues, you make sure `WEB-02` has enough free space to write normally again. If the runaway logs are still present, you preserve the incident-relevant slice and clear them. If you already cleaned or expanded the volume, there is nothing more to do.

The application starts and its local health check passes.

---

## What do you do?

- **[Return WEB-02 to service](add-web02-back.md)**
- **[Check both nodes before declaring victory](../reasoning/check-both.md)**
- **[Proceed with controlled recovery](../reasoning/controlled-recovery.md)**
