# continual-evolution-closed-loop

## What this is for

This chapter turns scored operational trajectories into later behavior that is allowed to change. A log, a reflection, or an in-session repair is not evolution. Evolution requires evidence, a released artifact on a named carrier, and a non-degradation check. The model is a component. The system around it records, verifies, routes, candidates, and gates.

## Core model

Dual loop around a frozen approval root. Four carriers (knowledge, instructions, programs, weights). Online serving appends immutable evidence. Offline evolution proposes and releases versions. Validators, thresholds, audit logs, keys, and stable backups sit in a trusted root the modifier cannot edit.

Terms. Continual evolution is a released, verified later-behavior change grounded in scored evidence. Experience knowledge is conditioned action advice, not a world fact or a user profile. A candidate cannot serve until gates pass. Sleep learning is offline consolidation, not an in-session MEMORY write.

## Clusters

### `preserve-is-not-learn`

When a run is written to a log, vector store, or long context.

Compare, generalize, and validate before changing later behavior. A stored trajectory mixes sound strategy with luck, misattribution, and untrusted input. In-session adaptation dies with the context. Weights do not change at inference. Retrieving a case is not extracting a transferable step.

Check. A promoted lesson cites a multi-run evidence table plus a held-out transfer result, not a single log id. A fresh session on the same family lacks the repair unless a released artifact exists.

source-ids: preserve-is-not-learn, within-task-adaptation-does-not-persist, evaluate-before-summarize, reflection-is-not-evidence, never-promote-single-run-summary, evolution-requires-trace-change-verify

### `three-layer-trajectory-verification`

When a task looks finished because tests passed or a user thanked the agent.

Score outcome, process, and quality as separate records. Implement the lower two in code against environmental state and policy. Delegate only hard-to-formalize quality items to a judge, and require per-item scores, citations, and uncertainty. Keep low-confidence rows out of automatic learning. Satisfaction is a quality metric among compliant runs. It cannot cancel a rule, privacy, or promise-action fail.

Check. One labeled trajectory has three distinct records. Any outcome or permission metric implemented as an LLM call fails. The learning set contains no below-threshold row. A high-satisfaction leak is a hard fail and is absent from the positive set.

source-ids: three-layer-trajectory-verification, score-outcome-and-process, code-first-lower-layers, rubric-with-evidence-and-uncertainty, exclude-low-confidence-from-learning, satisfaction-cannot-be-sole-signal, guardrails-override-satisfaction, diagnosis-must-route-update-layer

### `route-update-by-representation`

When a learning signal says the agent must change.

Pick the medium that can hold the capability. Facts fit documents. Verbal strategies fit prompts and skills. Deterministic procedures and non-bypassable limits fit programs. Perception, style, and implicit strategy fit parameters. Split a mixed job across carriers and name which carrier is authoritative on conflict. Representation picks the medium. Stability picks cadence. Prefer the smallest layer that can be tested and undone. A string-comparable false promise still needs a harness check on high-risk paths.

Check. The last five proposals name representation class, medium, and reason. Non-bypassable constraints have a program-level gate. A medical or analogously regulated map names knowledge, skill, code, and parameter roles without overlapping authority.

source-ids: route-update-by-representation, four-media-applicable-boundaries, split-capability-across-carriers, medium-follows-representation-not-stability, choose-smallest-validatable-layer, keep-stable-rules-in-server-code, coordinate-four-media-for-medical-safety, parameterize-inexpressible-capabilities

### `routing-is-only-a-proposal`

When the medium router emits a destination.

Hold the change as a candidate until independent validation and a release gate succeed. Choosing where to write is not earning the right to change live behavior. Every medium path (knowledge, prompt, skill, code, weights) creates a record that production cannot load until the gate flips the flag.

Check. Production cannot load a candidate. A router write that lands in serving files fails the audit.

source-ids: routing-is-only-a-proposal, wrap-learning-as-autonomous-system, isolate-candidates-from-production-traffic

### `distinguish-user-memory-from-action-experience`

When deciding whether a note belongs in a profile store or in experience learning.

