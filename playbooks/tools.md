# design-or-review-agent-tools

Review or design the agent tool surface. Copy these steps into the todolist before reasoning.

## Use when

- add a tool or MCP server
- install a skill from a hub
- the agent keeps picking the wrong tool
- edit or replace fails on text the model just read
- too many tools in context
- tool explosion
- sandbox or venv confusion
- send email or transfer money from an agent
- spawn a sub-agent
- HITL approval hang
- review tool descriptions

## 0. Name the data shape

Name the form-by-disclosure registry before writing a schema or a skill. Each capability stores a form field, dedicated or general executor or skill, and a separate disclosure field, resident or indexed or discover-on-gap or skill-lookup. Lookup the row in `references/data-shapes.md`. Do not infer form from how many schemas sit in the prefix.

If the registry lacks both fields, open `lessons/04-tools.md` cluster `form-vs-disclosure-independent`. source-ids: form-vs-disclosure-independent, choose-form-on-four-dimensions.

## 1. Classify, then stop on deferred categories

Tag invocation direction and target of action. Map the pair to perception, execution, collaboration, event-triggered, or user communication. Those two fields are a placement aid, not a twenty-five-cell grid.

**Hard stop.** Event-triggered and user-communication tools do not ship in the proactive loop. Tag them `deferred-to-async-runtime`. Give them no sync execute path here. Skip remaining steps in this playbook. Open `playbooks/interaction.md`. Cluster `defer-event-and-user-comm-tools` in `lessons/04-tools.md`. source-ids: defer-event-and-user-comm-tools, five-category-invocation-and-target, event-tools-register-then-trigger, user-comm-as-explicit-tool-call.

Skip this stop when the capability is perception, execution, or collaboration. Continue.

## 2. Pick form on four dimensions

Skip if step 1 stopped on a deferred category.

Score security and permissions, parameter complexity, change rate, and model strength. Default to a general executor plus optional skill text. Add a dedicated tool only for a named exception, security or audit grain, platform hide plus structured feedback, extreme frequency, or nested schema. Merge near-clones that share job and I/O. Chain bulky intermediates inside the executor so only an aggregate returns. Complex CLI flags belong in a file the executor imports, not in quoted soup.

Record disclosure as a second field. A cheap skill catalog line does not pick form.

If a leftover dedicated tool has no exception note, open `lessons/04-tools.md` cluster `choose-form-on-four-dimensions`. source-ids: choose-form-on-four-dimensions, prefer-general-executors-default, dedicated-for-security-permissions-audit, design-aci-around-agent-goals.

## 3. Write when, cannot, examples, return, cost

Skip if step 1 stopped on a deferred category.

Lead with the decision rule for when to call. State refused jobs and the sibling that owns them. Put a copy-ready example on every non-obvious parameter. Name return fields. Mark slow or heavy calls and the cheaper sibling. Ship one to five real invocations, including one non-default mix. Apply the same checklist to skill catalog lines and bodies. Repair descriptions before swapping models.

If a description is only a capability paraphrase, open `lessons/04-tools.md` cluster `describe-when-not-just-what`. source-ids: describe-when-not-just-what, state-boundaries-and-refusals, describe-skills-like-tools.

## 4. Prove argument fidelity

Skip if step 1 stopped on a deferred category.

Run read-then-edit on the exact snippet the read tool returned. Run write-then-read and compare bytes to the write payload. Ban silent rewrite of quotes, encoding, or punctuation. Ban hidden argv, headers, or stamps. If a transform is required, name it in the description and echo it on the result.

If edit cannot match text the model just read, open `lessons/04-tools.md` cluster `never-silently-rewrite-arguments`. source-ids: never-silently-rewrite-arguments, never-silently-inject-arguments, keep-perceived-world-identical-to-tool-world.

## 5. Review third-party sources

Skip if every capability is first-party and no hub or MCP install is in scope. Skip if step 1 stopped on a deferred category.

