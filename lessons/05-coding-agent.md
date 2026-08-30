# 05 Coding agent and code generation

Extensive notes behind [playbooks/coding-agent.md](../playbooks/coding-agent.md). Open a cluster only when a playbook step reports a failed check. Collapsed from 105 extracted lessons into 18 clusters.

## Terms

- **coding agent**. An agent whose primary means of acting is writing, modifying, and executing code.
- **meta-capability**. An ability that produces other abilities at run time, such as code generation minting tools, constraints, and presentations.
- **project instruction file**. A repository file injected at session start carrying agent-facing conventions, commands, and restricted zones.
- **acceptance baseline**. The concrete definition of done, expressed as suites, pipeline checks, and review standards.
- **execution boundary**. The explicit statement of what the agent may and may not touch.
- **feedback signal**. An automated correctness judgment routed back into the agent's input, such as linter output or test results.
- **rollback mechanism**. The guaranteed path back from a bad change.
- **call fingerprint**. A hash over tool name plus arguments, used to detect repeated calls that make no progress.
- **death spiral**. A cascade in which error-path logic itself calls the model, fails the same way, and re-triggers itself.
- **neutral trajectory**. A vendor-independent run record separating portable reasoning text from a non-portable vendor credential.
- **apply model**. A small fast model that merges a change description into a complete file.
- **artifact pattern**. A division in which the model emits a query and a view while the system moves the data.

## What this is for

Coding agents work better than agents in most other domains because software engineering already shipped the harness. Test suites give an acceptance signal, type systems and linters give instant feedback, and version control gives rollback. This chapter builds the general agent as a coding agent plus a file system, wraps it in that inherited harness, and then treats code generation as the meta-capability that mints tools, constraints, presentations, interfaces, and further agents at run time.

## Core model

Coding core plus filesystem hub. The ability to write, modify, and execute code is the architectural center for any agent whose task space cannot be enumerated in advance. Working state lives in context and durable state lives in tracked files, so memory, knowledge, and generated capability share one inspectable, versionable substrate. Everything else in this chapter is either a harness layer around that core or an application of it.

## Clusters

### `coding-core-plus-filesystem`

When the task boundary of an agent under design cannot be enumerated. Make code writing and execution the architectural core, and express anything that must be exact as code rather than as in-context reasoning, because code admits one reading and execution produces an objective verdict. Grant basic code execution even to research, analysis, and support agents. Produce documents, decks, and charts by writing their markup or script, and reserve graphical operation for systems that expose nothing else. Keep coding as one foundational tool, not the hub, inside closed-domain agents built around fixed processes. Build in the order capabilities, workflow, harness, failure recovery, execution efficiency, retrieval, editing, security, and refuse to skip a stage because the demo already runs.
Check. Sample answers containing a number or a compound condition and confirm each traces to an execution result. Then walk the repository and mark which of the nine build stages has an owning module.
source-ids: coding-core-plus-filesystem, code-as-thinking-and-expression, coding-as-general-problem-solving, content-generation-reduces-to-code, coding-core-applicability-boundary, coding-agent-build-order

### `seven-core-tools`

When provisioning tools for any agent that touches a codebase or a workspace. Provide a code interpreter, a shell, read, write, edit, filename search, and content search. The count is a reference point and the coverage is the requirement, so optimize for the five operation categories of browse, read, modify, execute, and search rather than for a tool total. Keep this set distinct from the general tool taxonomy that classifies by call direction and effect, and keep edit separate from whole-file write so a small change never costs a full rewrite.
Check. Open the tool schema file, confirm all five categories have an entry, confirm edit and write are distinct, and confirm no tool exists solely to call another agent.
source-ids: seven-core-tools, toolbox-is-reference-not-taxonomy

### `filesystem-as-hub`

