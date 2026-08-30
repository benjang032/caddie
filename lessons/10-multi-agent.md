# Multi-agent collaboration notes

Extensive notes for slug `10-multi-agent`. The runnable procedure lives in [../playbooks/multi-agent.md](../playbooks/multi-agent.md). Open this file only when a playbook step names a cluster. Eighteen clusters, collapsed from ninety-one extracted lessons.

## Terms

| Term | Meaning |
| --- | --- |
| shared context | A later agent inherits the earlier agent's full trajectory while taking a new system prompt and tool set. |
| non-shared context | Each agent holds an independent trajectory and cannot read another agent's trace. |
| collaboration topology | Where control and information flow, in peer, manager, or decentralized form. |
| orchestration and choreography | The microservices names for centrally scheduled and locally decided collaboration. |
| information gain | Evidence a collaboration supplies that the producing agent could not have held while answering. |
| loop engineering | Design of the outer loop that discovers work, executes, verifies, and records progress. |
| handoff package | Task with acceptance criteria, settled facts, and artifact references. |
| agent virtual file system | One tree mounting private scratchpads, a shared workspace, external resources, and read-only built-ins. |
| progress file | A small agreed-format file a sub-agent updates so the caller reads distilled progress cheaply. |
| message envelope | The uniform structure carrying sender, target, message type, and payload on every inter-agent message. |
| Byzantine agent fault | A failure where the agent keeps running while producing plausible wrong output. |
| comprehension debt | Accumulated agent output that no person has understood. |

## What this is for

This chapter decides whether a system should hold more than one agent, and it constrains the resulting structure so that failure stays diagnosable. The economics matter more than the architecture, because a group of agents costs a multiple of one agent and repays that multiple only through mechanisms that a single agent cannot reach, namely division of labor, mutual verification against outside evidence, and accumulated shared artifacts. The chapter then supplies the runtime primitives that keep those mechanisms honest, which are a declared file layout, a control plane, a bounded loop, and a verifier the producer cannot edit. Read it as organization design under current model and context limits rather than as a capability upgrade.

## Core model

The data shape is an information-gain gate plus a two-axis record. Axis one records whether a downstream agent inherits the upstream trajectory or receives an explicit package. Axis two records whether control lives in a peer loop, a manager, or each role. Both answers belong in one architecture document as governing constraints, because communication mechanism, file layout, and termination policy are derived from them rather than chosen independently. Organization-level capability is the outcome target, and multi-agent structure is one engineering means toward it, so every role must point at the binding constraint it exists to relieve.

source-ids: two-dimension-design-frame, organization-is-capability-not-architecture

## Clusters

### `information-gain-test`

When. Before adding any reviewer, debater, or extra role to a working single-agent system.

Rule. Add an agent only when it reads information that was unavailable to the producing agent at generation time, and collect that evidence inside the loop rather than requesting it in prompt text. Justify the group by the mechanism it adds and not by the count of agents. Reject a design in which every role shares one model, one prompt, one tool set, and one evidence source.

Check. Inspect the added role's input payload in a real trajectory and confirm at least one field originates outside the producer's context. Confirm the recorded token multiple and expected uplift exist before any build.

source-ids: information-gain-test, collective-intelligence-premise, multi-agent-cost-gate

### `information-gain-table`

When. Triaging a proposed collaboration mode.

Rule. Sort each candidate mode into no-new-information or new-information, and treat the first group as ineffective or harmful by default. Record which channel supplies the evidence, which is normally execution, rendering, or tool lookup. Open search is the standing exception where a coordinated swarm earns its token multiple through coverage, provided workers read peer findings and a separate arbiter produces no candidates of its own.

Check. Take the eval log for the collaboration stage and confirm the measured uplift belongs to a mode marked new-information. A debate comparison without an equal thinking-token control is uninformative.

source-ids: information-gain-table, open-search-coordination-premium, debate-information-bottleneck

### `shared-vs-isolated-context`

When. Defining how a downstream stage receives upstream work.

Rule. Choose shared context when the needed facts do not serialize into a bounded package, and choose isolated context when modularity, concurrency, or permission separation outweighs total recall. Give every transfer edge exactly one declared mechanism from tool parameters for small typed payloads, the shared file system for persistent artifacts, and the bus for asynchronous or fan-out delivery. Then label each edge shared-memory or message-passing and apply that paradigm's discipline, which means versioning and retry for shared writes and envelopes, ordering assumptions, and duplicate handling for the bus.

