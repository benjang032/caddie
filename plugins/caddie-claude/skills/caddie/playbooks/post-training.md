# choose-and-run-post-training

## Use when

- Should this be SFT or RL?
- pass@k is near zero
- the model forgets tool use after a LoRA
- need mid-training versus RAG
- reward hacking or premature completion
- build an RL environment or a user simulator
- distill a teacher into an agent
- credit assignment on a multi-turn agent
- sampler trainer mismatch
- turn bad cases into training data

Make a working checklist from these steps before reasoning. Use the host's task or todo list when available. A skipped step stays listed with its reason.

## Steps

### 0. Name the data shape

Name the data shape from [data shapes](../references/data-shapes.md). Foundation, then protocol, then policy. The object edited is a token distribution.
Skip if the ticket already names that shape and no other object is proposed.

### 1. Reproduce the miss on a held-out set

Record pass@1, pass@k, parse rate, partial progress, and a failure tag. Run `diagnose-foundation-protocol-or-policy` on that tag before any trainer name is written. Foundation is missing knowledge or a basic skill with pass@k near zero. Protocol is format, tools, or style that wobbles while success already exists. Policy is rare but real success that a faithful scorer can grade. Do not name mid-training, SFT, or RL in this step.
Skip never. Diagnosis is the gate.
If the classification is missing or blended, open `lessons/08-post-training.md` cluster `diagnose-foundation-protocol-or-policy`. Cite diagnose-foundation-protocol-or-policy, four-stage-capability-map, require-a-measurable-gate-to-change-stage.

### 2. Attempt a non-weight fix before any train job

Try a prompt, a tool, a program, or retrieval. Put updateable facts in retrieval and hard rules in code.
Skip only if the ticket shows a failed or impossible non-weight path.
If the first move is still a LoRA, open `lessons/08-post-training.md` cluster `place-capability-on-rag-prompt-code-or-weights`. Cite exhaust-context-tools-and-code-before-weights, place-capability-on-rag-prompt-code-or-weights.

### 3. Mid-train when the foundation is missing

If knowledge or a foundational skill is missing and pass@k is near zero, mid-train on the target distribution plus retention data. Gate length as effective window, not nominal tokens. Remeasure the held-out sheet.
Skip if the diagnosis is not foundation.
If the run is SFT pairs used as a domain dump, open `lessons/08-post-training.md` cluster `midtrain-repairs-target-distribution`. Cite choose-midtrain-when-passk-is-near-zero, do-not-stuff-knowledge-into-sft.

### 4. Stabilize protocol with SFT or constrained decoding

If success exists but protocol wobbles, SFT or constrain decoding on a clean small set. Mask prompt tokens. Stop at format stability and an OOD plateau, not at falling train loss. Treat "SFT memorizes, RL generalizes" as a tendency under a matched shift, not as a law.
Skip if parse and tool schema already let a verifier score.
If SFT continues after the protocol is stable, or RL is chosen because a slogan promised transfer, open `lessons/08-post-training.md` cluster `sft-memorizes-rl-generalizes-as-tendency`. Cite sft-memorizes-rl-generalizes-as-tendency, choose-sft-when-protocol-is-unstable, form-first-then-switch-on-plateau.

### 5. Build an RL environment when policy is the gap

If success is rare but real and a faithful scorer exists, build a resettable env with hidden tests. Probe group reward variance and sampler versus trainer logprobs. Do not start RL on all-zero groups or on unparseable output.
Skip if the diagnosis is not policy, or pass@k is still near zero, or no honest scorer exists.
If done is a self-report or tests sit in the policy context, open `lessons/08-post-training.md` cluster `hidden-tests-for-premature-completion`. Cite hidden-tests-for-premature-completion, never-reward-a-self-reported-done.

### 6. Choose outcome-first reward

Add path penalties for visible, machine-decidable violations. Add process scores only when mid steps are verifiable and the best path is known. Keep the outcome live so inaction cannot win.
Skip if no RL or distillation job is running.
If a lucky shortcut scores as success, open `lessons/08-post-training.md` cluster `rlvp-reward-outcome-and-penalize-path`. Cite rlvp-reward-outcome-and-penalize-path, start-with-outcome-then-add-verifiable-process.

### 7. Prefer on-policy distillation when appropriate

If env steps are expensive and a stronger teacher exists, prefer on-policy distillation on student prefixes. Roll out the student. Align to teacher token distributions on those prefixes. Mask tool observations from the policy loss.
Skip if env steps are cheap, or no stronger teacher exists, or the student cannot yet reach correctable states.
If distillation is only offline clones of teacher traces, open `lessons/08-post-training.md` cluster `student-rollout-plus-teacher-token-kl`. Cite student-rollout-plus-teacher-token-kl, opd-needs-student-in-correctable-states.

### 8. Split train and evaluation by template family

Validate on a boundary set and a retention set. Early-stop on retention, not train loss. Headline the OOD score. Reuse generators and verifiers, not questions.
Skip never after a train job has started.
If train questions are also the reported score, open `lessons/08-post-training.md` cluster `reuse-environments-not-questions`. Cite reuse-environments-not-questions, isolate-train-and-eval-by-template.

### 9. Ship only on an independent real-goal metric

Treat sim scores as auxiliary. Regress general tool use after every adapter.
Skip never at release.
If the train reward is the only reported number, open `lessons/08-post-training.md` cluster `hidden-tests-for-premature-completion`. Cite evaluate-the-real-goal-not-the-proxy, dual-validate-boundary-and-retention.

## Open next

- [Evaluating agents](evaluating-agents.md) when the five-component env or the first-error record is missing.
- [Continual evolution](continual-evolution.md) when a weight change is only one carrier among knowledge, instructions, and programs.

## Reply

State what changed, which gap was diagnosed, which trainer was chosen or skipped, and what remains open.
