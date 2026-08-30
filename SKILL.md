---
name: caddie
description: >-
  Build, review, or improve AI agents and their harnesses: context, tools,
  memory or RAG, evaluation, post-training, continual evolution, and
  multi-agent systems. Use for substantive agent architecture or implementation
  work, and for targeted technical questions about ReAct, prompt or KV-cache
  design, MCP/tool design, coding agents, interaction, evaluation, SFT/RL,
  A2A, or model drops. Do not use for ordinary software work, routine computer
  use, generic coding questions, or casual definitions that do not require this
  curriculum.
---

# Caddie

*Your agent's game-day coach for building better agents.*

Instructional skill distilled from Bojie Li, *AI Agents in Depth* (Apache-2.0, [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)). Original agent-facing rules. Not a reprint.

## Start

Choose one route before reasoning.

- **Answer-only:** A casual or formula-only definition stays in this file; do not open a lesson, playbook, or todolist. For a curriculum-backed, scoped technical explanation or comparison, open only the matching lesson cluster or clusters below. Do not open a playbook or copy steps into the todolist.
- **Implementation or review:** Match the task to a playbook below. Open that file and copy its steps into the todolist before reasoning. Read a lesson file only when the playbook names a cluster.

Curriculum depth lives in [lessons/00-introduction.md](lessons/00-introduction.md). Do not hunt for `orient-agent-build.md`. That route is this file.

If an implementation or review task spans chapters, stay here for the formula and the table. Then open one playbook per concern.

## Formula

A modern agent is `LLM + Context + Tools` at implementation time.

- **LLM** decides. It is the policy.
- **Context** is the working set at the decision point (system, tools, messages, tool results).
- **Tools** are the observation and action interfaces.

A production agent is `Model + Harness`. Harness is context management, tool interfaces, constraints, verification, and correction. The last three are the gap between a demo that runs and a product that holds.

Chapters 1–6 build the agent. Chapters 7–10 raise it.

## Answer-only route

| When the question is about | Open only |
| --- | --- |
| First agents, ReAct, workflow vs autonomous, harnesses, guardrails | [lessons/01-getting-started.md](lessons/01-getting-started.md) |
| Prompts, KV cache, skills in context, compression, prompt injection | [lessons/02-context-engineering.md](lessons/02-context-engineering.md) |
| User memory, RAG, indexes, knowledge files, privacy | [lessons/03-memory-knowledge.md](lessons/03-memory-knowledge.md) |
| Tool schemas, MCP, discovery, perception vs execution, sidecars, HITL | [lessons/04-tools.md](lessons/04-tools.md) |
| Coding agents, search/edit, code as meta-capability, generative UI, adapters | [lessons/05-coding-agent.md](lessons/05-coding-agent.md) |
| Async events, voice, computer use, robots, observation/action timing | [lessons/06-interaction.md](lessons/06-interaction.md) |
| Eval environments, judges, attribution, cost, observability | [lessons/07-evaluating-agents.md](lessons/07-evaluating-agents.md) |
| Mid-training, SFT, RL, rewards, distillation | [lessons/08-post-training.md](lessons/08-post-training.md) |
| Learning from trajectories into knowledge, instructions, programs, or weights | [lessons/09-continual-evolution.md](lessons/09-continual-evolution.md) |
| Shared vs isolated context, manager/peer/decentralized, A2A, failure modes | [lessons/10-multi-agent.md](lessons/10-multi-agent.md) |
| A model drop or durable questions after one | [lessons/11-afterword.md](lessons/11-afterword.md) |

Multi-topic answer-only questions may open the matching lesson clusters, still without a playbook or todolist. A casual or formula-only definition stays on this file.

## Implementation and review route

