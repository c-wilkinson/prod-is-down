# 🔌 Reboot a Web Server

The machine reboots cleanly.

If this was `WEB-02`, the application fails again because `/var/log` is still full. If this was `WEB-01`, the load balancer briefly has nowhere useful to send traffic.

The reboot has confirmed that electricity was not the root cause.

---

## What do you do?

- **[Check WEB-02 disk](../observability/disk.md)**
- **[Reboot it once more](../endings/cowboy-engineer.md)**
- **[Add another node instead](scale-out.md)**
