# first-agent-architecture-review

## Use when

- review this agent architecture
- is this an agent or a chatbot
- should we add tools or a stronger model
- workflow vs autonomous
- add guardrails
- design the harness
- ReAct loop is looping
- getting started with an AI agent

## Steps

Make a working checklist from the numbered steps before reasoning. Use the host's task or todo list when available. If a step does not apply, keep it listed with a one-line skip reason. Do not delete it.

### 0. Name the data shape

Open [data shapes](../references/data-shapes.md). Name the getting-started shape before writing loop logic. Agent sits inside. Environment sits outside. Every model call is a frozen prefix plus an append-only trajectory.

Skip this step only when the current review note already names that shape in those words.

### 1. Draw Agent versus Environment

Draw two boxes. Place the model, context assembly, and tool adapters inside Agent. Place files, users, pages, databases, and other agents in Environment. Harness policy stays inside Agent. World state and transition rules stay in Environment.

Check. The architecture note names Environment as a peer of Agent, not a field of Agent.

If the check fails, open `lessons/01-getting-started.md` cluster `agent-formula-inside-boundary` and cite source-ids `agent-formula-inside-boundary`, `agent-environment-closed-loop`, `harness-inside-agent-not-environment`, `one-skeleton-two-lenses`.

Skip when a current diagram already places those three insides and names Environment as a peer.

### 2. Inventory observation sources and action ports

List facts that can enter context. List operations that can change the world. Treat unseen facts as nonexistent to the model. Treat unexposed operations as speech-only recommendations. Expand a missing space before swapping the model.

Check. The last stuck ticket names a missing observation or a missing action, or a written reason that both spaces were already complete.

If the check fails, open `lessons/01-getting-started.md` cluster `expand-spaces-before-model` and cite source-ids `expand-spaces-before-model`, `observation-action-interface`, `product-three-axis-audit`.

Skip when the last experiment log already tried an interface change with the model held fixed.

### 3. Classify tools by interaction direction

Sort every interface into perception, execution, collaboration, event, or user communication. Register event triggers as inbound starts. Do not wait for the model to invoke the clock or the inbox. Route explore work to general executors. Route money, delete, send, and prod-deploy to specialized auditable tools.

Check. The catalog file has a type tag on every entry and a comment for unused types. A webhook or cron path starts a run without a model-issued trigger call.

If the check fails, open `lessons/01-getting-started.md` cluster `five-tool-types` and cite source-ids `five-tool-types`, `event-triggers-are-inbound`, `general-for-explore-specialized-for-risk`.

Skip when the live catalog already carries those five tags and inbound events start the loop.

### 4. Confirm prefix plus full trajectory

Confirm every model call is the stable prefix plus the entire trajectory so far. Append tool results. Do not send only the last result. Do not mutate the system prompt each turn.

Check. Call N's input messages include all prior user, assistant, and tool records from the same run. Two consecutive calls share an identical prefix hash unless a documented late-load occurred.

If the check fails, open `lessons/01-getting-started.md` cluster `react-reason-act-observe` and cite source-ids `context-is-prefix-plus-trajectory`, `static-prefix-and-trajectory`, `five-part-context`.

Skip when a dumped pair of consecutive calls already proves prefix identity and full trajectory replay.

### 5. Trace one run as reason, act, observe

Walk one recorded run. Label each iteration as reason, act, or observe. Let the model emit the next decision. Let the harness validate calls. Let the environment execute and return observations. Fan out independent calls in one iteration. Add a hard round cap and a repeat-call fingerprint.

Check. A trajectory viewer can label each iteration. A stuck-tool unit test hits max rounds or a fingerprint and exits without a further Environment.apply.

If the check fails, open `lessons/01-getting-started.md` cluster `react-reason-act-observe` and cite source-ids `react-reason-act-observe`, `model-decides-harness-runs-env-changes`, `parallel-independent-tool-calls`, `autonomous-needs-stop-conditions`.