Write what the world is like to memory. Write what to do under which conditions to experience artifacts. Action-policy rows need applicability, prohibitions, evidence ids, and a verification time. A project MEMORY file written during a session is not a sleep cycle.

Check. Ten stored notes are labeled world-fact or action-policy. Action-policy rows carry conditions and evidence. The architecture note describes both stores and does not label in-session writes as the full consolidator.

source-ids: distinguish-user-memory-from-action-experience, memory-vs-experience-learning, distinguish-domain-facts-from-action-experience, bound-and-layer-memory-loading

### `five-step-knowledge-distillation`

When turning operations into an experience store.

Keep raw runs immutable, per-run analyses mutable, and formal documents induced only after multi-run comparison. Distill through preserve, analyze, evidence table, promote above a support threshold, then transfer on unused tasks. Formal docs need scenarios, strategies, prohibitions, exceptions, sources, and last verification time. Stratify contradicting rows by environment version and conditions. Do not vote by count. Successes mine strategies. Failures mine exclusions. Partials locate the broken segment.

Check. One formal doc traces through five job records. Derivation and transfer task ids do not intersect. A four-row fixture with three old-version wins and one new-version fail narrows scope and mints a new-version candidate instead of a global revoke.

source-ids: five-step-knowledge-distillation, three-layer-experience-store, formal-experience-document-schema, preserve-evidence-then-organize-offline, success-failure-partial-roles, keep-derivation-and-transfer-disjoint, stratify-evidence-before-revoking-experience, version-freshness-and-retire-knowledge

### `observed-behavior-is-not-ought`

When inducing policy from customer-service failures or evolving a clarification skill.

Do not encode a frequent failure terminal as the official fallback. Feed the deriver the objects the rule must distinguish (tool ownership, policy text), not only error text. Verify on a disjoint transfer set with an independent harness. Measure the behaviors the new rule names, not only pass rate. Escalate on explicit human request or safety, not on an ordinary fee dispute. A clarification skill encodes a scoped path (assume-and-go versus ask-and-spec). It never requires an interview on every task. Bind feedback to trajectory, task type, and outcome before changing the skill. The skill asks and assembles a spec. The harness vetoes high-risk writes when confirmation is missing.

Check. Induced rules that recommend the eval's failure action are absent from the released candidate. Deriver and transfer ids are disjoint. A high-risk write without a confirmation token is refused even if skill text claims agreement. The skill names both a proceed-with-assumptions branch and an ask-first branch.

source-ids: observed-behavior-is-not-ought, skill-asks-harness-vetoes, deriver-input-sets-induced-rule, independently-verify-derived-rules, repair-plain-tool-misaddress, escalate-only-on-human-or-safety, measure-rule-aligned-behaviors, scoped-clarification-not-always-ask, risk-ambiguity-rework-decision-path, reconfirm-when-spec-breaks, bind-feedback-to-trajectory-and-outcome, release-clarification-only-if-less-deviation, customer-service-seven-dimensions

### `write-falsifiable-change-contract`

When compiling a repeated operable path or patching harness code.

Turn stable, repetitive, verifiable work into a parameterized program. Write a pre-declared contract (evidence, cause, target, expected gain, possible regressions, tests) and a bounded generator pack. Keep a first success as `candidate` until reset replay passes with before-action, after-action, and final-state checks. Locators are find aids, not proof of done. Do not validate mail, orders, or other side effects in a live account. On check fail, invalidate, unindex, and fall back to exploration.

Check. A validated workflow has a reset-and-replay receipt and template variables in place of first-run literals. A fixture that clicks Send with an empty required field fails even if every locator matched. A workflow without a reset hook is not retrievable for replay.

source-ids: write-falsifiable-change-contract, compile-stable-repetitive-verifiable-ops, four-self-modification-layers, browser-workflow-six-stage-lifecycle, locator-does-not-prove-completion, candidate-until-reset-replay-passes, never-validate-side-effects-in-production, invalidate-and-fallback-on-check-fail, require-before-after-and-final-checks, bound-candidate-space-with-rejects

### `isolate-candidates-from-production-traffic`

When any new capability is first created.

