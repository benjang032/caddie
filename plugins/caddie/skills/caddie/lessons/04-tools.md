# Tools

## What this is for

Design or review the agent tool surface. Form and disclosure are independent fields. Perception, execution, and collaboration ship with the proactive loop. Event-triggered and user-communication tools stop here and move to the async runtime. Capability creation by writing code belongs to the coding playbook.

## Core model

The data shape is a form-by-disclosure registry. Form is dedicated tool, general executor, or skill. Disclosure is resident, indexed, discover-on-gap, or skill-lookup. Cheap catalog lines relax the disclosure budget. They do not pick the form.

Short terms used below. ACI is a tool shaped as one agent goal. MCP is a schema and call bus, not a runtime. A skill hub installs folders. Progressive disclosure shows a thin catalog first. A sidecar classifies structured call fields in parallel. HITL is a human gate with timeout and default. The lethal triad is private data plus untrusted content plus outbound communication.

## Clusters

### `form-vs-disclosure-independent`

When choosing dedicated versus general versus skill, or how many capabilities sit in context.

Rule. Decide form and disclosure independently. Form sets resident token cost, parameter passing, and who can edit. Disclosure sets how many capabilities face the model at once. Injecting every MCP schema because the backend uses dedicated tools mixes the axes.

Check. Each registry row has an explicit form field and a separate disclosure field. At least one dedicated-tool capability is marked indexed or discover-on-gap.

source-ids: form-vs-disclosure-independent, synthesize-form-disclosure-and-three-proactive-classes

### `choose-form-on-four-dimensions`

When settling form for a new or leftover capability.

Rule. Score security and permissions, parameter complexity, change rate, and model strength. Default to a general executor plus optional skill text. Keep a dedicated tool for audit grain, platform hide plus structured hits, extreme frequency, or nested schema. Map each tool to an agent goal, not a vendor route. Merge near-clones that share job and I/O. Chain bulky intermediates inside the executor. Complex CLI flags go to a file the executor imports. Playbooks edited by non-engineers stay as skills.

Check. Every leftover dedicated tool cites one exception. Sample five names. At least four describe a goal rather than a vendor path.

source-ids: choose-form-on-four-dimensions, prefer-general-executors-default, dedicated-for-security-permissions-audit, dedicated-for-platform-hiding-and-feedback, dedicated-for-high-frequency-ops, dedicated-for-complex-parameter-schemas, skill-cli-params-fail-when-complex, skills-easier-for-human-authors, design-aci-around-agent-goals, integrate-similar-tools-not-subdivide, orchestrate-tool-chains-in-code

### `defer-event-and-user-comm-tools`

When the five-category set is being placed, or a timer, channel, card, or notify is proposed as a sync call.

Rule. Ship perception, execution, and collaboration with the proactive loop. Event tools are register now and wake later. User contact that leaves the live turn is an explicit reply, card, or notify tool. Both categories need the async runtime. A `set_timer` or `reply_to_user` wrapper in this loop is the wrong shape.

Check. Event-triggered and user-communication rows are tagged deferred-to-async-runtime and have no sync execute path. Invocation direction and target of action are filled and match one of the five categories.

source-ids: defer-event-and-user-comm-tools, five-category-invocation-and-target, user-comm-as-explicit-tool-call, event-tools-register-then-trigger

### `describe-when-not-just-what`

When authoring a tool schema or a skill catalog line.

Rule. Lead with when to call. List what the tool will not do and which sibling owns that job. Show copy-ready parameter examples. Name return fields and expensive calls. Attach one to five real invocations, including one non-default mix. Apply the same checklist to skills. Repair descriptions before swapping models.

Check. Every description begins with a when or use-when clause and has a cannot section. A recent wrong-tool incident has a description diff, or a written finding that when, cannot, and example were already specific.

source-ids: describe-when-not-just-what, state-boundaries-and-refusals, parameter-examples-not-abstract-specs, document-returns-and-latency-cost, ship-one-to-five-call-examples, fix-descriptions-before-swapping-models, describe-skills-like-tools

### `never-silently-rewrite-arguments`

When a read tool and a mutate tool share state, or a wrapper wants to normalize or stamp.

Rule. The world the model sees must match the world the tool operates. Pass arguments through unchanged. Do not append argv, headers, or fields the model did not pass. If encoding or line endings must unify, declare the rewrite in the description and echo it on the result.