When deciding where long-lived agent state belongs. Store memory, knowledge, and generated capability as files in the workspace. Default long-term memory to dated plain-text files and add a retrieval index only when volume makes reading infeasible, because a wrong belief should be correctable by deleting one line in a reviewable diff. Read durable memory before acting and write back what a future run would otherwise have to ask about. Record a new discovery as a dated observation immediately, and promote it to standing instruction or code only after repeated trajectories or an executable validation confirm it.
Check. Confirm memory, knowledge, and generated scripts all resolve to tracked files. Run one task twice in fresh sessions and confirm the second asks fewer setup questions. Sample standing rules and confirm each cites more than one confirming trajectory or a validation.
source-ids: filesystem-as-hub, markdown-memory-over-vector-db, memory-first-task-loop, record-before-promotion

### `workflow-trimming-by-task-size`

When applying the engineering workflow to work of varying size. The full sequence runs orient, clarify, design, implement, test, review, and sync documentation. Read available documentation first and, where key documents are missing, draft an architecture overview and a directory guide before editing. Keep a project instruction file naming build and test commands, style constraints, and restricted directories, and inject it ahead of anything task-specific. Proceed straight to code only when the boundary is clear and the impact is local. For complex or hard-to-reverse changes, write a design document answering which modules change and why, which approach wins and at what cost, which dependencies appear, and what system impact is expected, then wait for approval. Reuse existing abstractions instead of adding a duplicate helper, and update architecture documentation inside the same change set. Treat the workflow as recommended rather than mandatory, trim stages a small task does not need, and never trim verification. Judge repository readiness by whether a remote newcomer could work from tracked files alone. Attribute the point where an agent stops reading and starts editing mainly to the model, and use prompts, tools, and budgets only to amplify or suppress it.
Check. Sample trajectories by task size and confirm the stage set varies while a test execution appears in all of them. Confirm the instruction file names the test command and at least one restricted path.
source-ids: workflow-trimming-by-task-size, orient-before-editing, project-instruction-files, ai-ready-repo-gauge, requirement-clarification-gate, design-doc-four-questions, implement-with-existing-abstractions, sync-docs-on-architecture-change, investigation-threshold-is-model-behavior

### `tests-pass-as-completion`

When the agent believes an implementation is finished. Completion means the suite passed, never that the code was written. Write tests for normal paths, boundaries, and error cases, run them, and iterate the fix-and-rerun loop before reporting anything. A review pass for readability, performance risk, security risk, and style follows the passing run and can send the work back to editing. That self-review lints, it does not authorize. The done bit comes from the verifier, not from the producer.
Check. For every completion claim in a trajectory, confirm a test execution appears after the final edit with a recorded pass, and confirm a lint or review artifact exists between that run and delivery.
source-ids: tests-pass-as-completion, self-review-before-delivery

### `harness-four-components`

When building or auditing the machinery around a coding agent. Name an acceptance baseline, an execution boundary, feedback signals, and a rollback mechanism, and point each at a real artifact. Coding agent maturity comes from inherited infrastructure rather than from superior models, so reproduce those three functions of acceptance, instant feedback, and rollback when entering a new domain. Prefer enforced constraints over guidance, automate verification, keep feedback fast and structured, and keep rollback reliable. Put knowledge inside the codebase, encode constraints in linters and pipelines instead of documents, mine failure trajectories to drive harness changes, and split long work into a planning role and a stepwise execution role. Block destructive methods even when they reach a passing outcome. Thicken the harness where the model is weak, thin it where the model is strong, and always report which model an evaluated technique was measured on.
Check. For each of the four components, name the implementing file or system. For each non-coding agent, name its acceptance signal, its instant feedback signal, and its rollback path. Count prompt rules a linter or schema could enforce and confirm the count is falling.
source-ids: harness-four-components, coding-inherits-software-engineering-harness, harness-transfer-principles, harness-industry-practices, constrain-actions-not-only-outcomes, harness-thickness-tracks-model-strength

### `task-quadrant-table`

When deciding whether to hand a task to an agent, and how much harness it needs.

| Verification | Clear goal | Vague goal |
| --- | --- | --- |
| Automated | Delegate freely. Cheapest agent work. | Clarify first. Verification will pass on the wrong thing. |
| Manual | Add a verifier before scaling. Review cost dominates. | Do not delegate yet. Harness investment goes here. |

