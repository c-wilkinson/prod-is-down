# 🔎 A Suspicious Amount of Logging

The application is writing roughly **1.8 GB of DEBUG logs per hour**.

Yesterday it wrote less than 200 MB all day.

The first DEBUG line appears at **16:41:08**, almost exactly when today's configuration automation finished. The log entries themselves are valid; there are simply far too many of them.

---

## What do you do?

- **[Set logging back to INFO](../infrastructure/set-info.md)**
