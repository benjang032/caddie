# Context Engineering

Terms. Context is every token on the call. Trajectory is the growing role list. Prefix is the frozen system plus core tools. Cache boundary splits shared bytes from session bytes. Status bar is code-owned tail state. Skill is a three-layer domain packet. Isolation parks bulky work in a child. Source tags mark untrusted bodies.

## What this is for

The model acts only on the window it sees. The harness must assemble a frozen prefix, a growing trajectory, on-demand skills, a code-owned tail bar, and a planned compress or isolate path. This chapter owns single-task information layout. Cross-session memory is a later store.

## Core model

Frozen prefix, growing trajectory, tagged tail status. Rebuild a sufficient `c_t` on every stateless call. Cache reuse is an architectural constraint, not a later optimization.

## Clusters

### `context-is-what-the-model-sees`

When. Designing or reviewing any agent turn.
Rule. Treat context as every token on the call. Put assembly in one harness function. Rebuild a sufficient window each round because the API keeps no session brain.
Check. Diff the outgoing request against system, tools, user, assistant, tool results, and tail state. Fail the review if a second path concatenates prompts.
source-ids: context-is-what-the-model-sees, harness-implements-context-layer, next-action-depends-on-full-ct, reconstruct-context-every-call, pack-all-needed-info-in-one-stateless-call, build-each-call-from-messages-and-tools

### `context-sets-capability-ceiling`

When. A business task fails that a benchmark model should handle.
Rule. Raise context quality before swapping models. Ship code structure, process, and environment as the minimum brief. Write tacit rules into files a new run can read. Onboard each session as a capable hire on day one.
Check. Mark one failed trajectory as missing fact, missing process, or missing environment. If most marks are missing facts, keep the model and fix the window.
source-ids: context-sets-capability-ceiling, supply-code-process-environment, treat-tacit-knowledge-as-blocker, document-driven-teams-feed-agents, onboard-agent-like-new-hire, write-decisions-to-documents

### `assign-four-roles-plus-tools-field`

When. Mapping harness state onto an API request.
Rule. Use system, user, assistant, and tool for the four message parts. Put schemas in the tools field. Send structured roles and let the server apply the chat template. Keep tool output out of the user role except a documented status wrapper.
Check. Validate a recorded request. Every item is one of the four roles. Every core schema lives under tools or a documented late append.
source-ids: assign-four-roles-plus-tools-field, keep-system-once-at-front, bind-tool-results-by-call-id, send-structured-messages-not-concat, never-flatten-roles-to-plaintext, never-mislabel-tool-as-user, preserve-roles-to-separate-instruction-from-data

### `branch-on-tool-calls-or-exit`

When. Implementing or reviewing the core loop. Parser-leaked comment headings from the sample loop belong here, not as chapter titles.
Rule. The model requests. The harness executes. Branch on tool_calls or exit. Register static schemas once. Seed system then user. Append the assistant message before results, then recall. Cap iterations. Detect and break repeat tool loops. Parse arguments before dispatch. Replay assistant tool_calls verbatim. Parallelize only independent calls.
Check. Walk a two-round fixture. After round 1 the list has tool messages. After round 2 the list ends with assistant text. A forced forever-tool stops at the cap. A repeated read_file yields a stop or strategy change, not another identical call.
source-ids: branch-on-tool-calls-or-exit, model-requests-framework-executes, parallelize-independent-tool-calls, serialize-dependent-tool-args, replay-assistant-tool-calls-verbatim, resend-full-history-each-round, framework-owns-growing-message-list, register-static-tool-schemas-once, stub-or-real-execution-stays-in-harness, parse-tool-arguments-before-dispatch, seed-system-then-user, append-reply-then-results-then-recall, cap-loop-with-max-iterations, detect-and-break-repeat-tool-loops

### `assemble-prefix-trajectory-status`

When. Every production model call after the toy loop.
Rule. Build messages as frozen prefix, then trajectory, then a tail status message. Send the frozen core tools. Compress only when a budget gate fires. Leave the latest evidence in place.
Check. Read the assembler. Status is last. Tools are the frozen set. Prefix hashes match across a ten-turn log unless a recorded compress step replaced a span.
source-ids: assemble-prefix-trajectory-status, split-static-prefix-from-trajectory

### `stream-think-then-text-then-tools`