Check. Trace one real task and confirm every stage boundary is labeled inherit-trajectory or explicit-package in code. Confirm no fact arrives through two mechanisms, every shared-directory write shows a version or lock check, and every bus consumer handles duplicates.

source-ids: shared-vs-isolated-context, three-communication-mechanisms, ipc-paradigm-mapping

### `os-mapping-table`

When. Naming or designing runtime primitives for isolated agents.

Rule. Model each isolated agent as a process with private state, asynchronous messages, and the ability to spawn children, then keep an explicit correspondence table between operating-system constructs and agent constructs. Implement the agent side of every row the design relies on, and extend the table so that context compression maps to paging, tool allowlists and read-only mounts map to file permissions, cyclic handoff detection maps to deadlock detection, and event handling maps to scheduling. Record the row that has no counterpart, which is enforcement, since hardware constrains a process while guidance constrains an agent only probabilistically. Budget real work for task-state synchronization and cross-agent debugging as the price of isolation.

Check. Name the concrete runtime primitive behind each row, and treat missing primitives as the design backlog. Reconstruct one failed run across agents from logs using only the correlation identifier. Any code path that reads another agent's trajectory object directly breaks the isolation claim.

source-ids: os-mapping-table, isolated-context-process-model, isolation-costs-sync-and-debug

### `stage-role-switching`

When. One long task passes through stages with different responsibilities and no detail may be lost.

Rule. Switch the role rather than the trajectory. Change the system prompt and the tool set together at the stage boundary, since the available tools are themselves a strong role signal, and reinforce the current role near the end of the context where recent tokens compete with a long inherited history. Carry role guidance in a skill when the difference is knowledge, procedure, or style, and change the prompt or hand off to a separate agent when the difference is permissions or a forbidden action class. Enforce every hard tool restriction in harness code.

Check. Audit the trajectory after a switch and confirm actions use the new role's tools and criteria. Attempt a forbidden call for a restricted role in a test and confirm the harness rejects and logs it. No dangerous tool may be restrained by skill text alone.

source-ids: stage-role-switching, prompt-switch-vs-skill-carrier, harness-enforced-tool-boundary

### `three-topologies`

When. Choosing where control flow lives.

Rule. Use peer collaboration for two or three roles in an improvement loop, and build it from the roles, the communication mechanism, and the stop condition and nothing more. Move to a manager once subtasks exceed roughly five or scheduling turns dynamic. Choose the decentralized form when routing judgment belongs to each role and manager failure is unacceptable. Draw the execution graph with nodes for agents, plain programs, and human decisions, and edges for dependencies, conditional routing, and failure paths. Classify the system by the code site that selects the next actor, since a single such site is orchestration whatever the documentation claims, and resolve a swarm label into either a peer handoff network or a manager scaled to many workers.

Check. Compare the declared topology against the live subtask count and dependency graph. Confirm every retry and failure path appears as a graph edge, and that killing one non-critical agent in a decentralized design leaves the rest rerouting.

source-ids: three-topologies, graph-engineering-terminology, peer-pattern-scope, decentralized-motivation, orchestration-vs-choreography, swarm-label-ambiguity

### `four-area-checklist`

When. File system layout design and review.

Rule. Compose the tree from explicitly declared mounts and isolate by default. Audit four areas across visibility, lifecycle, read and write permission, and concurrency control, and reject any blank cell. Keep intermediate work in a per-instance scratchpad that dies with the instance and promote only finished artifacts. Treat the shared workspace as the single user-visible exchange point and the concurrency hotspot. Mount external sources read-only, eventually consistent, with declared timeouts and credential scope. Ship shared knowledge as a globally read-only package exposed index first. Exchange paths rather than contents.

Check. Print the mount table and confirm every writable path maps to a declared area with stated visibility and a concurrency mechanism. Confirm the shared workspace holds only promoted artifacts, a write to a read-only mount is refused, a typical trajectory loads the index before a full document, and handoff payloads carry large artifacts as references.

source-ids: four-area-checklist, agent-virtual-file-system, scratchpad-isolation, shared-workspace-hotspot, mounted-external-resources, builtin-readonly-resources, path-as-universal-interface