Classify each live task on both axes and spend harness effort moving tasks toward clear goal with automated verification.
Check. Label a batch of recent tasks by quadrant and confirm the worst outcomes sit outside the clear-and-automated cell.
source-ids: task-quadrant-table

### `failure-taxonomy-four-layers`

When building or reviewing error handling in an agent runtime. Sort every failure into the API layer, the tool layer, the context layer, or the control-flow layer, and give each layer its own recovery path with no unclassified catch-all. Maintain an explicit map from error type to strategy, and retry only errors whose cause can change on its own. Hash tool name plus arguments into a call fingerprint, alert when a fingerprint recurs, and keep a separate consecutive-failure counter per recovery path. Run an independent idle watchdog that kills and retries a stream when no output arrives within an interval, because connection timeouts miss silent stalls. Detect and repair a tool call missing its paired result before the request goes out, and disable that repair in any mode whose output becomes training data.
Check. Read the error handling module and confirm every branch maps to one layer. Grep retry sites and confirm each consults the classification map. Force a repeated identical call and confirm the fingerprint detector fires.
source-ids: failure-taxonomy-four-layers, retryability-classification, no-progress-pattern-detection, idle-watchdog-liveness, trajectory-integrity-repair

### `graded-recovery-escalation`

When a failure has been classified and recovery must begin. Try silent retry with jitter first, then degrade the request and retry, and surface the error to the user only once automatic means are exhausted, together with what was already attempted. Withhold intermediate errors while recovery is still running and release them only when recovery is confirmed impossible. Return tool-layer errors as ordinary structured tool results carrying specific contract hints so the session keeps running. Put an attempt ceiling on every recovery path, choose each threshold from observed session statistics, and sit global termination above all of them. Disable model-invoking side effects on the error path and add a recursion-depth counter that breaks any residual cascade. Keep trajectories vendor-neutral, splitting reasoning into portable text and a non-portable credential and recording tool calls as name plus arguments, so a mid-task handover raises no provider error and repeats no completed call. Handle high-frequency environment faults with deterministic detection and fixed repairs, route the long tail to model-driven diagnosis, and require confirmation for risky repairs.
Check. Inject a rate limit and confirm the ladder is walked in order with background calls dropped rather than retried. Enumerate recovery paths and confirm each has a ceiling, a data-derived justification, and a terminal action. Force the failure that triggers a model-calling hook and confirm the hook is skipped.
source-ids: graded-recovery-escalation, withhold-errors-until-recovery-fails, tool-errors-become-model-input, recovery-ceilings-from-data, death-spiral-defense, neutral-trajectory-and-handover, layered-self-repair

### `streaming-and-parallel-tool-execution`

When latency and context cost decide whether the harness feels usable. Dispatch the first tool call as soon as its arguments are complete and valid, overlapping execution with generation of the remaining calls, and run independent calls in parallel. Require each tool definition to declare concurrency support with a default of no, and abort only the dependents of a failed call inside the same batch, never independent calls or the parent operation. Support ranged reads with real line numbers attached. Keep the head and tail of long command output, mark the elision, and persist the full text to a readable file. Inject working directory, branch, recent commits, and pending change summaries as an appended status block before each inference rather than into the static prefix. Create one long-lived shell at start and keep isolated shells for parallel work. Run the relevant linter after every write and return its findings inside the tool result.
Check. Compare the first dispatch timestamp against the end of generation. Inject a missing path into one call of a three-call batch and confirm the other two results reach the model. Change directory and branch mid-session and confirm the next request carries updated values while the prefix is unchanged. Write a file with a deliberate syntax error and confirm the error text appears in the write result.
source-ids: streaming-and-parallel-tool-execution, concurrency-opt-in-and-cascading-abort, fault-boundary-within-batch, ranged-reads-with-line-numbers, truncate-and-persist-long-output, environment-status-bar, persistent-shell-session, instant-syntax-feedback

### `coarse-to-fine-search-ladder`

