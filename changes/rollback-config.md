# ↩️ Roll Back Configuration

You restore `log_level: INFO` and run the configuration against production deliberately this time.

New log growth drops immediately.

`WEB-02` is still down because its disk is already full. `WEB-01` is still carrying all traffic and its own log partition is uncomfortably full.

---

## What do you do?

- **[Check both web nodes before celebrating](../reasoning/check-both.md)**
- **[Assume the change fixed everything](../endings/fast-restore.md)**
- **[Perform a controlled recovery](../reasoning/controlled-recovery.md)**
