# 🌐 The Front Door

Synthetic checks agree with the users: some requests succeed, others crawl, and a few return `503`.

TLS negotiation is quick. DNS lookup time is normal. The failures happen after the request reaches the application.

**Jason Parse** from the API team posts in chat:

> Requests that make it through are valid. This doesn't look like payload handling.

That narrows things down, but it does not stop the incident channel filling with theories.

---

## What do you do?

- **[Trace a request through the stack](trace.md)**
- **[Inspect the load balancer](load-balancer.md)**
- **[Ask Dee N. Ess](../people/network-team.md)**
- **[Test the network path](network.md)**
- **[Check the TLS certificate](certificate.md)**
