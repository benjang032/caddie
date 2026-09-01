# 08-post-training

Terms. mid-training, SFT, RL, pass@k, LoRA, on-policy, importance ratio, RLVR, RLVP, hidden tests, on-policy distillation.

## What this is for

Change weights only after the miss is reproduced and tagged as foundation, protocol, or policy. Finish data, environment, and reward before naming an optimizer. SFT versus RL is a measured tendency under a matched shift, not a law.

## Core model

Foundation, then protocol, then policy. The object edited is a token distribution. Mid-training repairs the target mix. SFT writes protocol onto demonstrations. RL reallocates mass among self-generated traces when success already has nonzero probability and the scorer is honest.

## Clusters

### `diagnose-foundation-protocol-or-policy`

When every miss is filed as needs RL, or one fine-tune is asked to add facts, teach JSON, and discover a strategy.
Rule. Classify the gap as foundation, protocol, or policy before any trainer name. Require a measured gate to enter or skip a stage. Exhaust prompt, tool, program, and retrieval first.
Check. Each held-out incident has one diagnosis tag and one method, reviewed on the training ticket.
source-ids: diagnose-foundation-protocol-or-policy, four-stage-capability-map, four-part-cost-and-objective-map, require-a-measurable-gate-to-change-stage, foundation-protocol-policy-synthesis, split-knowledge-gaps-from-capability-gaps, use-pass-at-k-to-test-support, exhaust-context-tools-and-code-before-weights

### `data-and-environment-over-algorithms`

When the debate is PPO versus GRPO while the corpus, demonstrations, or verifier are unfinished.
Rule. Spend on the mid-training corpus, the demonstration protocol, and a resettable env-plus-reward loop before swapping recipes. Rank prior, then environment, then algorithm. Ship state transition and scoring together.
Check. The ticket names corpus, demo, and verifier owners. Algorithm is a one-line default unless a measured failure names it. A soak reset matches an initial hash.
source-ids: data-and-environment-over-algorithms, treat-algorithm-as-secondary-to-reward-and-env, rank-prior-then-environment-then-algorithm, require-resettable-parallel-reproducible-envs, env-includes-the-reward-function, env-engineering-order, budget-environment-fidelity-first, reject-distorted-practice-grounds, pretrained-priors-compress-search

### `sft-memorizes-rl-generalizes-as-tendency`

When a review cites a single OOD table as proof that SFT always memorizes and RL always transfers.
Rule. Treat the contrast as a result under matched task, model, and budget. SFT mass-covers labeled modes. RL mode-seeks high-reward modes. Opposite failures stay in scope. SFT that transfers, and RL that hacks a proxy.
Check. The write-up names the distribution shift and records both opposite risks.
source-ids: sft-memorizes-rl-generalizes-as-tendency, treat-generalpoints-ood-as-sft-overfit-warning, mass-covering-vs-mode-seeking, choose-rl-under-distribution-shift, output-is-a-probability-distribution

### `choose-by-optimization-objective`

When a method is chosen by fashion, or mid-training then SFT then RL is run as ceremony. Collapse the choose-by rows into one table.

| Dimension | Mid-train | SFT | RL |
| --- | --- | --- | --- |
| Objective | Raise document-token likelihood on the target mix | Raise labeled answer-token probability | Raise expected reward on self-generated traces |
| Signal | Dense next-token on documents | Token labels on a demonstration | Outcome or step scalars on rollouts |
| Data | Target corpus plus retention | Input-output pairs | Task, resettable env, reward |
| Enter | pass@k near zero, missing language or facts | Success exists, format or procedure wobbles | Success rare but real, scorer honest, group variance |
| Stop | Domain up, retention holds, first good traces | Parse stable, OOD plateau | Independent goal metric moves |

