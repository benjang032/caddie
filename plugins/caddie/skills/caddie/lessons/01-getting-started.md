# Getting started with AI agents

## What this is for

This chapter is the shared vocabulary for the first architecture review. It names the inside-boundary formula, the observation and action spaces, the ReAct close, the five harness jobs, the orchestration ladder, the three guardrail layers, and the five book-wide patterns. Later chapters expand one slot. They do not start a second skeleton. The operating brief from `01-chapter-synthesis` lives in the playbook reply, not as a second heading here. Thought wrappers live in the drills.

## Terms

- **Agent.** Reasoning engine, working set, and action interfaces inside one boundary.
- **Environment.** Peer that holds world state and returns observations.
- **Harness.** Runtime inside the agent that builds context, exposes tools, and applies constrain, verify, and correct.
- **ReAct.** Reason, act, observe until a stop.
- **Prefix / trajectory.** Stable front of system plus default tools. Growing user, assistant, and tool-result record.
- **Workflow / autonomy.** Coded order versus a runtime-chosen path.
- **Jailbreak / injection.** User bypass of model limits versus steering through external data.

## Core model

Name the getting-started shape from `references/data-shapes.md`. Agent inside. Environment outside. Frozen prefix plus append-only trajectory. Production rewrite is Model plus Harness facing that same Environment.

## Clusters

### `agent-vs-passive-chat`

When classifying a product or codebase as an agent versus a chatbot.
Rule. Require planned steps, tool use, and strategy updates from incoming results. Require an open action space, a pre-action reason, and a post-result plan change.
Check. A recorded session shows at least one tool call and one plan change after a result, not only a final paragraph.
source-ids: agent-vs-passive-chat, three-shared-agent-traits, chapter-as-orientation-map

### `agent-formula-inside-boundary`

When drawing a system box or writing an architecture comment.
Rule. Write Agent = LLM + Context + Tools as the inside-boundary composition. Keep files, users, pages, and other agents in the Environment. The model is policy. Context is the decision-time working set. Tools are every outbound effect and inbound trigger. The RL gloss is useful and inexact. Policy, observation encoding, and action ports are three artifacts. Keep LLM + Context + Tools as the only structural skeleton. Model + Harness is the production unfolding, not a rival map.
Check. The architecture note names Environment as a peer of Agent, not a field of Agent.
source-ids: agent-formula-inside-boundary, llm-reasoning-engine-scope, context-working-set-scope, tools-action-interface-scope, agent-environment-closed-loop, formula-maps-to-rl, one-skeleton-two-lenses

### `expand-spaces-before-model`

When performance is stuck and the model is already held constant.
Rule. Treat unseen facts as nonexistent. Treat unexposed operations as speech-only recommendations. Enlarge observation and action spaces as the first systems lever. Grow product generality by unioning spaces behind grants. Audit a product on working context, action interfaces, and strategy as three columns.
Check. An experiment log shows an interface change tried before a model change, or a written reason the interface was already complete.
source-ids: expand-spaces-before-model, observation-action-interface, product-generality-from-space-union, product-three-axis-audit

### `five-tool-types`

When designing or reviewing a tool catalog.
Rule. Sort every interface into perception, execution, collaboration, event trigger, or user communication. Model event tools as inbound starts. Keep tool calling as declare, decide, append, continue. Ship the narrowest tool that finishes the task. Use general foundation tools for exploration. Use specialized, parameterized, auditable tools for money, delete, send, and prod-deploy. Bound interpreters by path, net, time, and type.
Check. The catalog has a type tag on every entry. A webhook or cron path starts a run without a model-issued trigger call. Payment and delete do not exist as free code.
source-ids: five-tool-types, event-triggers-are-inbound, tool-calling-four-step-loop, start-narrow-then-expand-tools, general-for-explore-specialized-for-risk, sandbox-and-workspace-limits

### `understand-plan-execute-loop`

When a user request is vague or multi-step.
Rule. Infer the real goal, split work, and keep choosing the next tool, arguments, and stop. Allow a reasoning step that does not change the world. Do not treat the agent as a tabula-rasa explorer.
Check. A sample log restates intent or asks a clarifying question before a high-cost tool on an ambiguous request.
source-ids: understand-plan-execute-loop, reason-before-act-from-priors

### `native-tool-policy-not-orchestration`

