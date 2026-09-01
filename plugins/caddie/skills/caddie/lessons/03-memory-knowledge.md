# User Memory and Knowledge Base

Terms. User memory is persistent user-keyed facts. Knowledge base is a shared, ACL-scoped store. Trajectory is the append-only run log. Working memory is the filtered window. RAG retrieves then generates. RRF fuses ranks. Two-tier memory is resident cards plus on-demand prefixed RAG. Proposer-reviewer is the knowledge PR pair.

## What this is for

Persistent agents need a user-keyed archive and a tenant-scoped knowledge plane that retrieve, conflict-check, and update like a reviewed codebase. A growing prompt is not a store. This chapter is proposal stage for experience write-back. Later evolution reuses the same evidence, review, and index rules.

## Core model

Data shape. User-keyed archive plus tenant-scoped shared knowledge plane. Raw events stay append-only. The long-term archive is a rewritten, tool-mediated view. Serving indexes are derivatives of a merged tree. Unauthorized or expired rows never enter context.

## Clusters

### `two-scale-memory-and-kb`

When persistence must survive a conversation.
Rule. Split per-user memory from the shared knowledge base and reuse one retrieval, compression, conflict, and freshness stack.
Check. Both stores exist. Both attach source, time, and conflict metadata.
source-ids: two-scale-memory-and-kb, shared-conflict-stale-miss, memory-lifecycle-read-extract-verify

### `post-session-dedicated-extract`

When a session has ended and personalization must survive the next one.
Rule. Keep the live transcript in the trajectory. Run a separate extractor after the session. Accept a write only when it is selective, abstracted beyond the turn, and stored in a retrievable field.
Check. After a fixture session the memory file holds preferences and identifiers and omits ephemeral tool chatter.
source-ids: post-session-dedicated-extract, extraction-three-invariants, memobase-buffer-extract, memory-lifecycle-read-extract-verify

### `eight-capability-yardstick`

When calling a memory design assistant-grade.
Rule. Pass Level-1 exact recall, Level-2 retrieve-all-then-ask, and Level-3 proactive joins. Hide raw transcripts from the answerer. Tag the suite with identity, preference, topic switch, update, multi-session, cross-fragment, temporal, and conflict.
Check. The answerer prompt contains no session text. Level-1 returns the stored identifier. A two-vehicle fixture mentions both or asks which. A travel-plus-passport fixture warns about expiry without being asked.
source-ids: eight-capability-yardstick, level-1-basic-recall, level-2-multi-session, level-3-proactive-service, memory-eval-without-transcript

### `trajectory-is-append-only`

When recording what happened versus what is believed.
Rule. Append user, model, and tool events and never rewrite them. Summarize only the model-facing window. Rewrite the long-term archive only through memory tools. Keep task-stage enums in a business-state slot, not in preference notes. Working memory is the filtered, activated subset.
Check. A mutate-history test is rejected. After compaction the original events still exist. A cross-session answer comes from the archive as a tool call. A stage change does not rewrite preference notes.
source-ids: three-storage-questions, trajectory-is-append-only, runtime-context-may-summarize, long-term-memory-is-rewritten-archive, business-state-is-task-stage, working-memory-loads-from-ltm, working-memory-is-filtered-subset

### `hybrid-format-by-criticality`

When a production agent stores both scarce facts and chatter.
Rule. Use advanced cards (person, relationship, time, backstory) for critical low-volume facts. Use simple notes for high-volume non-critical facts. Use JSON paths when one field must change without rewriting siblings. Do not pick one format for the whole agent.
Check. A mixed fixture writes passport and relationships as cards and a weather aside as a simple note. Patching `work.position.title` leaves `work.company.name` unchanged.
source-ids: simple-notes-lose-joins, enhanced-notes-keep-narrative, json-cards-partial-updates, advanced-json-cards-disambiguate, hybrid-format-by-criticality

### `deterministic-rule-functions`

When recall is not enough and the model is doing counts or constraint math in prose.
Rule. Store typed state and write aggregation, clash, and validity rules as functions. Append facts to a write-ahead log and rebuild checkpoints from that log. Return a typed count from the function, not from a model recount.
Check. An international trip plus a passport under 180 days emits an alert before any model call. Deleting the checkpoint and rebuilding reproduces the same fields.
source-ids: user-as-code-shared-medium, wal-plus-checkpoint, deterministic-rule-functions, typed-count-is-deterministic