Rule. Match objective, signal, and data form. Use SFT under stable demos. Use RL under a real shift with an honest scorer. Use offline SFT, RFT, or DPO when no interactive env exists. Skip SFT only after measured parse and nonzero success. Leave SFT when format holds and more demos do not lift OOD.
Check. The training card's objective field matches the family, and a written predicate exists for every stage entered or skipped.
source-ids: choose-by-optimization-objective, choose-by-training-signal, choose-by-data-form, choose-sft-under-stable-demos, choose-rl-under-distribution-shift, choose-by-sample-efficiency, choose-by-training-stability, choose-midtrain-when-passk-is-near-zero, choose-sft-when-protocol-is-unstable, choose-rl-when-success-is-nonzero-and-reward-is-faithful, choose-offline-when-no-interactive-env, use-rl-when-verification-is-easier, form-first-then-switch-on-plateau, skip-sft-only-if-success-is-nonzero

### `midtrain-repairs-target-distribution`

When held-out pass@k stays near zero and failures cluster on unknown terms, language, or basic operations.
Rule. Continue next-token training on the target distribution plus a general retention slice. Loss over document tokens, not response-only. Mix long text, atomic long-context skills, and agent traces. Slice failures before adding crawl. Gate the claimed window as effective. Pilot the mix on a small model.
Check. Domain pass@k rises, the old-distribution set stays inside the drop budget, and product copy's window matches a passed capability-by-length row.
source-ids: midtrain-repairs-target-distribution, midtrain-dense-document-loss-vs-sft, prefer-midtrain-for-interconnected-knowledge, midtrain-then-small-sft-then-optional-rl, slice-failures-before-adding-midtrain-data, mix-long-text-cot-and-agent-trajectories, replay-general-and-lifted-old-tasks, stop-midtrain-on-multidimensional-gates, gate-effective-not-nominal-context, mix-retention-data-to-limit-forgetting, pilot-midtrain-mixture-before-scale, do-not-stuff-knowledge-into-sft, treat-context-window-as-effective-only-after-gates, next-token-prediction-builds-knowledge, pretrain-representation-caps-post-training

### `sft-writes-protocol-not-a-knowledge-base`

When a few thousand QA rows are proposed as the way to install a domain, or RL starts on free text.
Rule. Implement SFT as next-token loss on prompt-plus-completion with prompt tokens masked. Write format, style, and process. Keep large facts in mid-training or retrieval. Prefer a few thousand clean rows from experts, teachers, and verifier-filtered self-samples. Keep failures out of positive SFT. Stabilize parse before reward.
Check. The trainer unit test shows nonzero loss only on completion ids. Parse success meets the written SFT exit gate. No SFT set is the sole store of an updateable handbook.
source-ids: sft-writes-protocol-not-a-knowledge-base, sft-is-ntp-on-demonstrations, mask-prompt-tokens-in-sft-loss, prefer-clean-small-sft-sets, sft-solidifies-style-and-format-protocols, collect-sft-from-experts-teachers-or-rft, stabilize-format-before-reward, require-parseable-outputs-before-direct-rl, do-not-start-rl-on-unparseable-output, keep-failures-out-of-positive-sft, synthesize-from-task-blueprints, verify-tasks-then-trajectories, filter-wrong-teacher-trajectories

### `lora-as-default-post-training`

When full-parameter fine-tuning is the default, or a task LoRA wipes general tool calling. Fold forgetting controls here.
Rule. Attach adapters and freeze the base unless a measured gap needs full updates. Cover MLP and attention. Use about 10x the full-FT learning rate. High rank for SFT, small rank for RL. Mix a sizable general slice. Stop SFT at format-plus-basics. Keep a KL to the reference in RL. Isolate jobs with multiple adapters. Early-stop on retention, not train loss.
Check. The train card lists which controls are on, and a general-tool suite is in CI after every patch.
source-ids: lora-as-default-post-training, lora-must-cover-mlp-and-attention, lora-learning-rate-ten-times-full, lora-rank-high-for-sft-low-for-rl, thought-forgetting-controls, early-stop-on-retention-not-train-loss, mix-retention-data-to-limit-forgetting, dual-validate-boundary-and-retention

### `rl-raises-existing-success-probability`

