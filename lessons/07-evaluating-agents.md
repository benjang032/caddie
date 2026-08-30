# Evaluating Agents

Terms. **Pass@k** is possibility (any of k independent runs). **Best@k** is the best continuous score among k runs. **Pass^k** is operations (every one of k consecutive runs, including vetoes). **Harness** is the non-weight stack scored with the model. **First-error record** points at the earliest unacceptable step. **Mechanism** is the knob. **Target** is the outcome the product cares about.

## What this is for

Measure the model-plus-harness pair so a score becomes an attribution, a regression, and a gated change. A raw fraction without a business bar, a k protocol, and an instrument check is not a decision. This chapter owns eval environments, judges, first-error records, cost matrices, and the handoff into training.

## Core model

Five-component env plus first-error record. Dataset, resettable state, atomic tools, rubric, and protocol make a run comparable. The first-error record makes a miss teachable. Lookup `references/data-shapes.md` for `playbooks/evaluating-agents.md`.

## Clusters

### `evaluate-model-plus-harness`

When a run looks weak and the first impulse is a model swap.
Rule. Score the model and the harness as one unit. Hold the harness fixed to swap models. Disable one harness part to ablate. Change one variable per comparative run. A bare-model baseline is the master off switch.
Check. Every score row names model id and harness version. A swap table shares one harness hash. An ablation table has one off-row per major feature. Each experiment row lists exactly one changed field.
source-ids: evaluate-model-plus-harness, model-swap-locates-bottleneck, ablation-disables-one-component, change-one-variable-at-a-time, bare-model-baseline, one-change-per-round, isolate-model-vs-harness-policy, disable-each-major-feature, inject-ablation-at-boot, dose-response-variants

### `four-stage-eval-system`

When standing up a program or reading a headline claim.
Rule. Define success, source tasks, choose a verifier, then turn the score into a decision. Weakness in any stage lowers trust. Finish the private set even when current models miss the bar. Start from one fully specified production-like task.
Check. The eval README has four stage sections. A private eval manifest exists. One checked-in task file holds ticket, user spec, init, criteria, and a saved trajectory.
source-ids: four-stage-eval-system, four-stages-trust, ship-eval-set-ahead-of-model, dissect-one-real-task, scientific-eval-loop, declare-reward-basis-per-task

### `pass-at-k-ceiling`

When choosing a headline metric.
Rule. Pass@k and Best@k measure possibility. Pass^k with vetoes measures operations that cannot slip. Declare k and whether samples are independent or consecutive. Do not retry-until-pass on side-effecting work. At moderate p the two families diverge by an order of magnitude. Map the fraction onto a named business bar.
Check. The metrics section states name, k, protocol, and domain bar. A k>1 row shows both computed values or an omit reason. Side-effecting tasks mark sandbox or rollback and count failed attempts.
source-ids: pass-at-k-ceiling, pass-hat-k-reliability, best-at-k-for-scores, declare-k-and-protocol, no-retry-until-pass-with-side-effects, score-needs-business-bar, metrics-diverge-with-p-and-k, wonder-phase-uses-pass-at-k, metric-by-scenario

### `five-component-dataset`

When standing up a repeatable env. Collapse the five `five-component-*` lessons here.
Rule. Require dataset, resettable state, atomic tools, rubric, and protocol. Skip any one and do not call the setup an eval. Given the same init, the same agent must produce comparable results.
Checks.
1. Dataset. Each case record holds ticket, user spec or omitted-simulator mark, init, and criteria under a stable id.
2. State. Two consecutive resets produce equal snapshots. A mid-run illegal transition is rejected.
3. Tools. No tool schema name equals a full task goal. Agent tools and user tools stay atomic.
4. Rubric. evaluation_criteria and reward_basis (or named equivalents) exist on every task. Unused layers stay in the log.
5. Protocol. The protocol doc names stop signal, turn cap, and patience failure.
source-ids: five-component-dataset, five-component-state, five-component-atomic-tools, five-component-rubric, five-component-protocol, missing-component-breaks-loop, env-must-reset-and-compare