When locating the code relevant to a task in a large repository. Treat the four retrieval methods as complementary rather than competing. Start with filename and path patterns to narrow the region before reading content, use regular expression content search with type and path filters for exact and structural matches, add semantic search for concept-shaped queries, and use language-aware definition and reference lookup to trace a call chain. Where semantic search is offered, chunk along complete syntactic units and merge dense and keyword arms under a reranker. Default to on-the-fly pattern and path retrieval, and adopt an embedding index only where a measured cross-file recall gap pays for the infrastructure and the staleness it introduces.
Check. Trace one task's retrieval calls and confirm the candidate set narrows monotonically. State the recall gap the index closes with a measurement, or remove the index.
source-ids: coarse-to-fine-search-ladder, glob-path-search, regex-content-search, semantic-search-design, embedding-index-tradeoff, symbol-definition-reference-lookup

### `edit-scheme-decision`

When designing or replacing the file editing interface. Weigh five schemes by reliability, output cost for large deletions, tolerance for model counting errors, and support for batching several edits from one round of thinking. Old string plus new string fails loudly when the anchor is not unique, which is the desired behavior for small edits. Start and end anchors replace or delete a large block without echoing it. A change description merged by a small fast apply model keeps the main model on logic, at the cost of ambiguity between near-identical snippets. Line-number targeting requires numbers attached at read time and resists batching because each edit shifts later coordinates. Editor-style command languages assume an actor that sees state between every small step, so adopt them only where the deployed model handles their syntax reliably. Prefer content-anchored schemes over anything the model must count.
Check. Compute the apply-failure rate per scheme on a sample of real edits and confirm the deployed scheme is lowest. Confirm the edit tool rejects a non-unique anchor with a reason instead of picking an occurrence.
source-ids: edit-scheme-decision, old-string-new-string, start-end-anchor-edit, diff-plus-apply-model, line-number-targeting, vim-style-edit-commands

### `security-layer-order`

When designing or reviewing the posture of an agent that runs code. Work in order from threat model, to sandbox isolation, to execution-time command validation, to trust and loyalty rules, and mark which layers are coding-specific and which apply to every agent. Private data access, untrusted content exposure, and outward communication already close an attack loop, so remove or gate at least one. Persistent memory is the fourth boundary, so subject anything written to long-term memory to the same trust review as external input. Give the sandbox no network by default and admit named destinations through a whitelist proxy. Mount sources read-only, provide a separate writable workspace, and never mount credential files. Enforce processor, memory, disk, and time quotas, and on violation return a structured error naming what was terminated with the last output. Parse each proposed command for its real effect, including flags that consume following arguments and arguments hiding nested operations, and reject blacklist matching as a defense. State in the harness that only the principal's instructions carry force, and downgrade repository text, tool output, and third-party responses to consultable data.
Check. Point to an implementing mechanism for each of the four layers and name the asset each protects. Attempt an outbound request to an unlisted host, a write to a source path, and a read of a credential path, and confirm all three fail. Submit a command nesting a deletion inside a legitimate program's argument and confirm the validator identifies it. Run a negotiation-style evaluation and record both leakage of protected information and refusal of legitimate principal requests.
source-ids: security-layer-order, lethal-triad, persistent-memory-amplifier, network-egress-default-deny, filesystem-isolation-scope, resource-quotas-structured-termination, semantic-command-parsing, principal-loyalty-under-delegation

### `meta-capability-definition`

When deciding whether to add another tool or to grant the ability to make tools. Code generation is a meta-capability that produces new tools, new constraints, and new forms of expression at run time, so stop trying to pre-build every capability. Sweep six application directions in order, which are thinking, business rules, content presentation, system interfaces, user interfaces, and the agent itself, and pick the innermost one still unaddressed. For the innermost direction, translate arithmetic, symbolic manipulation, and strict inference into code and let an interpreter produce the answer, never accepting in-prose calculation as final. Where a problem has exact mathematical or logical structure, use the model to build a formal model and hand it to a solver.
Check. List capabilities exercised last month and confirm some were generated at run time. Score the agent on all six directions and confirm work is queued on the innermost failing one. Sample answers requiring exact values and confirm each has an attached executed script whose output matches the reported answer.
source-ids: meta-capability-definition, six-application-directions, offload-exact-work-to-code, formalize-then-solve

### `three-tier-rule-safeguard`