When. Streaming UI or early tool dispatch on a thinking model.
Rule. Parse stream order as internal reasoning, then user-facing text, then tool-call tokens. Start the first validated tool before later tokens finish. Follow the current vendor rule for historical reasoning_content. Treat old think as waste in plain chat and as state in long tool loops, then bound it.
Check. Capture a streamed two-call turn. Call 1 starts before call 2 tokens end. Each supported model has a contract test for required reasoning fields.
source-ids: stream-think-then-text-then-tools, start-first-valid-tool-during-stream, pass-reasoning-per-vendor-contract, weigh-strip-vs-retain-historical-cot

### `never-edit-finalized-system-or-tools`

When. Tempted to add a clock, flag, extra space, or a sorted tool list to the prefix.
Rule. Once system prompt and core tool definitions are finalized, do not change them. Reuse KV only through the token before the first difference. Freeze tool order. Do not slide history off the front. Place runtime variance after the cache boundary. Byte-align an inheriting child prefix. Treat editable KV notes as research.
Check. CI-hash the system file and the tools JSON. Fail the build on accidental churn. A one-character system edit must show a cache miss from the edit point.
source-ids: never-edit-finalized-system-or-tools, reuse-kv-only-for-unchanged-prefix, invalidate-from-first-changed-token, freeze-tool-definition-order, never-slide-away-history, distinguish-in-request-kv-from-cross-request-prompt-cache, split-prompt-at-cache-boundary, move-runtime-flags-after-boundary, byte-align-subagent-inherited-prefix, freeze-replacement-strings-for-previews, treat-editable-kv-as-research-not-default, expect-quadratic-prefill-without-cache, expect-linear-decode-with-cache, treat-qkv-as-search-label-content, cache-keys-and-values-across-tokens, expect-attention-sink-at-first-token, place-critical-facts-at-ends

### `treat-chat-template-as-envelope`

When. Reasoning about tokens, cache, or chain-of-thought retention.
Rule. Treat the chat template as the envelope that wraps API letters with role and boundary special tokens. Do not hand-write USER and ASSISTANT markers as the live path.
Check. Dump server tokens for one request. Role boundaries come from the official template, not from harness string art.
source-ids: treat-chat-template-as-envelope

### `never-put-clock-in-system-prompt`

When. The agent needs current time, locale, OS, plan tier, or quota.
Rule. Do not embed a changing timestamp or live user config in the system prompt. Append those facts at the tail or fetch them with a tool.
Check. Grep system templates for date, time, now, plan, and quota interpolation. Require zero matches before the cache boundary.
source-ids: never-put-clock-in-system-prompt, never-embed-live-user-config-in-prefix, append-timestamps-and-status-at-tail

### `measure-ttft-after-prefix-edit`

When. A system prompt or tool list changed by a few characters, or a merge is about to land.
Rule. Compare time to first token on an unchanged prefix versus an early edit. Keep hierarchy and tool prose in the ablation pack. Treat tone stunts as low leverage.
Check. A canary hashes the prefix and records TTFT. A prompt change without a before-and-after task metric does not merge.
source-ids: measure-ttft-after-prefix-edit, ablation-structure-and-tool-prose-matter

### `write-sops-not-rule-piles`

When. The system prompt has grown into scattered rules.
Rule. Organize the prompt as staged procedures with a next step at each stage. Product owns executable policy. Engineering encodes format. Route exceptions from the current stage. Reserve uppercase MUST and NEVER for true hard stops. Nest Markdown headings over named XML spans.
Check. A reviewer who does not own the product can point to the current stage for a typical ticket. A flat bullet pile fails.
source-ids: write-sops-not-rule-piles, route-exceptions-by-current-stage, make-product-own-executable-rules, remove-discretion-from-billing-choices, define-numeric-thresholds-and-rounding, test-prompt-as-new-hire-manual, reserve-uppercase-for-hard-stops, cap-failure-reply-length, nest-markdown-headings-over-xml-blocks, group-tool-rules-under-named-sections, encode-file-prechecks-as-executable-steps, encode-timeout-and-retry-as-bounds

### `use-few-shots-when-style-beats-rules`

When. Tone, layout, or nuance keeps missing under prose rules.
Rule. Prefer two or three high-quality boundary pairs over a long style essay. Freeze the set per task type. Do not expect those pairs to train the next session.
Check. Hash example blocks across a day of one task type. The hash stays constant. More than three pairs needs a written reason.
source-ids: use-few-shots-when-style-beats-rules, freeze-example-sets-per-task-type, prefer-two-or-three-boundary-examples, treat-few-shot-as-session-local-adaptation

