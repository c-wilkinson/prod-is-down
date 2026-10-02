# 💽 Disk Usage

There it is.

```text
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2        20G   20G     0 100% /var/log
```

`/var/log` is completely full.

The application cannot create or extend its log files, which explains why the service stopped. It does **not** yet explain why the disk filled so quickly.

---

## What do you do?

- **[Find what filled it](debug-logs.md)**
- **[Delete some logs](../infrastructure/clear-logs.md)**
- **[Extend the disk](../infrastructure/extend-disk.md)**
- **[Use rm with enthusiasm](../infrastructure/rm-logs.md)**
