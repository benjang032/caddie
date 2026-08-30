# coding-agent-harness-review

Copy these steps into the todolist before reasoning about the agent. Work them in order. A step that does not apply stays in the list with its skip reason recorded, because a silent omission reads later as a completed check.

Every fail-open line names one cluster in [lessons/05-coding-agent.md](../lessons/05-coding-agent.md). Open the lesson file only when a check actually fails.

## use_when

- build a coding agent
- why does my coding agent keep failing
- add code execution to my agent
- review my agent's tools and sandbox
- my agent says done but nothing works
- make my agent generate reports, slides, or dashboards
- let my agent write another agent
- secure an agent that runs shell commands

## Steps

**0. Name the data shape.**
The canonical shape here is coding core plus filesystem hub. Working state lives in context and durable state lives in tracked files. Confirm the shape in [references/data-shapes.md](../references/data-shapes.md) before writing logic, and state where memory, artifacts, and generated scripts resolve on disk.

**1. Classify the task space, then place code execution.**
Decide whether the task boundary is open-ended or closed. Make code execution the architectural hub for open-ended work with diverse artifacts, and keep it as one foundational tool inside an agent built around a fixed process. Record the classification and the matching tool permissions in the design document.
Fail open into cluster `coding-core-plus-filesystem`. source-ids: coding-core-plus-filesystem, coding-core-applicability-boundary, coding-agent-build-order.

**2. Audit tool coverage, not tool count.**
Confirm the registry reaches all five operation categories, which are browse, read, modify, execute, and search. Confirm partial edit exists as a tool distinct from whole-file write, and confirm no tool exists only to call another agent.
Fail open into cluster `seven-core-tools`. source-ids: seven-core-tools, toolbox-is-reference-not-taxonomy.

**3. Confirm one workspace holds durable state.**
Memory, artifacts, and generated scripts belong in version-controlled text under one directory. Test the claim by correcting a single wrong memory as a user and confirming one text edit with a reviewable diff is enough.
Fail open into cluster `filesystem-as-hub`. source-ids: filesystem-as-hub, markdown-memory-over-vector-db, memory-first-task-loop.

**4. Read the project instruction file.**
Verify it names build and test commands, style constraints, and restricted directories. Verify nothing task-specific sits ahead of it in the assembled context. Where key orientation documents are missing, draft an architecture overview and a directory guide before the first edit.
Fail open into cluster `workflow-trimming-by-task-size`. source-ids: project-instruction-files, orient-before-editing, ai-ready-repo-gauge.

**5. Name the four harness components.**
Name an acceptance baseline, an execution boundary, feedback signals, and a rollback mechanism. Point each one at a file or a running system. A component described only in prose counts as absent.
Fail open into cluster `harness-four-components`. source-ids: harness-four-components, coding-inherits-software-engineering-harness, harness-transfer-principles.

**6. Quadrant the current task set.**
Label each live task by goal clarity and by whether verification is automated. Pick the single harness investment that moves the largest group toward clear goals with automated verification, and confirm the worst outcomes cluster outside that quadrant.
Fail open into cluster `task-quadrant-table`. source-ids: task-quadrant-table.

**7. Gate completion on an executed suite.**
Confirm a test execution appears after the final edit in every trajectory that claims completion, and that a lint or review pass follows the passing run. The producing model never sets the done bit.
Fail open into cluster `tests-pass-as-completion`. source-ids: tests-pass-as-completion, self-review-before-delivery.

**8. Check the four failure layers and their detectors.**
Confirm the error handling module maps every branch to the API layer, the tool layer, the context layer, or the control-flow layer, with no unclassified catch-all. Confirm retryability comes from an explicit error-to-strategy map rather than from an assumption at the retry site. Confirm a call fingerprint detector and a per-path consecutive-failure counter both exist.
Fail open into cluster `failure-taxonomy-four-layers`. source-ids: failure-taxonomy-four-layers, retryability-classification, no-progress-pattern-detection, idle-watchdog-liveness.

**9. Put a ceiling on every recovery path.**
Confirm each retry, degradation, compaction, and continuation path carries an attempt ceiling justified by observed session statistics, plus a defined terminal action. Confirm the error path invokes no model, and confirm a recursion-depth counter breaks any residual cascade.
Fail open into cluster `graded-recovery-escalation`. source-ids: recovery-ceilings-from-data, death-spiral-defense, graded-recovery-escalation, withhold-errors-until-recovery-fails.

**10. Store trajectories vendor-neutral.**
Confirm the stored format records tool calls as name plus arguments and splits reasoning into portable text and a non-portable vendor credential. Switch vendors mid-trajectory and confirm no provider error appears and no completed tool call repeats.
Fail open into cluster `graded-recovery-escalation`. source-ids: neutral-trajectory-and-handover, trajectory-integrity-repair.

