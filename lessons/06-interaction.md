# expand-observation-action-timing

## What this is for

After content (context, memory, tools, code) is in place, grow observe and act by modality and timing so the world can push, interrupt, and be reconfirmed. A turn-bound text loop cannot run a live assistant, a barge-in voice, a changing GUI, or a contact-rich arm. This file holds the decision clusters. The procedure lives in `playbooks/interaction.md`.

## Core model

Event stream consumed at tool-boundary safe points. One queue unifies user text, tools, callbacks, and timers. Apply or cancel only at a defined boundary, or by manufacturing one for urgency. A placeholder marks an unfinished tool. It never invents a result. Fast paths may act only when the act is reversible. A new frame or `verify_state` is acceptance. Model speech is not.

Short terms. Observation space is what can be sensed and when it arrives. Action space is what can be emitted and whether it can span, halt, or preempt. Modality is the carrier. Timing is the rhythm. A Channel is a third-party push path. Cascade, Omni, and full-duplex are voice trades. SoM numbers marks so a click is an id. AOI turns continuous screen and sound into keyframe, transcript, and caption events. A VLA maps observation plus skill language to motion. Action chunking hides infer time. Perceive-Think-Act reconfirms after every GUI or robot act.

## Clusters

### `axes-content-modality-timing`

When. Task quality is stuck on a fixed model, or the loop still assumes the world waits.

Rule. Keep content expansions. Add modality (form) and timing (rhythm) as the remaining axes. Match primitives to scale. Seconds-to-days use event queues. Voice overlaps on a 10 ms to 1 s clock. Computer use reconfirms across sub-second to second frames. Robotics chunks and preempts on a millisecond clock. A turn-trained policy must not be deployed as if the environment idles until the next token.

Check. An architecture note has a 3-by-2 table of content versus modality versus timing for observe and act, and the change fills a modality or timing cell. Four scale rows have distinct cancel budgets. A test inserts a user event between tool call and tool result and stays schema-valid.

source-ids: expand-spaces-beyond-turns, drop-turn-taking-premise, axes-modality-is-form, axes-timing-is-rhythm, axes-content-modality-timing, axes-turn-trained-policy, axes-four-timescales

### `async-event-stream-not-poll`

When. The system repeatedly asks whether anything new arrived, or a long job blocks talk.

Rule. Build the event-driven runtime before adding voice or pixels. Unify inputs as timestamped events and wake on arrival. Do not poll as the primary sense. Require three assistant properties. Long work must not block talk. Events route by cancel, queue, or parallel. Interrupted work must resume. Hooks, cron, and heartbeat are time-driven or internal. Second-scale handoffs (OTP, three-way pickup) need a live Channel. Fold chat, tools, webhooks, and timers onto one enqueue.

Check. Ingress metrics show a push handler for a non-timer source. A live log handles a user message while a background tool still runs. A need-OTP inject notifies in seconds, not a heartbeat period.

source-ids: async-timing-not-modality, async-three-assistant-gaps, async-sync-train-async-deploy, async-event-stream-not-poll, openclaw-time-driven-gap, openclaw-channel-seconds-handoff, openclaw-unify-event-loop

### `evt-tools-filters-payloads`

When. The world must wake the agent, or the agent must reach the user without dumping traces.

Rule. Split event-trigger tools from user-communication tools. Use one-shot and recurring timers as time senses. Monitor long jobs instead of polling the log. Connect external push onto the shared queue. Write filters and put first-decision ids in the payload. Send user-visible messages through a dedicated tool that can carry files, cards, and urgency. Track delivery and read state across channels. Pick IM, SMS, mail, phone, or push from urgency, status, content, and preference. Use cards or generated UI when prose is the wrong surface.

Check. Trigger schemas document filters and payload ids. A finished background job produces a messaging-tool call. Policy tests send OTP on a realtime channel and a weekly report on a quiet one.

source-ids: evt-tools-timers, evt-tools-monitor-shell, evt-tools-connect-channel, evt-tools-filters-payloads, comms-dedicated-not-raw, comms-async-read-cross-channel, comms-channel-and-reengage, comms-generative-ui

### `identity-virtual-default`

When. The agent must act while the holder is away.

Rule. Default to a declared virtual identity and an isolated VM or emulator. User-account use is an exception path with visible login, not the default credential store. Expect datacenter IP blocks. Use residential egress for ordinary browse when policy allows. When the counterparty needs the holder, open VNC or RDP, watch the login, then reuse the session. Mount one shared volume and pass paths. Do not copy file bytes into context.