### `verifiers-env-type-table`

When choosing an environment class.
Rule. Map the task onto SingleTurnEnv, ToolEnv, StatefulToolEnv, or SandboxEnv using state persistence, tool use, and isolation. HCI keeps a spec-driven simulator. Tool-only work drops it. Score state changes in tool envs and communication strategy in HCI envs.
Check. Each task lists an env class that matches the three columns. HCI records include user_scenario. Tool-only tasks have no user_scenario and a programmatic verifier.
source-ids: verifiers-env-type-table, hci-needs-simulator, tool-env-drops-simulator, verify-action-vs-verify-guidance, dual-control-user-tools, partition-state-by-controller, simulator-spec-not-script, ground-simulator-on-tools, encode-user-knowledge-boundary

### `benchmark-design-choice-table`

When selecting or cloning a public agent bench.
Rule. Compare capability tested, task source, who plays the environment, and the verifier. Copy those design choices. Do not import a headline score into a product decision. Public benches screen. The business set decides. Attributed production traces become the majority.
Check. The design doc has a filled four-column comparison and no product gate tied to a foreign headline. The decision memo cites the business-set id. Each thumbs-down has a linked regression id or an explicit wont-fix.
source-ids: benchmark-design-choice-table, public-benches-for-screening, business-set-for-decisions, production-feedback-for-regression, production-becomes-majority, dataset-is-the-script, ship-eval-set-ahead-of-model

### `parameterized-templates`

When a static script can be memorized or leaked.
Rule. Store templates with slots and instantiate per run. Embed a canary GUID. Stratify difficulty so the set does not saturate. Add trap tasks that pressure policy. Hand-run cases to find ambiguity and cheat paths. Screen for signal before the official set.
Check. Two consecutive official runs of the same template id produce different slot values. Each released task file contains a canary and a scanner job exists. Reports split by difficulty band. The suite contains tagged trap tasks.
source-ids: parameterized-templates, canary-guid, stratify-difficulty, add-policy-trap-tasks, levels-are-diagnostic, hand-execute-to-find-ambiguity, screen-tasks-for-snr, dynamic-instance-generation, split-known-info-from-instructions, precise-acceptance-criteria

### `deterministic-when-possible`

When a new dimension is about to be scored by a judge by default.
Rule. Keep every mechanically decidable check as an assertion. Score facts an independent machine can check. Ignore self-congratulation. Move right on the verifiability spectrum only as far as the dimension requires. On patches, require FAIL_TO_PASS and PASS_TO_PASS. Prefer an unforgeable execution token.
Check. CI runs programmatic assertions with no LLM call on those dimensions. The scorer never reads the agent's task-complete sentence as success. A dimension table marks each item as assertion, rubric, or both.
source-ids: deterministic-when-possible, verify-facts-not-self-report, reserve-llm-judge-for-uncheckable, verifiability-spectrum, outcome-score-is-not-diagnosis, fail-to-pass-plus-pass-to-pass, unforgeable-execution-checks, deep-state-inspection, binary-reward-hides-process

### `judge-against-expert-rubric`

When residual dimensions have no unique gold string.
Rule. Judge against expert dimensions with levels, examples, edges, weights, and vetoes. Use heterogeneous families on one rubric. Treat a same-family judge as Goodhart risk. Penalize verbosity and audit score-versus-length.
Check. Judge outputs are structured per dimension. A veto-fail fixture with perfect other scores totals zero. Training configs that use a judge list a different-family auditor or a human gold set. An audit plot of score versus length exists.
source-ids: judge-against-expert-rubric, heterogeneous-multi-judge, goodhart-same-family-judge, rubric-weights-and-veto, length-bias-defenses, rubric-expert-guidance, rubric-coverage-and-pitfalls, rubric-self-contained-items, iterate-rubric-into-casebook, hallucination-veto-fires