**11. Measure the seven efficiency mechanisms.**
Check streaming dispatch of the first valid tool call, parallel execution with faults bounded to dependents inside the batch, ranged reads carrying real line numbers, truncated output persisted to a readable file, an appended environment status block, one persistent shell, and an automatic syntax check returned inside every write result.
Fail open into cluster `streaming-and-parallel-tool-execution`. source-ids: streaming-and-parallel-tool-execution, concurrency-opt-in-and-cascading-abort, ranged-reads-with-line-numbers, truncate-and-persist-long-output, environment-status-bar, persistent-shell-session, instant-syntax-feedback.

**12. Review the retrieval ladder and the edit scheme.**
Confirm the candidate set narrows monotonically from path and semantic search, through exact pattern matching, to symbol tracing. Then measure the apply-failure rate per edit scheme on real edits and prefer content-anchored edits over any scheme that depends on numbers the model must count.
Fail open into clusters `coarse-to-fine-search-ladder` and `edit-scheme-decision`. source-ids: coarse-to-fine-search-ladder, embedding-index-tradeoff, edit-scheme-decision, old-string-new-string, start-end-anchor-edit.

**13. Harden the sandbox.**
Default network egress to deny and open named destinations through a whitelist proxy. Mount sources read-only, provide a separate writable workspace, and keep credential files out of the mount set. Enforce processor, memory, disk, and time quotas, and return a structured error naming the limit, the duration, and the last output on violation.
Fail open into cluster `security-layer-order`. source-ids: network-egress-default-deny, filesystem-isolation-scope, resource-quotas-structured-termination, lethal-triad.

**14. Parse commands for effect and gate destructive actions.**
Replace blacklist matching with parsing that resolves the real effect of a command, including flags that consume following arguments and arguments that hide nested operations. Place explicit approval on destructive actions so a passing outcome reached by a forbidden method still gets blocked before execution.
Fail open into cluster `security-layer-order`. source-ids: semantic-command-parsing, constrain-actions-not-only-outcomes.

**15. Write loyalty into the prompt and downgrade external content.**
State in the system prompt that only the principal's instructions carry force. Downgrade repository text, tool output, and third-party responses to consultable data, and apply the same trust review to anything written into long-term memory.
Fail open into cluster `security-layer-order`. source-ids: principal-loyalty-under-delegation, persistent-memory-amplifier.

**16. Route each artifact class, then split generation from review.**
Choose generated code when the artifact has a compact exact description, hard dimensional constraints, and programmatic verifiability, and choose a generative model when intrinsic complexity is effectively unbounded. Add a reviewer that renders the artifact and judges the rendering, with structured findings and both a quality bar and a round cap.
Skip when the agent ships no rendered artifact, and record that skip reason.
Fail open into cluster `proposer-reviewer-render-loop`. source-ids: code-vs-generative-model-route, proposer-reviewer-render-loop, structured-review-feedback, explicit-stop-conditions.

**17. Enforce rule-bound operations from ground truth.**
Move the policy check inside the tool that performs the effect. Read every policy-relevant fact from the authoritative store and the server clock, treat model-supplied condition parameters as self-reports rather than facts, and log the mismatch rate as a detector.
Skip when no operation the agent can reach is policy-governed, and record that skip reason.
Fail open into cluster `three-tier-rule-safeguard`. source-ids: validation-inside-execution-tool, server-ground-truth-gatekeeper, expected-parameters-as-checklist, mismatch-logging-as-detector.

**18. Push authorization below generated code.**
Enforce who may do what to which data in a stable, human-reviewed data layer. Give generated application code only a scoped access context it cannot forge, and require every access path to pass through that layer. Bind generated queries to read-only credentials, approved read statements, and capped cost.
Skip when no generated code reaches a data store or a client renderer, and record that skip reason.
Fail open into cluster `generative-ui-when-text-fails`. source-ids: authorization-in-data-layer, sql-execution-hardening, declarative-manifest-over-executable-ui, artifact-pattern-off-data-path.

**19. Generate agents from a validated reference.**
Start from a working implementation and confine the diff to prompt, tools, and business logic. Verify the result against the architectural flaw checklist covering context handling, tool design, technology currency, and ecosystem health, and confirm it runs real tasks before it becomes the reference for anything else.
Skip when the deliverable is an ordinary application rather than an agent, and record that skip reason.
Fail open into cluster `generate-adapters-on-demand`. source-ids: example-based-agent-generation, agent-authoring-flaw-checklist.

## Open next

- [playbooks/evaluating-agents.md](evaluating-agents.md) once a harness change needs a measured delta rather than an argument, and whenever the apply-failure rate or the quadrant labels come from opinion.
- [playbooks/tools.md](tools.md) when the review turns into schema design, disclosure policy, or a decision between a general executor and a dedicated tool.
- [playbooks/interaction.md](interaction.md) when the agent must consume asynchronous events, operate a graphical interface, or hold a session open across long-running work.

## Reply shape

Report what changed in the harness, what was chosen at each fork with the artifact that justifies it, and what remains open. List every skipped step with its reason. Name the failure layer and the cluster for each defect found, so the next review starts from evidence rather than from a rerun.