### `data-plane-control-plane`

When. Before implementing any topology.

Rule. Stand up the shared file system as the data plane and messaging, status, termination, and scheduling as the control plane, then build topologies on top so no pattern invents its own transport. Carry sender identity, target or broadcast marker, message type, and structured payload in one system-wide envelope. Use direct calls only for a small fixed topology and move to a publish and subscribe bus once connections multiply or senders must not block. Read progress from an agreed progress file instead of a periodic status query. Persist trajectories as append-only event lines for diagnosis, not as the routine channel between agents.

Check. Reconstruct one task's full chain from envelope fields alone. Confirm the spawn payload names a progress path whose modification time advances during a run, and that repeated identical status queries do not appear in trajectories. Confirm each topology imports the shared modules and defines no transport of its own.

source-ids: data-plane-control-plane, message-envelope-format, point-to-point-vs-bus, status-polling-antipattern, progress-file-contract, trajectory-persistence-jsonl

### `graceful-then-forced-termination`

When. Work in progress becomes irrelevant, most often after another worker succeeds.

Rule. Verify the reported result against checks the workers cannot see, claim the winner through an idempotent settlement guarded by a lock or transaction, broadcast cancellation once, and assemble only after acknowledgments arrive or a timeout expires. Let each worker reach a safe point, release resources, acknowledge, then exit, and force a kill only for a worker that never answered. Cascade cancellation to every descendant, and require a detached background agent to declare a new lifecycle root explicitly. Treat a progress file whose modification time has stalled past a defined interval as an inactive agent and fire the fallback.

Check. Inject two simultaneous success events and confirm exactly one settlement and one cancellation broadcast. Cancel a parent and confirm no descendant survives. Simulate a hung worker and confirm the watchdog fires within the threshold.

source-ids: graceful-then-forced-termination, verified-first-success-settlement, cascade-cancel-lifecycle-tree, stuck-detection-timeout

### `agent-resource-scheduling`

When. More than a couple of agents can run at once.

Rule. Schedule tokens, money, and concurrency as scarce resources. Set per-spawn step and token budgets proportional to subtask complexity, match model strength to task difficulty, cap total concurrency, and allow preemption for a more urgent task. Expose total and remaining budget to the agent on every step so strategy shifts from broad exploration to focused depth as the remainder falls. Let the manager reallocate budget from verified progress signals and terminate explorations that have gone astray.

Check. Confirm dispatch payloads carry varying budgets rather than a constant, that a synthetic burst is throttled locally rather than rejected by the provider, and that trajectories at small and large budgets differ in phase structure. Confirm at least one reallocation traces to a verified progress signal rather than a self-assessment.

source-ids: agent-resource-scheduling, manager-allocates-step-budget, budget-aware-stepping, reasoning-scheduler-reallocation

### `loop-engineering-verifier-bottleneck`

When. Building any long-running agent that decides for itself when to stop.

Rule. Build a loop that discovers the next work item, executes, verifies, and records progress, and let a verifier rather than the model decide whether stopping is safe. Keep objective, boundary, gates, todos, evidence, quota, and handoffs in a durable control plane outside the chat history, and allow only independently verified results to advance progress or spend quota. Generate each next bounded subtask from verified progress and failure evidence, execute it in a fresh context, and audit the result read-only before admitting it. Test every completion claim against the three forms of premature stopping, which are partial work declared whole, one blocked path treated as impossibility, and a loop that never closed.

Check. Confirm the code path marking work complete is reachable only from the verifier. Refresh the context mid-task and confirm the loop resumes from durable state with the same objective and gates. Confirm each requested item, each attempted channel, and the closing condition are individually evidenced.

source-ids: loop-engineering-verifier-bottleneck, loopx-governed-loop, mea-manage-execute-audit, premature-termination-taxonomy

### `reviewer-independence-invariant`

When. Any generate-then-review arrangement.

Rule. Run the loop as propose, gather independent evidence by execution or rendering, review candidate plus evidence, then iterate until the standard is met or the budget ends. Agree completion criteria before generating and exercise the real artifact rather than a description of it. Forbid the reviewer from modifying tests, the evidence collector, or the release gate, and require every rejection to state a locatable repair condition. A model reviewing its own answer with no external feedback adds no information and can lower accuracy.