### `attribute-first-error`

When a failed trajectory has many later mistakes. Scoped-span comment lessons live here, not as their own headings.
Rule. Record the first unacceptable step. Choose the earliest class that explains followers. Write a structured record. Pre-filter with rules before a localizer model. Parse mixed documents into scoped spans. Treat fenced code as a protected span. Treat quotes inside comments as their own span. On silent fails, walk claims against tool returns or bisect the prefix. On old_string misses, hash the copy pipeline and mark the first divergence.
Check. Each failed trace has first_error_step and a schema-valid file. The pipeline has a rules stage. A fence-only quote fixture stays byte-stable under a prose quote job. A comment-plus-literal fixture keeps comment quotes and code quotes under different permissions.
source-ids: attribute-first-error, earliest-explains-followers, structured-attribution-record, rules-then-llm, three-bad-case-signals, taxonomy-becomes-skill, coding-failure-taxonomy, scoped-span-permissions, clarify-when-scope-unknown, code-block-is-protected-span, comment-quotes-are-own-span, copy-pipeline-first-divergence, encoding-probes-for-copy, harness-if-direct-copy-works, silent-failure-attribution, unused-context-evidence, evidence-for-discovery-loop

### `e2e-regression`

When attribution is done and no test was written.
Rule. Keep end-to-end tasks for whole-task capability. Freeze a prefix just before the first error to test one decision. Score an acceptable-action set, not one gold call. Map each failure class to a constructor.
Check. Each domain has at least one e2e in CI. Prefix fixtures freeze state at a named step. Each prefix task JSON has allowed and forbidden arrays. Each taxonomy class has at least one generated example.
source-ids: e2e-regression, prefix-regression, acceptable-action-set, class-to-regression-mapping

### `obtain-vs-apply`

When an e2e pass only proves a fact eventually appeared.
Rule. Test fetching a fact and using it on the current decision as two skills. E2e guards that basic tasks still work. Prefix boundary tasks check scope, instruction override, clarification, and confirm-before-danger.
Check. The memory or policy suite includes prefix apply tasks as well as e2e obtain tasks.
source-ids: obtain-vs-apply

### `span-tree-per-task`

When a fail exists and only a chat transcript is on file.
Rule. Record one trace per task as a span tree. Emit a general protocol plus LLM semantic fields. Promote anonymized traces into eval cases so the set tracks the live distribution.
Check. A sample production trace shows a main-loop parent with LLM and tool children. Traces import into a second backend without a custom parser rewrite. New cases cite a source trace id.
source-ids: span-tree-per-task, standard-trace-protocols, traces-become-eval-assets

### `paired-test-same-tasks`

When two configs were scored on unmatched samples.
Rule. Run both arms on the same tasks and seeds. Publish standard error. Run 3-5 seeds on official claims. Enlarge n when the hoped-for lift sits inside noise. Correct for multiple comparisons. Act only on a gap that beats noise, survives the pair, and reproduces.
Check. The comparison uses a paired test. Official rows show seed count ≥3 or a screen-only label. The ship checklist has noise, paired, and reproduce boxes ticked.
source-ids: paired-test-same-tasks, compute-standard-error, multi-seed-spread, grow-n-for-small-effects, correct-multiple-comparisons, ship-only-reproducible-gaps

### `check-eval-harness-first`

When a headline number fell and agent code opened first.
Rule. Inspect resource kills, verifier bugs, and task drift before editing the agent. Cluster misses by capability tag. Assign observation, reasoning, action, or verification before changing anything. Test the cheapest hypothesis first. Fix observation before piling on instructions. Compact noisy feeds after visibility works.
Check. The incident note has an eval-health section completed before an agent commit. The report has a cluster table. Each experiment card names a layer and one variable.
source-ids: check-eval-harness-first, iterate-harness-from-eval, cluster-failures, diagnose-layer-before-changing, cheapest-hypothesis-first, observation-before-prompt, compact-after-visibility