### `three-classifications-orthogonal`

When a review asks which memory taxonomy is the one.
Rule. Treat location, format, and cognitive type as independent axes. Classify long-term records as episodic, semantic, or procedural and retrieve with type-appropriate keys.
Check. The architecture note lists at least one filled triple such as long-term / simple-notes / semantic. A booking fixture writes an episodic record and any distilled preference separately.
source-ids: three-classifications-orthogonal, episodic-semantic-procedural, three-storage-questions

### `mem0-v3-append-and-retrieve`

When a new fact may contradict an existing row and history still matters.
Rule. Prefer a single ADD with dated rows side by side, then fuse semantic, keyword, entity, and time on read. Use write-time ADD, UPDATE, DELETE, or NOOP only when the store must stay singular. Never DELETE the only copy of a legal or medical value. Keep profile slots for stable attributes and a timeline for last-discussed questions.
Check. After two address facts both rows exist with timestamps and "where do I live" ranks the later city first. A delete path can still read the prior value from evidence.
source-ids: mem0-v2-write-time-decide, mem0-v2-irreversible-loss, mem0-v3-append-and-retrieve, memobase-profile-plus-events, reference-arch-typed-stores

### `importance-score-four-factors`

When the store is growing and retrieval drowns in near-duplicates.
Rule. Score importance from access frequency, time decay, emotional intensity, and uniqueness. Cluster similar notes, write one summary, and move originals to cold storage. Abstract recurring episodes into a semantic trait or procedural rule and keep episodes as evidence.
Check. A unique allergy stays hot. Duplicate weather notes become one summary. After N shopping fixtures a distilled preference points at source episodes.
source-ids: importance-score-four-factors, cluster-then-summarize, generalize-episodes-to-rules

### `sanitize-logs-on-device`

When traces may contain identifiers, addresses, or passwords.
Rule. Redact on a local model or hybrid filter before any outbound hop. Run regex first on structured patterns, then a schema-constrained model on the remainder. Record type, span, and confidence.
Check. A password sentence is redacted before outbound HTTP. A card number is caught at the regex stage. A prose password still emits a typed span.
source-ids: sanitize-logs-on-device, hybrid-pii-regex-then-llm

### `rag-retrieve-inject-generate`

When implementing the default non-agentic knowledge loop. Listing-leak headings from the refund snippet collapse here.
Rule. Search first. Materialize a bounded candidate list. Close that list. Generate only from those fragments plus the question. Store policy chunks apart from procedure chunks. Change a document, reindex, and answer from the new rule without a retrain. Require hit-rate at k before calling the stack done.
Check. A refund trace shows search before generate. The generator input hash matches the logged candidate ids. Empty hits refuse a window and a click path.
source-ids: rag-updates-beat-training-cutoff, rag-retrieve-inject-generate, retriever-returns-open-list, policy-chunk-is-a-hit, procedure-chunk-is-a-hit, candidate-list-is-closed, generator-must-use-hits, kb-pipeline-accepted-on-metrics

### `chunk-to-protect-embedding`

When a source is longer than the embedder or mixes topics.
Rule. Split before embed. Default to the largest natural boundary that still fits, then smaller boundaries. Use fixed size with 50 to 100 token overlap only when structure is missing. Start in the 256 to 1024 token band with 10 to 20 percent overlap. Record that chunking severs company, report, and time, and plan a later prefix.
Check. A two-H2 Markdown fixture does not cross headings unless a section exceeds the cap. Config records size, overlap, and the metric that last justified them. A bare growth-rate chunk fails a self-containedness lint and still carries a parent doc id.
source-ids: chunk-to-protect-embedding, fixed-size-with-overlap, recursive-structure-default, semantic-cut-at-cliffs, chunk-size-band, chunking-loses-source-context

### `run-both-engines`