Check. Confirm the reviewer role holds no write permission on test files or gate configuration, and sample findings for location and expected-behavior fields. Run the eval with the review step enabled and disabled, and drop the step when the enabled run is not better.

source-ids: reviewer-independence-invariant, proposer-reviewer-loop, no-self-correction-without-external-feedback, planner-generator-evaluator

### `designed-cognitive-diversity`

When. Independent judgment or independent review is the point of the design.

Rule. Engineer diversity instead of assuming that several instances of one model differ. Vary models, contexts, tools, visible evidence, or responsibilities, and capture each judgment before exposure to the others. Three practice modes follow from that discipline. Debate assigns opposing positions so each turn must answer specific claims from the previous turn. Brainstorming generates independently first and cross-pollinates second. A panel of experts assigns one complementary domain per role and requires the output to name a cross-domain constraint. None of these beats a compute-matched single agent on text alone, so the structure earns its place through independent sampling with aggregation or through a generation and verification split.

Check. Confirm the run record holds each peer's judgment before exposure and names the axis on which peers differ. Confirm independent-round idea sets differ across agents, and that panel output names at least one constraint absent from every single-domain assessment.

source-ids: designed-cognitive-diversity, debate-pattern, brainstorming-pattern, panel-of-experts-pattern

### `manager-single-point-bottleneck`

When. A manager coordinates more than a few agents or a deep task tree.

Rule. Introduce a manager to decompose, assign, track, handle exceptions, and integrate, and expose each specialist through the ordinary tool-call interface so adding a capability is a registry entry rather than a manager edit. Keep the manager's context to plan, call records, progress, and artifact indexes, and hold large artifacts in the file system. Spend the strongest model and the most careful prompt on planning, and review the plan before any executor starts. Sequence stages only where a genuine dependency exists, back parallel work with a bus and a status table, and distinguish a persistent hub from disposable workers and persistent specialists.

Check. Confirm every subtask in the plan record carries an owner, dependencies, status, and acceptance criteria. Measure manager context across a long run and confirm it stays flat as artifact count rises. Fail one worker deliberately and confirm the batch continues with the failure recorded.

source-ids: manager-single-point-bottleneck, manager-pattern-trigger, agents-as-tool-registry, strongest-model-to-planner, sequential-coordination, parallel-coordination-message-bus, context-isolation-by-decomposition, lingtai-role-taxonomy

### `handoff-package-three-parts`

When. Every transfer of work between agents without shared context.

Rule. Build the package from the task with its acceptance criteria, the settled facts and constraints, and references to structured artifacts, and exclude the sender's reasoning trace. Give each role a standardized deliverable that serves as the interface, and publish deliverables into a pool from which roles take only subscribed message types. Carry the visited-agent chain and remaining budget inside the handoff under runtime control, reject a handoff to an already visited agent, and escalate when budget runs out. Label a shared transcript with a central speaker selector as a hybrid rather than as decentralized.

Check. Inspect a real payload for the three parts and confirm no reasoning trace is attached. Force a handoff back to a visited agent and confirm the runtime rejects it as a cycle. Adding a role should touch subscriptions only.

source-ids: handoff-package-three-parts, metagpt-sop-message-pool, swarm-peer-handoff-cycle-guard, autogen-hybrid-groupchat, same-machine-peer-resource-negotiation

### `a2a-three-elements`

When. An agent must call an agent built and operated by another organization.

Rule. Publish a capability metadata document at a known address, model each unit of collaboration as a task with a defined state machine, and exchange only tasks and artifacts so prompts and reasoning stay private. Keep tool parameters, shared files, and the bus for internal edges, and adopt the standard protocol only where a party cannot be inspected.

Check. Capture one cross-organization call and confirm the traffic holds only task records and artifacts with state transitions visible. Confirm no internal edge carries the external protocol.

source-ids: a2a-three-elements, a2a-trust-boundary-layer

### `mast-taxonomy`

When. Diagnosing a multi-agent system that underperforms.