### `four-arm-cost-matrix`

When testing stable prefixes and history compression.
Rule. Run no-cache/no-compress, prefix-only, compress-only, and both on the same workflow. Split spend into inference, tools, and infra. Model uncached multi-turn cost as triangular growth. Never add isolated savings. Give each lever its own switch. Include retries and hidden thinking tokens.
Check. A local 2×2 table exists for the production workflow. The combined cell is measured. The cost report has three top-level buckets. A lint fails if combined is written as a sum.
source-ids: four-arm-cost-matrix, do-not-sum-isolated-savings, three-level-cost, context-accumulation, thinking-token-cost, tool-output-token-tax, switch-per-cost-lever, cost-with-retries, per-task-cost-cap, batch-non-realtime

### `slice-is-not-system-score`

When four tasks went 4/4 after a change.
Rule. Let a small slice authorize only the next larger test. Advance to the reference environment, full set, and multi-seed run. Write where the conclusion applies, which guardrails failed, and what must be tested next.
Check. The writeup says slice and names the next sample size. A promotion checklist blocks deploy until the full-matrix job is green. Every saved report has scope, guardrails, and next-test sections.
source-ids: slice-is-not-system-score, slice-gates-full-rerun, report-scope-and-next-test

### `mechanism-vs-target`

When the experiment shortens a plan file and treats plan length as success.
Rule. Gate A/B tests on the goal metric, not on the knob being turned. Set non-negotiable guardrails. Treat flags as architecture. Render prompts deterministically and regress them like code.
Check. The experiment card has separate mechanism and target fields and the ship rule uses the target. The A/B platform has configured guardrail stops. A prompt-only PR runs the eval suite.
source-ids: mechanism-vs-target, guardrail-metrics, flags-are-first-class, prompt-ci-regression, baseline-statistics, compile-time-strip, runtime-stale-ok, one-exposure-per-session, render-prompt-at-commit, five-internal-eval-parts

### `typed-safe-analytics`

When an event might include a file path, prompt, or user code.
Rule. Collect only values the compiler can prove are safe to measure. Force analytics APIs to take wrapped types. Design privacy before collection. If analytics cannot collect safely, evaluation cannot run on that data.
Check. A raw-string call to analytics fails typecheck. The analytics schema has no raw path, prompt, or secret fields.
source-ids: typed-safe-analytics, privacy-in-from-start

### `sim-for-post-training`

When the goal moves from scoring today's agent to teaching a new capability.
Rule. Reuse task schemas and validators. Turn the scoring script into the reward script. Reset every episode. Design for training-scale parallelism. Randomize digital faults and embodied scenes so configs cannot be memorized.
Check. The training config points at the same check functions the eval uses. A unit test fails if episode n+1 sees episode n mutations. Training docs state episode rate, reset, and randomization.
source-ids: sim-for-post-training, validator-as-reward, deterministic-reset, training-throughput, digital-sandbox-replay, embodied-randomization, fidelity-cost-tradeoff, domain-randomization

## Failure diagnostics

| Symptom | Open | First check |
| --- | --- | --- |
| Impulse to swap the model | `evaluate-model-plus-harness` | Score row names model id and harness version. |
| Headline is a raw fraction | `pass-at-k-ceiling` | Metric name, k, protocol, and business bar are present. |
| Suite cannot reset or compare | `five-component-dataset` | Five-component table is filled. Two resets match. |
| Public bench used as a ship gate | `benchmark-design-choice-table` | Decision memo cites the business-set id. |
| Judge scores a file hash | `deterministic-when-possible` | That dimension is an assertion in CI. |
| Ticket lists every later miss | `attribute-first-error` | first_error_step is set. Later misses are consequences. |
| Score fell, agent diff opened first | `check-eval-harness-first` | Eval-health section is complete. |
| Isolated savings added to 45% | `four-arm-cost-matrix` | Combined cell is measured. |
| 4/4 cited as system success | `slice-is-not-system-score` | Writeup says slice and names the next n. |
| Shorter plan, higher spend | `mechanism-vs-target` | Ship rule uses the target metric. |
| Analytics logs a path | `typed-safe-analytics` | Raw-string call fails typecheck. |

