# Principles

One row per extracted principle. Lookup only. Do not paste this catalog into SKILL.md.

| Owning file | Name | Rule | Source heading |
| --- | --- | --- | --- |
| SKILL.md | Practice precedes naming | Implement the mechanism when the failure appears. Treat later industry names as labels. | Introduction {.unnumbered} |
| SKILL.md | Ceiling demand writes the harness | Derive harness work from long-horizon, high-cost tasks the model cannot cover alone. | Introduction {.unnumbered} |
| SKILL.md | No eval, no progress | Refuse to merge an alleged improvement that cannot be distinguished from luck. | Introduction {.unnumbered} |
| SKILL.md | Principles outlast models | Encode how the system observes and acts, not how one named model is prompted. | Introduction {.unnumbered} |
| SKILL.md | Agent is a triple | Require LLM, context, and tools. None is optional. | Introduction {.unnumbered} |
| SKILL.md | Demo-to-product is the harness | Close reliability gaps with context management, tool interfaces, constraints, verification, and correction. | Introduction {.unnumbered} |
| SKILL.md | Completion is judged | Do not accept a self-declared done on a long-horizon task. | Introduction {.unnumbered} |
| SKILL.md | Context is the ceiling | Treat the message list as the most critical construction surface. | Book Structure {.unnumbered} |
| SKILL.md | Split reasoning from inference | Use reasoning for stepwise thinking and inference for serving-time computation. | How to Read This Book {.unnumbered} |
| SKILL.md | Architecture over algorithm | Keep loops, stores, and evals as the payload when techniques change. | Prerequisites {.unnumbered} |
| playbooks/getting-started.md | Inside-boundary formula | Compose the agent as LLM plus context plus tools and keep the Environment outside that box. | Modern Agent = LLM + Context + Tools |
| playbooks/getting-started.md | Expand spaces first | With the model held fixed, enlarge observation and action spaces before requesting a stronger model. | Observation and Action Spaces: The Interface Between Model and World |
| playbooks/getting-started.md | General explore, specialized risk | Use general foundation tools for composition. Use specialized auditable tools for high-risk business operations. | Tools: The Agent's Action Interfaces |
| playbooks/getting-started.md | Endorse direction, pragmatic pace | Let models absorb harness layers over time. Keep harness code on the current reliability frontier. | Model as Agent: When the Model Itself Becomes the Product |
| playbooks/getting-started.md | Three update timescales | Adapt in context for this task, persist via artifacts across tasks, and train parameters only for skills rules cannot state. | Agent Learning Mechanisms: From Contextual Adaptation to Persistent Updates |
| playbooks/getting-started.md | Context equals prefix plus trajectory | Send a stable prefix and the full growing trajectory on every model call. | The ReAct Loop |
| playbooks/getting-started.md | Fluent is not finished | Score closed-loop completion against observations. Do not accept a polished unsupported answer. | Context: The Agent's Working Set |
| playbooks/getting-started.md | Information sufficiency | Make each decision from a working set that contains every fact that would change the action. | Harness Engineering: Competitiveness Beyond the Model |
| playbooks/getting-started.md | Clear interface | Give tools intuitive names, parameter examples, and explicit boundaries. | Harness Engineering: Competitiveness Beyond the Model |
| playbooks/getting-started.md | Fail-safe defaults | Leave capabilities off until they are explicitly enabled. | Harness Engineering: Competitiveness Beyond the Model |
| playbooks/getting-started.md | Input isolation | Verify on structured tool fields and environment state, never on free-form model text. | Harness Engineering: Competitiveness Beyond the Model |
| playbooks/getting-started.md | Hide unrecovered intermediates | Retry and roll back quietly. Surface a partial only after recovery is known to be impossible. | Harness Engineering: Competitiveness Beyond the Model |
| playbooks/getting-started.md | Keep it simple | Start with the simplest design and add layers only when a measured need appears. | Core Principles for Building Effective Agents |
| playbooks/getting-started.md | Keep it transparent | Show plans, logs, and the decision trajectory to operators and users who must trust the result. | Core Principles for Building Effective Agents |
| playbooks/getting-started.md | ACI poka-yoke | Design the agent-computer interface so the likely mistake cannot be expressed. | Core Principles for Building Effective Agents |
| playbooks/getting-started.md | Escalate complexity last | Prefer one call, then a workflow, then autonomy, and price the latency and cost of each step up. | Orchestration Patterns: Workflow vs. Autonomous |
| playbooks/getting-started.md | Bypass-hardness layering | Stack context, execution, and data guardrails so a lower layer still denies after an upper layer fails. | Types of Guardrails |
| playbooks/getting-started.md | Self-review is unreliable | Give judgment to a role that does not share the producer's context and that sees the artifact, not the rationale. | Design Patterns That Run Through the Book |
| playbooks/getting-started.md | One skeleton | Keep LLM plus context plus tools as the only book-wide skeleton. Use model plus harness as the production unfolding of the building part. | The Five Harness Elements and the "Building" Part |
| playbooks/context-engineering.md | Prefix stability | Never mutate a finalized system prompt or core tool list, including whitespace. | KV Cache-Friendly Context Design |
| playbooks/context-engineering.md | Append dynamics | Append clocks, live user state, and status at the tail or fetch them with a tool. | KV Cache-Friendly Context Design |
| playbooks/context-engineering.md | Official roles | Send structured API roles and let the server apply the chat template. | The Four Message Roles |
| playbooks/context-engineering.md | Context ceiling | Raise context quality before swapping models. | Context: The Ceiling of Agent Capability |
| playbooks/context-engineering.md | Rebuild c_t | Reconstruct sufficient context on every stateless call. | Context: The Ceiling of Agent Capability |
| playbooks/context-engineering.md | Harness executes | Let the model request tools and let the harness execute them. | Multi-Turn Interaction with Tool Calls: The Core Loop of an Agent |
| playbooks/context-engineering.md | Retrieval not aggregation | Precompute counts and other aggregates. Do not rely on one forward pass to tally the trace. | The Internal Mechanism of In-Context Learning: Retrieval, Not Reasoning |
| playbooks/context-engineering.md | Distill to the tail | Write implicit state as explicit tail facts in a code-owned status bar. | Agent Status Bar: Managing Trajectories with Meta-Information |
| playbooks/context-engineering.md | Isolation first | Keep bulky intermediates out of the main window with a sub-agent before paying to compress them. | Isolation Over Compression: Sub-Agent Context Isolation |
| playbooks/context-engineering.md | Instruction versus data | Tag untrusted observations and keep them in the tool role. | Prompt Injection: The Core Threat to Context Security |
| playbooks/context-engineering.md | SOP over piles | Organize the system prompt as staged procedures, not scattered rules. | Process-Driven vs. Rule Stacking: The "Organization" of the System Prompt |
| playbooks/context-engineering.md | Product-owned policy | Let product write executable rules. Let engineering encode them. | Translating Business Rules into Executable Instructions |
| playbooks/context-engineering.md | Progressive disclosure | Keep a short skill catalog always visible and load bodies on demand. | Skills: Composable Units of Domain Capability |
| playbooks/context-engineering.md | Cache as architecture | Place runtime variance after the cache boundary and byte-align inheriting sub-agents. | Caching as an Architectural Constraint |
| playbooks/context-engineering.md | Batch compress | Compress old tool bodies between calls in one batch near the window threshold. | Compression and KV Cache: Apparent Contradiction, Practical Complementarity |
| playbooks/context-engineering.md | Code-owned status | Compute the status bar in deterministic code. Never one-shot LLM batch-count. | Two Implementations of Status Updates and Their Cache Costs |
| playbooks/context-engineering.md | Keep-list | When compressing, keep decisions, constraints, failures, times, names, ids, and sources. | Design Principles for Compression Strategies |
| playbooks/memory-knowledge.md | Two scales one stack | Reuse retrieval, compression, conflict, and freshness machinery for user memory and the shared knowledge base. | User Memory and Knowledge Base |
| playbooks/memory-knowledge.md | Extract after the session | Write long-term memory in a dedicated pass that is selective, abstract, and structured. | User Memory System |
| playbooks/memory-knowledge.md | Three-level memory bar | Pass basic recall, multi-session retrieval, and proactive joins before calling memory assistant-grade. | Evaluating Memory Capabilities: A Three-Level Framework |
| playbooks/memory-knowledge.md | Log versus archive | Keep trajectories append-only and keep long-term memory a rewritten, tool-mediated archive. | The Hierarchical Structure of Memory |
| playbooks/memory-knowledge.md | Format follows criticality | Route scarce critical facts to rich cards or code and bulk facts to simple notes. | Four Storage Formats for User Memory |
| playbooks/memory-knowledge.md | Executable rules | Run counts, clashes, and constraints as functions over typed state. | Advanced Knowledge Representation: Executable Code |
| playbooks/memory-knowledge.md | Orthogonal taxonomies | Choose location, format, and cognitive type independently. | Cognitive Science Foundations of User Memory |
| playbooks/memory-knowledge.md | Resolve at the safer time | Prefer append-plus-retrieval-time ranking when write-time UPDATE or DELETE would erase history. | Memory Framework Case Studies |
| playbooks/memory-knowledge.md | Compress in three tiers | Score, cluster, then generalize. Do not only append. | Memory Compression and Organization Mechanisms |
| playbooks/memory-knowledge.md | Sanitize locally | Redact PII before logs leave the machine. | Privacy Protection: Log Sanitization |
| playbooks/memory-knowledge.md | Retrieve then generate | Ground answers in a closed candidate list from a store that can change after training. | RAG Basics: Building an Agent's Knowledge Acquisition Pipeline |
| playbooks/memory-knowledge.md | Chunk with a known wound | Split for embed quality and restore identity with prefixes later. | Document Chunking |
| playbooks/memory-knowledge.md | Hybrid then rerank | Run dense and sparse in parallel, fuse ranks, then cross-encode the pool. | Hybrid Retrieval: The Art of Having the Best of Both Worlds |
| playbooks/memory-knowledge.md | Index-time thinking | Precompute aggregates and boundary rules because attention will not. | Beyond Flat Text: Knowledge Organization and Retrieval |
| playbooks/memory-knowledge.md | Structure is a paid upgrade | Buy trees or graphs only for drill-down or multi-hop queries. | Structured Indexing: From Information Retrieval to Knowledge Modeling |
| playbooks/memory-knowledge.md | Files need a wiki | Progressive L0/L1/L2 loading works only with forced cross-links and index pages. | The Filesystem Paradigm: Organizing Knowledge with Directory Structures |
| playbooks/memory-knowledge.md | Knowledge as PRs | No model writes main or the live index. Heterogeneous tool-using review is mandatory. | Incremental Updates for User Memory and Knowledge Bases |
| playbooks/memory-knowledge.md | Qualify, do not newest-win | Keep conflicting claims under conditions or mark them unresolved. | Periodic Reorganization of User Memory and Knowledge Bases |
| playbooks/memory-knowledge.md | ACL at retrieve | Unauthorized chunks must never enter the prompt. | Periodic Reorganization of User Memory and Knowledge Bases |
| playbooks/memory-knowledge.md | Hits are data | Mark retrieved text as reference and block side effects without a separate grant. | Agentic RAG: A Paradigm Shift Toward Tool-Based Knowledge Retrieval |
| playbooks/memory-knowledge.md | Two-tier memory | Resident critical cards plus prefixed on-demand RAG enable proactive service. | RAG Technique: Contextual Retrieval |
| playbooks/memory-knowledge.md | Discover then review | Induce factors from data and require expert review of schema and bias. | Extracting Deep Knowledge from Datasets: From Information Retrieval to Knowledge Discovery |
| playbooks/tools.md | ACI over API wrap | Define a tool as an agent goal, not as one vendor endpoint. | Universal Principles of Tool Design |
| playbooks/tools.md | General by default | Prefer a general executor plus optional skill text unless security, platform hide, frequency, schema complexity, or a weak model requires a dedicated tool. | Forms of Capability Expression: Dedicated Tools, General Executors, and Skills |
| playbooks/tools.md | Form is not disclosure | Pick capability form and how many capabilities face the model as two independent decisions. | Tools |
| playbooks/tools.md | When plus cannot | Write when to call and what the tool refuses. Capability paraphrase is not enough. | The Art of Tool Description |
| playbooks/tools.md | Perceived world equals operated world | Do not silently rewrite or inject arguments. If a transform is required, declare it in the description and echo it in the result. | Fidelity of Parameter Passing |
| playbooks/tools.md | Descriptions are untrusted | Review third-party tool text as prompt injection, pin versions, isolate credentials, and namespace names against shadowing. | Tool Ecosystem: MCP and Skill Hubs |
| playbooks/tools.md | Skills outrank MCP on danger | Treat skill folders that run host code as more dangerous than schema-only MCP. Isolate them. | Tool Ecosystem: MCP and Skill Hubs |
| playbooks/tools.md | Three disclosure layers | Escalate from index-and-load, to gap-declared discovery, to skill catalog lookup as the lighter path. | What to Do When There Are Too Many Tools: Hierarchical Organization and Proactive Tool Discovery |
| playbooks/tools.md | Append then pin | Append a discovered schema once at the then-end of context and leave it there so the prefix cache survives. | Model-Native Proactive Tool Discovery |
| playbooks/tools.md | Fail fast, no clever fix | Reject illegal execution inputs. Do not sanitize them into a different action. | Execution Tools |
| playbooks/tools.md | Execute, validate, feedback | When a result has a cheap oracle, run that oracle in the same tool return. Skip this pattern when the check is another irreversible event. | Execution Tools |
| playbooks/tools.md | Read-only may fan out | Cache and parallelize perception. Serialize execution. | Perception Tools |
| playbooks/tools.md | Visible truncation | Announce omitted ranges and how to continue. Never clip in silence. | Perception Tools |
| playbooks/tools.md | Sidecar sees fields, not prose | Classify live calls from structured arguments only. | Execution Tools |
| playbooks/tools.md | Cognitive diversity for plans | Pre-approve irreversible plans with a similar-strength model from another family. | Execution Tools |
| playbooks/coding-agent.md | coding core | Architect open-ended agents around code execution plus a file system. | Coding Agent and Code Generation |
| playbooks/coding-agent.md | category coverage | Cover browse, read, modify, execute, and search before adding any specialized tool. | Coding as a Foundational Agent Capability |
| playbooks/coding-agent.md | files as hub | Keep memory, knowledge, and generated capability in inspectable, version-controlled files. | Case Study: From Manus to OpenClaw — The Coding Core of General-Purpose Agents |
| playbooks/coding-agent.md | verification decides done | Define completion as tests passing, never as code written. | The Overall Workflow of a Coding Agent |
| playbooks/coding-agent.md | constraints over guidance | Encode any rule a linter, schema, or pipeline can enforce instead of writing it as advice. | Harness Engineering in Practice for Coding Agents |
| playbooks/coding-agent.md | constrain the path | Block destructive methods even when they would produce a passing outcome. | Harness Engineering in Practice for Coding Agents |
| playbooks/coding-agent.md | recovery loop as unit | Handle errors at the granularity of the recovery loop and withhold intermediate failures. | Failure and Error Recovery |
| playbooks/coding-agent.md | every path has a ceiling | Cap every recovery path with a data-derived limit and a defined terminal action. | Failure and Error Recovery |
| playbooks/coding-agent.md | neutral trajectory | Store trajectories in a vendor-neutral format with portable text separated from credentials. | Failure and Error Recovery |
| playbooks/coding-agent.md | coarse to fine retrieval | Move from path and semantic search to exact matching to symbol tracing. | Search Tools in Coding Agents |
| playbooks/coding-agent.md | content matching over line counting | Prefer edit schemes anchored on file content rather than on numbers the model must count. | File Editing Tools in Coding Agents |
| playbooks/coding-agent.md | assume injection succeeds | Design so an injected agent still cannot complete a dangerous action. | Security for Coding Agents |
| playbooks/coding-agent.md | ground truth gatekeeping | Build the last line of defense on data the model cannot forge. | Code as a Constraint for Business Rules |
| playbooks/coding-agent.md | render before judging | Let an independent reviewer see the rendered artifact the generator cannot see. | Code-Driven Multimedia Generation |
| playbooks/coding-agent.md | keep the model off the data path | Have the model write the query and the view, and let the system move the data. | Code as Generative UI |
| playbooks/coding-agent.md | authorization below generation | Enforce permission constraints in a stable layer that generated code cannot rewrite or bypass. | Code as Generative UI |
| playbooks/coding-agent.md | adapt from examples | Generate a new agent by modifying a validated implementation rather than starting from scratch. | Code Creating Code: Agent Bootstrapping |
| playbooks/interaction.md | Expand three axes | After content (context, memory, tools, code), expand modality and timing. | Two Axes: Modality and Timing |
| playbooks/interaction.md | World pushes | Wake from a pushed event stream. Do not poll as the primary sense. | Why Asynchrony is Needed |
| playbooks/interaction.md | Safe-point consume | Apply events and cancel only at defined safe points, or by manufacturing one for urgency. | Event Handling Mechanism |
| playbooks/interaction.md | Typed then semantic route | Route typed events with rules. Classify only ambiguous wording, from structured fields. | Event Handling Mechanism |
| playbooks/interaction.md | Never fake a tool result | Use an explicit unfinished placeholder. Never write a success the tool did not return. | Event Handling Mechanism |
| playbooks/interaction.md | Virtual identity default | Act under a declared agent identity and sandbox unless the holder must appear. | Virtual Identity and Isolated Execution Environment |
| playbooks/interaction.md | Initiate not complete | Name long tools as start plus later events, not as call-equals-done. | Engineering Implementation: How to Make Synchronous Models Support Asynchronous Interruptions |
| playbooks/interaction.md | Cover the whole batch | Number flushed events and demand a response to every type count. | Engineering Implementation: How to Make Synchronous Models Support Asynchronous Interruptions |
| playbooks/interaction.md | Paradigm is a trade | Pick cascade, Omni, or full-duplex from latency, cost, and observability, not from novelty. | Interaction timing: from cascaded to full-duplex |
| playbooks/interaction.md | Two end-to-end axes | Name speech-path fusion and cognitive fast/slow separately. They combine. | The trade-off between separated fast/slow thinking and end-to-end reasoning |
| playbooks/interaction.md | Reconfirm after every act | A new frame or verify step is the truth. Model speech is not completion. | Computer Use: GUI Automation Agents |
| playbooks/interaction.md | Closed-set then coordinates | Click ids when structure or marks exist. Keep scaled coordinates as fallback. | Visual Grounding |
| playbooks/interaction.md | Predict checkable state | World models forecast task-checkable diffs, not photoreal frames, and never replace acceptance. | World Models for Computer Use |
| playbooks/interaction.md | Skills not joints | High-level models pick bounded skills. Executors and e-stop own motion. | The Basic Structure of Robot Control |
| playbooks/interaction.md | Chunk to hide infer only | Chunk length meets inference time. Abort the rest when the scene jumps. | VLA Control |
| playbooks/interaction.md | Fast path is reversible | Fast thinking may not call irreversible tools. | Thought Questions |
| playbooks/interaction.md | Safe-point density | Match safe-point spacing to change rate. Add non-model guards from irreversibility. | Chapter Summary |
| playbooks/evaluating-agents.md | Evaluate the pair | Score the model and the harness as one unit. | Evaluating Agents |
| playbooks/evaluating-agents.md | Swap versus ablate | Swap models to locate the bottleneck. Disable one harness part to locate the part. | Evaluating Agents |
| playbooks/evaluating-agents.md | One variable | Change one factor per comparative run. | Evaluating Agents |
| playbooks/evaluating-agents.md | Ceiling versus reliability | Use Pass@k or Best@k for possibility. Use Pass^k with vetoes for operations that cannot slip. | Business Reliability: Focus on Pass^k |
| playbooks/evaluating-agents.md | Five components | Require dataset, resettable state, atomic tools, rubric, and protocol or do not call it a repeatable eval. | The Five Components |
| playbooks/evaluating-agents.md | Deterministic first | Keep every machine-checkable fact as an assertion. Reserve judges for the rest. | Automated Evaluation Methods |
| playbooks/evaluating-agents.md | First error | Attribute the earliest step that sent the task off course. | Failure Attribution: Locate the First Error in a Trajectory |
| playbooks/evaluating-agents.md | Rules then LLM | Pre-filter cheap, checkable failure classes before calling a localizer model. | Failure Attribution: Locate the First Error in a Trajectory |
| playbooks/evaluating-agents.md | Mechanism is not the target | Gate A/B tests on the goal metric, not on the knob being turned. | A/B Testing Methodology: Distinguishing Mechanism from Goal |
| playbooks/evaluating-agents.md | Check the instrument | When scores drop, inspect the eval system before the agent. | From Benchmark Reports to System Improvements |
| playbooks/evaluating-agents.md | Do not add savings | Measure combined cost levers. Never sum isolated percentages. | Cost Analysis of Agent Systems |
| playbooks/evaluating-agents.md | Slice is not the system | Let a small slice authorize only the next larger test. | Continuous Iteration: From First Improvement to System Evolution |
| playbooks/evaluating-agents.md | Obtain is not apply | Test fetching a fact and using it on the current decision as two skills. | Chapter Summary |
| playbooks/evaluating-agents.md | Privacy in the type system | Collect only values that the compiler can prove are safe to measure. | Privacy-Aware Analytics as an Evaluation Foundation |
| playbooks/post-training.md | Data and environment over algorithms | Finish the corpus, the demonstrations, and the env-plus-reward loop before swapping PPO for GRPO. | Model Post-Training |
| playbooks/post-training.md | Foundation then protocol then policy | Diagnose the gap as knowledge, interface, or decision before naming a trainer. | When to Choose Mid-training, SFT, and RL |
| playbooks/post-training.md | RL amplifies existing mass | Use RL only when pass@k is nonzero and a group already shows reward variance. | When to Repair the Foundation Before Applying SFT or RL |
| playbooks/post-training.md | Form first | Stop SFT when outputs parse and OOD stops rising. Do not wait for train loss to finish falling. | When to Choose Mid-training, SFT, and RL |
| playbooks/post-training.md | SFT copies. RL searches. | Choose SFT to raise labeled-token probability. Choose RL to raise expected reward on self-generated traces. | The Essential Difference Between SFT and RL (The Most Important Table in This Chapter) |
| playbooks/post-training.md | Reward the outcome. Penalize the path. | Keep a verifiable outcome channel and add deterministic path penalties for machine-decidable violations. | A Correct Outcome Is Not Enough: Path Constraints and RLVP |
| playbooks/post-training.md | Hidden tests decide done | Score completion on isolated real state the policy cannot author. | When the Reward Is Given: Outcome or Process |
| playbooks/post-training.md | Student visits. Teacher labels. | For dense cheap updates, roll out the student and KL-align to a teacher on those prefixes. | On-Policy Distillation: Making One Rollout Produce Dense Supervision |
| playbooks/post-training.md | On-policy is a numeric fact | Treat sampler and trainer logprob disagreement as off-policy data even after a weight sync. | Why Training Is Sensitive to Sampler/Trainer Numerical Mismatch |
| playbooks/post-training.md | Reuse environments, not questions | Share generators and verifiers. Hold out whole template families and headline the OOD score. | Environments, Task Distribution, and Evaluation Isolation |
| playbooks/post-training.md | External symbols before weights | Place facts in retrieval, principles in prompts, hard rules in programs, and only inexpressible high-volume skills in parameters. | Post-Training Practical Takeaways |
| playbooks/post-training.md | Prior then environment then algorithm | Buy pretrained priors and a faithful env before inventing an optimizer. | Two Action Representations: Classic RL Settings and Variable-Length LLM Policies |
| playbooks/continual-evolution.md | Preserve is not learn | Compare, generalize, and validate before changing later behavior. | Continual Evolution of Agents |
| playbooks/continual-evolution.md | Evaluate first | Run outcome and process verifiers before any lasting summary. | Deriving Learning Signals from Operational Trajectories |
| playbooks/continual-evolution.md | Route by representation | Choose knowledge, instruction, program, or parameters from how the capability is expressed. | Four Methods for Continual Agent Evolution |
| playbooks/continual-evolution.md | Routing is a proposal | Hold every routed change as a candidate until an independent gate passes. | Four Methods for Continual Agent Evolution |
| playbooks/continual-evolution.md | Record then organize | Append immutable evidence online. Induce formal artifacts offline. | Consolidating Experience into Knowledge |
| playbooks/continual-evolution.md | Reflection is not evidence | Promote verbal lessons only after environmental labels, multi-run support, and transfer. | Consolidating Experience into Knowledge |
| playbooks/continual-evolution.md | Minimal attributed diff | Change prompts and skills as small provenance-bearing diffs tested on boundary and retention sets. | Encoding Experience as Instructions |
| playbooks/continual-evolution.md | Observed is not ought | Reject induced rules that copy a frequent failure terminal. | Example 1: Turning the Escalation Boundary into Rules |
| playbooks/continual-evolution.md | Skill asks, harness vetoes | Keep interview and spec assembly in skills. Keep non-bypassable stops in code. | Example 2: Requirement Clarification Skill—From Direct Execution to Confirm First |
| playbooks/continual-evolution.md | Action success is not task success | Require before-action, after-action, and final-state checks plus independent replay. | Encoding Experience as Programs |
| playbooks/continual-evolution.md | Host composability caps evolution | Do not scale self-modification beyond reversible effects and a verifiable dependency graph. | Case: DeepSeek Harness—Self-Evolution Where Everything Is a Plugin |
| playbooks/continual-evolution.md | Hard rules stay in code | Keep long-stable authorization and money rules in server code, not only in weights. | Encoding Experience in Parameters |
| playbooks/continual-evolution.md | Local first | Edit one local artifact before searching workflows, harnesses, or optimizers. | From Updating Artifacts to Updating the “Update Method” |
| playbooks/continual-evolution.md | Dual loop | Serve and record online. Aggregate, propose, and release offline. | Building a Continual-Evolution Closed Loop for Long-Term Operation |
| playbooks/continual-evolution.md | Update is not benefit | Score candidate quality, activation, and adherence as separate metrics. | Building a Continual-Evolution Closed Loop for Long-Term Operation |
| playbooks/continual-evolution.md | Done is not progress | Do not promote open-ended work on pipeline completion alone. | The Boundary of a Verifiable Loop: When “Done” Does Not Mean “Progress” |
| playbooks/continual-evolution.md | Evidence is not instruction | Keep untrusted text and its summaries out of executable skills and prompts. | Safety Boundaries for Continual Evolution |
| playbooks/continual-evolution.md | Frozen approval root | Deny the agent writes to validators, thresholds, audit logs, and stable backups. | Safety Boundaries for Continual Evolution |
| playbooks/continual-evolution.md | Sleep consolidates | Merge, conflict-mark, prune, and reindex in a background cycle with snapshots and rollback. | Sleep Learning: Consolidation, Forgetting, and Capability Maintenance |
| playbooks/continual-evolution.md | Guarantee from an untouchable layer | Pin bases, evidence logs, and gates on surfaces the modifier cannot edit. | Sleep Learning: Consolidation, Forgetting, and Capability Maintenance |
| playbooks/multi-agent.md | information gain first | Add an agent only when it brings information the producing agent could not have had. | When Is Multi-Agent Truly Better Than a Single Agent? |
| playbooks/multi-agent.md | two axes before code | Fix context sharing and topology before writing orchestration logic. | A Classification Framework for Multi-Agent Collaboration |
| playbooks/multi-agent.md | isolate by default | Make every shared area an explicit declaration and keep everything else private. | The File System from an Agent's Perspective |
| playbooks/multi-agent.md | paths not payloads | Exchange artifact references and let the recipient read what it needs. | The File System from an Agent's Perspective |
| playbooks/multi-agent.md | the model cannot approve its own done | Route every completion through a verifier the executing agent cannot modify. | Loop Engineering |
| playbooks/multi-agent.md | diversity is designed | Vary model, context, tools, or evidence before treating two agents as independent. | Failure Mode Three: Homogeneous Convergence |
| playbooks/multi-agent.md | guidance is not a boundary | Enforce permissions and limits in harness code, never in instruction text. | Multi-Agent Collaboration with Shared Context |
| playbooks/multi-agent.md | expect Byzantine agents | Assume agents keep running while producing plausible wrong output, and guard with deterministic checks. | Failure Modes of Multi-Agent Collaboration |
| playbooks/multi-agent.md | every loop is bounded | Give each loop a budget, a cancellation path, and a stop condition. | Failure Mode Five: Runaway Loops |
| playbooks/multi-agent.md | opaque across trust boundaries | Exchange only tasks and artifacts with parties you cannot inspect. | Cross-Organization Collaboration: The A2A Protocol |
| playbooks/multi-agent.md | understanding is not delegable | Keep a human able to explain the architecture without reading agent output. | Failure Mode Six: Comprehension Debt and Cognitive Surrender |
| SKILL.md | Formula spine | Place every capability in LLM, Context, or Tools before adding architecture. | Afterword: Back to Agent = LLM + Context + Tools {.unnumbered} |
| SKILL.md | Coupled arcs | Do not run build, evolution, and collaboration as independent shelves. | Afterword: Back to Agent = LLM + Context + Tools {.unnumbered} |
| SKILL.md | Convergence prerequisites | Refuse long-horizon improvement without stores, editable programs, and an eval gate. | Afterword: Back to Agent = LLM + Context + Tools {.unnumbered} |
| SKILL.md | Clouds persist | Do not treat a single model upgrade as clearing real-time interaction or post-deploy learning. | Two Clouds {.unnumbered} |
| SKILL.md | Orthogonal axes | Split fast presence and slow depth when one model cannot hold both. | Two Clouds {.unnumbered} |
| SKILL.md | Hypothesis fork | Use train-once plus data for small-world general skills, and post-deploy carriers for big-world particulars. | Two Clouds {.unnumbered} |
| SKILL.md | Adaptation over recall | Optimize the ability to learn from new outcomes, not only to memorize a corpus. | Two Clouds {.unnumbered} |
| SKILL.md | Harness as weakness log | Annotate fallbacks with the model failure they hide and retire them after internalization. | The Co-Evolution of Models and Agents {.unnumbered} |
| SKILL.md | Layerwise eating | Let models absorb the harness one layer at a time and never expect the process to finish. | The Co-Evolution of Models and Agents {.unnumbered} |
| SKILL.md | Flywheel mesh | Close users to patches to training, and colocate both ends when possible. | The Co-Evolution of Models and Agents {.unnumbered} |
| SKILL.md | Harness buys time | Spend wrapper leverage on barriers a future model cannot eat. | The Co-Evolution of Models and Agents {.unnumbered} |
| SKILL.md | Three durable questions | Keep asking what the system sees, what it can do, and how a run is verified. | The Co-Evolution of Models and Agents {.unnumbered} |

_186 principles._
