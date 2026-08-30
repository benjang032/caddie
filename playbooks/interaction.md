# expand-observation-action-timing

## Use when

- the world should wake the agent
- adding voice, computer use, robotics, barge-in, GUI grounding, virtual identity, action chunking, VLA, full-duplex, or an event-driven loop

## Steps

Copy these steps into the todolist before reasoning. Name the data shape before any loop or tool change. If a check fails, open [lesson 06](../lessons/06-interaction.md) and the named cluster `source-ids`.

### 0. Name the data shape

The shape is an event stream consumed at tool-boundary safe points. Look up [the interaction row](../references/data-shapes.md) in data shapes. Do not write a consumer, cancel path, or actuator until that name is on the page.

### 1. Inventory observe and act

Inventory observe and act on content, modality, and timing. Name the timescale.

List current observations and actions as two registries. Mark missing forms (audio, pixels, sensors) and missing rhythms (push, interrupt, preempt). Tag the surface as seconds-to-days, voice overlap, GUI reconfirm, or robot milliseconds. Refuse a seconds-scale cancel on a contact-rich arm.

Check. An architecture note has a content / modality / timing table for observe and act, and the change fills a modality or timing cell. A design row lists a cancel latency for that scale.

Fail. Open `lessons/06-interaction.md` cluster `axes-content-modality-timing`. source-ids `expand-spaces-beyond-turns`, `axes-content-modality-timing`, `axes-four-timescales`.

### 2. Install one event stream

Install one event stream and consume only at safe points. Add push channels where heartbeat is too slow.

Unify chat, tool returns, timers, and third-party I/O as timestamped events. Wake on arrival. Do not poll as the primary sense. Hooks, cron, and heartbeat are not third-party push. Consume the queue only after think ends or a tool returns, unless urgency manufactures a safe point.

Check. Ingress metrics show a push handler for at least one non-timer source. A race test that posts mid-decode grows the trajectory only at the next recorded boundary.

Fail. Open `lessons/06-interaction.md` clusters `async-event-stream-not-poll` and `events-safe-point-loop`. source-ids `async-event-stream-not-poll`, `openclaw-time-driven-gap`, `events-safe-point-loop`.

### 3. Split trigger tools from talk tools

Split event-trigger tools (timer, monitor, channel) from user-communication tools. Filter wakes and send rich payloads.

Expose one-shot and recurring timers, a monitor on long jobs, and a connect-channel that enqueues immediately. Put ids and snippets in the payload so the first decision does not fetch again. Send user-visible notices through a messaging tool with channel, urgency, and attachments. Model speech in an agent log is not delivery.

Check. Each trigger schema documents filters and a payload with first-decision ids. A finished background job produces a messaging-tool call.

Fail. Open `lessons/06-interaction.md` cluster `evt-tools-filters-payloads`. source-ids `evt-tools-filters-payloads`, `comms-dedicated-not-raw`, `comms-channel-and-reengage`.

### 4. Default to virtual identity

Default to virtual identity and a sandbox. Use HITL remote login only when the holder must appear. Pass files as shared paths.

Provision agent-owned accounts and an isolated VM or emulator. Do not hold the user's primary credentials as the default store. Route CAPTCHA through residential egress when policy allows. Open VNC or RDP only for holder-present auth, then reuse the session. Return share paths, not file bytes in context.

Check. Runtime config shows agent-owned credentials as default. Process mounts show no home bind except the declared share. A tool result is a path that exists.

Fail. Open `lessons/06-interaction.md` cluster `identity-virtual-default`. source-ids `identity-virtual-default`, `identity-isolate-runtime`, `identity-antibot-and-hitl`, `identity-shared-fs`.

### 5. Route urgent, routine, and parallel

Route urgent, routine, and parallel events. Hard-code typed urgency. Classify only ambiguous text from structured fields.

Treat `user.interrupt`, supervisor instruction, agent interrupt, and marked alerts as cancel. Treat ordinary user input, tool results, and timers as queue. Start a side loop only for a cheap independent query, then mark it parallel on the main trajectory. Typed routes use zero model calls. A leftover classifier reads source, channel, and short content only.

Check. Three fixtures (stop, extra constraint, weather) take cancel, queue, and parallel. Typed interrupts show zero classifier latency.

Fail. Open `lessons/06-interaction.md` cluster `events-urgency-taxonomy`. source-ids `events-cancel-queue-parallel`, `events-urgency-taxonomy`, `events-hybrid-router`.

### 6. Keep paired trajectories

Keep paired trajectories. Placeholder only on true interrupt. Prefer initiate plus completion events. Number batch items.