When a vendor advertises built-in search or a thinking mode.
Rule. Credit post-training with the when-which-args-and-whether-to-continue policy. Keep tool binaries and sandboxes outside the weights. Raise constrain, verify, and correct as decision authority grows. Keep harness code on the current reliability frontier. Delete an adapter only after a kill eval.
Check. An architecture note states that built-in tools still return observations the model did not invent. A changelog that raises autonomy also tightens one safeguard. Each adapter has a kill criterion.
source-ids: native-tool-policy-not-orchestration, stronger-model-needs-stronger-harness, harness-covers-current-frontier, rl-writes-policy-not-tools

### `three-capability-update-paths`

When a behavior must change now, across tasks, or as a high-dimensional skill.
Rule. Use context for in-task adaptation. Use external artifacts for auditable cross-task change. Use post-training when rules cannot express the skill. Do not skip to weights when a prompt or program suffices.
Check. A change request is tagged context, artifact, or parameters, with a reason the cheaper path is insufficient if a costlier path is chosen.
source-ids: three-capability-update-paths

### `five-part-context`

When assembling an LLM request or cutting tokens.
Rule. Include system prompt, tool definitions, user messages, assistant messages, and tool results. Store reasoning, content, and tool_calls as distinct assistant slots. Ablate one part at a time. Tool defs are the action foundation. Tool results are the closed-loop foundation. A fluent paragraph is a failure unless observations support it.
Check. A dumped request has all five parts or an explicit empty array. An eval table has tool-def-off and tool-result-off rows scored on completion, not fluency. A scorer fails a run that states live numbers with zero tool-result messages.
source-ids: five-part-context, assistant-message-three-slots, context-ablation-inequality, fluent-answer-is-not-done

### `react-reason-act-observe`

When executing any multi-step agent task.
Rule. Reason, act, observe until a stop. Feed stable prefix plus the entire trajectory on every call. The model emits the next decision. The harness validates. The environment changes state and returns observations. Fan out independent calls in one iteration. Treat freeform arguments as a codec, not a new loop. Clarify underspecified research before spending the search loop.
Check. A trajectory viewer can label each iteration as reason, act, or observe. Call N includes every prior record from the run. A fan-out task shows multiple tool results under one assistant tool_calls array.
source-ids: react-reason-act-observe, context-is-prefix-plus-trajectory, static-prefix-and-trajectory, model-decides-harness-runs-env-changes, parallel-independent-tool-calls, freeform-args-same-client-loop, clarify-intent-before-research

### `harness-five-responsibilities`

When auditing harness completeness or moving a demo toward production.
Rule. Write Agent = Model + Harness facing Environment. Give context, tools, constrain, verify, and correct each an owner. Context means information sufficiency. Tools means a clear interface. Constrain means fail-safe defaults. Verify runs on structured fields, never on free-form model prose. Correct retries and rolls back without leaking half-state. Spend most production effort on the last three jobs. Sandbox policy is harness. Sandbox file bytes are environment.
Check. A repo tour can point to five modules. A fresh session cannot run a side-effecting tool until a grant exists. An injected success sentence cannot pass if the structured result is a failure.
source-ids: production-formula-model-plus-harness, harness-five-responsibilities, model-harness-inner-structure, harness-inside-agent-not-environment, information-sufficiency, clear-tool-interface, fail-safe-capability-defaults, verify-on-structured-data, correct-without-leaking-partials, production-gravity-on-safeguards

### `start-simple-add-later`

When choosing APIs, frameworks, and abstractions.
Rule. Begin with the simplest working design. Add complexity only when a measured need appears. Show plans and the decision trajectory. Design the agent-computer interface so the likely mistake cannot be expressed. Treat prompt, context, harness, loop, and graph as nested scopes, not replacement religions. Once models converge, compete on harness diffs with the model id held constant.
Check. The first merged version of a feature has no unused orchestration layer. An operator can open a run and see each call and result. The top historical misuse no longer type-checks.
source-ids: start-simple-add-later, show-the-trajectory, design-aci-to-forbid-misuse, nested-engineering-waves, compete-on-harness-not-model

### `eval-on-own-tasks`

When picking or refreshing a model id.
Rule. Run the team's real tasks. Treat public boards as a shortlist. Test willingness, exposure, and terms, not only accuracy. Require a reasoning-capable model once steps or choices branch. Budget wait as rounds times per-round generation time. Treat a missing modality as a hard fail.
Check. A dated eval sheet lists the chosen model against private tasks with tool-call scores. A matrix row exists for each sensitive capability. A capacity note shows measured round time times expected rounds.
source-ids: eval-on-own-tasks, test-policy-boundaries, require-reasoning-except-trivial, budget-output-speed-and-modality

### `escalate-to-agent-last`