## Namespaced drills

Collapsed from `eval-design-thought-drills`.

### 07-evaluating-agents-q1

A language model scores another language model's output. Name systematic holes, how to detect them, and how to correct them. Length bias, style preference, and same-family gaming are the usual holes. Detect with a human gold set plus agreement, a score-versus-length audit, and padded red-team answers. Correct with a verbosity penalty, a length cap, and heterogeneous families.

### 07-evaluating-agents-q2

Public static question banks leak into training. Design an evaluation that resists leakage at the root. Publish the generation mechanism. Keep concrete instances private. Instantiate parameterized templates each run. Verify final environment state, not a memorized action list.

### 07-evaluating-agents-q3

Helpfulness and tone stay subjective. Translate the abstract word into an observable behavior. Give each grade examples and edges. Grow the rubric from rater disagreements. Aggregate multi-judge scores and calibrate on a gold set.

### 07-evaluating-agents-q4

The simulated user is itself a model. Validate by hand-spotting dialogues for progressive disclosure and no invented facts, plus a small real-user study that checks whether rankings match.

### 07-evaluating-agents-q5

Bradley-Terry assumes transitive preference. Multi-dimension tradeoffs plus judges who weight dimensions differently produce cycles. Rank per capability and publish the pairwise win-rate matrix. Do not collapse a multi-objective agent into one Elo.

### 07-evaluating-agents-q6

Single-run success is 60%. Pick the metric from rollback reality. Retryable drafts use Pass@k with k equal to the real retry budget. Irreversible pay, mail, or deploy uses Pass^k. At p=0.6 those families describe different products.

### 07-evaluating-agents-q7

The behavior space is huge. Cluster failures. Pilot on diagnostic tasks. Use cheap one-variable paired tests. Treat a small pilot as a gate to a larger run. Grow n when the lift sits inside noise. Correct for many silent peeks.

### 07-evaluating-agents-q8

A full UI tree raised success and tokens. Compaction held success at a fraction of the tokens. Write a retain-with-evidence pruner. Keep visible, textual, actionable, state-bearing, and accessibility-labeled nodes. Diff ids and states before and after prune. Block release on accessibility or success regressions.

### 07-evaluating-agents-q9

If the simulator's reveal strategy differs from real users, absolute scores lose reference value. Relative ranks can still be useful. Calibrate on real dialogues, spot-check by hand, and publish the simulator-policy limit with every HCI score.

## Depends-on

- `playbooks/getting-started.md` for the model-plus-harness formula and harness duties.
- `playbooks/coding-agent.md` for `tests-pass-as-completion` as the coding completion gate.
- `playbooks/context-engineering.md` for stable prefixes and compression, which the cost matrix measures.
- `playbooks/tools.md` for atomic schemas and argument fidelity, which prefix regressions reuse.

Needed-by. `playbooks/post-training.md` consumes `sim-for-post-training` and `validator-as-reward`. `playbooks/continual-evolution.md` and the afterword route `evaluate-before-summarize` and `eval-decides-progress` here. Introduction `eval-or-no-progress` is a pointer at `evaluate-model-plus-harness`.

## Open tensions

- `pass-at-k-ceiling` versus `pass-hat-k-reliability`. Possibility is not an ops bar. Chapter 8 may use Pass@k as a support test.
- `mechanism-vs-target`. A moved knob is not a moved goal.
- `check-eval-harness-first` versus `iterate-harness-from-eval`. Instrument health first. Then close a harness loop from attributed data.
- `four-arm-cost-matrix` versus chapter 2 isolation. Combined savings are measured. Isolation remains the default when a subtask can return a bounded artifact.
