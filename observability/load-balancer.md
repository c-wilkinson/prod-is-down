# ⚖️ Load Balancer

The load balancer is healthy.

Its backends are not.

`WEB-01` is **UP** but very busy. `WEB-02` has been **DOWN** since 16:46 and is failing its application health check. All surviving traffic is being sent to `WEB-01`.

This seems worth remembering.

---

## What do you do?

- **[Inspect WEB-02](web02.md)**
- **[Inspect WEB-01](web01.md)**
- **[Restart the load balancer anyway](../infrastructure/restart-unrelated.md)**
- **[Remove WEB-01 too, for symmetry](../infrastructure/remove-web01.md)**
