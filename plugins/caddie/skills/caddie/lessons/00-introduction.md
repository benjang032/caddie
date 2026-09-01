# Introduction

Curriculum notes for the skill root. Runtime matching stays on `SKILL.md`. This file is depth, not a playbook.

## Terms

- **Agent.** LLM plus context plus tools. The system that chooses and acts.
- **Context.** Everything perceivable at a decision, including tool definitions.
- **Tools.** The action space the model can invoke.
- **Harness.** Context management, tool interfaces, constraints, verification, and correction.
- **Skill.** On-demand procedure text loaded to bound standing prefix growth.
- **Loop engineering.** Proposer-reviewer control that blocks a self-declared done.
- **Policy / observation / action.** The same triple under RL names.
- **ReAct.** Think, act, observe, with the observation written back into context.

## What this is for

This chapter orients the rest of the skill. An agent is the formula triple, and durable architecture comes from ceiling-stressing work plus evaluation, not from waiting for industry names or a better backbone. Match work on the `SKILL.md` route table first. Open these notes only when a cluster must be taught or a check failed.

## Core model

Name the formula shape before writing agent logic. Agent equals LLM plus Context plus Tools. The production rewrite is Model plus Harness. Environment sits outside. Tool schemas belong in the context column and in the tools column. Lookup lives in `references/data-shapes.md` under Formula.

## Clusters

### `principle-driven-agent-design`

**When.** A new sketch is justified only by one successful run or by copying a popular stack, or the next quarter plan is a model swap.

**Rule.** Record the trade-off each major choice accepts and rejects before treating the design as finished. Spend the next increment on deployment architecture. Plan for tool skill moving into weights and for named models turning over on a month scale. Keep message, tool, and eval interfaces stable across a swap.

**Check.** Open the architecture note. Every major component has a written trade-off pair. Flag any component that names only a vendor or model. A quarter plan whose only agent milestone is a model-id swap fails.

source-ids: principle-driven-agent-design, dictate-survey-discuss-revise, deployment-over-backbone, weights-plus-iteration-pace

### `practice-before-naming`

**When.** A new term such as Skill, harness, or loop engineering appears in a review, or a backlog item waits for an industry phrase to trend.

**Rule.** Treat the name as a label for work already done in the field, not as a permission slip to start. Schedule the mechanism as soon as the failure is observed in production or rehearsal. Keep the internal name if it is clearer than the fashion name.

**Check.** Find the last architecture ticket titled after a blog-post term. Confirm it cites a product failure that predated the term. Any deferred ticket whose next step is wait-until-the-industry-names-this fails.

source-ids: practice-before-naming, do-not-wait-for-buzzwords

### `extreme-ceiling-demand`

**When.** Deciding whether to invest in harnesses, status, or review loops.

**Rule.** Derive harness requirements from a real business that stresses the capability ceiling. Long, multi-party, money-sensitive tasks expose gaps the model cannot cover alone. A modest chat never generates that pressure.

**Check.** Name one production task that can last hours and lose money if a number is wrong. If none exists, the harness backlog will stay empty for the wrong reason.

source-ids: extreme-ceiling-demand

### `eval-or-no-progress`

**When.** A prompt, tool, or model swap is about to be merged as an improvement.

**Rule.** Treat a change as progress only when an evaluation can tell design from luck. The local rule is already binding. The full pair-eval method is `evaluate-model-plus-harness`, reached from the `SKILL.md` route table.

**Check.** Open the last merged agent change. Require an eval log, benchmark row, or failing-then-passing check in the same change. Absence fails.

source-ids: eval-or-no-progress

### `principles-outlast-models`

**When.** Docs, prompts, or wrappers treat a current model name as the architecture, or a new technique wave arrives.

**Rule.** Encode how the system observes and acts in the world so the description survives a model swap. Keep loops, stores, and evals as the payload. Keep model IDs in config, not in the conceptual diagram. A missing math course is not a reason to abandon the architectural payload.

