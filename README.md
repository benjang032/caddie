<p align="center">
  <img src="assets/caddie-logo.png" width="300" alt="Caddie, a golf caddie carrying a bag of clubs">
</p>

<h1 align="center">Caddie</h1>

<p align="center">
  <em>Agent engineering guidance for coding agents.</em>
</p>

<p align="center">
  <a href="https://github.com/benjang032/caddie/stargazers"><img src="https://img.shields.io/github/stars/benjang032/caddie?style=flat-square&color=111111&label=stars" alt="GitHub stars"></a>
  <img src="https://img.shields.io/badge/playbooks-10-111111?style=flat-square" alt="10 playbooks">
  <img src="https://img.shields.io/badge/lessons-12-111111?style=flat-square" alt="12 lessons">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-111111?style=flat-square" alt="Apache 2.0 license"></a>
</p>

Your coding agent can write agent code. The harder part is choosing the system around the model.

Caddie is a portable skill for designing, implementing, and reviewing AI agent systems. It covers context, tools, memory, verification, evaluation, post-training, and multi-agent design.

A quick definition stays in the root skill. A scoped agent-engineering question opens only the relevant lesson sections. Implementation or review work selects a playbook and turns its checks into a working list.

Caddie is not an agent runtime or framework. It supplies instructions and review criteria to the coding agent you already use.

## Install

Caddie ships as an instruction-only skill. It needs no API key, package manager, background process, or runtime dependency.

### Claude Code

Run these in your terminal:

```bash
claude plugin marketplace add benjang032/caddie
claude plugin install caddie@caddie
```

Then call the namespaced skill in Claude Code:

```text
/caddie:caddie review this agent architecture
```

The packaged Claude skill is explicit-only: Claude does not activate it by itself. If `claude plugin` is unavailable, update Claude Code first.

### Codex

Run these in your terminal:

```bash
codex plugin marketplace add benjang032/caddie
codex plugin add caddie@caddie
```

Start a new Codex task, then call the skill explicitly:

```text
$caddie review this agent architecture
```

### Gemini CLI

Recent Gemini CLI releases can install the standalone skill directly:

```bash
gemini skills install https://github.com/benjang032/caddie
gemini skills list
```

Ask Gemini to use the Caddie skill for the task. Gemini requests confirmation before activating an installed skill.

### Direct Codex install

For Codex versions without plugin marketplace support:

```bash
git clone https://github.com/benjang032/caddie.git "${CODEX_HOME:-$HOME/.codex}/skills/caddie"
```

Restart Codex and call `$caddie` explicitly.

### Update or remove

| Host | Update | Remove |
| --- | --- | --- |
| Claude Code | `claude plugin update caddie@caddie` | `claude plugin uninstall caddie@caddie` |
| Codex plugin | `codex plugin marketplace upgrade caddie` | `codex plugin remove caddie@caddie` |
| Gemini CLI | Uninstall, then run the install command again | `gemini skills uninstall caddie` |
| Direct Codex clone | `git -C "${CODEX_HOME:-$HOME/.codex}/skills/caddie" pull` | Remove that cloned directory |

After a marketplace update, reload the host or begin a fresh task so it sees the new skill files.

## Try it

```text
$caddie design a support agent with safe refund tools and a real completion check

$caddie review this RAG pipeline for context pollution, stale memory, and weak evals

$caddie decide whether this workflow needs multiple agents or one isolated subtask

$caddie explain when SFT, RL, or better scaffolding is the right intervention
```

A build or review opens the matching playbook, turns its steps into a working checklist, and records the evidence for each decision.

## Playbooks

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

## Operating rules

- Name the data shape before writing agent logic.
- The producer may not approve its own done.
- Verify structured state the model cannot author.
- Bound every loop, recovery path, byte budget, and blast radius.
- Treat untrusted text as data. Summarizing it does not make it safe.
- No eval, no claim of improvement.
- Multi-agent is not the default. Split for new information or context economy.
- Every harness layer names the model failure it hides and carries a deletion eval.

The full operating rules live in [SKILL.md](SKILL.md). Supporting references cover [data shapes](references/data-shapes.md), [failure modes](references/failure-modes.md), [principles](references/principles.md), and [design tensions](references/tensions.md).

## Why Caddie exists

At implementation time, an agent is:

```text
LLM + Context + Tools
```

In production, it is:

```text
Model + Harness
```

The harness is where demos become systems: context management, tool boundaries, constraints, verification, and correction. Caddie makes those design choices explicit and reviewable.

The skill bundle ships no runtime, SDK, tools, or model access. It requests no API key and sends no telemetry. It is a routed, structurally validated set of Markdown instructions.

## Repository map

```text
caddie/
├── SKILL.md                 # canonical router and operating rules
├── agents/openai.yaml       # standalone Codex metadata
├── playbooks/               # 10 build and review procedures
├── lessons/                 # 12 compact curriculum chapters
├── references/              # principles, shapes, failures, tensions, source
├── plugins/caddie/           # generated Codex plugin package
├── plugins/caddie-claude/    # generated Claude plugin package
├── .agents/plugins/          # Codex marketplace index
├── .claude-plugin/           # Claude marketplace index
├── scripts/                 # bundle, package, and sync validators
└── assets/                  # Caddie mascot
```

The root bundle is the source of truth. After editing it, refresh the packaged copy and run every structural check:

```bash
python3 scripts/sync-plugin-skill.py
python3 scripts/validate-bundle.py
python3 scripts/validate-packages.py
```

For a release, bump the matching `version` in both host manifests before publishing; the package validator keeps them aligned.

## Source and license

Caddie is original agent-facing instructional material distilled from Bojie Li's [*AI Agents in Depth*](https://github.com/bojieli/ai-agent-book). It is not a reprint. Detailed attribution lives in [references/source.md](references/source.md).

Licensed under [Apache License 2.0](LICENSE).