Check. A golden test reads a file, passes the exact snippet to edit, and succeeds. A write-then-read compares bytes to the write payload. Wrapper source has no hidden argv absent from the public schema.

source-ids: never-silently-rewrite-arguments, never-silently-inject-arguments, keep-perceived-world-identical-to-tool-world, document-normalization-in-description-and-return

### `mcp-as-interop-not-framework-lock`

When the same capability must run in more than one client, or a skill folder must travel.

Rule. Publish dedicated tools as an MCP server with JSON Schema. Map actions to tools, browseable data to resources, and user-chosen templates to prompts. Use stdio locally and Streamable HTTP remotely. Do not start new remote servers on deprecated SSE-only transport. A skill hub is a registry of folders, not a second protocol. Treat every MCP schema as resident unless disclosure is layered. A skill is a short catalog line until the body is read.

Check. Each third-party dedicated tool is reachable via a server descriptor. The manifest keeps tools, resources, and prompts separate. Installed skills exist as folders with `SKILL.md`.

source-ids: mcp-as-interop-not-framework-lock, mcp-three-primitives-tools-resources-prompts, mcp-transport-stdio-or-streamable-http, skill-hubs-as-registries-not-protocols, resident-cost-schema-vs-catalog-line

### `treat-tool-descriptions-as-untrusted-input`

When installing an MCP server or a hub skill from outside the org.

Rule. Review descriptions as prompt injection. Pin versions and re-review on upgrade. Issue least-privilege credentials per server. Address tools as server plus name. Isolate skill folders that execute host code. A sidecar that still reads free-text descriptions is not a last defense. Refuse or isolate a stack that has private data, untrusted content, and outbound communication at once.

Check. The lockfile pins versions. A fixture description that asks for a secret is rejected. Two servers that share a bare name fail closed or require an alias. An enabled-server review lists the three triad bits.

source-ids: treat-tool-descriptions-as-untrusted-input, pin-third-party-versions-and-re-review, isolate-credentials-per-server, prevent-same-name-tool-shadowing, isolate-untrusted-skills-as-code, sidecar-last-defense-against-description-injection, lethal-triad-for-mcp-combo-risk

### `three-disclosure-layers-load-discover-lookup`

When the catalog grows past a few dozen, especially past about one hundred.

Rule. Scale alone drops selection accuracy and busts the prefix cache. Apply three layers in order of how on-demand they are. Hierarchical index and load. Gap-declared discovery. Skill catalog lookup. Using MCP as a backend protocol is a different decision from dumping every MCP schema at session start. Group perception tools by search, read, parse, and query. Retrieve a shortlist only when the set is already huge.

Check. Turn-zero full schemas are well under a hundred, or a written exception names the layer that replaced the flat list. The architecture doc names which layer each capability uses.

source-ids: three-disclosure-layers-load-discover-lookup, scale-degrades-selection-and-cache, expose-index-load-schema-on-demand, keep-mcp-backend-separate-from-frontend-disclosure, group-tools-by-information-source-type, retrieve-shortlist-by-semantic-similarity

### `declare-capability-gap-then-inject`

When the needed tool is missing from the opening shortlist.

Rule. Keep a few core tools plus one discover tool resident. Accept a need statement mid-task. Match server first, then tool inside it. Return explicit not-found instead of a low-score cousin. Append the schema once at the tail and leave it at that offset. Blame cache misses on TTL expiry or a set edit, not on discovery itself. Select or train models that can read a schema that appeared mid-history.

Check. A two-turn log shows an unchanged prefix, a trailing schema, and a cache hit on prefix tokens. A missing capability returns a not-found object.

source-ids: declare-capability-gap-then-inject, keep-core-plus-search-meta-tool, match-server-then-tool, return-explicit-not-found-and-fallback, append-schemas-once-then-pin, do-not-reposition-loaded-schemas, invalidate-cache-only-on-ttl-or-set-edit, post-train-for-scattered-tool-defs

### `progressive-disclosure-catalog-then-body`

When startup would otherwise hold full playbooks, or a team is about to build embeddings just to hide skills.

Rule. At start, show name and description. Read the skill body when the current task needs it. Follow inner links to scripts last. If the capability can live as a skill, skip a dedicated retrieval stack. Hub folders and MCP-delivered skills are two transports for one document.

Check. Startup tokens for skills are catalog lines only. A using trace shows a later read of `SKILL.md`. Skill-form capabilities have no embedding-index box on the diagram.