Check. Runtime config shows agent-owned credentials as default. Mounts show no home bind except the declared share. A HITL auth path and session cache exist. A tool result is a path under the share.

source-ids: identity-virtual-default, identity-isolate-runtime, identity-antibot-and-hitl, identity-shared-fs

### `events-safe-point-loop`

When. A new event arrives while the model is decoding or a tool is running.

Rule. Run one long-lived consumer. Dequeue a batch, append, call the model once, run tools, then wait. Consume arrivals only at round boundaries. Cancellation asks at the safe point rather than killing an arbitrary instruction. Model every input as source, channel, content, and context. Leave tool bodies and stranger mail in structured fields. Never promote them to the user role.

Check. A race test that posts mid-decode grows the trajectory only at the next boundary. Stored events always have the four keys. An eval shows a malicious tool payload and an unchanged later permission decision.

source-ids: events-safe-point-loop, events-structured-four-fields, events-structured-blocks-injection

### `events-urgency-taxonomy`

When. Several events hit one instance.

Rule. Urgent events manufacture a safe point now (cancel). Routine events wait for the next natural safe point (queue). Independent cheap queries start another loop (parallel) and write back with a parallel marker. Hard-code typed urgency. `user.interrupt`, supervisor instruction, agent interrupt, and marked alerts cancel. Ordinary user input, tool results, and timers queue. A leftover classifier reads structured fields only.

Check. Three fixtures (stop, extra constraint, weather) take the three routes. Unit tests map typed events with no model call. Router traces show structured fields only.

source-ids: events-cancel-queue-parallel, events-urgency-taxonomy, events-hybrid-router, events-parallel-mark

### `events-placeholder-never-fake`

When. Cancel hits while a tool has no result yet.

Rule. Write a placeholder that states the tool is still running. Never invent a successful result. Training almost always showed a real result after a tool call, so models fill the hole. Fire placeholders only on a true user or supervisor stop. Keep the real result as a later event.

Check. Interrupted traces contain a not-complete placeholder. An eval fails if later thought quotes a concrete field the placeholder did not contain.

source-ids: events-placeholder-never-fake, syncfmt-placeholder-hallucination

### `syncfmt-five-rules`

When. A user or urgent event arrives before a tool returns, while the API still wants pairs.

Rule. Apply five write rules. Record the assistant (think, text, tool call) immediately. Record the tool result only when the tool finishes. On interrupt during a tool, insert a background placeholder, append the new event, and re-invoke. On interrupt during thinking, drop the partial think and start a new round. Non-interrupts wait and flush as a batch after the cycle. Prefer `initiate_*` plus completion events so fewer in-flight pairs exist. Number flushed items and demand a response to every type count. Label these repairs as temporary. Plan model-side out-of-order read, resume without believing a cancelled tool, and full batch coverage.

Check. A recorded interrupt trace is schema-valid. A non-urgent note during a tool does not create a placeholder. A 20-event fixture shows numbered lines and a type-count footer. No tool description says it waits until hangup.

source-ids: syncfmt-five-rules, syncfmt-initiate-complete, syncfmt-status-bar-batch, future-prompt-patches-are-temporary, future-three-async-skills, future-async-rl-infra, future-continuous-thinking, future-think-while-waiting

### `voice-three-paradigms`

When. A voice stack is being picked, or a strong model still misses handovers.

Rule. Treat voice as a continuous, interruptible loop, including outbound calls. Let the model decide content. Let the architecture decide hearing, latency, floor, and in-call confirm. Pick cascade, Omni, or full-duplex as a trade, not a ladder. Cascade when modules must swap and debug. Omni when paralinguistics matter and turns are acceptable. Full-duplex when overlap must be a model decision. Stream ASR, speculative LLM, and incremental TTS if the stack is still cascaded. Do not call a full-segment encoder streaming. Omni stays turn-based until a digit-pause fixture passes. Locate Omni misses with a self-cascade plus inner text and acoustic markers.

Check. An ADR names one paradigm and the accepted limit. A latency log has four cascade stages when that shape is kept. An overlap fixture exists for full-duplex. A digit-pause fixture is marked expected-fail on Omni if it still cuts.

source-ids: voice-continuous-not-dictation, voice-architecture-vs-model, voice-three-paradigms, voice-escape-vad-floor, cascade-serial-bottlenecks, cascade-keep-for-debug, stream-perception-pipeline, stream-not-whisper-encoder, stream-endpoint-online-labels, stream-acoustic-markers, omni-paralinguistics, omni-still-turn-based, omni-self-cascade-observe, duplex-no-preset-turns, duplex-interaction-model