When queries mix nicknames, codes, and paraphrases.
Rule. Issue the same query to dense and sparse at once. Fuse with RRF as the sum of 1/(k + rank). Rerank the fused pool with a cross-encoder. Encode query and document separately for retrieve. Concatenate them for rerank. Use ANN at production cardinality. Measure hit-rate, MRR, and nDCG. Treat operational recall@k as hit-rate.
Check. A production trace shows two retriever id lists. Fused output is not a raw BM25-plus-cosine sum. A unique error code ranks on sparse. A kitty-versus-cat fixture fails sparse-only and passes hybrid.
source-ids: dense-vectors-encode-nearness, cosine-is-direction, word2vec-is-static, context-aware-embeddings, ann-not-brute-force, annoy-vs-hnsw, sparse-is-exact-bow, tfidf-then-bm25, inverted-index-required, sparse-misses-synonyms, run-both-engines, fuse-ranks-with-rrf, rerank-after-fusion, bi-vs-cross-encoder, measure-hit-rate-mrr-ndcg

### `index-time-precompute-aggregates`

When a question needs a ratio, a boundary, or a rule over many records.
Rule. Write and index a summary of the full population. Distill who is in, who is out, and the negation. Extract, abstract, and structure at index time. Attention is not a summarizer.
Check. A 90/10 population fixture retrieves a summary card that matches the full set. A nurse-eligibility fixture retrieves a rule card that mentions nurses. The index pipeline lists an extraction or summary job beside the embed job.
source-ids: flat-chunks-lose-structure, index-time-precompute-aggregates, distill-boundary-rules, attention-is-not-a-summarizer

### `when-to-pay-for-structure`

When deciding whether hybrid search is enough.
Rule. Keep dense plus sparse plus rerank for fragment finding. Buy a RAPTOR tree for summary-to-leaf travel. Buy a graph for relation chains and same-name split. Keep prose as source of truth. Use triples only as an index. Budget extra model calls at index and query time.
Check. A query-class histogram justifies the structured index, or the job is disabled. A two-doctor fixture stores two node ids. A conditional-plan fixture keeps the if-clause in prose.
source-ids: raptor-tree-for-drill-down, graphrag-for-relations, graph-disambiguates-same-name, triples-drop-conditionals, keep-prose-plus-index, when-to-pay-for-structure

### `l0-l1-l2-progressive`

When knowledge should be navigable like files and humans must edit the same store.
Rule. Give every resource a URI. Distill about 100 tokens of L0 and about 2000 tokens of L1. Resolve most questions at L1. Store Markdown under Git. Link every mention and update the index page. Put retrieve-then-link in the writer prompt. A folder of orphans is not an architecture.
Check. A directory listing includes L0 and does not include L2 until a later read. A new entry commit changes at least one existing file. A no-link PR is rejected.
source-ids: virtual-fs-uri-map, l0-l1-l2-progressive, markdown-git-as-source, wiki-links-required, prompt-must-force-links

### `treat-updates-as-prs`

When any store that looks like Markdown, rules, or executable memory is about to change.
Rule. Pair event-triggered incremental PRs with periodic reorg. The proposer retrieves first and writes the smallest complete diff with links, time, and evidence ids. The reviewer is a different family, searches the full in-scope store, and returns line-level evidence comments. Cap iterations and escalate. Never merge by timeout. CI then rebuilds affected chunks and vectors from the git sha. Proposer writes a branch. Reviewer only verdicts. Merge job alone writes main and the live index.
Check. Proposer push to main fails. A planted unsupported claim is rejected with an evidence id and a line number. A conflict in an unselected file is found. The index manifest stores the git sha.
source-ids: pair-incremental-and-reorg, treat-updates-as-prs, proposer-smallest-complete-diff, reviewer-checks-evidence-and-diff, iterate-then-escalate, ci-then-rebuild-derived-index, three-layer-evidence-knowledge-serving, reviewer-reads-full-authorized-store, heterogeneous-reviewer-models, permission-split-three-roles

### `filter-acl-before-context`

