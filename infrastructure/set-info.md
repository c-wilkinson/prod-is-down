# 🔧 Restore INFO Logging

You set the production logging level back to `INFO`.

The configuration applies cleanly. Log growth returns to normal almost immediately.

There are still consequences to clean up: `WEB-02` has a full disk and `WEB-01` has been running hot enough that its own log volume is at 91%.

---

## What do you do?

- **[Clean WEB-02 safely](clear-logs.md)**