source-ids: progressive-disclosure-catalog-then-body, skills-drop-embedding-index-requirement, skills-can-travel-over-mcp-or-hub

### `perception-design-focus-granularity`

When adding search, fetch, grep, or read.

Rule. Grain and output volume are the design problem. Search returns title, location, snippet, total, and a cursor. Read supports offset and limit. Every clip states what was omitted and how to continue. Bodies over about 10,000 characters compress against the current question. Cache and parallelize read-only calls. Do not grant that freedom to execution.

Check. One search tool pages structured candidates. One read tool supports range plus an omission notice. Perception rows are marked cacheable and parallel-safe. Execution rows are not.

source-ids: perception-design-focus-granularity, compress-oversized-perception-by-query-intent, search-return-candidates-then-page, read-with-offset-and-visible-truncation, cache-and-parallelize-read-only-perception

### `pick-among-three-multimodal-paths`

When images, audio, video, or PDFs enter the agent.

Rule. Pick native pixels when spatial layout is the task. Extract to text when the file is mostly words and layout is disposable. Wrap a specialist as a question-answer tool when the main model is text-only but the question is not. Record the trade. OCR on a dashboard the question asks about spatially is the wrong path.

Check. A layout question uses an image-bearing path. A prose-only PDF uses extraction. A vision question in the main transcript is a short tool Q and A, not raw media.

source-ids: pick-among-three-multimodal-paths, choose-multimodal-return-form-by-layout-need, native-vision-via-shared-token-space, extract-text-when-layout-is-disposable, wrap-specialist-multimodal-as-qa-tools

### `fail-fast-validate-inputs-without-correction`

When adding shell, write, edit, send, pay, or any world-changing tool.

Rule. Validate, then fail. Do not sanitize a traversal or a splice into a guessed-safe command. Scope files to a workspace and parse intent. String deny lists are the weakest layer. Grade risk. Pre-approve high-risk work with a similar-strength model from another family, same rules, different job. Write a rejection into the trajectory as a tool error. After a reversible action, check in another modality. When a cheap oracle exists, run it in the same return. Persist long output and return head plus tail. A venv is not a sandbox. Scale isolation from process to container to microVM. Log, audit, and alert. Retry with an idempotency key or a query-first path. Mail, money, and calls use prepare then commit. Do not blind-replay a timed-out send.

Check. Path-traversal fixtures return validation errors and produce no side effect. Irreversible tools name a reviewer from another family. Email and payment schemas have prepare and commit. The deploy matrix maps local-dev, production, and untrusted to process, container, or microVM.

source-ids: execution-design-focus-security, fail-fast-validate-inputs-without-correction, constrain-permissions-beyond-string-blacklists, pre-approve-irreversible-ops-across-model-families, give-proposer-and-reviewer-same-rules-different-focus, feed-reviewer-rejection-as-tool-error, grade-approval-and-escalate-uncertainty, post-validate-by-switching-modality, auto-validate-when-result-is-observable, persist-long-output-return-head-and-tail, treat-venv-as-dependency-isolation-not-sandbox, scale-isolation-process-container-microvm, log-audit-and-alert-execution-tools, make-retries-idempotent-or-query-first, two-phase-confirm-non-idempotent-side-effects

### `sidecar-classifies-structured-call-fields-only`

When a live call must be gated while the main model streams, or a review mechanism is being chosen.

Rule. Proposer-reviewer shares context and judges a plan or a result. A sidecar runs in parallel on structured fields only, tool name and arguments. Hide user text, web text, descriptions, and chain-of-thought. Show progress before admit. Side effects wait on the gate. After a short deny streak, ask a human. The same sidecar pattern can prefetch memories or summarize a long tool result.

Check. The sidecar request body contains only structured call fields. A hidden allow-this-command in a description does not flip approve. Three denies open a human prompt and issue no fourth automatic retry.

source-ids: sidecar-classifies-structured-call-fields-only, distinguish-proposer-reviewer-from-sidecar, break-sidecar-reject-loops-to-human, overlap-security-check-with-progress-display, sidecar-can-prefetch-context-in-parallel

### `expose-spawn-message-cancel-and-discover`

When a task needs parallelism or a specialist context.

