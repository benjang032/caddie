# Failure modes

Lookup by symptom. Open the owning playbook. Use the lesson ids as `source-ids` in the matching lesson file.

| Symptom | Playbook | Lesson ids | First check |
| --- | --- | --- | --- |
| Memory conflict, stale fact, or missed fragment | memory-knowledge | shared-conflict-stale-miss | Diff the archive write against the source turn. Confirm a conflict field exists. |
| Coding agent fails and the class is unknown | coding-agent | failure-taxonomy-four-layers | Label model, spec, environment, or infrastructure before retrying. |
| Score moved and no one knows which step broke | evaluating-agents | attribute-first-error | Find the first bad span. Do not blame the last message. |
| Shared files overwrite or cross-file logic breaks | multi-agent | concurrency-conflict-control | Versioned write rejected on stale read. Semantic merge gate on cross-file work. |
| Downstream agent amplifies an upstream error | multi-agent | cascading-error-amplification | Reviewer checks raw evidence, not the prior rationale. |
| Independent agents pick the same name or title | multi-agent | homogeneous-convergence | Vary model, context, or namespace. Treat same-scaffold reviews as correlated. |
| Agents fight over objectives or blame each other | multi-agent | objective-conflict-arbitration | Predeclared ownership and a human pause when rules cannot settle it. |
| Loop never stops | multi-agent | runaway-loop-bounds | Round cap, cost ceiling, and cancel check all present. |
| Humans no longer understand shipped output | multi-agent | comprehension-debt | Unreviewed output is debt. Architecture review is required. |
| Reward or demo teaches a shortcut | post-training | never-reward-a-self-reported-done | Hidden tests. The producer cannot mark done. |
| Event handler invents a payload | interaction | events-placeholder-never-fake | Missing fields stay tagged unknown. No fabricated values. |
| Tool arguments were rewritten in the harness | tools | never-silently-rewrite-arguments | Logged args equal model args. |
| Completion claimed without tests | coding-agent | tests-pass-as-completion | The done bit is set only from the verifier. |