Rule. Keep three buckets and label each observed failure as a system design flaw, an inter-agent alignment failure, or a missing task verification, then fix the labeled category rather than the symptom. Design failures call for repaired interfaces, reduced role overlap, and corrected tool configuration. Alignment failures call for restated objectives, clarified message semantics, and contradiction detection. Verification failures call for acceptance checks that do not rest on an agent's claim. Escalate to redesign when local patches yield small gains. Assume Byzantine faults throughout, since an agent normally fails by continuing to run while supplying confident wrong output, so every consumed output needs a deterministic check or an independent vote. The chapter names six concrete modes under these buckets, listed as rows in failure diagnostics below. The MAST paper carries a longer mode list than the chapter writes, and [../references/source.md](../references/source.md) points at it.

Check. Keep a labeled failure register for recent incidents and confirm each fix targets the labeled category. For every agent output consumed downstream, name the deterministic check or vote that guards it.

source-ids: mast-taxonomy, byzantine-agent-faults

### `agent-society-three-lenses`

When. Many agents coexist for long periods without a single shared goal.

Rule. Read open populations through spontaneous social structure, market-based allocation, and strategic behavior under information asymmetry, and measure all three rather than task success alone. Long-lived social agents need a scored memory stream, a periodic reflection step, and a revisable plan, and coordination may emerge from one seeded intention with no coordinating code. Reflection during activity updates immediate state only, so a lesson becomes durable capability only after outcome evaluation, cross-trajectory synthesis, and later validation. Long-horizon simulation needs a coarse loop, a separate model acting as environment authority, external scoring, and file-based self-managed memory, and its top self-relative-improvement trajectories can train the base model. At population scale, expect unplanned norms, competitive behavior distinct from single-agent coherence, and collusion signals through public channels. Where central orchestration does not fit, allocate work by price with deterministic verification, escrow, and reputation. Enforce information asymmetry with a code-driven judge that holds global state.

Check. Confirm outcome scores come from the environment rather than from agent reports, that durable guidance entries carry evaluation and validation records, that no code arranges an emergent outcome, and that every agent invocation payload holds no field outside its role's entitlement.

source-ids: agent-society-three-lenses, generative-agent-architecture, emergence-without-orchestration, reflection-scope-boundary, long-horizon-society-loop, society-as-training-signal, open-scale-emergent-norms, competitive-market-emergence, market-based-coordination, judge-held-information-access-control

Collapsed into the clusters above and the playbook reply shape. source-ids: multi-agent-synthesis, thought-question-drills

## Failure diagnostics

The six named modes the chapter writes, as rows under the three buckets.

| Symptom | Mode | First check |
| --- | --- | --- |
| A later write erases an earlier one, or cross-file references break after a rename that no file-level check caught | Concurrency conflict in a shared file system. Apply optimistic locking for same-file writes and working-copy isolation plus semantic validation at a merge gate for cross-file conflicts | Run two agents writing one file and confirm the second write is rejected and retried, then run a cross-file renumbering and confirm the merge gate catches broken references. source-ids: concurrency-conflict-control |
| A small upstream mistake grows across handoffs, and validators repeat the framing they were meant to test | Cascading error amplification. Have at least one agent ignore upstream reasoning and check only whether raw evidence supports the conclusion | Inspect the validator payload and confirm it holds raw evidence and the conclusion without the upstream chain. source-ids: cascading-error-amplification |
| Clones agree on the same wrong answer, or many agents collide on one resource name | Homogeneous convergence. Vary models, contexts, and data sources, and add namespaces, quotas, and rate limits | Start a nominally independent batch on one task and count identical artifact names or identical choices. Any collision means missing namespacing or missing diversity. source-ids: homogeneous-convergence |
| A defect bounces between roles with no owner, or agents revoke one another's permissions | Objective conflict without arbitration. Declare objective priority, resource ownership, and permission boundaries before start, and pause for human arbitration | For every mutable resource, name its single owner and confirm no other agent holds write permission. source-ids: objective-conflict-arbitration |
| A repair loop retries the same fix forever, or budget exhaustion is reported as success | Runaway loop. Give every loop a budget, a cancellation path, and a stop condition | Inspect each loop for a round cap, a cost ceiling, and a cancellation check. A loop missing any of the three is a defect. source-ids: runaway-loop-bounds |
| Review degrades into accepting whatever the agent claims, and nobody can explain the live system | Comprehension debt. Require a person to hold a working understanding and treat unreviewed output as debt | Ask the responsible engineer to explain the current architecture without reading agent output. source-ids: comprehension-debt |