Record the assistant turn at once. Record a tool result only when the tool finishes. On a true interrupt during a tool, write an unfinished placeholder, never a success. On interrupt during think, drop the partial think and start a new round. Non-urgent notes wait and flush as a numbered batch with a type-count footer. Rename blocking tools to `initiate_*` plus later events.

Check. An interrupt trace is schema-valid. A non-urgent note during a tool does not create a placeholder. After a placeholder the model does not quote a field that never arrived.

Fail. Open `lessons/06-interaction.md` clusters `events-placeholder-never-fake` and `syncfmt-five-rules`. source-ids `events-placeholder-never-fake`, `syncfmt-five-rules`, `syncfmt-initiate-complete`, `syncfmt-status-bar-batch`.

### 7. Voice trade

For voice, pick cascade, Omni, or full-duplex as a trade. Stream perception if still cascaded. Split speech-path fusion from cognitive fast/slow. Gate irreversible speech-side tools.

Skip if the product has no spoken channel. Record the skip and keep the event loop.

Cascade when stages must swap and debug. Omni when tone must survive and turns are acceptable. Full-duplex when overlap is a product requirement. Do not treat later rows as replacements. Foreground may mask latency. It may not commit a purchase-grade fact or call an irreversible tool. Keep a self-cascade debug path on any fused stack.

Check. An ADR names one paradigm and its accepted limit. Fast-stream fixtures never place a yes or no before the slow result. Irreversible tools are absent from the fast registry.

Fail. Open `lessons/06-interaction.md` clusters `voice-three-paradigms` and `cog-two-dimensions`. source-ids `voice-three-paradigms`, `cog-two-dimensions`, `cog-s1-contradiction`, `cog-two-e2e-meanings`.

### 8. GUI reconfirm

For GUIs, run perceive-think-act with reconfirm. Prefer DOM or a11y ids, then SoM, then aspect-matched coordinates. Add AOI keyframes, gated ASR, and captions. Predict checkable state before irreversible clicks.

Skip if the product has no GUI or mobile drive. Record the skip.

Screenshot, act, wait, screenshot again. Score closed-loop completion, not one-shot captions. Log which grounder fired. Scale coordinates by matching aspect, never by stretch. Convert video and toasts into keyframe and transcript events. Predict window, focus, and dialog diffs, then accept only from a new frame.

Check. Each step stores a post-action frame (or hash) and a match bit. Release criteria include multi-step success, not only screenshot QA. A planner log shows a predicted state delta before an irreversible click.

Fail. Open `lessons/06-interaction.md` clusters `cu-perceive-think-act`, `cu-grounding-three-routes`, and `cu-world-predict-state`. source-ids `cu-perceive-think-act`, `cu-grounding-three-routes`, `cu-world-predict-state`.

### 9. Robot five layers

For robots, split five layers. Expose observe, pick, place, verify, stop. Chunk only to hide infer. Rank with a short-horizon world model. Accept only from a fresh camera. Keep hardware e-stop.

Skip if the product has no physical actuator. Record the skip.

Separate goal, skill order, bounded skills, VLA or skill policy, and low-level safety. The language model emits a skill enum, not a joint vector. After every skill, observe and test the postcondition. Humans may start the run and hit e-stop. They must not finish a motion. Set chunk time to the infer-time floor and abort on a scene jump.

Check. A rate diagram shows five layers. A passing episode has `verify_state` after the last place and no mid-run human motion. A chunk-abort test drops remaining commands when the object moves.

Fail. Open `lessons/06-interaction.md` clusters `robot-five-layer-stack`, `robot-five-tool-contract`, and `robot-action-chunking`. source-ids `robot-five-layer-stack`, `robot-five-tool-contract`, `robot-action-chunking`, `robot-predict-not-accept`.

### 10. Grade reversibility and eval the loop

Grade tools by reversibility. Set cancel latency to the harm clock. Eval loops, not one-shot captions.

Split the registry into fast-safe and slow-only. Space safe points with environmental change rate. Add a non-model guard where a missed safe point cannot be undone. Hand the expanded single agent to loop eval before a train job or a second agent.

Check. Each action class has a documented safe-point interval and, if irreversible, a non-model guard. The handoff list points at loop success, not module scores.

Fail. Open `lessons/06-interaction.md` cluster `summary-safe-point-density`. source-ids `summary-safe-point-density`, `summary-feeds-eval-and-evolution`.

## Open next

[Evaluating agents](evaluating-agents.md). Do not open a second lesson file to start.

## Reply

State what changed in observe or act, which timescale and paradigm were chosen, which steps were skipped and why, and what remains open.