Land knowledge, prompts, skills, programs, and weights in a candidate area that cannot serve. Scan generated code and dependencies (sandbox, permissions, supply chain, behavioral tests) before promote. Treat self-modification as a release process with a complete manifest and rollback. Host composability caps evolution. Effects must be invertible and dependencies must be declared. Persist plugins only through a reviewed change, not a hot write.

Check. The production retriever and model mount return no candidate ids. The last manifest has every required field and a rollback hash. A single failed check equals reject.

source-ids: isolate-candidates-from-production-traffic, treat-self-mod-as-release-process, scan-code-and-deps-before-promote, record-release-manifest-and-rollback, validate-new-tools-before-library, host-composability-caps-self-evolution, persist-plugins-only-via-pr, isolate-generator-from-release-gate

### `freeze-safety-mechanisms-from-self-mod`

When a business agent may change prompts, skills, knowledge, or tools.

Deny writes to validators, test cases, release thresholds, audit logs, keys, and stable backups. Put evolvable code in a low-privilege sandbox that can only emit patches and tests. Treat pages, tool output, and their summaries as untrusted evidence. Summarization is not sanitization. Extract claims into a fixed schema and never execute extracted strings. Model-produced confidence is not an approval gate.

Check. A candidate that edits a validator, threshold, audit sink, or backup is rejected by permission before tests run. A 1.0 confidence field with a failed allowlist check is rejected. The reviewer identity differs from the generator. Raw tool output cannot be saved as a skill body.

source-ids: freeze-safety-mechanisms-from-self-mod, sandbox-patches-from-trusted-root, treat-untrusted-text-as-evidence-only, summarization-is-not-sanitization, extract-schema-never-execute-strings, model-confidence-is-not-approval, bind-one-time-token-to-risky-op

### `no-unverified-online-parameter-updates`

When satisfaction, a click, or raw text is available as a live signal, or when a high-dimensional skill cannot be written as rules.

Block direct parameter writes from unverified online feedback. Collect signals as evidence. Train only offline against a redacted, filtered set with a held-out regression and post-job safety scores. Retrain adapters from a pinned original base the modifier cannot reach. Keep long-stable authorization and money rules in server code even after a successful train.

Check. The serving path has no hook that fine-tunes production weights from a single live reward. The training config references a pinned base hash that is read-only to the evolution agent. A jailbreak-style forbidden transfer is still refused by the server.

source-ids: no-unverified-online-parameter-updates, convert-clean-trajectories-to-training, retrain-adapters-from-untouchable-base, parameterize-inexpressible-capabilities, keep-stable-rules-in-server-code

### `prefer-local-attributable-reversible-updates`

When a failed trajectory suggests a missing rule or exception.

Change the innermost content first. Escalate from a local rule, to structured context, to workflow, to harness code, to the optimizer that proposes candidates, only with a written reason. Keep system prompt, skill, and harness in different scopes. Ship instruction changes as minimal diffs with provenance. Stop full rewrites that collapse rare constraints.

Check. The last five evolution tickets show an attempted local artifact edit unless a recorded reason skipped that rung. The latest prompt change is a small diff with source trajectory ids and a stored parent. A method-level change cites failed local attempts and a rollback pointer.

source-ids: prefer-local-attributable-reversible-updates, default-to-local-artifact-edits, keep-prompt-skill-harness-apart, minimal-diff-with-provenance, stop-full-rewrite-context-collapse, production-prompt-updates-stay-auditable, incremental-context-entries-with-ids

### `separate-online-execution-from-offline-evolution`

When wiring production traffic to learning.

Let the online loop finish tasks and append evidence only. Let the offline loop aggregate, diagnose, propose, validate, and release. The loops meet through versioned stores and evaluation sets, not through a mid-request write. Build record, verify, extract, route, candidate, and gate around the model. Do not wait for reliable autonomous continual learning inside the weights.

Check. A live request does not mutate knowledge, prompts, skills, programs, or weights. Those writes belong to an offline job with a version id. The architecture shows online record, offline evolve, four media, and a frozen gate as distinct parts.