When starting an LLM feature or mixing compliance with surprise.
Rule. Use one call if prompts and examples suffice. Use a workflow when order is law. Mix a workflow spine with autonomous joints. Use a ReAct loop only when the path must be chosen at runtime. Price the extra latency. Encode illegal orders in code. Treat format-only adapters as temporary. Give autonomy explicit stops. Split long jobs into an initializer and an executor with handover artifacts. Map context, knowledge, tools, and verify-plus-correct onto later building chapters rather than inventing a second outline.
Check. The design record shows which rung was tried first. A skip-payment test still cannot invoke a book node. A stuck-tool test hits max rounds or a fingerprint. A multi-session fixture keeps done false while the remaining-work list is nonempty.
source-ids: escalate-to-agent-last, workflow-locks-order-and-attack-surface, adapters-get-absorbed, autonomous-needs-stop-conditions, mix-compliance-and-flexibility, split-init-and-execute-for-long-tasks, map-five-elements-to-build-chapters

### `pick-thin-frameworks`

When choosing among runtimes and builders.
Rule. Choose by whether the kit stays out of the way of business logic, not by sophistication. Record dimensions. Drop vendor rankings.
Check. The chosen kit can dump prefix and trajectory. The README names why thicker kits were rejected.

| Dimension | What to record |
| --- | --- |
| Orchestration mode | one call, workflow, mixed, autonomous, or event-driven |
| Harness visibility | raw prefix and trajectory can be dumped |
| Deployment shape | library, service, visual builder, or embedded kernel |
| Event support | inbound starts without a model-issued trigger call |
| Integration path | batch exec, SDK, or persistent app-server |

source-ids: pick-thin-frameworks

### `layered-guardrails-plus-false-refusal`

When adding safety to an agent.
Rule. Stack specialized rails and score both blocked bad asks and allowed good asks. Order layers by bypass hardness. Context, then execution, then data. Lower layers must not trust upper ones. Separate jailbreaks from prompt injection. If a classifier is used, judge question and answer together and run a cheap probe first. Context rails are rate reducers. Review tool-plus-arguments outside the injected context. Enforce who-may-touch-which-row in a trusted data plane. Escalate after retry caps and before irreversible ops. Pause if the human is silent.
Check. A safety eval reports block-rate and completion-rate. A threat model lists one control per layer. A red-team injection that fools the model still fails at permission or row policy. Exceeding the retry cap creates a handover record and stops apply.
source-ids: layered-guardrails-plus-false-refusal, rank-layers-by-bypass-hardness, separate-jailbreak-from-injection, two-stage-classifier-guard, context-guard-has-ceiling, review-outside-injected-context, data-layer-survives-injection, escalate-on-caps-and-irreversible

### `proposer-reviewer-separate-context`

When approving knowledge, tools, UIs, patches, or update proposals.
Rule. Give produce and judge to two roles that do not share a context. Let the judge see the artifact itself, not the producer's reasoning. Self-review may lint. It does not mark done.
Check. The reviewer call's messages omit the proposer's reasoning and include the artifact bytes or structured result.
source-ids: proposer-reviewer-separate-context

### `progressive-disclosure`

When skills, retrieval, tool discovery, or agent discovery would overflow the window.
Rule. Keep a searchable catalog in context. Load bodies, pages, or schemas only when selected. Later three-layer skill and tool disclosure rules specialize this pattern.
Check. A first-call dump shows catalog lines without full bodies, and a later call shows one loaded body after a select.
source-ids: progressive-disclosure

### `append-only-state`

When updating memory, tool schemas, or conversation history.
Rule. Append new facts, events, and schemas. Do not edit earlier bytes in place. Later chapters keep raw trajectories append-only and rewrite only a reviewed archive.
Check. A replay from the log reconstructs the same states, and prefix hashes stay stable until an intentional new run.
source-ids: append-only-state

### `boundary-and-retention-sets`

When shipping a prompt, tool, or model update.
Rule. Score a boundary set of cases that must change and a retention set of cases that must stay.
Check. The CI job for an agent change has two named sets and fails if either predicate is missed.
source-ids: boundary-and-retention-sets

### `minimal-diff-reversible`

When updating knowledge, code, prompts, or programs.
Rule. Keep each change small, carry provenance, and make it independently revertible. Prefer a patch over a wholesale rewrite.
Check. The artifact store can revert the last agent-driven change without reverting unrelated edits.
source-ids: minimal-diff-reversible

## Failure diagnostics

