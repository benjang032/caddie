# multi-agent-design-review

Multi-agent structure is an engineering means, not a capability upgrade. Add a second agent only when the collaboration injects evidence the first agent could not have produced. Then encode the context choice, the topology, the handoff contract, and the verifier as inspectable system structure rather than prompt wording.

## Use when

- should I split this into multiple agents
- add a reviewer agent
- build a manager and sub-agents
- orchestrate agents
- my agents keep overwriting each other's files
- sub-agent says done but the work is not done
- agents are stuck in a handoff loop
- design an agent swarm
- call another company's agent
- multi-agent system is too expensive
- cascading termination when one agent finds the answer
- how do I share context between agents

## Steps

Make a working checklist from every step before reasoning. Use the host's task or todo list when available. Run the steps in order, because each later step reads an answer an earlier step recorded. A step that does not apply stays in the checklist with a one-line skip reason, so a reviewer can see what was deliberately not done. When a step check fails, open the named cluster in `lessons/10-multi-agent.md`, repair the design, then continue. Symptom-first lookup lives in `references/failure-modes.md`.

### 0. Name the data shape

Fix the canonical shape before any orchestration code exists. The shape for this playbook is an information-gain gate plus a two-axis record, where axis one is shared versus isolated context and axis two is topology. Look it up in [data shapes](../references/data-shapes.md). Every later decision about communication mechanism, file layout, and termination policy derives from those two axis answers, so an unnamed shape leaves the rest of the review with nothing to check against.

Check. One architecture record states the context-sharing mode and the topology in one place, and no path contradicts it.
On failure open `lessons/10-multi-agent.md` core model. source-ids: two-dimension-design-frame, organization-is-capability-not-architecture

### 1. Gate the added agent on new information

Name the exact evidence the added agent will read, and confirm that evidence was absent from the producer's context at generation time. Wire the evidence collection into the loop rather than stating it as an instruction. When no new evidence exists, stop here and spend the budget on the single agent instead. A second copy of the same model reading the same text is cost without mechanism.

Check. In a real trajectory, the added role's input payload carries at least one field that originates outside the producer's context.
On failure open `lessons/10-multi-agent.md` cluster `information-gain-test`. source-ids: information-gain-test, information-gain-table, collective-intelligence-premise, multi-agent-cost-gate

### 2. Price the collaboration before approving it

Estimate the token multiple against the recorded single-agent baseline, then set the minimum quality delta that would justify that multiple. Write both numbers down before building. Coverage of an open search space can justify a large multiple, and a tidy diagram cannot.

Check. The same eval set has recorded cost and quality numbers for the single-agent baseline and for the proposed design. A missing baseline fails this step.
On failure open `lessons/10-multi-agent.md` cluster `information-gain-table`. source-ids: multi-agent-cost-gate, open-search-coordination-premium, debate-information-bottleneck

### 3. Fix axis one: inherited trajectory or independent contexts

List the facts each downstream stage genuinely needs. When those facts serialize into a bounded package, choose isolated context and specify the package schema. When they do not, choose shared context and plan for window growth and role inertia. Label every stage boundary in code as inherit-trajectory or explicit-package, and give each transfer edge exactly one mechanism from tool parameters, the shared file system, or the message bus.

Check. Tracing one real task end to end shows every stage boundary labeled in code, and no edge carries the same fact through two mechanisms.
On failure open `lessons/10-multi-agent.md` cluster `shared-vs-isolated-context`. source-ids: shared-vs-isolated-context, three-communication-mechanisms, ipc-paradigm-mapping

### 4. Fix axis two: peer, manager, or decentralized

Count the subtasks and inspect the dependency graph. Peer collaboration holds for two or three roles in an improvement loop. A manager belongs where planning, scheduling, and integration must be centralized, which is roughly where subtask count passes five or scheduling turns dynamic. The decentralized form belongs where routing judgment lives inside each role and manager failure is unacceptable. Record the choice, and classify the system by the code site that decides the next actor rather than by the label in the documentation.

Check. The declared topology matches the live subtask count and dependency graph, and a single next-actor decision site is reported as orchestration.
On failure open `lessons/10-multi-agent.md` cluster `three-topologies`. source-ids: three-topologies, graph-engineering-terminology, orchestration-vs-choreography, swarm-label-ambiguity