When pass@k is near zero or groups are all reward-zero, and PPO or GRPO still starts.
Rule. Apply RL only to behaviors the current policy can already emit sometimes. Restore within-group variance with path or process signals, or abort. Compare siblings inside one prompt for GRPO. Use a value baseline when the horizon is long. DPO is offline pairs, not on-policy RL.
Check. The launch review shows a positive rollout class, nonzero within-group reward std on a probe batch, and an abort when group std stays at zero.
source-ids: rl-raises-existing-success-probability, do-not-run-rl-on-all-zero-groups, restore-within-group-variance-or-get-no-gradient, grpo-compares-siblings-on-one-prompt, ppo-subtracts-a-learned-value-baseline, pick-ppo-for-long-credit-assignment-grpo-for-group-compare, run-grpo-as-rollout-reward-advantage-update, use-dpo-only-on-offline-pairs, watch-value-collapse-and-entropy, raise-probability-of-high-reward-rollouts, online-feedback-scores-unseen-candidates

### `rlvp-reward-outcome-and-penalize-path`

When surface success arrives through edited tests, skipped auth, or a shallow done, or a PRM is the first reward.
Rule. Keep a verifiable outcome channel. Add a deterministic path signal for machine-decidable violations. Prefer penalties for specific visible actions. Add progress only after a probe shows the partial is reachable. Prefer programmatic RLVR. Treat reward models as hackable proxies. Separate hacking (a hole) from seeking (the policy's picture of the grader).
Check. A unit suite scores a test-file edit as high penalty, a clean pass as high outcome with path near zero, and a golden trio that keeps that order after every reward change.
source-ids: rlvp-reward-outcome-and-penalize-path, start-with-outcome-then-add-verifiable-process, keep-outcome-so-inaction-cannot-win, rlvp-four-design-rules, asymmetric-verifier-and-reachability, test-path-signal-reachability-first, prefer-programmatic-rlvr, treat-reward-models-as-hackable-proxies, separate-reward-hacking-from-reward-seeking, use-sparse-outcome-when-the-best-path-is-unknown, source-timing-and-density-are-separate-choices, do-not-add-unverifiable-reward-axes

### `hidden-tests-for-premature-completion`

When a coding agent stops before tests, finishes two of three goals, or a harness trusts a self-reported done.
Rule. Score completion on isolated real state the policy cannot author. Attribute the first error to conclude-without-evidence. Mix prefix pairs of premature reject versus verify-then-conclude. Keep a boundary set of unfinished tasks and a retention set of truly finished ones. Evaluate the real goal, not the train proxy.
Check. A `done` string with failing hidden tests scores negative. Hidden tests are invisible. The patch report includes premature-stop rate, healthy-finish rate, and a general-skill spot-check.
source-ids: hidden-tests-for-premature-completion, never-reward-a-self-reported-done, keep-a-retention-set-against-never-finishing, dual-validate-boundary-and-retention, evaluate-the-real-goal-not-the-proxy, post-training-sets-action-threshold

### `treat-sampler-trainer-mismatch-as-off-policy`

When vLLM samples and FSDP trains, and the batch is called on-policy because weights were copied.
Rule. On-policy is a numeric fact. Online is live interaction. After a weight sync and before an update, if token logprobs disagree, call the batch off-policy. Store behavior logprobs at generate. Sync tokenizer, chat template, precision, and kernels, not only `state_dict`. Limit reuse epochs and async lag. Monitor ρ, KL, and clip fraction as launch blockers.
Check. A pre-update test fails the job if logprob MAE or KL exceeds the set epsilon. Config hashes match across sampler and trainer.
source-ids: treat-sampler-trainer-mismatch-as-off-policy, distinguish-online-from-on-policy, avoid-stale-rollouts-in-policy-gradients, long-token-importance-ratios-explode, monitor-pre-update-rho-and-kl, store-behavior-logprobs-at-generation, sync-more-than-weights, limit-reuse-epochs-and-async-lag, do-not-ignore-train-infer-mismatch

### `reuse-environments-not-questions`

When a public bench is both the train mix and the claimed score, even if parameters are randomized.
Rule. Share generators and verifiers. Hold out whole template families and headline the OOD score. Deduplicate by template, customer, or time. Keep hidden tests off the model context. Treat simulator bias as the ceiling. Watch apology farms, leaked-answer queries, and comfort-zone retreat. Anchor the main reward to programmatic real state.
Check. A script asserts empty intersection of train and eval template ids, and a correlation plot of sim score versus real outcome exists before launch.
source-ids: reuse-environments-not-questions, share-env-code-not-eval-tasks, isolate-train-and-eval-by-template, simulator-reward-hacking-patterns, treat-simulator-bias-as-the-ceiling, hybrid-calibrate-simulators-with-real-calls, simulate-tools-with-curriculum-noise, simulate-full-dynamics-only-with-calibration

### `student-rollout-plus-teacher-token-kl`

When distillation is only off-policy SFT on teacher traces, or RL is only a terminal score on student traces, and env steps are expensive.
Rule. Roll out the student. Minimize KL from the student distribution to the teacher on those prefixes. Wait until the student reaches correctable states. Keep the same numeric-agreement gate as PPO. Privileged self-distillation never ships the answer in the serve template. A weaker model may judge a stronger explorer. It may not be the SFT ceiling.
Check. The trainer path rolls out the student and applies teacher KL on those prefixes. A leak test shows privileged fields absent from serve.
source-ids: student-rollout-plus-teacher-token-kl, opd-needs-student-in-correctable-states, opd-still-needs-numeric-agreement, opd-beats-sparse-agent-rewards-when-a-teacher-exists, self-distill-with-privileged-answers, never-deploy-privileged-context, opsd-cannot-invent-inexplicable-knowledge, count-sample-efficiency-as-updates-per-env-step, sparse-feedback-is-the-rl-bottleneck, sample-efficiency-and-distribution-consistency, distill-full-cot-from-an-open-teacher, pick-a-stronger-open-teacher-not-closed-sota, weak-verifier-can-teach-a-strong-explorer

### `mask-tool-observation-tokens-from-the-policy-loss`

When sandbox stdout is trained as if the model wrote it, or a single-turn recipe is copied onto a ten-turn agent.
Rule. Mask observation tokens. Backpropagate only through thoughts and tool-call arguments. Treat thinking tokens as actions that cost context and do not move the world. Assign delayed credit with process scores, a value net, or path signals. Replan from the current observation. Prove sandbox reset and replay before claiming multi-tool RL.
Check. A trainer test shows zero loss on injected observation tokens. The episode schema has turn index, thought, action, observation, and a written credit plan.
source-ids: mask-tool-observation-tokens-from-the-policy-loss, multi-turn-is-react-with-delayed-payoff, assign-credit-under-delayed-reward, replan-from-current-observation, retool-style-tool-feedback-loop, multi-tool-sandbox-must-reset-and-replay, environment-is-what-the-agent-cannot-change, llm-actions-are-variable-length-compositions, treat-thinking-tokens-as-policy-actions, delayed-reward-and-exploration-tradeoff

### `map-eval-artifacts-to-training-uses`

When chapter-7 bad-case packs sit unused, or every miss is dumped into SFT, or edit misses are all blamed on the model.
Rule. Send verified end-to-end tasks to RLVR and RFT. Send prefix boundaries to DPO, boundary SFT, and OPD states. Send first-error records to PRM negatives and RLVP rules. Attribute edit failures across harness hops before training. Train exact copy only after a model-fault label, and treat tokenizer lossless rate as a ceiling.
Check. A routing table maps every eval artifact class to one training use and one isolation rule. Byte-exact tables include a tokenizer-ceiling column.
source-ids: map-eval-artifacts-to-training-uses, attribute-edit-failures-before-training, train-exact-copy-only-after-model-fault, tokenizer-ceiling-on-copy, scope-sensitive-edits-not-global-replace, keep-failures-out-of-positive-sft

### `place-capability-on-rag-prompt-code-or-weights`

When a capability is trained because LoRA is convenient, or left in a prompt when it is high-dimensional and high-volume.
Rule. Put facts and evidence in retrieval. Put language-expressible principles in prompts or skills. Put deterministic procedures and hard constraints in programs. Update parameters only for high-dimensional skills that symbols cannot carry, once the approach is stable and volume justifies it. Audit data at every stage. Validate assumptions at small scale. Budget RL as tens to hundreds of SFT time.
Check. A placement table exists for the product's top capabilities with one carrier per row, and each large job has a pilot report.
source-ids: place-capability-on-rag-prompt-code-or-weights, exhaust-context-tools-and-code-before-weights, do-not-stuff-knowledge-into-sft, audit-data-quality-at-every-stage, validate-assumptions-at-small-scale, budget-rl-as-tens-to-hundreds-of-sft, drill-post-training-decisions-on-live-failures

## Failure diagnostics

- All-zero groups or pass@k near zero, yet RL is scheduled. Open `diagnose-foundation-protocol-or-policy`, then `rl-raises-existing-success-probability`.
- Parse failure, JSON or tool schema wobble, verifier cannot score. Open `sft-writes-protocol-not-a-knowledge-base`.
- Domain language or facts missing. Open `midtrain-repairs-target-distribution`.
- Self-reported done, tests edited, or proxy up while the real goal is flat. Open `hidden-tests-for-premature-completion` and `rlvp-reward-outcome-and-penalize-path`.
- Sampler and trainer logprobs disagree after a weight sync. Open `treat-sampler-trainer-mismatch-as-off-policy`.
- Train questions reported as the score, or sim CSAT is the launch gate. Open `reuse-environments-not-questions`.
- Task LoRA wipes general tools. Open `lora-as-default-post-training`.
- First move is a train ticket with no prompt, tool, program, or retrieval attempt. Open `place-capability-on-rag-prompt-code-or-weights`.

## Namespaced drills

#### `08-post-training-q1`

A task LoRA wipes general tool calling even though the base is frozen. Name the controls besides "use LoRA".
Expect. Mix a general slice, stop SFT at format-plus-basics, small RL rank plus reference KL, freeze fragile towers, isolate adapters, regress a general-tool suite.

#### `08-post-training-q2`

A capability could live in weights, a prompt, retrieval, or a program. Fill the four-carrier table before opening a train ticket.
Expect. Facts in retrieval, expressible principles in prompts, hard rules in programs, parameters only for high-dimensional volume that symbols cannot carry.

#### `08-post-training-q8`

A smaller model is proposed to teach a larger agent. When is that safe?
Expect. Safe when the small model is a verifier or reward model and the large model explores. Unsafe when the small model is the demonstrator. SFT cannot beat its demonstrator.

#### `08-post-training-q9`

Which is more dangerous, a clean process with a wrong result, or a dirty process that lucks into a right result?
Expect. Lucky success is more dangerous. Keep outcome live, penalize visible path crimes, leave enough sparsity to discover a better tactic.

#### `08-post-training-q10`

A bench can train and evaluate. How is its training value used without destroying independence?
Expect. Reuse the environment and the generator, not the questions. Hold out whole template families. Headline OOD.

#### `08-post-training-q11`

pass@1 is tiny. How do pass@k, parse rate, partial progress, and failure tags choose a stage?
Expect. Near-zero pass@k plus knowledge tags means mid-train. Nonzero pass@k plus parse failure means SFT. Parse works, success is occasional, reward is honest means RL may amplify. Do not run the three stages as ceremony.

#### `08-post-training-q13`

The world is an LLM simulator. Which hacks appear, and what blocks them?
Expect. Apology farms, invented facts, leading queries that leak answers, tone farms, comfort-zone retreat. Anchor to programmatic real state. Never launch on sim scores alone.

## Depends-on

`playbooks/evaluating-agents.md` and `lessons/07-evaluating-agents.md` for the five-component env, first-error records, and validators reused as rewards. `playbooks/coding-agent.md` for `tests-pass-as-completion`, joined here by `never-reward-a-self-reported-done`.

## Needed-by

`playbooks/continual-evolution.md` treats weights as one carrier among four. `SKILL.md` After a model drop retires harness layers only after a retirement eval.

## Open tensions

- SFT versus RL. `sft-memorizes-rl-generalizes-as-tendency` forbids the law-like slogan. Use `choose-sft-when-protocol-is-unstable`, `choose-rl-when-success-is-nonzero-and-reward-is-faithful`, and `choose-midtrain-when-passk-is-near-zero`.
- Harness versus weights. `exhaust-context-tools-and-code-before-weights` wins first. Then `diagnose-foundation-protocol-or-policy`.
- pass@k versus Pass^k. This chapter uses pass@k as a support test. It is not an operations reliability bar.
- Self-report versus independent verify. `never-reward-a-self-reported-done` owns the train-time gate. The producer never marks done.