source-ids: separate-online-execution-from-offline-evolution, wrap-learning-as-autonomous-system, collect-online-consolidate-offline, build-verifiable-learning-system-around-model, preserve-evidence-then-organize-offline

### `layer-evolution-evaluation-metrics`

When judging whether continual evolution is working.

Answer four questions with named evidence. Did the updater propose a useful change. Did the task agent load it in the right situation. Did it follow the new rule after load. Did held-out tasks improve without collapse. A local repair that drops retention or transfer is a failed candidate. Score updater ability and task-agent benefit separately. Stream learn, transfer, rule-change, and retention. Compare static, append-only, and evolving controls. Compute outcomes in an external harness. The model does not grade itself.

Check. The latest evolution dashboard has validity, activation, adherence, and retention-set gain with evidence pointers. A candidate with only in-sample repair numbers is rejected. Official metrics are produced by harness code.

source-ids: layer-evolution-evaluation-metrics, separate-harness-update-from-harness-benefit, local-fix-without-retention-is-failure, evaluate-learn-transfer-retire-retain, distinguish-static-append-evolving, score-with-external-harness-only, watch-five-long-term-outcomes, test-boundary-and-retention-sets

### `done-does-not-mean-progress`

When the task is open research, strategy, or product design with delayed or non-unique feedback.

Add evidence and supervision structure. A flawless harness run can still emit lookalike results that do not advance the real objective. Watch implementation drift, over-optimism, and missing tacit judgment. Follow a discovery loop (hypothesis, experiment, external evaluation, feedback). Ban self-awarded success. People own problem definition and stop decisions on open-ended families. Retain negative results. Keep claims on an evidence graph.

Check. If the only green bit is pipeline completion, the record is marked process-complete, not objective-complete. Every evolution experiment has a hypothesis field and an evaluator id that is not the proposing agent. Every open-ended family names a human owner for problem and rubric and disables auto-release on process-complete.

source-ids: done-does-not-mean-progress, watch-research-drift-optimism-tacit-gaps, follow-scientific-discovery-loop, humans-own-open-ended-eval-design, move-humans-to-problem-and-stop-decisions, retain-negative-results-as-first-class, separate-claims-from-evidence-graph, self-update-is-not-task-gain

### `run-five-step-sleep-cycle`

When starting a sleep-learning or idle-maintenance job.

Trigger on time, new-trajectory count, storage, or error rate only when the online path is free. Orient on current versions and immutable bounds. Consolidate with local patches. Approve on transfer, retention, and safety sets, with humans on high-risk writes. Then prune and reindex while keeping provenance and rollback. Snapshot before prune. Merge duplicates. Move local rules out of the global prompt. Retrain adapters from the pinned base. Retrieve original messages, not model summaries of them. Open a background skill review from operational signals, not from every chat.

Check. The last sleep-job log shows all five stages in order, and high-risk writes show an approval field. After a curator run, a snapshot or rollback pointer exists. A quiet session does not enqueue a skill review. A correction-heavy session may.

source-ids: run-five-step-sleep-cycle, collect-online-consolidate-offline, snapshot-then-prune-with-rollback, consolidate-without-unbounded-growth, trigger-background-skill-from-operational-signals, retrieve-original-messages-not-summaries, retrain-adapters-from-untouchable-base

## Failure diagnostics

Repeats yesterday's miss in a clean session. Start at `preserve-is-not-learn`, then `separate-online-execution-from-offline-evolution`.

Satisfaction rose while policy breaks rose. Start at `three-layer-trajectory-verification`.

Every failure became another prompt sentence. Start at `route-update-by-representation`.

The router wrote serving files. Start at `routing-is-only-a-proposal`.

A profile note was used as an operating procedure. Start at `distinguish-user-memory-from-action-experience`.

One green run rewrote the official guide. Start at `five-step-knowledge-distillation`.

The induced rule copies the bench's failure terminal, or a skill claims confirmation the harness never saw. Start at `observed-behavior-is-not-ought`.

A first-success click path was indexed, or replay skipped reset. Start at `write-falsifiable-change-contract`.

A draft skill or LoRA is retrievable on live traffic. Start at `isolate-candidates-from-production-traffic`.