When a shared store has tenants, roles, replaced policies, or drifted summaries.
Rule. Apply ACL and tenant isolation in the retriever, not in the prompt. Store version, effective time, and expiry. Drop expired rows or mark them repealed. Qualify conflicts by condition or mark them unresolved. Deduplicate serving files without erasing raw evidence. Reread raw sources against a checklist. Replay golden queries after reorg.
Check. A tenant-A query returns zero tenant-B chunk ids. A superseded policy is omitted or labeled repealed. A two-home fixture keeps both addresses with conditions. Evidence byte count does not drop after reorg.
source-ids: reorg-fixes-global-drift, dedup-without-erasing-evidence, reread-raw-with-checklist, qualify-conflicts-by-condition, replay-retrieval-after-reorg, attach-expiry-and-filter, filter-acl-before-context

### `retrieval-as-react-tool`

When the first query cannot name every required fact.
Rule. Wrap retrieval as a tool and iterate until evidence is enough. Keep one-shot RAG for a single known fragment. Mark retrieved text as data. Require an independent grant before any side-effecting tool. Chunk large user history and search again when a hit names another entity. Isolated turn windows miss validity. Add prefixes and resident cards.
Check. A multi-hop fixture logs a second-round query that names the missing relation. A transfer-ordering page does not produce a transfer call without a grant. A two-vehicle memory search logs a follow-up after the first hit names the other car.
source-ids: retrieval-as-react-tool, iterate-until-sufficient, keep-non-agentic-for-narrow, mark-retrieved-as-data-not-orders, no-side-effects-from-hits, agentic-search-user-memory, chunked-history-misses-validity

### `two-tier-resident-plus-rag`

When the product target is proactive service.
Rule. Hold advanced cards in the live window as an overview. Retrieve prefixed conversation details on demand. Write prefixes at index time that name document, actor, time, and intent. Prefixing is additive. Runtime compression of the live chat is subtractive. Keep both engines after prefixing. Attach version, times, and authority so rerank can down-rank stale or low-authority chunks.
Check. A travel-coordination fixture shows trip and passport cards in the prompt and a later memory-search before the expiry warning. A growth-rate chunk stores company and period in the prefix field. Indexer and session modules are separate functions.
source-ids: prefix-before-embed, not-runtime-compression, prefixes-help-both-engines, cache-prefix-generation, prefixes-carry-actor-time-intent, two-tier-resident-plus-rag, quality-signals-in-retrieval

### `data-driven-needs-expert-review`

When knowledge lives in thousands of outcomes rather than a handbook paragraph.
Rule. Extract to a frozen schema, estimate factor importance, cluster prototypes with statistical ranges, and require expert review of schema and bias. Use indicator vectors for nominal classes. Models drive questions. Statistics explain. Induced rules are reviewed drafts, not unsupervised law.
Check. Every extracted sample row passes JSON Schema. A conversation asks high-weight factors first. The answer payload includes a prototype id and a range. A release checklist includes an expert-review artifact and a bias note.
source-ids: from-retrieval-to-discovery, extract-to-schema, factor-importance-hierarchy, bottom-up-schema, one-hot-not-ordinal, cluster-prototypes-not-black-box, data-driven-needs-expert-review

### `later-chapter-uses-this-store`

When a later chapter will record what to do under which conditions, or when media and parametric slots are proposed as memory.
Rule. Keep declarative tenant facts here. Point experience learning at the same evidence, review, and index rules. Record a merge as a proposal, not as a global quality win. Write user-preference updates after review. Flag agent operational notes as candidates until outcome eval. Persist media plus caption and offer a native multimodal read. Reciting a LoRA is not Level-3 memory.
Check. Architecture notes state that experience records reuse this PR and evidence pattern, or they list an exception. A merged memory PR is revertable by git revert and does not flip a global gate by itself. A use-the-stored-passport-to-warn-about-a-trip case must pass.
source-ids: this-chapter-is-proposal-stage, later-chapter-uses-this-store, single-write-is-not-experience, parametric-memory-misses-indirect, store-media-plus-caption, native-multimodal-tool, pack-embeddings-in-context, engram-slot-with-gate

## Failure diagnostics

