# Data shapes

Name one of these before writing agent logic. Playbook step 0 points here.

| Playbook | Canonical shape |
| --- | --- |
| Formula (this skill root) | Agent = LLM + Context + Tools. Production rewrite is Model + Harness. Environment sits outside. |
| `playbooks/getting-started.md` | Agent inside, Environment outside. Frozen prefix plus append-only trajectory. |
| `playbooks/context-engineering.md` | Frozen prefix, growing trajectory, tagged tail status. |
| `playbooks/memory-knowledge.md` | User-keyed archive plus tenant-scoped shared knowledge plane. |
| `playbooks/tools.md` | Form-by-disclosure registry (dedicated, general executor, or skill, independent of how many are shown). |
| `playbooks/coding-agent.md` | Coding core plus filesystem hub. Working state in context, durable state in files. |
| `playbooks/interaction.md` | Event stream consumed at tool-boundary safe points. |
| `playbooks/evaluating-agents.md` | Five-component env (dataset, resettable state, atomic tools, rubric, protocol) plus first-error record. |
| `playbooks/post-training.md` | Foundation, then protocol, then policy. Token distribution is the object edited. |
| `playbooks/continual-evolution.md` | Dual loop around a frozen approval root. Four carriers. Knowledge, instructions, programs, weights. |
| `playbooks/multi-agent.md` | Information-gain gate plus a two-axis record (shared vs isolated context, topology). |
