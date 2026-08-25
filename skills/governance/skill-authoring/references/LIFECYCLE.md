# Skill Lifecycle Reference

This reference expands the lifecycle rules used by `skill-authoring`.

## Creating

A skill is a good candidate when its workflow is reusable, independently understandable, has recognizable triggers, and would otherwise be repeatedly re-explained to agents.

Avoid creating a skill solely for a single Issue, temporary workaround, small formatting convention, or one agent-specific syntax detail.

## Extending

Prefer extension when the new behavior naturally belongs to an existing responsibility and would share most of the same trigger conditions.

## Splitting

Split when independent workflows have become coupled only because they were historically placed in the same file. A split should improve discovery, reduce irrelevant context, or create clearer ownership.

## Merging

Merge when separate skills mainly duplicate the same workflow. Preserve useful unique rules and update all references.

## Deprecating

Deprecation means the skill should no longer be used for new work but may remain temporarily for compatibility or migration.

Record:

- why it is deprecated;
- replacement skill, when one exists;
- affected references;
- expected removal decision, if applicable.

## Removing

Remove only after confirming that no required process, rule, reference, or adapter still depends on it.

## Changing governance

Changes to `skill-authoring`, approval boundaries, the official template, category model, or source-of-truth strategy are governance changes and require explicit human approval.