### `cog-two-dimensions`

When. A hard question arrives in a live voice session, or a design is labeled end-to-end.

Rule. Keep realtime engagement and deep intelligence on two clocks. Do not let a fast answerer commit a fact the slow path may reverse. Prefer a foreground that holds the floor and a background that returns advice on a side channel, or a swappable slow brain behind a frozen interaction interface. Name the axis before saying end-to-end. Speech-path fusion (audio in and out) is independent of cognitive fast/slow. Drive TTS with markers that show pause or uncertainty. Do not copy misspeak-then-reverse on commitments. Fast thinking may not call irreversible tools.

Check. Latency and quality budgets are separate numbers. A hard-question fixture never places a yes or no in the fast stream before the slow result. The architecture page has a two-axis label. A spoken eval fails on a commitment reversal.

source-ids: cog-two-dimensions, cog-s1-contradiction, cog-s2-advice-channel, cog-mgrd-acoustics, cog-mps-parallel, cog-decouple-swap-slow, cog-two-e2e-meanings, tts-control-markers, tts-signal-not-false-correct

### `cu-perceive-think-act`

When. The agent must operate a GUI.

Rule. Close a perceive-think-act loop that reconfirms reality. Screenshot, think, act, wait, screenshot again. Score closed-loop completion under load and irreversible dialogs. One-shot frame QA is necessary and not sufficient. Keep a harness any vision model can drive. Cover mouse, keyboard, wait, and screenshot, plus a persistent shell and unique-string file edits.

Check. A trajectory stores a post-action frame (or hash) and a match bit per step. Release criteria include multi-step success. Two backends complete the same recorded task through one executor.

source-ids: cu-perceive-think-act, cu-understand-vs-complete, cu-harness-model-agnostic, cu-computer-tool, cu-bash-and-editor

### `cu-grounding-three-routes`

When. The model must click a control.

Rule. Prefer closed-set ids, then marks, then coordinates. If a DOM or a11y tree exists, number interactive nodes and click by id. Else overlay Set-of-Mark. Else predict coordinates with aspect-matched scale and invert map. Never stretch to a different aspect. Keep coordinates as the annotation-free fallback for Canvas, WebGL, and moving controls. On mobile, attach a gesture type to every coordinate.

Check. The grounder logs which route fired. A unit test at a large live resolution maps a center click back to center. The action schema allows both `element_id` and scaled `x,y`. Mobile actions require a gesture field.

source-ids: cu-grounding-three-routes, cu-structured-index-steps, cu-coord-scale, cu-hybrid-coord-fallback, mobile-a11y-and-gestures

### `cu-world-predict-state`

When. The screen plays video, toasts, or audio between stills, or the planner acts only after the last click.

Rule. Redesign the observation interface. Take a keyframe when a small model says the screen changed. Transcribe only when volume is present. Keep a one-sentence caption after the image leaves context. Encode checkable desktop state (windows, focus, fields, load, permissions). Predict the next state after click, type, scroll, or wait. Continue if reality matches. Re-observe on mismatch. Predict diffs the task can check, not a photoreal frame. Measure steps and wait against a human baseline. Treat mobile store and OS blocks as a business conflict, not only CAPTCHA.

Check. Between two clicks the log can contain extra keyframes or a transcript. A planner log shows a predicted delta and a match bit. The eval table has success, steps, and wait. The connector matrix has an ecosystem-risk column.

source-ids: cu-aoi-three-techniques, cu-osworld-efficiency, cu-world-predict-state, mobile-ecosystem-conflict

### `robot-five-layer-stack`

When. One model is asked for both tidy-the-desk and the next joint tick.

Rule. Split five timescales. Task goal (minutes). Long-horizon order (seconds to minutes). Bounded skills such as pick and place (about 1 to 3 s). VLA or skill policy (about 1 to 10 Hz). Low-level control plus safety (about 50 to 1000 Hz). The high-level model chooses calibrated skills only. Keep order off the high-frequency path. Use teleop on the same cell to decide hardware versus algorithm. Filter bad takes before they enter a VLA set. A sim ceiling is not a hardware proof.

Check. A rate diagram shows five layers, and the LLM output type is a skill, not a joint vector. A teleop log meets the acceptance checklist on the same hardware the agent failed. Control-thread logs continue while the planner is idle between skills.

