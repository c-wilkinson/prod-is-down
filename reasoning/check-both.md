# 🔍 Check Both Web Nodes

`WEB-02` is the obvious casualty, but `WEB-01` has been writing the same DEBUG logs while handling double traffic.

Its `/var/log` volume is already **91%** full.

Had the incident continued, the surviving node would have failed too.

You have found the difference between restoring service and actually stabilising it.

---

## What do you do?

- **[Restore INFO logging](../infrastructure/set-info.md)**
- **[Clean the affected logs](../infrastructure/clear-logs.md)**
- **[Ignore WEB-01 and stop](../endings/cowboy-engineer.md)**