When an operation is governed by policy and the boundary must be identical every time. Layer prose rules for understanding, parameter-driven checklists for pre-call verification, and server-side ground-truth validation as the final gate, and be explicit that only the third tier is the security boundary. Transform documented business rules into executable validation so the rule becomes enforced behavior rather than advisory text, while keeping the natural-language version in the prompt so the agent can explain policy and propose a compliant alternative. Embed the check inside the tool that performs the effect so no call path reaches the effect unchecked. List the full policy in the tool description and add optional parameters recording the agent's own judgment of each condition, treating those values as self-reports rather than facts. Fetch every policy-relevant fact from the authoritative store and the server clock, and compare it against the self-report, treating the mismatch rate as a detector for erroneous belief and for injection.
Check. Call the governed tool with a deliberately false self-reported fact and confirm the decision follows the store. Confirm the mismatch log carries per-field rates and a recent review. Demonstrate all three tiers separately for one operation and identify which is the boundary.
source-ids: three-tier-rule-safeguard, codify-ambiguous-rules, nl-and-code-rules-complementary, validation-inside-execution-tool, expected-parameters-as-checklist, server-ground-truth-gatekeeper, mismatch-logging-as-detector

### `proposer-reviewer-render-loop`

When the agent generates code whose quality is only visible after rendering. Choose a document framework whose source is compact markup or script and generate that source instead of operating a visual editor. Split generation and quality review across two roles, have the reviewer render the artifact and evaluate the rendering, and iterate until the quality bar passes or the round cap fires. The generator cannot see its own rendering, which is what makes the review independent. Emit findings as structured records with location, issue type, severity, and a concrete remedy, and reject vague aesthetic verdicts. Keep the reviewer's context to the latest rendering and the generator's context to structured text feedback so neither accumulates the other's bulk. Route each artifact class to generated code when it has a compact exact description, hard dimensional constraints, programmatic verifiability, or a need for parametric editing, and to a generative model when intrinsic complexity is effectively unbounded. Delegate inspection of long media to a sub-agent that brackets coarsely then samples finely, returning only intervals.
Check. Inspect a generation session and confirm rendered images were evaluated and at least one revision followed from that evaluation. Measure tokens per round for both roles and confirm neither grows with completed rounds. Confirm every loop run logs a stop reason and that cap-terminated runs are triaged.
source-ids: proposer-reviewer-render-loop, markup-frameworks-for-documents, structured-review-feedback, dual-agent-context-economy, explicit-stop-conditions, code-vs-generative-model-route, media-analysis-subagent

### `generative-ui-when-text-fails`

When the interaction requires collecting structured information, showing relationships, or choosing among options. Generate a form, chart, or small application instead of extending a text dialogue, and collect an underspecified request through one form with the right control per field and conditional logic for dependent questions. Deliver interactive documents that demonstrate behavior and keep improving during the task rather than a static report at the end, and for long-running research keep one continuously updated site exposing per-experiment data, raw model responses, and internal health metrics plotted apart from outcome metrics. Have the agent emit a declarative interface description that the client renders from a trusted component catalog, and reserve direct code generation for genuinely custom visuals inside a sandbox. Where a request would otherwise have the model restate a large result set, emit the query and the view as artifacts and route the data from its source to the interface without passing through the model. Never execute generated statements as given, so use read-only credentials, allow only approved read statements, bind user values as server-side parameters, and cap query cost and scope. Keep a stable base application with selected aspects open to conversational customization applied by hot reload. Enforce who may do what to which data in a stable, human-reviewed data layer, and give generated code only a scoped access context it cannot forge.
Check. Sample interactions that collected several fields and confirm recent ones used a generated interface. Emit a manifest requesting an uncataloged component and confirm the renderer rejects it. Run a large-result query and confirm the rows never enter the model context while the rendered table matches the database. Write application code that skips a state transition and reads across tenants, and confirm the data layer rejects both.
source-ids: generative-ui-when-text-fails, dynamic-form-clarification, html-deliverable-over-markdown, living-artifact-site-purposes, declarative-manifest-over-executable-ui, artifact-pattern-off-data-path, sql-execution-hardening, semi-custom-hot-reload, authorization-in-data-layer

