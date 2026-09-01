# evaluation-driven-agent-improvement

## Use when

- which model should we use
- did this harness change actually help
- set up agent evals or a benchmark
- pass@k versus reliability
- LLM as a judge rubric
- failure attribution on a trace
- A/B or ablation for an agent feature
- feature flags for prompts
- agent cost and KV cache
- simulation for post-training
- observability traces to regressions

Make a working checklist from these steps before reasoning. Use the host's task or todo list when available.

## Steps

### 0. Name the data shape

Look up [data shapes](../references/data-shapes.md) for `playbooks/evaluating-agents.md`. The unit is a five-component env plus a first-error record. Dataset, resettable state, atomic tools, rubric, and protocol sit on the env. The first-error record sits on every failed trajectory. Refuse to write scoring logic until both are named.

### 1. Define success

Name one metric, one business bar, and a k protocol. Exploration and demos use Pass@k or Best@k. Side-effecting work uses Pass^k and counts vetoes as fails. State whether k is independent samples of one task or k consecutive jobs. Map the raw fraction onto the cost of a miss before calling the system usable.

Check. The report prints metric name, k, sampling protocol, sandbox or rollback flag, and a named domain bar. A k>1 row shows both ceiling and reliability or an explicit omit reason.

If the check fails, open `lessons/07-evaluating-agents.md` cluster `pass-at-k-ceiling` (source-ids pass-at-k-ceiling, pass-hat-k-reliability, best-at-k-for-scores, declare-k-and-protocol, no-retry-until-pass-with-side-effects, score-needs-business-bar, metrics-diverge-with-p-and-k).

### 2. Stand up the five components

Reset state before every trial. Store ticket, init, criteria, and simulator spec (or an omitted-simulator mark) in one record. Keep tools atomic. Write check layers plus an aggregator. Write stop signal, turn cap, and patience failure.

Check. Two consecutive resets produce equal snapshots. No tool name equals a full task goal. Every task has evaluation_criteria and reward_basis. The env README has a filled five-component table.

If the check fails, open `lessons/07-evaluating-agents.md` cluster `five-component-dataset` (source-ids five-component-dataset, five-component-state, five-component-atomic-tools, five-component-rubric, five-component-protocol, missing-component-breaks-loop, env-must-reset-and-compare).

Pick env class from `verifiers-env-type-table`. HCI keeps a spec-driven simulator. Tool-only work drops the simulator.

### 3. Fill the dataset

Draw from a public technique bench, a domain business set, and attributed production traces. Clone design choices (capability, source, environment actor, verifier). Do not import a foreign headline score as a ship gate. Public benches screen. The business set decides. Production misses become the majority over time.

Check. The design doc has a four-column comparison. The decision memo cites the business-set id. Each incident has a linked regression id or an explicit wont-fix.

If the check fails, open `lessons/07-evaluating-agents.md` cluster `benchmark-design-choice-table` (source-ids benchmark-design-choice-table, public-benches-for-screening, business-set-for-decisions, production-feedback-for-regression, production-becomes-majority, dataset-is-the-script).

Add parameterized templates, canaries, difficulty bands, and policy traps before treating the set as official.

### 4. Score with assertions first

Keep every machine-checkable fact as an assertion in CI. Add a rubric and heterogeneous judges only on dimensions with no unique state or keyword test. Ignore the agent's done sentence. Require FAIL_TO_PASS and PASS_TO_PASS on patches. Prefer an unforgeable environment artifact.

Check. No CI dimension that has a code oracle is scored only by an LLM. A veto-fail fixture totals zero. Training that uses a judge lists a different-family auditor or a human gold set.

If the check fails, open `lessons/07-evaluating-agents.md` clusters `deterministic-when-possible` and `judge-against-expert-rubric` (source-ids deterministic-when-possible, verify-facts-not-self-report, reserve-llm-judge-for-uncheckable, verifiability-spectrum, fail-to-pass-plus-pass-to-pass, unforgeable-execution-checks, judge-against-expert-rubric, heterogeneous-multi-judge, goodhart-same-family-judge, rubric-weights-and-veto).

### 5. Reconstruct the decision-time information flow

Before assigning blame, name every model, agent, runtime, and handoff in the failed path. For each boundary, record the actor or component, expected input, actual decision-time input, output produced, output delivered, boundary transformation, and supporting artifact. A runtime possessing a result does not mean the next model saw it, and a model seeing a result does not mean the terminal handoff carried it to the parent.

Check. Every claim that a component knew, saw, or was blind to something points to its captured prompt, tool result, or handoff. The table names the first boundary that dropped, summarized, rewrote, or misclassified information, and labels later effects as consequences. If those artifacts are absent, stop attribution and repair observability first.

### 6. Attribute the first error

Walk each fail from the start. Record the earliest unacceptable step that explains later misses. Store a structured record (step, class, evidence, primary versus consequence, recoverability, confidence). Run cheap rules before a localizer model. For mixed documents, parse scoped spans before blaming a quote or an old_string miss.

