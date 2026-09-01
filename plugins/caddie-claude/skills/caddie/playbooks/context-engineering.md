# context-layout-review

Make a working checklist from these steps before reasoning. Use the host's task or todo list when available.

## Use when

- TTFT jumped after a prompt tweak
- the agent repeats the same tool call
- context is growing without bound
- a webpage or PDF hijacked the agent
- a skill never loads or loads too often
- the model violates a count cap
- need to add time or quota to the agent
- too many tools in the always-on list
- reviewing system prompt structure
- designing compression or sub-agents

## Steps

### 0. Name the data shape

Name the window as a frozen prefix, a growing trajectory, and a tagged tail status.
Look up the row for this playbook in [data shapes](../references/data-shapes.md).
Do not write assembler logic before that name is on the card.

### 1. Hash the frozen prefix

Hash the system prompt and the core tools JSON.
Confirm both stay frozen for the session and the agent version.
Whitespace counts as a change.
If the hash drifts mid-session, open [lesson 02](../lessons/02-context-engineering.md).
Read cluster `never-edit-finalized-system-or-tools`.
source-ids: never-edit-finalized-system-or-tools, freeze-tool-definition-order, reuse-kv-only-for-unchanged-prefix

### 2. Confirm the assembler layout

Confirm the assembler builds messages as prefix plus trajectory plus tagged tail status.
Core tools stay a sibling field, not a fake user paragraph.
If a second path concatenates prompts, open [lesson 02](../lessons/02-context-engineering.md).
Read cluster `assemble-prefix-trajectory-status`.
source-ids: assemble-prefix-trajectory-status, split-static-prefix-from-trajectory, harness-implements-context-layer

### 3. Move live fields off the prefix

Move clocks, locale, OS, plan tier, quota, and other live fields after the cache boundary or into the bar.
Fetch time with a tool when a tool already exists.
If a clock or plan string sits in the system line, open [lesson 02](../lessons/02-context-engineering.md).
Read cluster `never-put-clock-in-system-prompt`.
source-ids: never-put-clock-in-system-prompt, never-embed-live-user-config-in-prefix, append-timestamps-and-status-at-tail, move-runtime-flags-after-boundary

### 4. Freeze tool order and park the long tail

Confirm tools stay in a fixed order for a given agent version.
Append a long-tail schema once at first use and leave it.
Move domain manuals into skills, not into the always-on list.
If the always-on list grows or sorts by recency, open [lesson 02](../lessons/02-context-engineering.md).
Read cluster `write-tool-docs-as-operating-manuals`.
source-ids: freeze-tool-definition-order, keep-core-tool-set-small-and-stable, append-discovered-schemas-once

### 5. Confirm skill routing is visible

Confirm each skill description names Use when and Do not use when.
Confirm the catalog is resident at session start.
If a needed skill never loads, or a body sits in the frozen system line, open [lesson 02](../lessons/02-context-engineering.md).
Read cluster `disclose-skills-in-three-layers`.
source-ids: disclose-skills-in-three-layers, write-skill-description-as-router, keep-skill-catalog-always-visible

### 6. Cap the loop and break repeats

Confirm the loop caps iterations and detects repeat tool calls.
Register static schemas once. Seed system then user. Append the assistant message before execution.
If the loop can run forever or rereads one path, open [lesson 02](../lessons/02-context-engineering.md).
Read cluster `branch-on-tool-calls-or-exit`.
source-ids: branch-on-tool-calls-or-exit, cap-loop-with-max-iterations, detect-and-break-repeat-tool-loops, register-static-tool-schemas-once, seed-system-then-user

### 7. Keep observations in the tool role

Confirm tool results use the tool role and wrap external bodies in source tags.
Inner instructions in those tags are data, not orders.
If a webpage or PDF can rewrite the next action, open [lesson 02](../lessons/02-context-engineering.md).
Read cluster `wrap-external-content-as-untrusted-data`.
source-ids: wrap-external-content-as-untrusted-data, treat-every-perception-tool-as-injection-surface, never-mislabel-tool-as-user

### 8. Keep the status bar in code

Confirm the status bar is code-owned and is not filled from webpage text.
Counts, cwd, and caps come from the event log.
If a one-shot model tally writes the bar, open [lesson 02](../lessons/02-context-engineering.md).
Read cluster `maintain-status-in-deterministic-code`.
source-ids: maintain-status-in-deterministic-code, keep-status-bar-off-untrusted-inputs, distill-counts-into-explicit-facts

### 9. Compress in one batch near the cap

Confirm history is append-only.
Near about 80 percent of the window, batch-compress unmarked old tool bodies and mark them.
Leave the static prefix untouched.
If last-N deletion is the history policy, open [lesson 02](../lessons/02-context-engineering.md).
Read cluster `trigger-batch-compress-near-eighty-percent`.
source-ids: trigger-batch-compress-near-eighty-percent, never-slide-away-history, never-compress-the-static-prefix, compress-between-calls-in-batches

### 10. Isolate bulky search first

Confirm bulky search is isolated in a self-briefed sub-agent when it would junk the main window.
Keep a short task and a short return in the parent.
If tens of thousands of search tokens land in the main trace, open [lesson 02](../lessons/02-context-engineering.md).
Read cluster `isolate-bulky-exploration-in-subagents`.
source-ids: isolate-bulky-exploration-in-subagents, brief-subagents-with-self-contained-goals

### 11. Check the compress keep-list

Confirm the compress keep-list includes decisions, constraints, failures, citations, and identifiers.
Times, names, UUIDs, and hashes stay verbatim.
If a gold id vanishes from a note, open [lesson 02](../lessons/02-context-engineering.md).
Read cluster `preserve-value-integrity-relevance-understanding`.
source-ids: preserve-value-integrity-relevance-understanding, keep-citations-as-lossless-index

### 12. Run the prefix canary before merge

Run a prefix-edit TTFT canary and a structure ablation before merging prompt changes.
A tiny copy edit that moves TTFT is a cache miss, not a model regression.
If a prompt change ships without those two checks, open [lesson 02](../lessons/02-context-engineering.md).
Read cluster `measure-ttft-after-prefix-edit`.
source-ids: measure-ttft-after-prefix-edit, ablation-structure-and-tool-prose-matter

No worker step is skipped.

## Open next

- [Memory and knowledge](memory-knowledge.md) when the missing store is cross-session user memory or a shared knowledge plane.
- [Tools](tools.md) when the defect is schema form, disclosure policy, or a minted tool rather than window layout.

## Reply

State what changed in the prefix, trajectory, skills, bar, or compress path.
State what was chosen between isolation and batch compress.
State what remains open, including any cluster still red.