### `write-tool-docs-as-operating-manuals`

When. Authoring the tools field or watching the always-on list grow.
Rule. Write each core tool as an operating manual with a boundary, an example value, and a relation or batch note. Freeze a small core. Append discovered schemas once. Use mid-conversation tool definitions only on models trained for that pattern.
Check. Count always-on full schemas. Growth is rare and reviewed as a cache-key change. After a tool_search, the full schema stays at a fixed index.
source-ids: write-tool-docs-as-operating-manuals, append-discovered-schemas-once, require-trained-support-for-mid-context-tools, keep-core-tool-set-small-and-stable

### `wrap-external-content-as-untrusted-data`

When. A webpage, email, PDF, or file body enters the window.
Rule. Wrap untrusted text in source tags and state that inner instructions are not to be executed. Treat every perception tool as an injection surface. Phrase filters are a weak auxiliary. Review third-party skills before install. Keep the status bar off untrusted inputs. Stack context defense under permission and sandbox controls.
Check. Inspect a web-read tool message. It includes a source tag around the body. A planted status-like sentence on a page does not change the harness bar. A high-risk write stays blocked even when the model says it will comply.
source-ids: wrap-external-content-as-untrusted-data, treat-every-perception-tool-as-injection-surface, treat-sanitization-as-weak-auxiliary, review-third-party-skills-before-install, keep-status-bar-off-untrusted-inputs, stack-context-defense-under-execution-controls

### `disclose-skills-in-three-layers`

When. Packaging a domain capability or watching the system prompt grow a new manual.
Rule. Ship a short name and description first, the full SKILL.md when selected, then optional linked detail. Keep unused manuals out of the window. Inject the body at the invocation site, not into the frozen system line. Match the vendor-trained skill pattern. This is the same disclosure pattern as `progressive-disclosure` and `three-disclosure-layers-load-discover-lookup`.
Check. Token accounting shows catalog tokens every turn and body tokens only after the first load. A new session can name installed skills from the catalog without a file read.
source-ids: disclose-skills-in-three-layers, load-domain-knowledge-on-demand, keep-skill-catalog-always-visible, keep-catalog-small-and-body-late, inject-skill-body-at-invocation, match-skill-pattern-to-vendor-training

### `write-skill-description-as-router`

When. Authoring the always-visible skill description.
Rule. Write Use when and Do not use when, including negative examples. Do not write a feature brochure. The catalog carries the metacognition the model lacks.
Check. Each installed skill description contains a use-when clause and a do-not-use-when clause.
source-ids: write-skill-description-as-router

### `write-role-principles-bans-and-refs`

When. Drafting SKILL.md.
Rule. Start with who it serves, three to five principles with examples, prohibitions with exceptions, and references. Phrase each rule as scope, action, exception, and check. Iterate from sample diffs. Bundle scripts and templates with the skill.
Check. A skill review ticks those four parts or records an explicit waiver. Sampled rules have the four pieces.
source-ids: write-role-principles-bans-and-refs, phrase-rules-as-scope-action-exception-check, iterate-skill-from-sample-diffs, bundle-scripts-and-templates-in-skill

### `treat-icl-as-retrieval-not-aggregation`

When. Expecting one forward pass to count, tally, or summarize the whole trace.
Rule. In-context learning retrieves. It does not reliably aggregate. Precompute conclusions and write them back as tail facts. Replace raw logs with retrievable notes. Distinguish rot (fits but cannot be found) from overflow (cannot fit).
Check. Ask how many times a tool ran. The answer matches a code counter in the bar, not a silent recount. A quality drop before the cap is rot, not a reason to scale the window and stop.
source-ids: treat-icl-as-retrieval-not-aggregation, distill-counts-into-explicit-facts, pin-status-near-generation-for-attention, use-status-bar-to-flatten-reasoning-cost, replace-raw-logs-with-retrievable-conclusions, distinguish-context-rot-from-overflow, inject-runtime-state-as-status-bar

### `maintain-status-in-deterministic-code`

When. Tempted to ask the model to summarize the whole trace into a bar.
Rule. Compute the bar in deterministic code. If a model must extract items, extract one by one and aggregate in code. Never ask for a one-shot batch count. Treat the bar as a lossy projection. Keep raw evidence when later query dimensions are unknown.
Check. Unit-test the bar builder against a fixture log. The model is not on the path for counts.
source-ids: maintain-status-in-deterministic-code, keep-raw-evidence-when-query-dims-unknown

