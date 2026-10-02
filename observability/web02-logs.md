# 📜 WEB-02 Application Logs

The application log ends abruptly at **16:46:12**.

Just before that, there are thousands of DEBUG entries per minute. There is no graceful shutdown message, crash dump, or stack trace. The final line is cut off halfway through writing a request identifier.

Something stopped it from writing.

---

## What do you do?

- **[Check disk usage](disk.md)**
- **[Restart the application](../infrastructure/restart-app.md)**
- **[Assume the application deployment is bad](../changes/app-deploy.md)**
