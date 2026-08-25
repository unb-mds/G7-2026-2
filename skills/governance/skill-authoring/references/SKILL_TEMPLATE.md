# Official Project Skill Template

Use this template when creating a new skill.

```markdown
---
name: <skill-name>
description: <what the skill does and when to use it>
metadata:
  project-version: "0.1.0"
  project-status: "proposed"
  project-category: "<governance|process|engineering|technology>"
  project-scope: "<scope>"
  agent-agnostic: "true"
---

# <Skill Name>

## 1. Objective

<What recurring project problem does this skill solve?>

## 2. Scope

<What is inside this skill's responsibility?>

## 3. When to use

<Clear trigger conditions.>

## 4. When not to use

<Boundaries and responsibilities owned by other skills.>

## 5. Expected inputs

<Required or useful information.>

## 6. Pre-conditions

<Conditions that should exist before execution.>

## 7. Procedure

1. <step>
2. <step>
3. <step>

## 8. Expected output

<Required format or properties of the result.>

## 9. Constraints

<What the agent must not do.>

## 10. Human approval

<What can be executed and what must only be proposed.>

## 11. Verification

- [ ] <check>
- [ ] <check>

## 12. Interaction with other skills

<Dependencies, precedence, and handoffs.>

## 13. Handling uncertainty and failures

<What to do when information is missing, conflicting, or validation fails.>

## 14. Examples

<Optional. Include only when they reduce ambiguity.>
```

## Notes

- The directory name must exactly match `name`.
- Keep `description` concise but specific enough for automatic skill selection.
- Keep project-specific fields inside `metadata`.
- Prefer references over an oversized `SKILL.md`.
- Do not add a section merely because the template contains it; write concise operational content.