**Check.** Open the system diagram. If removing the model brand name makes the diagram empty, the design is model-usage, not a pattern. Architecture notes must state the triple, eval, and harness without depending on one algorithm name.

source-ids: principles-outlast-models, architecture-over-algorithm

### `agent-llm-context-tools`

**When.** Decomposing or reviewing any agent, or translating the same system for training talk.

**Rule.** Require all three parts. Agent equals LLM plus Context plus Tools. Map LLM to thinking and to policy. Map context to everything perceivable, including which tools exist, and to observation space. Map tools to action and to action space. The metaphor and the RL wording are not a second machine. The shorter orientation lives here. The boundary placement check is `agent-formula-inside-boundary`.

**Check.** Fill a three-column inventory for the live agent. Any empty column fails. Tool schemas must appear in the context column as well as the tools column. Compare a production context dump to the training observation spec. Fields that exist in only one place fail.

source-ids: agent-llm-context-tools, brain-eyes-hands, policy-obs-action

### `harness-closes-demo-gap`

**When.** A prototype chat works and a production task does not, or tool calls flake, invent results, or skip a standing instruction.

**Rule.** Explain the demo-to-product gap as missing context management, tool interfaces, constraints, verification, and correction. Buying a stronger model does not install those pieces. Wrap unstable calls, hallucinations, dangerous operations, unauthorized operations, and ignored instructions.

**Check.** Write a one-page harness inventory. If constraints, verification, and correction are all prompt-only on a path that can spend money or change accounts, the product is still a demo. For each of the five failure classes, a class with only a prompt sentence fails.

source-ids: harness-closes-demo-gap, harness-unstable-and-unsafe

### `four-layer-curriculum`

**When.** Planning what to implement first, or someone asks which chapter to read.

**Rule.** Follow the four-level order. Fundamentals, then construction, then evaluation and evolution, then multi-agent work. Block training without eval. Block multi-agent without a single-agent eval. When someone says the agent learned, name which store changed. In-task context, a durable artifact, or training-time parameters. Chapter previews and reading paths are not a second map. Match the concern on the `SKILL.md` route table and open one playbook. Never open two lesson files to start.

**Check.** Locate the project on the four-level map. If collaboration or training is in flight and evaluation is absent, the order fails. If this file is being used as a chapter tour, stop and return to the route table.

source-ids: four-layer-curriculum, ch1-three-layers-react-orchestration, three-update-timescales, ch2-context-is-messages, ch3-session-spanning-memory, ch4-five-tool-kinds, ch5-coding-agent-foundation, ch6-two-axes-five-primitives, ch7-eval-then-improve, ch8-sft-rl-data-first, ch9-four-carriers, ch10-context-times-structure, builder-path-1-through-9, short-path-1-and-2, trainer-path-7-and-8, first-experiment-per-chapter, difficulty-bands-by-chapter, starter-builder-maintainer-read, required-python-llm-git-json, study-a-live-coding-agent, chapter-specific-recommended-prereqs, star-difficulty-on-experiments, debug-to-form-intuition

### `proposer-reviewer-completion`

**When.** A long-horizon task is marked done by the same loop that performed the work.

**Rule.** Split propose from review so completion is a judged claim. Keep a written success contract. The worker proposes done plus evidence. A reviewer accepts, rejects, or requests another round against that contract.

**Check.** Inspect a finished trajectory. The terminal state must include a review accept against a success contract, not only an assistant sentence that claims completion.

source-ids: proposer-reviewer-completion

### `status-bar-environment`

**When.** The agent lacks current time, working directory, or task-status awareness.

**Rule.** Inject a compact status bar that states environment, user time, and current work status. Keep the format fixed so the standing prefix remains cache-friendly. Refresh time, workspace id, and task phase each turn or each cheap interval.

**Check.** Capture one model input. A status block with time and work state must be present and current relative to the wall clock of that step.

source-ids: status-bar-environment

### `cli-bounds-tool-lists`

**When.** The JSON tool catalog grows with every new API, or a general-purpose product is being designed.