Rule. Export spawn, message, cancel, and discover. Split specialists instead of growing one omni-agent. Fix role, scope, and output schema. Tag inbound text by source. Wait only for short jobs. Return a task id for long ones. Human gates need a timeout, a conservative default, and a priority channel for urgent work. Store HITL reasons. Lift generalizable rules into a skill. Keep high-dimensional preferences for later training.

Check. The collaboration surface lists all four primitives. A cancelled worker stops further model calls. A HITL test that never answers applies the default.

source-ids: collaboration-design-focus-parallel-specialize, specialize-subagents-instead-of-one-omni, label-subagent-context-sources, fix-subagent-role-scope-and-output-schema, expose-spawn-message-cancel-and-discover, choose-sync-async-stream-or-multi-turn, hitl-timeouts-defaults-and-priority-channels, recycle-hitl-into-skills-or-training-data

## Failure diagnostics

- Edit cannot match text the model just read. Cluster `never-silently-rewrite-arguments`. Logged args must equal model args.
- Wrong tool on a vague request. Cluster `describe-when-not-just-what` first. Then `three-disclosure-layers-load-discover-lookup` if the list is huge.
- Prefix cache dies after every discover. Cluster `declare-capability-gap-then-inject`. The schema was re-emitted or moved.
- Hundreds of schemas at turn zero. Cluster `three-disclosure-layers-load-discover-lookup`.
- Community MCP plus a god token plus mail. Cluster `treat-tool-descriptions-as-untrusted-input`.
- `../` becomes a guessed-safe path. Cluster `fail-fast-validate-inputs-without-correction`.
- Sidecar approves after reading a description. Cluster `sidecar-classifies-structured-call-fields-only`.
- Approval hangs with no timeout. Cluster `expose-spawn-message-cancel-and-discover`.
- Timer or notify implemented as a sync function. Cluster `defer-event-and-user-comm-tools`. Stop this playbook.
- Calculator tool beside a Python interpreter. Cluster `choose-form-on-four-dimensions`.
- Venv sold as the security boundary. Cluster `fail-fast-validate-inputs-without-correction`.
- Search concatenates full documents. Cluster `perception-design-focus-granularity`.

## Namespaced drills

### 04-tools-q1

MCP splits schemas from any one framework. It still standardizes a capability call, not a continuously online agent. Wake-and-queue, mail callbacks, and retry across sessions belong in the async runtime. Shared conventions there widen the bus without stuffing a kernel into the protocol. Do not wait for MCP to grow timers.

### 04-tools-q2

Two servers offer near-duplicate tools. Two same-named tools return summary versus full text. Before connect, review descriptions, pin versions, and attach least-privilege credentials. Namespace so a twin cannot steal a trusted call. At run time, narrow with groups and discovery. The model can use summary versus full only if those behaviors are written in the description.

### 04-tools-q3

A cheap oracle belongs after a config write or a rendered document. Apply the change in a sandbox, or look at frames. Skip the pattern when the check would be another irreversible event, mail, a call, or a money move. Those paths use a different-family pre-approve and a prepare-then-commit split.

### 04-tools-q4

Thousands of tools wreck selection. Discovery is not the only lever. Group by server or app, then pick a leaf. Keep a thin catalog and look up bodies like a handbook. Keep a few daily-driver tools resident. Reach the rest through the index.

source-ids: stress-test-mcp-overlap-validation-and-scale

## Depends-on

`playbooks/getting-started.md` places the five tool types and the inside-versus-outside boundary. `playbooks/context-engineering.md` owns prefix stability, untrusted wrappers, and the three skill layers this file specializes as `three-disclosure-layers-load-discover-lookup`.

Needed by `playbooks/coding-agent.md` when a general executor mints adapters or new tools. Needed by `playbooks/interaction.md` for the two deferred categories. Needed by `playbooks/multi-agent.md` once topology outgrows the four primitives.

## Open tensions

General versus dedicated. `prefer-general-executors-default` wins for reversible composition. `dedicated-for-security-permissions-audit` wins for permissioned or auditable effects. The same split appears in chapter 1 as explore versus risk.

Form versus disclosure. `form-vs-disclosure-independent` forbids inferring one from the other. A skill catalog does not mean the disclosure problem is solved.

Progressive disclosure has twins in other chapters. `disclose-skills-in-three-layers` and `progressive-disclosure` point here for the tool-catalog version.

Event and user-communication tools stay classified and unimplemented in this layer. The hard stop is `defer-event-and-user-comm-tools`.