### `generate-adapters-on-demand`

When the system boundary or the agent itself is the thing that needs to be written. Where an external service has no ready client, poor documentation, or a nonstandard response shape, have the agent read the documentation or inspect real responses and generate the adapter, covering client construction, authentication, parsing, and translation into the downstream model. Where a system exposes only a graphical interface and the task recurs, operate it once visually and capture the successful sequence as a verified script, keeping the visual fallback. On a parsing failure, generate parsing code, validate it automatically before deployment, and record the adaptation rather than absorbing it silently. Have the agent read production trajectories against architecture documents, locate the responsible module, emit a structured report, generate a regression test bound to the trajectory, and file the work item. For agent-authoring work, start from the agent's own code or another validated implementation and confine the diff to prompt, tools, and business logic, because a strong code model without agent domain knowledge produces serious architectural defects. Verify context handling, tool design, technology currency, and ecosystem health against the flaw checklist.
Check. Confirm each generated adapter has recorded response fixtures and a test exercising them. Feed an unseen format through the system and confirm it adapts, passes validation, and leaves an alert. Take one filed issue and confirm it names the trajectory, the module, and a replaying regression test. Confirm the generated agent runs real tasks and passes the checklist item by item.
source-ids: generate-adapters-on-demand, rpa-solidification, self-repairing-parser-loop, log-diagnosis-to-issue-pipeline, example-based-agent-generation, agent-authoring-flaw-checklist

## Failure diagnostics

Label the failure before rerunning anything. Reliability here means every failure class owns a detection path, a recovery path, a handover path, and a termination path, and maturity comes from inherited verification infrastructure rather than from model strength.

| Symptom | Layer | First check | Cluster |
| --- | --- | --- | --- |
| Completion claimed, nothing works | control flow | No test execution after the final edit | `tests-pass-as-completion` |
| Same tool call repeats forever | control flow | Call fingerprint detector absent or unwired | `failure-taxonomy-four-layers` |
| Stream hangs with no error | API | No idle watchdog, only a connection timeout | `failure-taxonomy-four-layers` |
| Errors cascade after a stop or cleanup hook | control flow | Model-invoking side effect on the error path | `graded-recovery-escalation` |
| One failed parallel call kills the task | tool | Fault boundary wider than the failing call's dependents | `streaming-and-parallel-tool-execution` |
| Edits apply to the wrong place or fail silently | tool | Anchor uniqueness not enforced, or line numbers stale | `edit-scheme-decision` |
| Context floods on a build or test run | context | Long output neither truncated nor persisted to a file | `streaming-and-parallel-tool-execution` |
| Agent follows instructions found in a repository file | tool | External content not downgraded to consultable data | `security-layer-order` |
| Destructive command passed a blacklist | tool | No parse of nested effects and consuming flags | `security-layer-order` |
| Policy violated while the agent reported compliance | tool | Decision read a model parameter instead of the store | `three-tier-rule-safeguard` |
| Generated code read across tenants | tool | Authorization above the data layer rather than inside it | `generative-ui-when-text-fails` |
| Generated slides or dashboards look wrong | tool | Reviewer never rendered the artifact | `proposer-reviewer-render-loop` |
| Generated agent runs but is architecturally broken | model | Flaw checklist never run, no validated reference | `generate-adapters-on-demand` |

source-ids: 05-chapter-synthesis, failure-taxonomy-four-layers, coding-inherits-software-engineering-harness

## Drills

Namespaced review prompts. Each one has a defensible answer and a decision it forces.