**Rule.** Expose a general command-line or code-execution tool so new capabilities do not each require a new schema. Default a general agent to generated code plus a persistent file system. Add a typed tool only when the primitive path is unsafe or too slow to discover. If generated code may change tools or prompts, name a review or eval gate, or an explicit ban.

**Check.** Count first-class tool schemas. If the count tracks product features one-for-one and no general execute path exists, the list is unbounded. Confirm a writable file tree exists and that at least one core path is write code, run it, read the output file.

source-ids: cli-bounds-tool-lists, codegen-plus-filesystem, self-modifying-agent-mission

### `dynamic-prompt-loading`

**When.** The system prompt or skill dump grows every time a new capability is added.

**Rule.** Load prompt fragments when the task needs them instead of stuffing every skill into the standing prefix. Split standing rules from task-specific procedures. Index procedures by name and trigger.

**Check.** Measure standing system-prompt tokens. If adding a skill requires editing the always-on prefix rather than adding an indexed fragment, the design fails.

source-ids: dynamic-prompt-loading

## Failure diagnostics

| Symptom | Open cluster |
| --- | --- |
| Stack copied from one demo | `principle-driven-agent-design` |
| Work waits for a blog term | `practice-before-naming` |
| Harness backlog is empty | `extreme-ceiling-demand` |
| Merge has no eval artifact | `eval-or-no-progress` |
| Diagram is a model-name changelog | `principles-outlast-models` |
| Empty column on the triple | `agent-llm-context-tools` |
| Money path is prompt-only rails | `harness-closes-demo-gap` |
| Training or multi-agent with no eval | `four-layer-curriculum` |
| Done is an assistant sentence | `proposer-reviewer-completion` |
| Wrong cwd or stale date | `status-bar-environment` |
| Tool count tracks features | `cli-bounds-tool-lists` |
| Always-on prefix grows with every skill | `dynamic-prompt-loading` |

## Drills

### `00-introduction-q1`

A new industry name is trending. The team has not felt the named pain and wants to wait. How should work be scheduled, and what two inputs replace waiting?

Schedule from the observed failure, not from the name. Names arrive after leading systems have shipped the mechanism. The first input is a real business that stresses the capability ceiling long enough and at high enough cost that the model alone cannot cover the gaps. That pressure writes harness requirements. The second input is an evaluation that can tell a real gain from luck. A team with only toy tasks and no eval will neither need nor notice the pattern.

### `00-introduction-q2`

Why must an agent be specified as model plus context plus tools, and why do brain, eyes, and hands, and policy, observation, and action, not add a different machine?

The model chooses. Context is the observation. Tools are the actions. Drop tools and the system cannot act. Drop context design and it cannot see the environment, history, or which tools exist. Drop the model and the rest is a script. The metaphor and the RL wording name the same triple. Eyes include tool definitions, so a huge tool list is both an action-space and an observation-space problem.

### `00-introduction-q3`

A teammate says the last chat shows the agent learned. What three stores could have changed, and why does the distinction matter?

In-task context changed, a durable artifact changed, or parameters changed in a training cycle. A correction that lives only in the current message list vanishes in a new chat. A document, skill, or harness change can load next time. A weight change requires an eval-backed training loop. Calling all three learning hides whether the next session will see the fix.

## Depends-on

`SKILL.md` Start, Formula, and Route. No prior lesson file.

## Needed-by

Later lesson files after a playbook names a cluster. Do not start by opening two lesson files. Chapter depth after this file still goes through the route table.

## Open tensions

- `weights-plus-iteration-pace` leaves two model-layer vectors open. In-weight tool skill versus month-scale replacement. Interfaces must survive both.
- `eval-or-no-progress` is binding here. The full pair-eval method is `evaluate-model-plus-harness`.
- `self-modifying-agent-mission` leaves scope open. Generated code that changes tools or prompts needs a review or eval gate, or an explicit ban.
- `three-update-timescales` is easy to collapse in speech. A chat correction is not a weight update.