### `combine-timestamp-counter-todo-errors-env`

When. Shipping a production bar rather than a single field.
Rule. Enable timestamp, counter, restated TODOs, error alerts, and environment together. Stamp events next to the event. Append the bar as a tagged user message. Do not edit the leading system line.
Check. A missing-file fixture checks cwd, lists files, then cancels or replaces the TODO. After a cd tool, the next bar shows the new directory. The last mid-task message is role user and contains the status tag.
source-ids: combine-timestamp-counter-todo-errors-env, restated-todos-at-tail, attach-event-side-channels, surface-env-and-repeat-alerts, append-status-as-tagged-user-message, use-tool-counters-to-change-strategy

### `choose-append-vs-replace-by-cost`

When. The bar must update every turn.
Rule. Compare replacing the previous bar with appending a new one. Prefer append for a small bounded bar in a short session. Prefer replace for a wide, frequent, or unbounded bar. Record size, tokens between updates, expected count, and cache discount.
Check. A design note records those inputs and the chosen machine. A long-session fixture contains exactly one live status block per request when replace is the machine.
source-ids: choose-append-vs-replace-by-cost, prefer-append-for-small-bounded-status, prefer-replace-for-large-frequent-status

### `stack-five-compression-layers`

When. A single summary call is the only compress path, or density is already poor.
Rule. Combine tool-result budgets, noise deletion, API micro-edits near overflow, archival per-round notes, and last-resort full compress. Compress for length, retrievable quality, and early-quit anxiety. Skip summarizing chrome. Circuit-break a failed full compress. Prefer context-aware summaries over isolated blurbs.
Check. The compress module exposes five named stages. A chrome-heavy page leaves citations or used lines only.
source-ids: stack-five-compression-layers, treat-compression-as-density-not-only-length, compress-for-length-quality-and-anxiety, skip-summarizing-pure-noise, use-api-edits-only-near-overflow, archive-round-by-round-not-squash, circuit-break-failed-full-compress, prefer-context-aware-summaries

### `trigger-batch-compress-near-eighty-percent`

When. Trajectory growth conflicts with prefix-cache advice.
Rule. Edit the list between API calls, not during a call. When prompt tokens pass about 80 percent of the window, compress all unmarked old tool bodies at once and mark them. Never compress the static prefix. Isolation remains the default when a child can return a bounded artifact.
Check. A token probe fires one batch at the threshold and leaves later already-marked bodies alone. After compress, the system hash and tools JSON hash still match.
source-ids: trigger-batch-compress-near-eighty-percent, compress-between-calls-in-batches, never-compress-the-static-prefix

### `preserve-value-integrity-relevance-understanding`

When. Writing a compress prompt or a keep-list.
Rule. Keep decisions, constraints, and failures over supporting evidence over noise. Keep times, names, and identifiers intact. Attach a source URL or disk pointer to every kept fact. Write decisions into documents during the task so compress is not the only memory.
Check. A compress eval fails if a timestamp, company name, or id in the gold keep-set is missing. Every sentence in a compressed note has a citation or an explicit derived mark.
source-ids: preserve-value-integrity-relevance-understanding, keep-citations-as-lossless-index, manage-information-explicitly-inside-one-task

### `isolate-bulky-exploration-in-subagents`

When. A broad search or scan would pour tens of thousands of tokens into the main window.
Rule. Delegate the bulky work. Keep only a short task and a short conclusion in the main trace. Write a complete goal, constraints, and done check into the child brief. Isolation wins when a bounded artifact can return. Batch compress wins when one trajectory must stay continuous and the window nears the cap.
Check. A find-the-callback task adds about two main messages, not dozens of file bodies. A child-spawn test fails if the brief omits the question or the return shape.
source-ids: isolate-bulky-exploration-in-subagents, brief-subagents-with-self-contained-goals

`apply-chapter-decision-rules-to-design-reviews` is collapsed into the drills below. Do not treat that wrapper as its own cluster.

## Failure diagnostics