### 5. Declare the file system mount table

Build the mount table over the four areas, which are the per-instance private scratchpad, the shared workspace, external read-mostly mounts, and read-only built-in resources. Fill visibility, lifecycle, read and write permission, and concurrency control for every area, and default to private. Promote only finished artifacts into the shared workspace, and exchange paths rather than inlined contents.

Check. The filled table has no blank cells, and no writable multi-party area lacks a declared concurrency mechanism.
On failure open `lessons/10-multi-agent.md` cluster `four-area-checklist`. source-ids: four-area-checklist, agent-virtual-file-system, scratchpad-isolation, shared-workspace-hotspot, mounted-external-resources, builtin-readonly-resources, path-as-universal-interface

### 6. Stand up the control plane

Build the shared transport once and let every topology import it. Carry sender, target or broadcast marker, message type, and structured payload in one envelope. Read progress from a small agreed progress file instead of a periodic status query. Persist trajectories as append-only event lines for diagnosis rather than as the routine channel between agents. Terminate by signalling first, letting the worker finish its current step at a safe point, releasing resources, acknowledging, then exiting, and force a kill only for workers that never acknowledge. Cascade cancellation down the creation tree, and cap total spend and concurrency with per-spawn budgets.

Check. One task's message log reconstructs the whole chain from envelope fields, a test cancellation produces an acknowledgment from every worker, and a synthetic burst is throttled locally rather than rejected by the provider.
On failure open `lessons/10-multi-agent.md` clusters `data-plane-control-plane`, `graceful-then-forced-termination`, and `agent-resource-scheduling`. source-ids: data-plane-control-plane, message-envelope-format, progress-file-contract, graceful-then-forced-termination, cascade-cancel-lifecycle-tree, agent-resource-scheduling

### 7. Define the handoff schema

Before specifying the desired schema, reconstruct one actual sender-to-receiver path through the harness or transport. Record what the sender or action runtime produced, what the receiving model actually saw at its next decision, and what the terminal handoff carried to the parent. At each edge, identify any dropped, summarized, rewritten, or misclassified information and point to the captured input, result, or handoff rather than inferring knowledge from runtime state or telemetry.

Then build every transfer from three parts, which are the task with its acceptance criteria, the settled facts and constraints, and references to structured artifacts. Exclude the sender's private reasoning trace, both because it defeats the isolation the handoff was chosen for and because a validator that inherits upstream reasoning inherits the framing it was meant to test.

Check. The reconstruction separately answers whether the producer possessed the result, the receiving model saw it, and the terminal handoff carried it. A real handoff payload contains the three parts, carries artifacts as references, and attaches no reasoning trace.
On failure open `lessons/10-multi-agent.md` cluster `handoff-package-three-parts`. source-ids: handoff-package-three-parts, metagpt-sop-message-pool, swarm-peer-handoff-cycle-guard, autogen-hybrid-groupchat

### 8. Install the verifier

Give the loop a shape that discovers the next work item, executes, verifies, and records progress. Hold completion authority outside the executing agent. Deny the reviewer write access to tests, evidence collectors, and the release gate, and require every rejection to state a locatable repair condition. Judge a completion claim against the three known forms of premature stopping, which are partial work declared whole, one blocked path treated as impossibility, and a loop that never closed.

Check. The code path that marks work complete is reachable only from the verifier, and the reviewer role holds no write permission on tests or gate configuration.
On failure open `lessons/10-multi-agent.md` cluster `reviewer-independence-invariant`. source-ids: reviewer-independence-invariant, proposer-reviewer-loop, no-self-correction-without-external-feedback, planner-generator-evaluator, loop-engineering-verifier-bottleneck, premature-termination-taxonomy

### 9. Bound every loop

Give each iterative or self-continuing loop a round cap, a cost ceiling, a cancellation check at a safe point, and a stop condition that a verifier evaluates. Keep loop state in a durable control plane outside the chat history so a context refresh resumes the same objective and gates. Treat a missing bound as a defect rather than as a tuning question.

Check. Every loop in the codebase shows a round cap, a cost ceiling, and a cancellation check, and loop exhaustion is never reported as success.
On failure open `lessons/10-multi-agent.md` cluster `loop-engineering-verifier-bottleneck`. source-ids: loop-engineering-verifier-bottleneck, loopx-governed-loop, mea-manage-execute-audit, runaway-loop-bounds