## Drills

Namespaced rewrites of the chapter's open questions. Run one as a design review, not as a quiz.

### `10-multi-agent-q1`

A reviewer stage inherits an analyst's trajectory and keeps judging by the analyst's criteria. Detect the bleed with a trajectory audit after the switch, remove it by switching prompt and tool set together plus a short role block near the context tail, and drop shared context at that boundary when interference survives both measures.

### `10-multi-agent-q2`

A manager's decomposition caps the whole system. Make it trustworthy by assigning the strongest model to planning, cross-validating the plan before any executor starts, and requiring acceptance criteria and dependencies per subtask so an incoherent plan is visible as a missing field.

### `10-multi-agent-q3`

Decentralized designs inherit organizational pathologies, which appear as unclear role interfaces, divergent objective understanding, and unverified completion claims, plus amplified errors, work cycling between two roles, and group conversations that expand without converging. Ship only with contractual interfaces, one envelope, per-state acceptance verification, evidence-based cross-validation, and a blame-loop detector.

### `10-multi-agent-q4`

Parallel workers race for one answer. Terminate by verifying the find against hidden checks, settling once through an idempotent claim, broadcasting cancellation, awaiting acknowledgments or a timeout, then aggregating, with a safe-point cancellation check inside every worker loop and cascade cancellation to spawned children.

### `10-multi-agent-q5`

Versioned writes alone leave cross-file contradictions, directory chaos, and destructive mistakes. Govern with area partitioning, directory-level locks for changes that span files, enforced naming conventions, version history for rollback, and least-privilege write scopes.

### `10-multi-agent-q6`

An agent pays another party for work. Build acceptance from deterministic verification, escrowed payment, third-party arbitration, and a reputation record that feeds pricing, so cheap low quality cannot crowd out good work. Model the human as evidence source, acceptor, arbitrator, accountable authorizer, and goal setter rather than only as a physical actuator.

### `10-multi-agent-q7`

Total transparency can freeze a group into one line of thought. Share artifacts and settled facts freely, withhold reasoning chains from validators, and vary prompt or model on any path where independent judgment is the point.

### `10-multi-agent-q8`

Raising a coding agent from thirty steps to three hundred does not improve results on step count alone. Expose total and remaining budget every step, switch phase structure by budget size, and place milestone checkpoints that detect shallow saturation. Treat the operating-system correspondence table the same way, as a design backlog whose borrowed constructs need explicit harness checks wherever the original relied on hardware enforcement.

## Depends-on

- `isolate-bulky-exploration-in-subagents` in `lessons/02-context-engineering.md` supplies the single-agent isolation move that this chapter's step 1 must rule out first.
- `form-vs-disclosure-independent` in `lessons/04-tools.md` governs a sub-agent registered as a tool.
- `trajectory-is-append-only` in `lessons/03-memory-knowledge.md` owns the storage rule behind `trajectory-persistence-jsonl`.
- `tests-pass-as-completion` in `lessons/05-coding-agent.md` is the same verification invariant as `reviewer-independence-invariant`.

## Needed-by

- `lessons/07-evaluating-agents.md` supplies the baseline that `multi-agent-cost-gate` and per-role justification both require.
- `lessons/09-continual-evolution.md` inherits the frozen approval root idea from the verifier the producer cannot edit.

## Open tensions

- Isolation versus recall. `shared-vs-isolated-context` isolates by default, and shared context wins only when no bounded package preserves a required fact.
- Structure versus compute. `collective-intelligence-premise` argues for organizational mechanism while `debate-information-bottleneck` shows text-only debate matching a single agent at equal compute. The gain must come from outside evidence, designed divergence, or context capacity.
- Central judgment versus resilience. `manager-single-point-bottleneck` concentrates the ceiling in one role and `decentralized-motivation` removes that role at the cost of cycling handoffs, which `swarm-peer-handoff-cycle-guard` then has to bound.
- Transparency versus independence. `designed-cognitive-diversity` needs withheld reasoning on validation paths, which contradicts the coordination benefit of a shared transcript.
- Taxonomy completeness. `mast-taxonomy` keeps three buckets and six written modes, and the source paper lists more. Treat the buckets as the diagnostic surface and the paper as background.