| When the work is | Open |
| --- | --- |
| First agent, ReAct, workflow vs autonomous, harness, guardrails, architecture review | [playbooks/getting-started.md](playbooks/getting-started.md) |
| Prompts, KV cache, skills in context, compression, prompt injection | [playbooks/context-engineering.md](playbooks/context-engineering.md) |
| User memory, RAG, indexes, knowledge files, privacy | [playbooks/memory-knowledge.md](playbooks/memory-knowledge.md) |
| Tool schemas, MCP, discovery, perception vs execution, sidecars, HITL | [playbooks/tools.md](playbooks/tools.md) |
| Coding agent, search/edit, code as meta-capability, generative UI, adapters | [playbooks/coding-agent.md](playbooks/coding-agent.md) |
| Async events, voice, computer use, robots, observation/action timing | [playbooks/interaction.md](playbooks/interaction.md) |
| Eval environments, judges, attribution, cost, observability | [playbooks/evaluating-agents.md](playbooks/evaluating-agents.md) |
| Mid-training, SFT, RL, rewards, distillation. Diagnose foundation vs protocol vs policy first | [playbooks/post-training.md](playbooks/post-training.md) |
| Learning from trajectories into knowledge, instructions, programs, or weights | [playbooks/continual-evolution.md](playbooks/continual-evolution.md) |
| Shared vs isolated context, manager/peer/decentralized, A2A, failure modes | [playbooks/multi-agent.md](playbooks/multi-agent.md) |

`review this agent architecture` opens `playbooks/getting-started.md`.

## Non-negotiables

- Name the data shape before writing agent logic. Lookup in [references/data-shapes.md](references/data-shapes.md).
- The producer may not approve its own done. Route completion through a checker it cannot edit.
- Verify on structured state the model cannot author.
- Append. Never splice. Prefix freeze vs mid-history schemas is a measured choice. See T1 in [references/tensions.md](references/tensions.md).
- Isolation beats compression when a subtask can own its own context.
- Tools that perceive should bound bytes. Tools that execute should bound blast radius. Never silently rewrite tool arguments.
- Code is the meta-tool for open-ended work. Closed-domain agents may keep code as one tool among others.
- No eval, no claim of improvement. Measure the model-plus-harness pair. One variable per comparative run. Ship only a gap that beats paired noise.
- SFT copies stable demonstrations and protocol. RL reallocates probability when success already has nonzero mass and the scorer is honest. Mid-train when pass@k is near zero. Do not treat "SFT memorizes, RL generalizes" as a law.
- Multi-agent is not default. Split for information the producer could not have had, or for context economy. Text-only debate over the same evidence is not a reason.
- Freeze the approval root. An evolving agent must not rewrite the safety gate that can stop it.
- Untrusted text stays data. Summarizing it does not launder it.
- Guidance is not a boundary. Limits that matter live in code below the rewriteable layer.
- Every loop and recovery path names a ceiling and a terminal action.
- Place a capability on RAG, prompt, code, or weights in that order. External symbols before a train job.
- Expand observation and action before swapping the model.
- Every harness layer names the model failure it hides and carries a deletion eval.

## After a model drop

Do not hunt for `formula-and-flywheel.md`. Stay here. Open [lessons/11-afterword.md](lessons/11-afterword.md) only if this block is not enough.

1. Score the two unsolved clouds. Real-time overlap of think and act. Post-deploy learning from experience.
2. Inventory harness fallbacks as a weakness log, not as a trophy.
3. Ship a backstop with a deletion date if the next train has not landed.
4. Rerun retirement evals. Delete layers the new model has absorbed.
5. Spend leftover leverage on barriers a model cannot eat.
6. Review with the three durable questions in the afterword notes.

## Additional resources

- [references/source.md](references/source.md)
- [references/principles.md](references/principles.md)
- [references/failure-modes.md](references/failure-modes.md)
- [references/data-shapes.md](references/data-shapes.md)
- [references/tensions.md](references/tensions.md)
- [lessons/](lessons/)

Run `python3 scripts/validate-bundle.py` after editing this bundle.