### 10. Add fault tolerance for plausible wrong output

Assume agents fail by continuing to run while producing confident wrong output. Guard same-file writes with versioned optimistic locking and guard cross-file logical conflicts with per-agent working copies plus semantic validation at a merge gate. Have at least one validator read raw evidence and the final conclusion while ignoring the upstream chain. Vary model, context, tools, or visible evidence deliberately, and collect independent judgments before aggregation. Give every agent a namespace and a quota, and settle races through one idempotent claim.

Check. Two concurrent writers to one file produce one rejection and one retry, the validator payload holds evidence without upstream reasoning, and a batch of nominally independent agents produces no identical artifact names.
On failure open `lessons/10-multi-agent.md` cluster `mast-taxonomy` and the failure diagnostics rows for the first three named modes. source-ids: concurrency-conflict-control, cascading-error-amplification, homogeneous-convergence, byzantine-agent-faults, designed-cognitive-diversity

### 11. Predefine arbitration

Declare objective priority, resource ownership, and permission boundaries in the runtime before any agent starts. Give every mutable resource one owner and deny write permission to everyone else. Route a conflict that verifiable rules cannot settle to a human arbitration path rather than to another round of negotiation.

Check. Every mutable resource names a single owner, and the runtime holds an escalation path that pauses work instead of looping.
On failure open `lessons/10-multi-agent.md` cluster `mast-taxonomy` and the failure diagnostics row for objective conflict. source-ids: objective-conflict-arbitration, same-machine-peer-resource-negotiation, judge-held-information-access-control

### 12. Cross a trust boundary only with the standard protocol

Keep tool parameters, shared files, and the message bus inside one organization. Adopt the cross-agent standard protocol only on edges where the counterparty cannot be inspected. On such an edge, publish a capability document at a known address, model each unit of collaboration as a task with an explicit state machine, and exchange only tasks and artifacts so internal prompts and reasoning stay private.

Skip when no edge leaves the organization. Record the skip as no cross-organization edge in this design.

Check. Captured traffic on one external call contains only task records and artifacts, and no internal edge carries the external protocol.
On failure open `lessons/10-multi-agent.md` cluster `a2a-three-elements`. source-ids: a2a-three-elements, a2a-trust-boundary-layer

### 13. Measure per-role justification and remove what fails

Measure per-agent context usage, cost, and quality against the single-agent baseline from step 2. Confirm the manager's context stays flat as completed artifact count rises, since a manager that accumulates contents rather than indexes becomes the system bottleneck. Delete roles that cannot point to a recorded binding constraint that justifies them.

Check. A long run shows flat manager context growth, and every surviving role names the constraint it exists to relieve.
On failure open `lessons/10-multi-agent.md` cluster `manager-single-point-bottleneck`. source-ids: manager-single-point-bottleneck, context-isolation-by-decomposition, agents-as-tool-registry, strongest-model-to-planner, lingtai-role-taxonomy

### 14. Track comprehension debt

Treat unreviewed accumulated agent output as debt rather than as progress, and record the backlog as a number. Schedule periodic architectural review by a person who can explain the current system without reading agent output.

Check. The responsible engineer explains the live architecture unaided. Failure to do so measures the debt already accrued.
On failure open `lessons/10-multi-agent.md` cluster `agent-society-three-lenses` and the failure diagnostics row for comprehension debt. source-ids: comprehension-debt, agent-society-three-lenses

Keep skipped steps visible. Write the step number, the reason in one line, and the condition that would reopen it. A silent omission reads as a completed review, which is the same defect this playbook installs a verifier to prevent.

## Open next

- [evaluating-agents.md](evaluating-agents.md) to measure the collaboration as a pair of model and harness, since steps 2 and 13 both need a baseline that only an eval environment produces.
- [tools.md](tools.md) when a sub-agent is registered as a tool, or when a role boundary turns out to be a permission boundary that belongs in harness code.

## Reply

Report what changed in the architecture record, which axis answers and topology were chosen with the evidence behind them, and what remains open, including every skipped step and every failed check with its cluster in `lessons/10-multi-agent.md`.
