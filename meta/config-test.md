# 🧪 Add the Guardrail

You replace the wildcard with an explicit allow-list and add a pipeline check requiring production to be deliberately selected.

A test now fails if a lower-environment change can implicitly include production.

The automation becomes slightly less clever and considerably safer.

---

## What do you do?

- **[Improve alerting too](alerting.md)**
- **[Stop here](../endings/root-cause-found.md)**