- **05-coding-agent-q1**. Code execution is what makes generation a meta-capability, and it is also what lets generated code exfiltrate, spin, or drain the machine. Locate the balance. The answer removes specific attack elements rather than capability in general, tiering isolation per scenario, denying egress by default with a named whitelist, mounting sources read-only, excluding credentials, bounding resources, and managing the sandbox lifecycle.
- **05-coding-agent-q2**. An agent that writes agents can accumulate a defect every generation. Explain what stops the drift. The gate is a fixed, difficult, machine-checkable task suite plus the architectural flaw checklist, adaptation from a validated reference rather than generation from scratch, and a rule that an unverified generation never becomes the parent of the next.
- **05-coding-agent-q3**. A self-repairing parser can absorb a format change that is actually a defect. Separate adaptation from anomaly. Diagnose before adapting, check version control for a legitimate commit, treat sourceless drift as suspicious, then adapt and report in parallel so adaptation never consumes the anomaly signal.
- **05-coding-agent-q4**. A reviewer with taste that differs from the user's converges the loop on the wrong optimum. State the fix. Rank user feedback above reviewer findings, persist stated preferences to memory, and scope the reviewer to objectively checkable defects.
- **05-coding-agent-q5**. Distilled experience makes the prompt rule set grow without bound. Describe its garbage collection. Audit on a schedule, migrate enforceable rules into code, retire rules that never fire, and require evidence, forward improvement, and regression survival before calling a change an improvement.
- **05-coding-agent-q6**. Teams friendly to remote work tend to be friendly to agents. Apply the gauge. Run the remote newcomer test before tuning prompts, and close the largest documentation gap first when poor agent results look like model weakness.
- **05-coding-agent-q7**. Private data, untrusted content, outward communication, and persistent memory make four boundaries rather than three. Assign controls. Every control belongs to exactly one boundary, no boundary is unowned, and the design is validated by assuming injection already succeeded.
- **05-coding-agent-q8**. Compare the artifact pattern against having the model answer from the rows. Choose the artifact pattern only when the model does not need to reason over the values, and pair it with read-only credentials, statement parsing, cost caps, and catalog-bounded or sandboxed rendering.
- **05-coding-agent-q9**. Compare codified validation against rules written in prose. Keep prose for explanation and alternative-finding, enforce the decision in code against ground truth, and never treat checklist parameters as the boundary.

source-ids: thought-question-design-review

## Depends-on and needed-by

- Depends on [playbooks/tools.md](../playbooks/tools.md) for schema form, disclosure policy, and the general-executor decision that `seven-core-tools` specializes.
- Depends on [playbooks/context-engineering.md](../playbooks/context-engineering.md), since the status block in `streaming-and-parallel-tool-execution` must append after the frozen prefix rather than edit it.
- Depends on [playbooks/memory-knowledge.md](../playbooks/memory-knowledge.md) for the archive rules that `filesystem-as-hub` writes into files.
- Needed by [playbooks/evaluating-agents.md](../playbooks/evaluating-agents.md), which measures whether a harness change in this chapter actually helped, and which owns first-error attribution for the four failure layers.
- Needed by [playbooks/multi-agent.md](../playbooks/multi-agent.md), where `proposer-reviewer-render-loop` is the rendering specialization of the base proposer and reviewer loop.
- Needed by [playbooks/continual-evolution.md](../playbooks/continual-evolution.md), which promotes what `record-before-promotion` has confirmed.

## Open tensions

- Trim ceremony, never verification. `workflow-trimming-by-task-size` lets a small task skip design and documentation stages, while `tests-pass-as-completion` holds for every size.
- Self-review lints, an independent verifier gates. `self-review-before-delivery` runs inside the producer, so it cannot supply the done bit that `tests-pass-as-completion` requires.
- Capability versus containment. `meta-capability-definition` wants execution breadth and `lethal-triad` wants an element removed. Resolve per scenario inside `security-layer-order` rather than by one global isolation level.
- Prose rules versus codified rules. `nl-and-code-rules-complementary` keeps both, and `three-tier-rule-safeguard` names ground truth as the only boundary.
- Generated code versus a generative model. `code-vs-generative-model-route` decides by intrinsic complexity and precision need, so an unbounded-complexity artifact is not a failure of the code path.
- Retrieval speed versus recall. `embedding-index-tradeoff` defaults to on-the-fly search, and `coarse-to-fine-search-ladder` still wants concept-shaped queries served.
- Harness thickness versus model strength. `harness-thickness-tracks-model-strength` makes every layer here provisional, so rerun ablations after a model drop and retire what the model has absorbed.
