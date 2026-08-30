# Afterword

Start on `SKILL.md` After a model drop. Open this file only when that short block cannot place a change, score a cloud, or retire a layer. Do not hunt for `formula-and-flywheel.md`.

Long-horizon improvement is not specified here. Stores, editable programs, and the eval gate meet in [playbooks/continual-evolution.md](../playbooks/continual-evolution.md) (`ch9-convergence`).

## Terms

- **Formula triple.** LLM decides. Context is the working set. Tools observe and act.
- **Two clouds.** Streaming overlap with a moving world. Post-deploy write-back of experience.
- **Harness.** Application fallbacks that cover a current model gap and must migrate.
- **Small world.** Stable general knowledge. Train once after data access.
- **Big world.** Tenant particulars that move. Write after deploy.
- **Carriers.** Knowledge, instructions, programs, parameters. Names only in this file.
- **Layerwise eating.** Absorption one layer at a time. Never a single deletion of the whole stack.

## What this is for

Hold the formula as the placement grid after a model drop. Score the two unsolved clouds before adopting a vendor primitive as architecture. Read harness code as a weakness log with a retirement eval, not as a trophy. Spend leftover leverage on barriers a future model cannot eat.

## Core model

Named shape from [references/data-shapes.md](../references/data-shapes.md). Agent = LLM + Context + Tools. Production rewrite is Model + Harness. Environment sits outside.

Afterword objects that sit on that shape.

- Two-cloud register. Cloud one is overlap of sense, think, and act. Cloud two is a write from outcomes into future behavior.
- Weakness-annotated harness stack. Each fallback names the model failure it hides and a retirement eval.
- Four named carriers. This file does not design their stores.

Invariants. A single checkpoint does not clear either cloud. Harness deletion requires a retirement eval with the layer off. Absorption is layerwise and never complete.

## Clusters

### `formula-as-spine`

**When.** A new model feature, product bet, or harness patch needs a home.

**Rule.** Map every change onto LLM, Context, or Tools before adding architecture. A named join such as verification is allowed. A fourth ambient bucket is not. State the same objects as parts, as roles, and as policy plus observation plus action. Declare the orchestration point on the workflow-to-autonomy spectrum. Multi-agent work re-partitions those three terms. It does not mint a fourth primitive.

**Check.** Every merged design note has a one-line formula slot and a mode field. A vendor announcement also scores both clouds before a harness add or delete.

source-ids: formula-as-spine, three-layer-reading, orchestration-spectrum, collaboration-reorganizes, arcs-are-coupled, place-capability-in-formula, building-sequence

### `two-clouds-persist`

**When.** A launch note claims the latest model closed agent research.

**Rule.** Refuse the claim that one upgrade clears either open problem. Ask whether the system can act while the world is still changing. Ask whether a failure today changes behavior tomorrow without a full retrain wait. If either answer is no, keep the problem on the risk register.

**Check.** The risk register lists both clouds with a current mitigation and an owner.

source-ids: two-clouds-persist, place-capability-in-formula, co-move-not-pipeline

### `realtime-cloud`

**When.** The agent must share time with speech, a changing scene, or an arriving inbox.

**Rule.** Design for overlap of sensing, thinking, and acting. A request-response loop that waits for a finished utterance is late by construction. Accept live behavior only if listen-while-think, speak-while-think, mid-utterance planning, and unsolicited notice exist. Split rhythm onto a fast path and depth onto a cancellable slow path when one checkpoint cannot hold both. Treat published throughput points as existence proofs, not as a copy-paste stack. Accept hardcoded-chip speed only with a tape-out update plan.

**Check.** The interaction design names each live stream and an overlap policy. A mid-utterance interrupt trace shows a cancel or a documented turn-batched gap.

source-ids: realtime-cloud, request-response-mismatch, living-agent-invariants, fast-slow-split, decode-speed-blurs-turns, speed-reference-points, hardcoded-inference-tradeoff

### `experience-cloud`

**When.** The agent repeats a domain and still repeats the same mistakes.

**Rule.** Require a path from interaction outcomes back into future behavior. Extract the workaround before context disposal. Rank adaptation from new outcomes above more factory recall. On frontiers with no answer key, close the loop on experimental success and failure. Do not write experience into a carrier until evaluation produces a trustworthy signal. Progress is `evaluate-model-plus-harness`. This file does not own a second eval law.

**Check.** A weekly review shows at least one failure that became a write, or an explicit deferral with a reason. A completed task leaves a trajectory record a later session can retrieve.

source-ids: experience-cloud, discard-on-the-job-lessons, store-experience-first, adaptation-over-memorization, frontier-needs-autonomous-learn, eval-evolution-sequence, eval-decides-progress, shift-build-to-improve

### `small-world-hypothesis`

**When.** The capability gap is general professional knowledge, not a single tenant's taste.

