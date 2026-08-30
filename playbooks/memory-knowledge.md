# user-memory-and-knowledge-base

use_when
- remember this user next time
- build RAG
- hybrid retrieval
- knowledge base
- user memory
- conflict in memory
- memory framework
- chunking strategy
- contextual retrieval
- agentic RAG
- structured index
- filesystem knowledge
- sanitize logs
- PII in traces
- update the knowledge base
- tenant isolation for documents
- proactive assistant memory

Copy these steps into the todolist before reasoning. A skipped step stays listed with a one-line skip reason. Do not drop it.

## 0. Name the data shape

Name the shape before any store or retriever logic. The shape is a user-keyed archive plus a tenant-scoped shared knowledge plane. Lookup in `references/data-shapes.md`. Bind personal facts to a user id. Bind shared procedures and manuals to the tenant. Reuse one retrieval, conflict, and freshness stack on both.

## 1. Name the scale

Name user-keyed memory, shared knowledge, or both. Confirm a user-id key on the archive and a tenant-scoped index on the knowledge plane. Attach source, time, and conflict metadata on both. Skip only when the task is a single-session prompt with no persistence. Skip reason. Persistence is out of scope.

If the check fails, open [lessons/03-memory-knowledge.md](../lessons/03-memory-knowledge.md) cluster `two-scale-memory-and-kb`. source-ids: two-scale-memory-and-kb, shared-conflict-stale-miss.

## 2. Pick location, format, and cognitive type

Answer the three axes per record class. Location is trajectory, working window, long-term archive, or business-state slot. Format is notes, cards, or typed functions. Cognitive type is episodic, semantic, or procedural. Record a filled triple in the design note. Skip only when no new record class is added. Skip reason. Axes already recorded.

If the check fails, open [lessons/03-memory-knowledge.md](../lessons/03-memory-knowledge.md) cluster `three-classifications-orthogonal`. source-ids: three-storage-questions, three-classifications-orthogonal, episodic-semantic-procedural.

## 3. Instrument the three-level bar

Stand up Level-1 exact recall, Level-2 multi-session retrieval, and Level-3 proactive joins. Hide raw transcripts from the answerer. Tag cases with the eight capability classes, including one update case and one conflict case. Skip only when the review is a paper design with no runtime. Skip reason. Eval harness is not yet wired.

If the check fails, open [lessons/03-memory-knowledge.md](../lessons/03-memory-knowledge.md) cluster `eight-capability-yardstick`. source-ids: eight-capability-yardstick, level-1-basic-recall, level-2-multi-session, level-3-proactive-service, memory-eval-without-transcript.

## 4. Write events append-only. Extract after the session

Append user, model, and tool events. Never rewrite a historical event. After the session, run a dedicated extractor through tools. Accept a write only when it is selective, abstracted beyond the turn, and stored in a retrievable field. Skip only when the session produced no reusable fact. Skip reason. Extractor returned an empty candidate set.

If the check fails, open [lessons/03-memory-knowledge.md](../lessons/03-memory-knowledge.md) cluster `post-session-dedicated-extract`. source-ids: post-session-dedicated-extract, extraction-three-invariants, trajectory-is-append-only, long-term-memory-is-rewritten-archive.

## 5. Route by criticality

Route scarce critical facts to advanced cards or typed state with functions. Route bulk chatter to simple notes. Run counts, clashes, and validity windows as functions over typed state. Prefer append plus retrieval-time rank when a write-time UPDATE or DELETE would erase history. Skip only when the class list is already routed and unchanged. Skip reason. Format map is current.

If the check fails, open [lessons/03-memory-knowledge.md](../lessons/03-memory-knowledge.md) cluster `hybrid-format-by-criticality`. source-ids: hybrid-format-by-criticality, advanced-json-cards-disambiguate, deterministic-rule-functions, mem0-v3-append-and-retrieve.

## 6. Run both engines, then rerank

Chunk first. Embed dense and sparse. Fuse ranks with reciprocal rank fusion. Rerank the fused pool with a cross-encoder. Score hit-rate, MRR, and nDCG. Treat operational recall@k as hit-rate. Skip only when the scale is user-keyed cards with no document corpus. Skip reason. No chunk index exists yet.