| Symptom | First cluster | First check |
| --- | --- | --- |
| Single-shot essay labeled an agent | `agent-vs-passive-chat` | No tool call and no plan change after a result |
| Database or user drawn inside the agent object | `agent-formula-inside-boundary` | Environment is a field, not a peer |
| Stuck ticket says only "model too weak" | `expand-spaces-before-model` | Missing observation or action never named |
| Events wait for the model to call the clock | `five-tool-types` | Trigger is on the model call list |
| Fluent live numbers with zero tool results | `five-part-context` | Completion scored as prose |
| Same tool plus args repeats until the budget dies | `react-reason-act-observe` | No round cap or fingerprint |
| Demo loop shipped as a product | `harness-five-responsibilities` | No verify module, capabilities on by default |
| Autonomous checkout for a four-step pay path | `escalate-to-agent-last` | Book node reachable before pay |
| Prompt-only security | `layered-guardrails-plus-false-refusal` | No execution or data deny |
| Reviewer shares the producer's context | `proposer-reviewer-separate-context` | Reviewer saw the chain of thought |
| Prefix hash changes every turn | `append-only-state` | System prompt rewritten in place |

## Namespaced drills

Run each drill against a live system. Record a decision, not a slogan. Wrapper id `thought-questions-as-design-reviews` is collapsed here.

### `01-getting-started-q1`

Only one upgrade is allowed among a stronger model, a richer working set, or more action interfaces. Tag the miss on a failing trajectory as observation, policy, or action. Enrich context when the needed facts never entered the window. Swap the model when the facts were present and the plan still collapsed. Add a tool when the needed operation exists only as prose.

### `01-getting-started-q2`

Cumulative cache-read charges grow with the triangular sum of prefix lengths. Live trajectory length stays roughly linear. Batch-compress unmarked early tool bodies at a token threshold. Keep conclusions and identifiers. Isolate bulky intermediates. Do not compress every round.

### `01-getting-started-q3`

More autonomous tool choice widens blast radius. Framework value moves to constrain, verify, and correct (permissions, breakers, recovery, compression, tool ecosystem). Raising autonomy adds a safeguard. It does not delete harness code.

### `01-getting-started-q4`

Loops also come from a repeated error, an invented tool, compression that dropped state, stripped reasoning that breaks the API, or an unsatisfiable task. Ship a max iteration count, a fingerprint on repeated tool-plus-args, and escalate-to-human after a failure cap.

### `01-getting-started-q5`

Score a live product on working context, action interfaces, and strategy. Judge fit against the job. Propose one space or strategy change rather than a new model name.

### `01-getting-started-q6`

For a regulated booking or pay path, keep identity, search, pay, and book on a workflow spine so pay-before-book is law. Use an autonomous joint for open understanding and alternatives. Keep human confirm on large money.

### `01-getting-started-q7`

Rate tool-plus-arguments at call time on reversibility, privilege, and blast radius. Prefer deterministic allowlists and regexes on structured fields. Injected prose must not bless a dangerous path.

### `01-getting-started-q8`

High-compliance, hard-to-reverse settings want a constrained action space. A short allowed list makes the illegal action inexpressible. That is poka-yoke, not a weaker agent.

### `01-getting-started-q9`

If the human is offline, slow, or vague, fail safe. Do not execute the high-risk step by default. Finish reversible work. Write a resume packet. Notify on an async channel with a timeout that pauses, never silent proceed.

### `01-getting-started-q10`

Tag each harness helper with a kill test on the next model. Constrained JSON sampling, some external stores, and front-only prompt placement can shrink. Verify, provenance, access control, and prefix stability for cache remain.

## Depends-on

- `lessons/00-introduction.md` for the short formula, `eval-or-no-progress`, and the demo-versus-product gap.
- `references/data-shapes.md` for the Agent-inside shape used as playbook step 0.

## Needed-by

- `playbooks/context-engineering.md` expands prefix stability, disclosure, and compression.
- `playbooks/tools.md` expands form versus disclosure and execution safety.
- `playbooks/evaluating-agents.md` owns scored claims after `eval-on-own-tasks`.
- Later building chapters reuse the five patterns and the three guardrail layers.

## Open tensions

- `general-for-explore-specialized-for-risk` versus a dedicated permissioned tool. General wins for reversible composition. Dedicated wins for money, delete, send, and audit.
- `harness-covers-current-frontier` versus deleting adapters on a model drop. Keep the layer until a retirement eval passes.
- `proposer-reviewer-separate-context` versus same-context self-check. Self-review may lint. Completion stays outside the producer.
- `escalate-to-agent-last` versus jumping to autonomy. Trim ceremony. Never trim verification.
- `append-only-state` versus a rewritten memory archive. This chapter owns the append-only trajectory. Later memory work may rewrite only a reviewed store.