Skip when a golden trajectory already shows those labels, a stop test, and one parallel fan-out.

### 6. Map the five harness jobs

Map code to context, tools, constrain, verify, and correct. Default capabilities off. Verify on structured tool fields and environment state, never on assistant prose. Recover or roll back without showing half-finished artifacts.

Check. A repo tour can point to five modules. A fresh session cannot run a side-effecting tool until a grant exists. An injected success sentence cannot pass if the structured result is a failure.

If the check fails, open `lessons/01-getting-started.md` cluster `harness-five-responsibilities` and cite source-ids `harness-five-responsibilities`, `fail-safe-capability-defaults`, `verify-on-structured-data`, `correct-without-leaking-partials`.

Skip when the five-module map and the three checks already exist for the current revision.

### 7. Choose the lowest orchestration rung

Try one call if prompts and examples suffice. Encode a known sequence as a workflow. Mix a workflow spine with autonomous joints when compliance and surprise both exist. Use a ReAct loop only when the next step must follow live feedback. Price latency as rounds times per-round generation time.

Check. The design record shows which rung was tried first and why the next rung was required. A skip-payment test still cannot invoke a book node.

If the check fails, open `lessons/01-getting-started.md` cluster `escalate-to-agent-last` and cite source-ids `escalate-to-agent-last`, `workflow-locks-order-and-attack-surface`, `mix-compliance-and-flexibility`.

Skip when the live graph already records the rung, the cost budget, and a coded illegal-order test.

### 8. Place three guardrail layers

Place rails on context, execution, and data. Treat context rails as rate reducers, not guarantees. Score tool-plus-arguments outside the working context. Keep row policy in a trusted data plane. Add human handover on retry caps and irreversible ops. Pause rather than default-approve if the human is silent. Score both block-rate on prohibited items and completion-rate on permitted sensitive items.

Check. A threat model lists at least one control in each layer. A red-team injection that fools the model still fails at permission or database policy. Exceeding the retry cap creates a handover record and stops apply.

If the check fails, open `lessons/01-getting-started.md` cluster `layered-guardrails-plus-false-refusal` and cite source-ids `layered-guardrails-plus-false-refusal`, `rank-layers-by-bypass-hardness`, `escalate-on-caps-and-irreversible`.

Skip when the threat model, the dual safety eval, and the handover test already pass.

### 9. Apply the five patterns

Separate reviewer context from producer context. Disclose a catalog first and load bodies on demand. Append facts, events, and schemas. Score a boundary set and a retention set on every change. Ship the smallest attributed, reversible diff.

Check. The reviewer call omits producer reasoning and includes the artifact. A first-call dump shows catalog lines without full bodies. Replay from the log reconstructs the same states. CI has two named sets. The last agent-driven change can revert alone.

If a pattern check fails, open `lessons/01-getting-started.md` and the matching cluster among `proposer-reviewer-separate-context`, `progressive-disclosure`, `append-only-state`, `boundary-and-retention-sets`, `minimal-diff-reversible`.

Skip when all five checks already pass on the current revision.

## Open next

- [Context engineering](context-engineering.md) when prefix stability, skills, compression, or injection wrapping is the next gap.
- [Tools](tools.md) when schemas, disclosure, perception grain, or execution safety is the next gap.
- [Evaluating agents](evaluating-agents.md) when a change needs a scored claim.

Do not open two lesson files to start.

## Reply

State what changed, what was chosen, and what remains open. Fold `01-chapter-synthesis` into that reply.

1. Agent is reasoning engine, working set, and action interfaces, with Environment outside.
2. Expand observation and action spaces before swapping the model.
3. Context is frozen prefix plus full trajectory.
4. Production reliability lives in constrain, verify, and correct.
5. Climb one call, then workflow, then mixed, then autonomy, and price the step.
6. Apply the five patterns.
7. Treat security as the three-layer stack, not a launch checklist.

A teammate should recast those seven lines without naming a vendor.