Check. Every failed trace has `first_error_step` and a schema-valid record. A fence-only quote fixture stays byte-stable under a prose quote job.

If the check fails, open `lessons/07-evaluating-agents.md` cluster `attribute-first-error` (source-ids attribute-first-error, earliest-explains-followers, structured-attribution-record, rules-then-llm, code-block-is-protected-span, comment-quotes-are-own-span, scoped-span-permissions, silent-failure-attribution, copy-pipeline-first-divergence).

### 7. Mint regressions

From those records, add end-to-end tasks for whole-task capability and prefix tasks that freeze state just before the first error. Score an acceptable-action set, not one gold call. Split obtain (did the fact appear) from apply (was the fact used on the next decision).

Check. Each domain has at least one e2e in CI. Each prefix task has allowed and forbidden arrays. The memory or policy suite includes prefix apply tasks.

If the check fails, open `lessons/07-evaluating-agents.md` clusters `e2e-regression` and `obtain-vs-apply` (source-ids e2e-regression, prefix-regression, acceptable-action-set, class-to-regression-mapping, obtain-vs-apply).

### 8. Compare configs

Run both arms on the same tasks and seeds. Use a paired test. Publish 3-5 seed spread on official claims. Compute standard error before celebrating a few-point gap. Correct for multiple comparisons when screening many ideas. Ship only a gap that beats noise, survives the pair, and reproduces.

Check. The comparison notebook is paired. Official rows show seed count ≥3 or a screen-only label. The ship checklist has noise, paired, and reproduce boxes ticked.

If the check fails, open `lessons/07-evaluating-agents.md` cluster `paired-test-same-tasks` (source-ids paired-test-same-tasks, compute-standard-error, multi-seed-spread, grow-n-for-small-effects, correct-multiple-comparisons, ship-only-reproducible-gaps).

### 9. Debug the instrument first

If scores drop, inspect resource kills, verifier diffs, and task drift before editing the agent. Then cluster misses by capability tag. Record one span tree per task so the next incident is not a chat paste.

Check. The incident note has an eval-health section completed before an agent commit. A sample trace shows a main-loop parent with model and tool children.

If the check fails, open `lessons/07-evaluating-agents.md` clusters `check-eval-harness-first` and `span-tree-per-task` (source-ids check-eval-harness-first, cluster-failures, four-stages-trust, four-stage-eval-system, span-tree-per-task, traces-become-eval-assets).

### 10. One variable, then a larger gate

Test the cheapest one-variable hypothesis. Hold model, tasks, seed, step limit, and env fixed. A slice may authorize only the next larger test. For cache and compression, run the four-arm matrix on the local workflow. Never add isolated savings.

Check. Each experiment row lists exactly one changed field. The writeup says slice and names the next sample size. Combined cost is a measured cell, not a sum.

If the check fails, open `lessons/07-evaluating-agents.md` clusters `evaluate-model-plus-harness`, `slice-is-not-system-score`, and `four-arm-cost-matrix` (source-ids evaluate-model-plus-harness, model-swap-locates-bottleneck, ablation-disables-one-component, change-one-variable-at-a-time, slice-is-not-system-score, slice-gates-full-rerun, four-arm-cost-matrix, do-not-sum-isolated-savings).

### 11. Keep product eval machinery

Keep ablation flags, A/B guardrails, two-layer feature flags, prompt CI, and typed analytics in the product. Gate the experiment on the target metric, not on the knob being turned. Abort if guardrails regress.

Skip when the work is a one-off offline bench with no product traffic. Reason. Flags and prompt CI have no boot path to inject.

Check. The experiment card has separate mechanism and target fields and the ship rule uses the target. A raw-string analytics call fails typecheck. A prompt-only PR runs the eval suite.

If the check fails, open `lessons/07-evaluating-agents.md` clusters `mechanism-vs-target` and `typed-safe-analytics` (source-ids mechanism-vs-target, guardrail-metrics, flags-are-first-class, prompt-ci-regression, typed-safe-analytics, privacy-in-from-start).

### 12. Reuse the env for training

When a train job starts, reuse validators as rewards. Add deterministic reset, parallelism, and domain randomization. Raise interaction count so configs cannot be memorized.

Skip when no train job is on the table. Reason. Scoring today's pair does not require an RL episode loop.

Check. The training config points at the same check functions the eval uses. Episode n+1 cannot see episode n mutations.

If the check fails, open `lessons/07-evaluating-agents.md` cluster `sim-for-post-training` (source-ids sim-for-post-training, validator-as-reward, deterministic-reset, training-throughput, domain-randomization). Then open next.

## Open next

- [Post-training](post-training.md) after `sim-for-post-training` and `validator-as-reward` hold. Diagnose foundation, protocol, or policy there. Do not name a trainer from an eval score alone.

## Reply

State what changed in the env or the report, what metric and decision rule were chosen, and what remains open (instrument health, next gate, or a train handoff).