**Rule.** Prefer one more training corpus over a custom evolution loop when the knowledge is stable and public or partnerable. Attribute a coding lead to public source volume, not to a special affinity in the architecture. Bring industry data into one shared frontier model unless isolation is legally required.

**Check.** The capability brief labels the skill small-world and names the corpus or partner path.

source-ids: small-world-hypothesis, openness-explains-coding-lead, industry-by-industry-distill

### `big-world-hypothesis`

**When.** The missing knowledge is a house style, a client temper, or another moving particular.

**Rule.** Do not expect a factory checkpoint to contain private, shifting particulars. Install a post-deploy learning path. List those particulars. Mark each as a post-deploy write. Choose a carrier per particular. Recursive research and science sit on this path because no answer key exists.

**Check.** Each named particular has a store location and a refresh trigger in the memory or evolution config.

source-ids: big-world-hypothesis

### `four-experience-carriers`

**When.** A stored lesson must change future behavior.

**Rule.** Name exactly one primary carrier. Knowledge, instructions, programs, or parameters. This cluster names the four write targets. It does not merge user memory with action experience. Tenant facts stay in [playbooks/memory-knowledge.md](../playbooks/memory-knowledge.md). Gated strategy writes stay in [playbooks/continual-evolution.md](../playbooks/continual-evolution.md). Routing remains a proposal. The frozen approval root is not a carrier.

**Check.** A sample of stored lessons each has a carrier enum and a review hook that matches that carrier. No lesson object treats the two stores as one pile.

source-ids: four-experience-carriers

### `harness-as-weakness-log`

**When.** Reviewing retries, deep compression stacks, or pessimistic permission defaults.

**Rule.** Annotate each fallback with the model failure it hides. Compression towers, huge retry counters, circuit breakers, and default-unsafe permissions are a diary, not decoration. Export recoveries into the training or review queue. Close live challenges, patches, and training on purpose. Measure harness leverage with a same-model ablation. Read a large accuracy jump as a remaining gap, not as eternal IP. The operational loop lives in `SKILL.md` After a model drop. Do not reprint it here.

**Check.** Each major fallback file names the failure class and a retirement eval. An eval report can show one model id, two harness hashes, and two scores.

source-ids: harness-as-weakness-log, patches-become-training-signal, challenge-patch-train-flywheel, own-both-ends, mutual-boundary-knowledge, harness-only-accuracy-lift, leverage-equals-model-gap, coupled-iteration-moat, model-side-flywheel

### `eat-harness-layerwise`

**When.** Someone asks whether the harness will vanish after the next model, or a new checkpoint stops failing the case a fallback was written for.

**Rule.** Answer yes on direction and no on completion. Plan absorption one layer at a time. Delete the matching layer only after a retirement eval holds with the fallback off. Keep the eval as a regression net. Ship a backstop with a deletion date when training still lags the business. Leave external logic for the newest preference the model cannot hold. Put the densest harness on the newest capability frontier. Migrate effort with the model. Do not forecast a harness-free end state.

**Check.** The harness catalog has an absorption column (active, candidate, retired). A retired fallback has a merged deletion and an eval that still runs with the layer absent. No row says delete-all next quarter.

source-ids: eat-harness-layerwise, delete-internalized-layers, interaction-now-in-model, training-lag-vs-business, newest-boundary-backstop, new-frontier-is-unreliable, harness-migrates

### `three-durable-questions`

**When.** APIs, products, and leaderboards turn over on a months-long cycle, or harness skill is still a large accuracy lever.

**Rule.** Judge a stack by what the system sees, what it can invoke, and how a run is verified. Use harness leverage to buy calendar. Spend that calendar on exclusive data, distribution, trust, networks, or human-plus-agent physical work. Treat wrapper edges as eroding. Prefer creating a tool or harness edit in code over waiting for a matching vendor feature. Special-case logic is pavement. It is not the destination.

**Check.** A new-dependency review template has the three questions as required fields. A timeline ties a measured harness delta to a named barrier milestone inside the estimated survival window.

source-ids: three-durable-questions, harness-buys-time, harness-advantage-erodes, nontechnical-app-moats, bitter-lesson-with-harness, create-and-self-improve

## Failure diagnostics