If the check fails, open [lessons/03-memory-knowledge.md](../lessons/03-memory-knowledge.md) cluster `run-both-engines`. source-ids: run-both-engines, fuse-ranks-with-rrf, rerank-after-fusion, measure-hit-rate-mrr-ndcg, chunk-to-protect-embedding.

## 7. Add organization only for the query class that needs it

Add index-time summaries, boundary cards, prefixes, trees, graphs, or a wiki filesystem only when the query-class histogram requires them. Precompute aggregates. Do not ask attention to summarize a sample. Keep prose as source of truth. Skip when the histogram is fragment lookup only. Skip reason. Hybrid retrieve plus rerank is enough.

If the check fails, open [lessons/03-memory-knowledge.md](../lessons/03-memory-knowledge.md) cluster `index-time-precompute-aggregates` or `when-to-pay-for-structure`. source-ids: index-time-precompute-aggregates, when-to-pay-for-structure, l0-l1-l2-progressive.

## 8. Expose search as a tool for multi-hop

Wrap retrieval as a ReAct tool when the first query cannot name every required fact. Keep one-shot retrieve-then-generate for a single known fragment. Mark hits as data. Block side effects without a separate grant. Skip agentic search when every question is a single known fragment. Skip reason. Narrow lookup stays non-agentic.

If the check fails, open [lessons/03-memory-knowledge.md](../lessons/03-memory-knowledge.md) cluster `retrieval-as-react-tool`. source-ids: retrieval-as-react-tool, keep-non-agentic-for-narrow, mark-retrieved-as-data-not-orders.

## 9. Update through proposer and reviewer PRs

Treat knowledge as a repo. The proposer writes the smallest complete diff on a branch. The reviewer is a different model family, reads the full in-scope store and evidence, and cannot merge. Only the merge job writes main and rebuilds the live index. Cap iterations. Escalate on deadlock. Never merge by timeout. Skip only when the store is still empty and no write is proposed. Skip reason. No candidate PR exists.

If the check fails, open [lessons/03-memory-knowledge.md](../lessons/03-memory-knowledge.md) cluster `treat-updates-as-prs`. source-ids: treat-updates-as-prs, permission-split-three-roles, heterogeneous-reviewer-models, reviewer-reads-full-authorized-store.

## 10. Reorganize on a schedule. Filter expiry and ACL in the retriever

Pair event-triggered incremental PRs with a periodic reorg PR. Qualify conflicts by condition. Do not newest-win. Filter expiry and ACL before any chunk enters context. Isolate indexes per tenant. Sanitize logs on the device. Skip the reorg job only when the library is still below the volume trigger. Skip reason. Incremental path is sufficient this cycle. Do not skip ACL or sanitizer.

If the check fails, open [lessons/03-memory-knowledge.md](../lessons/03-memory-knowledge.md) cluster `filter-acl-before-context`. source-ids: filter-acl-before-context, attach-expiry-and-filter, qualify-conflicts-by-condition, sanitize-logs-on-device.

## 11. Keep a small resident overview

Hold critical cards in the live window. Fetch prefixed details on demand. Use both for Level-3 joins. Skip only when Level-3 is out of scope. Skip reason. Product bar stops at Level-2.

If the check fails, open [lessons/03-memory-knowledge.md](../lessons/03-memory-knowledge.md) cluster `two-tier-resident-plus-rag`. source-ids: two-tier-resident-plus-rag, prefix-before-embed, level-3-proactive-service.

## Open next

Hard open [playbooks/continual-evolution.md](continual-evolution.md). `this-chapter-is-proposal-stage`. `later-chapter-uses-this-store`. Tenant facts stay here. Gated action experience and strategy wait for that playbook. Do not merge the two stores.

Also open [playbooks/context-engineering.md](context-engineering.md) when the miss is prefix stability, injection tags, or window layout rather than the archive.

## Reply

What changed. What scale, format, and retrieval path were chosen. What remains open, including any proposal-stage item that waits for `playbooks/continual-evolution.md`.