The agent edited a validator, threshold, or audit sink. Start at `freeze-safety-mechanisms-from-self-mod`.

A live reward writes production weights. Start at `no-unverified-online-parameter-updates`.

The first response was rewriting the optimizer. Start at `prefer-local-attributable-reversible-updates`.

A mid-request reflection patched the system prompt. Start at `separate-online-execution-from-offline-evolution`.

The report has only an end-to-end score. Start at `layer-evolution-evaluation-metrics`.

Pipeline completion was counted as science or strategy progress. Start at `done-does-not-mean-progress`.

The store only grows and conflicts cancel retrieval. Start at `run-five-step-sleep-cycle`.

## Namespaced drills

#### `09-continual-evolution-q1`

A formal experience record has three supporting runs and one new failure on a newer API. Slice by version and conditions. If wins are old-version-only, narrow applicability and mint a new-version candidate. If the same slice now fails, lower confidence or revoke. Do not globally delete from a raw win/loss count.

#### `09-continual-evolution-q2`

Satisfaction rises while rule violations rise. Keep satisfaction as a quality metric among compliant runs. Give rule breaks, privacy leaks, unsupported claims, promise-action mismatches, and unauthorized ops hard thresholds that an average cannot cancel. Violating runs stay out of the positive learning set.

#### `09-continual-evolution-q3`

The same false-promise bug can be a prompt rule, a harness check, or a train job. Start from cause and testability. If promise text is comparable to tool state, put a deterministic check in the harness and keep it as last defense on high-risk paths. Prefer the smallest change that is easy to validate and roll back. Compare a failure set and a retained old-task set.

#### `09-continual-evolution-q4`

The agent may generate tool and validator patches. It must not edit the trusted root that approves those patches. Evolvable code lives in a low-privilege sandbox. Permissions, keys, release-controller config, and update validators have no sandbox read or write. Reject any patch that touches those paths.

#### `09-continual-evolution-q5`

As an experience store grows, retrieval errors and conflicts can cancel learning. Each record keeps sources, applicability, environment version, validation time, and confidence. Conflicts branch by condition. A sleep pass merges duplicates and expires contradicted or unused entries while keeping provenance. Silent overwrite is forbidden.

#### `09-continual-evolution-q6`

Parameter learning can improve medical language style and cannot guarantee clinical rules. Put current guidelines in a cited knowledge base, intake and escalation in a skill, identity, privacy, contraindication, and permission bounds in server code. Refuse a design that stores contraindications or identity rules only in weights. Weight or workflow release needs a retained medical-safety set and human review.

## Depends-on

- `playbooks/memory-knowledge.md` for the user-keyed archive and the shared knowledge plane. This chapter owns gated action experience, not tenant facts.
- `playbooks/evaluating-agents.md` for `evaluate-model-plus-harness`. `evaluate-before-summarize` is the local pointer, not a second eval law.
- `playbooks/post-training.md` when the routed medium is parameters. Local artifact edits still come first.
- `playbooks/tools.md` for form versus disclosure and for non-bypassable execution gates.

Needed-by. `lessons/11-afterword.md` points here for post-deploy write-back. `SKILL.md` After a model drop spends leftover leverage on carriers a new model cannot eat.

## Open tensions

Harness versus weights. Exhaust context, tools, and code before a train job (`prefer-local-attributable-reversible-updates`, `route-update-by-representation`). Local first still applies after training is on the table.

User memory versus action experience. `distinguish-user-memory-from-action-experience` splits the stores. Chapter 3 owns tenant facts. This chapter owns gated strategy.

Skills versus harness veto. `skill-asks-harness-vetoes` keeps interview and spec in the skill and the stop in code. After a model drop, retirement of a harness layer is a later eval, not an evolution write.

Self-review versus independent verify. A generator may draft. `routing-is-only-a-proposal` and `model-confidence-is-not-approval` own the gate. The producer never marks done.

Append-only evidence versus rewritten archives. Raw trajectories stay immutable (`preserve-is-not-learn`). Formal experience is rewritten only offline (`five-step-knowledge-distillation`, `run-five-step-sleep-cycle`).