source-ids: robot-four-questions, robot-teleop-diagnoses-algo, robot-teleop-is-data, robot-sim-ceiling, robot-five-layer-stack, robot-bounded-skills, robot-separate-order-from-now

### `robot-five-tool-contract`

When. An embodied reasoner will drive the real arm.

Rule. Expose only `observe_scene`, `pick`, `place`, `verify_state`, and `stop`. Decompose into checkable skill nodes with start, done, and risk limits. After every skill, observe and test the postcondition. Retry only the current skill on a failed grasp. Call stop on user stop, object leaving the workspace, or an unconfirmable state. Humans may start the run and hit e-stop. They must not finish a motion. The VLA maps current frame plus skill text to motion. Photograph again before place.

Check. A passing autonomous episode has `verify_state` after the last place and no mid-run human motion. The tool schema is a closed enum. A test that sends raw joints is rejected.

source-ids: robot-checkable-nodes, robot-five-tool-contract, robot-vla-maps-skill, robot-discrete-vs-continuous

### `robot-action-chunking`

When. Policy infers at 1 to 10 Hz and the controller needs tens to thousands of Hz, or a video model is sold as a world model.

Rule. Chunk only long enough to hide inference. Keep perception live and discard the rest if the scene jumps. Do not ask a VLA for consequences, other bodies, or stale scenes. A world model must understand state, predict action-conditioned futures, and pass scores to the planner. Use it before, during, and in training. Prediction ranks. The camera accepts. Prefer check-and-retry over open-loop sequences. Treat sim success as a different environment. Widen visual variation while training local decisions. Even a sim gain is not a real-arm certificate.

Check. A chunk-abort test moves the object mid-chunk and drops remaining commands. Success requires a fresh camera check and a safety process that can halt without the VLA. A go-live checklist includes calibration, actuator test, and e-stop.

source-ids: robot-action-chunking, robot-vla-limits, robot-world-three-jobs, robot-world-three-uses, robot-predict-not-accept, robot-open-check-predict, robot-sim2real-gaps, robot-widen-visual-train

### `summary-safe-point-density`

When. Voice, GUI, and robot stacks grow in parallel, or the same cancel primitive is copied from mail to contact.

Rule. Reuse one perceive, judge, act, observe skeleton. Share wake, safe point, cancel, preempt, and fast/slow. Space safe points with environmental change rate. Add extra guards in proportion to irreversibility. Observation cost is the weaker driver. Freeze the claim that observe and act now cover content, modality, and timing. Later work tests the pair, then trains, then evolves, and only then splits agents.

Check. A platform doc lists the shared loop steps and per-surface latency. Each irreversible class has a non-model guard. The handoff list points at loop eval, not module scores.

source-ids: summary-shared-skeleton, summary-safe-point-density, summary-feeds-eval-and-evolution

## Failure diagnostics

| Symptom | Cluster | First check |
| --- | --- | --- |
| Heartbeat-only OTP or missed callback | `async-event-stream-not-poll` | A non-timer push handler exists. |
| Torn assistant text or half-applied tool | `events-safe-point-loop` | Trajectory grows only at a recorded boundary. |
| Invented contacts after a cancelled search | `events-placeholder-never-fake` | Placeholder denies completion. Later real event if the job finishes. |
| Weather aside kills a long analysis | `events-urgency-taxonomy` | Typed stop cancels. Weather is parallel or queued. |
| Stop button waits on an LLM | `events-urgency-taxonomy` | Typed urgency has zero classifier latency. |
| Agent spends the user's primary account | `identity-virtual-default` | User credentials are an exception path. |
| Fast voice commits, then reverses | `cog-two-dimensions` | Fast registry has no irreversible tools and no yes or no before slow return. |
| Click storm on a changed page | `cu-perceive-think-act` | Post-action frame and match bit exist. |
| Missed Canvas control or retina offset | `cu-grounding-three-routes` | Route log plus aspect-matched invert map. |
| Spoken done with the cup still on the desk | `robot-five-tool-contract` | `verify_state` after last place. No mid-run human motion. |
| Arm finishes an old reach after the cup moves | `robot-action-chunking` | Chunk abort on live change. |
| Email-style cancel on a moving gripper | `summary-safe-point-density` | Cancel SLA matches change rate. Hardware e-stop exists. |

## Namespaced drills

Collapse the twelve `thought-*` wrappers here. Prompts are paraphrased. Ids are `06-interaction-qN`.