Treat descriptions as untrusted text that enters context every session. Pin versions and re-review on upgrade. Issue per-server credentials. Namespace by server plus name so a twin cannot steal a trusted call. Isolate skill folders that run host code. Score the enabled set on private data, untrusted content, and outbound communication. A full triad needs isolation or a human gate.

If an install has floating versions or a shared god token, open `lessons/04-tools.md` cluster `treat-tool-descriptions-as-untrusted-input`. source-ids: treat-tool-descriptions-as-untrusted-input, pin-third-party-versions-and-re-review, prevent-same-name-tool-shadowing, lethal-triad-for-mcp-combo-risk.

## 6. Choose a disclosure layer

Skip if the resident catalog is a few dozen or fewer and selection is already reliable. Skip if step 1 stopped on a deferred category.

Escalate in this order. Hierarchical index, load a full schema on inspect. Gap-declared discovery, append the schema once at the tail and pin it. Skill catalog lookup, name plus description until the body is read. Keep a tiny resident core plus one search or discover tool. Do not flatten hundreds of schemas into the prefix.

If turn-zero still injects a flat hundred-plus list, open `lessons/04-tools.md` cluster `three-disclosure-layers-load-discover-lookup`. source-ids: three-disclosure-layers-load-discover-lookup, scale-degrades-selection-and-cache, declare-capability-gap-then-inject, progressive-disclosure-catalog-then-body.

## 7. Grain perception

Skip if the capability under review is not perception. Skip if step 1 stopped on a deferred category.

Return paged candidates from search. Support offset and limit on read. Announce every omission and how to continue. Compress oversized bodies against the current question. Cache and fan out read-only calls. For media, pick native pixels, extract-to-text, or a specialist wrapped as a question-answer tool. Choose by layout need, not habit.

If search dumps full documents or a clip is silent, open `lessons/04-tools.md` cluster `perception-design-focus-granularity`. source-ids: perception-design-focus-granularity, search-return-candidates-then-page, read-with-offset-and-visible-truncation, pick-among-three-multimodal-paths.

## 8. Stack execution safety

Skip if the capability under review is not execution. Skip if step 1 stopped on a deferred category.

Fail fast on path traversal, injection, and type errors. Do not smart-correct a dangerous input into a different action. Scope permissions past a string deny list. Grade risk. Pre-approve irreversible work with a similar-strength model from another family. Run a sidecar on structured call fields only. Isolate on the process, container, microVM ladder. A language venv is package isolation, not a sandbox. Log, audit, and alert. Retry with an idempotency key or a query-first path. Split prepare and commit for mail, money, or any non-idempotent event. When a cheap oracle exists, run it in the same tool return.

If a world-changing wrapper has only a happy-path description, open `lessons/04-tools.md` cluster `fail-fast-validate-inputs-without-correction`. source-ids: fail-fast-validate-inputs-without-correction, sidecar-classifies-structured-call-fields-only, scale-isolation-process-container-microvm, two-phase-confirm-non-idempotent-side-effects.

## 9. Ship collaboration primitives

Skip if the capability under review is not collaboration. Skip if step 1 stopped on a deferred category.

Export spawn, message, cancel, and discover. Give each specialist its own prompt, tool subset, and output schema. Tag inbound text as coordinator, user, or tool. Pick sync, async, stream, or multi-turn per subtask. Human gates need a timeout, a conservative default, and a later recycle of reasons into a skill or a training queue.

If spawn exists without cancel, or approval can hang forever, open `lessons/04-tools.md` cluster `expose-spawn-message-cancel-and-discover`. source-ids: expose-spawn-message-cancel-and-discover, hitl-timeouts-defaults-and-priority-channels, specialize-subagents-instead-of-one-omni.

## Open next

- Deferred event or user-communication work. `playbooks/interaction.md`.
- A capability minted as generated code, adapter, or UI. `playbooks/coding-agent.md`.

## Reply

State what changed in the registry. State the form and disclosure chosen for each capability. State what remains open, including any item tagged deferred-to-async-runtime.
