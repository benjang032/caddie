# continual-evolution-closed-loop

## Use when

- the agent repeats yesterday's production mistake
- should this fix be a prompt, a skill, code, or a fine-tune
- add learning from trajectories or an experience store
- sleep learning, memory consolidation, or skill curator
- self-modifying agent or generated workflow from a browser trace
- is this agent actually evolving or only appending logs
- false promise, early escalation, or unconfirmed high-risk action
- satisfaction rose while policy breaks rose

Copy these steps into the todolist before reasoning. A skipped step stays listed with its reason. Do not drop it.

## Steps

### 0. Name the data shape

Name the data shape from [data shapes](../references/data-shapes.md). The shape is a dual loop around a frozen approval root, with four carriers (knowledge, instructions, programs, and weights). Online serving only finishes the task and appends evidence. Offline evolution proposes, gates, and releases. The approval root cannot be edited by the evolving agent.

### 1. Score the triggering trajectories

Score the triggering trajectories on outcome, process, and quality. Attach evidence spans and confidence. Keep low-confidence rows out of the learning set. Outcome is environmental state. Process is the allowed path. Quality is a rubric scored only after the hard layers pass. Satisfaction never overrides a policy, privacy, or promise-action fail.

   Check. Each scored run has three distinct records, and the learning-set query for below-threshold confidence is empty.

   Skip if no triggering trajectories exist. Reason. There is no scored evidence to learn from.

   If the check fails, open `lessons/09-continual-evolution.md` cluster `three-layer-trajectory-verification` (source-ids preserve-is-not-learn, evaluate-before-summarize, three-layer-trajectory-verification, exclude-low-confidence-from-learning, satisfaction-cannot-be-sole-signal).

### 2. Route by representation

Route by representation into knowledge, instruction, program, or parameters. Split mixed capabilities. Treat the route as a proposal, not a release. Facts go to documents. Verbal strategies go to prompts or skills. Exact procedures and hard limits go to programs. High-dimensional perception, style, and implicit strategy go to parameters. Stability sets cadence, not the medium.

   Check. The last five proposals each name a representation class, a matching medium, and a one-line reason. Production files are untouched.

   Skip if every scored row stayed below the confidence threshold. Reason. There is no gated diagnosis to route.

   If the check fails, open `lessons/09-continual-evolution.md` cluster `route-update-by-representation` (source-ids route-update-by-representation, four-media-applicable-boundaries, split-capability-across-carriers, routing-is-only-a-proposal).

### 3. Draft a minimal candidate with provenance

Attach triggering trajectory ids and a parent version. For programs, write a falsifiable change contract and a bounded generator pack (failure diagnosis, must-keep successes, prior rejects). Prefer a small attributed diff over a full rewrite.

   Check. The candidate record exists with medium, diff, evidence ids, and an unreleased flag. A program candidate also has a change contract and a bounded pack.

   Skip if routing produced no writable medium. Reason. The diagnosis does not yet justify a candidate.

   If the check fails, open `lessons/09-continual-evolution.md` cluster `write-falsifiable-change-contract` (source-ids minimal-diff-with-provenance, write-falsifiable-change-contract, bound-candidate-space-with-rejects).

### 4. Validate boundary and retention

Boundary must rise. Retention must hold. For compiled workflows, require a reset hook, independent replay, and before-action, after-action, and final-state checks. For weights, redact, filter errors, hold out a regression set, and regress general skill plus safety.

   Check. The candidate report has boundary and retention numbers. A workflow without a reset-and-replay receipt stays `candidate`. A weight job names redaction, filter, held-out regression, and post-job safety scores.

   Skip compiled-workflow replay when the candidate is not a program. Reason. No compiled path is on the table.
   Skip weight redact and safety regress when the candidate is not a parameter update. Reason. No train job is on the table.

   If the check fails, open `lessons/09-continual-evolution.md` cluster `layer-evolution-evaluation-metrics` (source-ids test-boundary-and-retention-sets, local-fix-without-retention-is-failure, candidate-until-reset-replay-passes, convert-clean-trajectories-to-training).

### 5. Keep candidates off live traffic

Run schema, allowlist, provenance, security, and independent review. Freeze the approval root. Validators, test cases, release thresholds, audit logs, keys, and stable backups are not writable by the generator. Model-produced confidence is not an approval bit.

   Check. The production retriever and model mount return no candidate ids. A patch that touches a validator, threshold, audit sink, or backup is rejected by permission before tests run.

   Skip none of the freeze. Reason. The approval root is a standing constraint, not an optional gate.

   If the check fails, open `lessons/09-continual-evolution.md` clusters `routing-is-only-a-proposal` and `freeze-safety-mechanisms-from-self-mod` (source-ids routing-is-only-a-proposal, isolate-candidates-from-production-traffic, freeze-safety-mechanisms-from-self-mod, model-confidence-is-not-approval).

### 6. Release to canary with a full manifest and rollback

Measure validity, activation, adherence, and retention-set gain. Do not ship on end-to-end score alone. A finished pipeline is not progress on open-ended work.

   Check. The manifest has evidence ids, a behavior diff, a rollback hash, and the four evolution metrics. Missing fields or any failed check equal reject.

   Skip canary if no candidate passed the gate. Reason. There is nothing legal to serve.

   If the check fails, open `lessons/09-continual-evolution.md` clusters `layer-evolution-evaluation-metrics` and `done-does-not-mean-progress` (source-ids record-release-manifest-and-rollback, layer-evolution-evaluation-metrics, evolution-requires-trace-change-verify, done-does-not-mean-progress).

### 7. Run sleep cycles

Merge, branch conflicts, prune, and reindex. Retrain adapters from a pinned base the modifier cannot reach. Never let the online path rewrite official artifacts. User-memory files are not the action-experience store.

   Check. The last sleep-job log shows trigger, orient, consolidate, approve, and prune in order. The request path cannot merge or delete official experience. The training config, if any, references a pinned base hash that is read-only to the evolution agent.

   Skip if no sleep trigger fired and the online path is in a high-priority incident. Reason. Time, batch size, storage, and error-rate triggers are quiet, or serving must stay undisturbed.

   If the check fails, open `lessons/09-continual-evolution.md` cluster `run-five-step-sleep-cycle` (source-ids run-five-step-sleep-cycle, collect-online-consolidate-offline, distinguish-user-memory-from-action-experience, retrain-adapters-from-untouchable-base).

## Open next

- [Memory and knowledge](memory-knowledge.md) when a note might be a tenant fact rather than gated action experience (`distinguish-user-memory-from-action-experience`).
- [Post-training](post-training.md) when the chosen medium is parameters and a train job is actually on the table.

## Reply

State what changed (which carrier, which version), what was chosen (route and gate outcome), and what remains open (skipped steps, failed checks, canary metrics still running).