source-ids: thought-priority-router, thought-batch-twenty, thought-virtual-vs-user-id, thought-omni-observability, thought-mimic-human-speech, thought-som-fallback, thought-bad-teleop-data, thought-five-year-interaction, thought-dual-grounding, thought-chunk-vs-change, thought-reversible-fast-path, thought-cancel-across-scales

**06-interaction-q1.** Who decides event priority, a rules engine or another model, and what does each cost? Use both layers. Typed events stay on hardcoded rules. Ambiguous text goes to a small classifier that reads structured fields only.

**06-interaction-q2.** Twenty events wait (ten tool results, five user notes, five alerts). How should they be ordered so a class is not dropped? Lift alerts and interrupts onto cancel. Persist huge tool bodies to files. End with a status bar that counts each type and requires a response to every group.

**06-interaction-q3.** When should the agent use a virtual identity versus the holder's accounts? Default to virtual identity. Switch to holder-present VNC or RDP only when the other side requires the holder. Criteria are holder-required plus credential blast radius.

**06-interaction-q4.** An end-to-end voice model hid ASR, LLM, and TTS. How can a stage miss still be found? Emit inner text and acoustic markers. Run a self-cascade (transcribe then reason with the same weights) and compare to the direct audio path.

**06-interaction-q5.** Should think-while-speaking copy human fillers, pauses, and self-correction? Copy the imperfections that carry signal. Do not copy commitment reversals. Fail evals that speak a fact and then reverse it.

**06-interaction-q6.** If SoM or DOM marks miss a custom or moving control, should coordinate prediction return? Yes, as fallback. Keep both `element_id` and scaled `x,y` in the action schema.

**06-interaction-q7.** How does a weak teleop operator hurt a VLA, and how can bad takes be dropped? A VLA mainly imitates. Filter retries, jitter, collisions, and failed finals at collection time. Dataset quality dominates architecture.

**06-interaction-q8.** Voice, computer use, and robotics all move toward end-to-end models. What lasts in the interaction layer? A stable interaction interface plus a swappable background reasoner, not one fused checkpoint.

**06-interaction-q9.** DOM and a11y fail on Canvas and custom-drawn UI. Bet on vision only, or keep both? Keep both for now. Feature-detect structure. Keep a vision path in CI. Pure vision has the higher long-term ceiling.

**06-interaction-q10.** Action chunks hide infer but go stale if the object moves. How can smoothness and reactivity coexist? Set chunk time to the infer-time floor. On a sudden change, drop the rest and re-infer.

**06-interaction-q11.** Fast paths now speak, click, or step before the slow check. How can those acts avoid irreversible harm? Grade by reversibility. Do not expose irreversible tools to the fast model.

**06-interaction-q12.** How does cancel differ on an event loop versus inside a robot chunk? On the loop, cancel waits for a tool-boundary safe point. Seconds can be acceptable. Inside a chunk, the control thread must halt in milliseconds. Change rate sets density. Add a non-model guard wherever a missed safe point cannot be undone.

## Depends-on

Needs the coding hub and the tools deferral. `coding-core-plus-filesystem` in `lessons/05-coding-agent.md` is the content hub. Do not skip it. `defer-event-and-user-comm-tools` in `lessons/04-tools.md` stops those categories and opens this playbook. Prefix stability and untrusted-data wrapping from `lessons/02-context-engineering.md` still apply to event bodies.

## Needed-by

`playbooks/evaluating-agents.md` scores the expanded loop, not one-shot captions. `playbooks/continual-evolution.md` later folds traces. `playbooks/multi-agent.md` waits until the single agent covers content, modality, and timing.

## Open tensions

`expand-spaces-beyond-turns` grows modality and timing only after the coding hub. Isolation still wins for bulky exploration (`isolate-bulky-exploration-in-subagents`). One event loop is the interaction default, not a license to share every subtask context.

`future-prompt-patches-are-temporary` versus a forever interrupt harness. Keep placeholders and status bars behind flags. Invest in async evals the next model must pass without the patch.

`cog-decouple-swap-slow` versus unified trainings that rebalance intelligence, latency, and naturalness on every upgrade. Freeze the interaction interface when reasoners churn.

`robot-predict-not-accept` versus photoreal world models. Prediction ranks. Live observe accepts. Hardware e-stop stays off the learned path.

`sft-memorizes-rl-generalizes-as-tendency` still forbids a law-like SFT versus RL slogan if this chapter's async skills later become a train job. Diagnose foundation, protocol, or policy first.