| Symptom | First cluster | First check |
| --- | --- | --- |
| Framework folklore with no formula slot | `formula-as-spine` | Design note missing LLM, Context, Tools, or named join |
| Launch copy treats a checkpoint as the end of agent research | `two-clouds-persist` | Risk register missing a cloud or an owner |
| Chat box thinks only after send. Interrupts finish a stale monologue | `realtime-cloud` | No overlap policy. No cancel on mid-utterance interrupt |
| Same pit every week. Workarounds die with the window | `experience-cloud` | No trajectory record. No carrier write |
| Local memory tries to teach general physics | `small-world-hypothesis` | Brief unlabeled. No corpus or partner path |
| House style re-pasted every session | `big-world-hypothesis` | Particular has no store or refresh trigger |
| Everything stuffed into the system prompt, or a one-line rule burned into weights | `four-experience-carriers` | Lesson missing a carrier enum |
| Retries accrete with no owner. A stronger model still wears the old mask | `harness-as-weakness-log` | Fallback file missing failure class or retirement eval |
| Blog-driven delete-all, or a dead retry that never faced an eval | `eat-harness-layerwise` | Catalog row says delete-all, or deletion without a layer-off eval |
| Company story is only orchestration. Barrier work starts after commoditization | `three-durable-questions` | No funded non-wrapper barrier inside the harness survival window |

Progress claims without a pair eval fail closed to `evaluate-model-plus-harness` in [lessons/07-evaluating-agents.md](07-evaluating-agents.md). Evolution writes without stores, an edit path, or a gate fail closed to [playbooks/continual-evolution.md](../playbooks/continual-evolution.md).

## Drills

### `11-afterword-q1`

Will the next checkpoint absorb the application harness entirely, and should that stack be deleted on arrival?

Absorption is the direction. It is not a single event. Layers fall when a retirement eval holds with the layer off. The process never completes because training lags the business, because private preferences sit outside weights, and because each generation opens an unreliable new frontier. Delete only a layer that passes. Migrate the rest. Do not strip verification from the newest surface.

### `11-afterword-q2`

When is a capability gap a missing public corpus rather than a missing post-deploy path?

If the skill is stable general knowledge that an industry could share, the small-world path applies. The bottleneck is data access. That is why coding looks uniquely strong. If the skill is a house style, a client temper, or another moving particular, the big-world path applies. Write to one named carrier after deploy. Recursive research sits on the second path because no answer key exists. Refuse a single default of fine-tune everything or memory everything.

### `11-afterword-q3`

Where does lasting application advantage sit if a same-model harness change can move accuracy by more than ten points?

That lift shows the wrapper is still a sharp lever and that the model has not internalized the layer. The same lever will shrink as absorption proceeds. Lasting barriers sit in exclusive data, distribution, trust, network effects, and physical joint work. Use the harness to buy the calendar for those barriers. Log the delta as temporary.

## Depends-on

- `SKILL.md` After a model drop owns the procedure. This file is notes behind that block.
- [playbooks/continual-evolution.md](../playbooks/continual-evolution.md) from `ch9-convergence`, `store-experience-first`, `code-edits-harness`, and the carrier write path. `distinguish-user-memory-from-action-experience` keeps the two stores apart.
- [playbooks/memory-knowledge.md](../playbooks/memory-knowledge.md) for the user-keyed archive. Tenant facts are not action experience.
- [playbooks/evaluating-agents.md](../playbooks/evaluating-agents.md) for `evaluate-model-plus-harness`. `eval-decides-progress` is a pointer, not a second law.
- [playbooks/interaction.md](../playbooks/interaction.md) for live streams and event-safe points under `realtime-cloud`.
- [playbooks/getting-started.md](../playbooks/getting-started.md) for the canonical inside-boundary formula. `formula-as-spine` is the placement check, not a rival skeleton.

Needed-by. `SKILL.md` After a model drop, steps 1 through 6.

## Open tensions

Small world versus big world (`small-world-hypothesis`, `big-world-hypothesis`). Train-once plus data wins for stable shared skills. Post-deploy carriers win for moving particulars. The failure is one default for every skill.

Fast and slow architecture versus raw decode speed (`realtime-cloud`). Split paths buy overlap when one checkpoint cannot span rhythm and depth. Extreme tokens per second can make a remaining turn-batch feel live. Hardcoded silicon then trades update freedom for latency. Both paths may run. Neither clears cloud two.

Models will eat the harness versus the harness never finishes disappearing (`eat-harness-layerwise`, `delete-internalized-layers`). Direction is absorption. Completion is denied for training lag, newest preferences, and each new unreliable frontier. Delete only after a retirement eval.

Short-term harness leverage versus long-term wrapper IP (`harness-as-weakness-log`, `harness-buys-time`). Double-digit same-model lifts are real and temporary. Read them as gap, not moat. Spend the window on barriers a model cannot eat.

Own both ends versus application-only teams (`harness-as-weakness-log`). The flywheel is fastest when one party owns model and harness. Application-only teams still owe patch-to-vendor speed and must park durable advantage outside the wrapper.

Memorization versus adaptation (`experience-cloud`). Factory recall is already strong. The remaining prize on open frontiers is learning from outcomes.

Create in code versus wait for the next vendor primitive (`three-durable-questions`). Prefer a created tool. Self-edit still needs the frozen approval root in [playbooks/continual-evolution.md](../playbooks/continual-evolution.md).
