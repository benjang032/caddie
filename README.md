<p align="center">
  <img src="assets/caddy-logo.png" width="300" alt="Caddy, a golf caddy carrying a bag of clubs">
</p>

<h1 align="center">Caddy</h1>

<p align="center">
  <em>Your model can swing. Caddy picks the club.</em>
</p>

<p align="center">
  <a href="https://github.com/benjang032/caddy/stargazers"><img src="https://img.shields.io/github/stars/benjang032/caddy?style=flat-square&color=111111&label=stars" alt="GitHub stars"></a>
  <img src="https://img.shields.io/badge/playbooks-10-111111?style=flat-square" alt="10 playbooks">
  <img src="https://img.shields.io/badge/lessons-12-111111?style=flat-square" alt="12 lessons">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-111111?style=flat-square" alt="Apache 2.0 license"></a>
</p>

Models are getting better at swinging. They still choose the wrong club.

Caddy is a Codex skill for building and reviewing AI agents that survive contact with the real world. It handles the work around the model: context, tools, memory, verification, evaluation, training, and multi-agent design.

It does not reach for every club in the bag. It routes the job to the smallest useful lesson or playbook, then requires the agent to show its evidence.

## Install

```bash
git clone https://github.com/benjang032/caddy.git "${CODEX_HOME:-$HOME/.codex}/skills/caddy"
```

Restart Codex, then call the skill explicitly:

```text
$caddy review this agent architecture
```

Update later with:

```bash
git -C "${CODEX_HOME:-$HOME/.codex}/skills/caddy" pull
```

## Call your shot

```text
$caddy design a support agent with safe refund tools and a real completion check

$caddy review this RAG pipeline for context pollution, stale memory, and weak evals

$caddy decide whether this workflow needs multiple agents or one isolated subtask

$caddy explain when SFT, RL, or better scaffolding is the right intervention
```

A quick definition stays quick. A build or review opens the matching playbook, turns its steps into a working checklist, and follows the evidence.

## What is in the bag

| Job | Playbook |
| --- | --- |
| First agent, ReAct loop, harness, guardrails | [Getting started](playbooks/getting-started.md) |
| Prompt layout, KV cache, compression, injection | [Context engineering](playbooks/context-engineering.md) |
| User memory, RAG, indexes, privacy | [Memory and knowledge](playbooks/memory-knowledge.md) |
| Tool schemas, MCP, sidecars, approval | [Tools](playbooks/tools.md) |
| Search, edit, code execution, generative UI | [Coding agents](playbooks/coding-agent.md) |
| Async events, voice, computer use, robotics | [Interaction](playbooks/interaction.md) |
| Environments, judges, attribution, observability | [Evaluation](playbooks/evaluating-agents.md) |
| Mid-training, SFT, RL, rewards, distillation | [Post-training](playbooks/post-training.md) |
| Learning from trajectories without eating the safety gate | [Continual evolution](playbooks/continual-evolution.md) |
| Managers, peers, A2A, shared-context failures | [Multi-agent systems](playbooks/multi-agent.md) |

Each playbook points to the exact lesson cluster it needs. The root skill carries the routing, formulas, and rules that must stay visible throughout the job.

## The yardage book

- Name the data shape before writing agent logic.
- The producer may not approve its own done.
- Verify structured state the model cannot author.
- Bound every loop, recovery path, byte budget, and blast radius.
- Treat untrusted text as data. Summarizing it does not make it safe.
- No eval, no claim of improvement.
- Multi-agent is not the default. Split for new information or context economy.
- Every harness layer names the model failure it hides and carries a deletion eval.

The full operating rules live in [SKILL.md](SKILL.md). Supporting references cover [data shapes](references/data-shapes.md), [failure modes](references/failure-modes.md), [principles](references/principles.md), and [design tensions](references/tensions.md).

## Why Caddy exists

At implementation time, an agent is:

```text
LLM + Context + Tools
```

In production, it is:

```text
Model + Harness
```

The harness is where demos become systems: context management, tool boundaries, constraints, verification, and correction. Caddy keeps the model focused on the shot while making those boundaries explicit.

The skill bundle itself ships no SDK, requests no API key, and sends no telemetry. It is a routed, structurally validated set of Markdown instructions.

## Repository map

```text
caddy/
├── SKILL.md             # router, formulas, non-negotiables
├── agents/openai.yaml   # Codex display metadata and explicit invocation
├── playbooks/           # 10 build and review procedures
├── lessons/             # 12 compact curriculum chapters
├── references/          # principles, shapes, failures, tensions, source
├── scripts/             # structural bundle validator
└── assets/              # Caddy mascot
```

Run the validator after an edit:

```bash
python3 scripts/validate-bundle.py
```

## Source and license

Caddy is original agent-facing instructional material distilled from Bojie Li's [*AI Agents in Depth*](https://github.com/bojieli/ai-agent-book). It is not a reprint. Detailed attribution lives in [references/source.md](references/source.md).

Licensed under [Apache License 2.0](LICENSE).