| Symptom | First cluster | First check |
| --- | --- | --- |
| TTFT jumped after a tiny prompt tweak | `never-edit-finalized-system-or-tools` | Prefix hash changed. Compare TTFT on a frozen canary. |
| Clock, locale, or plan sits in the system line | `never-put-clock-in-system-prompt` | Grep the prefix for live interpolation. |
| Same tool and args repeat | `branch-on-tool-calls-or-exit` | Histogram the tool log. Cap and repeat-break must fire. |
| Window grows without bound | `trigger-batch-compress-near-eighty-percent` | Last-N deletion is present, or no 80 percent batch exists. |
| Main trace holds dozens of search bodies | `isolate-bulky-exploration-in-subagents` | Parent message count after a bulky scan. |
| Webpage or PDF hijacked the next action | `wrap-external-content-as-untrusted-data` | Tool body lacks source tags, or bar copied page text. |
| Skill never loads | `write-skill-description-as-router` | Description lacks Use when and Do not use when. |
| Skill body sits in the frozen system line | `disclose-skills-in-three-layers` | Body tokens appear before first invoke. |
| Count cap or quota is violated | `maintain-status-in-deterministic-code` | Bar count was model-tallied or missing. |
| Always-on tool list exploded | `write-tool-docs-as-operating-manuals` | Core schema count grew without a cache-key review. |
| Prompt success dropped after a tidy rewrite | `write-sops-not-rule-piles` | Hierarchy became a pile. Ablation was skipped. |
| Compress note lost a UUID or decision | `preserve-value-integrity-relevance-understanding` | Gold keep-set item is absent. |

## Namespaced drills

`apply-chapter-decision-rules-to-design-reviews` is the wrapper. Work the machines, not a new window policy.

#### `02-context-engineering-q1`

A last-N sliding window drops early tool results and busts the prefix cache. Keeping every raw body grows without bound. Design a history policy that keeps needed facts, bounds length, and leaves the KV prefix intact. Reject last-N deletion. Use threshold batch compress, disk previews, and sub-agent isolation.

#### `02-context-engineering-q2`

Some templates keep think text only after the last real user line. A long ReAct loop can drown in that text. One vendor line stripped historical reasoning. A later line required every reasoning_content when tools were present. Bound old think with a fixed-position note. Keep the latest spans. Follow the current vendor contract.

#### `02-context-engineering-q3`

Context-aware compression can shrink about 148k characters to about 2k. That is a lossy projection. Bound the risk with a lossless index, off-window raw store, and a verbatim keep-list of decisions, times, names, and ids.

#### `02-context-engineering-q4`

A wrong bar count can drive a harmful extra call. Keep the model off the count path. Build the bar in code. Track bar accuracy against the event log. Fill fields only from trusted observations.

#### `02-context-engineering-q5`

A disorganized system prompt can drop success by more than thirty percent. Treat prompts as code. Product defines rules. Engineering encodes structure. Require a task metric and a prefix-hash check before merge.

#### `02-context-engineering-q6`

If in-context learning is mostly retrieval, stop pouring more raw text into the window. Distill conclusions into the bar. Isolate noisy work. Treat tools as a way to write facts back.

#### `02-context-engineering-q7`

Progressive disclosure loads a skill body only after a decision. The model does not know what it does not know. Keep name and description resident. Write Use when and Do not use when so the catalog routes.

#### `02-context-engineering-q8`

After a skill body loads, later steps may or may not follow it. Inject site and vendor training change the answer. Leave the body where it first landed. Do not rewrite it into the frozen system line.

#### `02-context-engineering-q9`

Live clocks and a changing tool order bust prefix cache. Freeze a small core in a fixed order. Deliver the long tail through skills and one-shot schema append. Copy an inherited child prefix byte-for-byte.

## Depends-on

- `playbooks/getting-started.md` and `lessons/01-getting-started.md` for the inside-boundary formula, the ReAct loop, and harness ownership of the message list.
- `SKILL.md` for the stable-prefix non-negotiable.

## Needed-by

- `playbooks/memory-knowledge.md` for the later user-keyed archive. This chapter does not solve cross-task memory.
- `playbooks/tools.md` for form versus disclosure. Skill layers here are the context half of that split.
- `playbooks/multi-agent.md` for shared versus isolated context. Isolation here is the single-task default.

## Open tensions

Isolation versus compression. `isolate-bulky-exploration-in-subagents` wins when a subtask can return a bounded artifact. `trigger-batch-compress-near-eighty-percent` and `stack-five-compression-layers` win when one trajectory must stay continuous and the window nears the cap. Isolation is the default.

Progressive disclosure is one pattern with three names. This file owns `disclose-skills-in-three-layers`. Chapter 1 owns `progressive-disclosure`. Chapter 4 owns `three-disclosure-layers-load-discover-lookup`.