| Symptom | First label | Cluster |
| --- | --- | --- |
| Wrong remembered fact or policy answer | conflict, stale, or miss | `shared-conflict-stale-miss` via `two-scale-memory-and-kb` |
| Two live addresses, no decision record | write-time clash | `mem0-v3-append-and-retrieve` |
| Answer invents a window with empty hits | generator ignored the closed list | `rag-retrieve-inject-generate` |
| Tenant-B chunk ids in a tenant-A prompt | ACL applied after retrieve | `filter-acl-before-context` |
| Password or card in an outbound trace | sanitizer ran off-device or regex-only | `sanitize-logs-on-device` |
| Extractor upserted production vectors | proposer wrote main | `treat-updates-as-prs` |
| Level-3 miss with cards only or RAG only | missing the other tier | `two-tier-resident-plus-rag` |
| Retrieved page orders a transfer | hit treated as a grant | `retrieval-as-react-tool` |

## Namespaced drills

### `03-memory-knowledge-q1`

Two sessions state two home addresses. Silent-append of a second live address fails. Either run extract-then-decide so a move overwrites the live field with a timestamp, or keep both dated rows and let hybrid plus time rank pick the current city. Never DELETE the only copy if history questions matter.

### `03-memory-knowledge-q2`

Prefixes that copy a messy source need version, effective time, expiry, and authority on the chunk. Filter expired rows or mark them repealed. Rerank on freshness and authority, not only semantic match. Detect inter-chunk contradictions at index time.

### `03-memory-knowledge-q3`

A caption drops architecture-box containment, crossing plotted curves, and header-to-cell alignment. Persist the file and register a native multimodal read or image tool. Caption-only storage fails figure questions.

### `03-memory-knowledge-q4`

Longer windows do not retire index-time aggregate and boundary jobs. Attention is soft retrieval. Expiry, ACL, audit, and cost remain even if the model is strong.

### `03-memory-knowledge-q5`

A larger foundation model does not erase a domain knowledge base. Training has a cutoff. Private process needs ACL. External rows are auditable and can go offline. Parametric recitation still fails indirect multi-hop use.

### `03-memory-knowledge-q6`

RAPTOR fits summary-to-leaf travel. GraphRAG fits relation chains, same-name split, and community themes. Pick by query class, not by fashion.

### `03-memory-knowledge-q7`

A filesystem beats vector-only RAG when humans must edit and revert the same Git files and the agent writes experience onto a review branch. The win depends on wiki links and L0/L1/L2. Orphan files get harder to retrieve as they grow.

### `03-memory-knowledge-q8`

Induced factors can capture tacit trade-offs and stay measurable. They also inherit extractor error and dataset bias. Ship them as reviewed drafts. Models drive questions. Statistics support explanations.

### `03-memory-knowledge-q9`

A Markdown memory library still merges silent errors if proposer and reviewer share a family and see only proposer snippets. Fix independence (two families), coverage (full in-scope store plus evidence), and permissions (branch write, verdict-only review, merge-only index). Incremental and reorg both ship as PRs. `thought-exercises-apply-here` collapses into this drills section.

## Depends-on

- `playbooks/getting-started.md` for the agent-versus-environment boundary and append-only trajectory.
- `playbooks/context-engineering.md` for frozen prefixes, untrusted-data wraps, and window compression that must not delete the audit log.

## Needed-by

- `playbooks/continual-evolution.md` reuses this evidence, PR, and index pattern for gated action experience. `distinguish-user-memory-from-action-experience` splits the stores. Chapter 3 owns tenant facts. Chapter 9 owns gated strategy.
- `playbooks/evaluating-agents.md` can host the three-level memory bar as part of the model-plus-harness pair.

## Open tensions

- `trajectory-is-append-only` versus `long-term-memory-is-rewritten-archive`. Evidence stays append-only. The reviewed archive may rewrite. Do not edit the log to match the card.
- `this-chapter-is-proposal-stage` and `later-chapter-uses-this-store`. A merged memory PR is not a product-quality win. Experience write-back waits for `playbooks/continual-evolution.md`.
- `distinguish-user-memory-from-action-experience`. Tenant facts stay here. Gated strategy does not merge into this archive. `four-experience-carriers` in the afterword only names carriers.
- `single-write-is-not-experience`. One tool trace is a candidate, not a procedural rule.
- `mem0-v2-write-time-decide` versus `mem0-v3-append-and-retrieve`. Prefer append-plus-rank when an incorrect UPDATE would be irreversible.
