> # 003-tools-basic:

### 🧱 4 Primitives of OpenAI Agents SDK
Primitives are the building blocks of Agents SDK:

1. Agent – Have main AI brain and tools.
3. Handoff – Pass task from one agent to another.
3. Guardrails – Safety rules and policies.
4. Session – Memory of a conversation.
---
### 🧾 3 Types of OpenAI API
1. Chat Completion – Stateless, no memory between messages.
2. Responses – Stateful, remembers conversation.
3. Assistant – (More advanced, used for long-term memory & tools)

> # 004-model-settings:
- Temperature = How creative vs. focused your agent is
- Tool Choice = Whether your agent can use calculators, weather apps, etc.
- Max Tokens = How long the response can be
- Parallel Tools = Whether your agent can use multiple tools at once

> # 005-local-context:
Local context is any data or dependencies you pass to your agent's run that your code (tools, lifecycle hooks, etc.) can use. It’s entirely internal and never sent to the LLM.
- **Creating Context:** You create a Python object—often using a dataclass or a Pydantic model—to encapsulate data like a username, user ID, logger, or helper functions.

- **Passing Context:** You pass this object to the run method (e.g., Runner.run(..., context=your_context)). The SDK wraps your object in a RunContextWrapper, making it available to every tool function, lifecycle hook, or callback during that run via wrapper.context.