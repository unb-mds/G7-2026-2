# Skill Validation Checklist

Use this checklist before requesting approval for a new or changed skill.

## Need

- [ ] Does it solve a real recurring project problem?
- [ ] Is the responsibility sufficiently distinct?
- [ ] Would extending an existing skill be worse?
- [ ] Is this more than a one-off task or documentation note?

## Agent Skills compatibility

- [ ] Is the entry file named exactly `SKILL.md`?
- [ ] Does frontmatter contain `name`?
- [ ] Does frontmatter contain `description`?
- [ ] Does `name` match the skill directory?
- [ ] Does the name follow lowercase kebab-case rules?
- [ ] Does the description explain both purpose and trigger context?
- [ ] Are project-specific fields stored under `metadata`?
- [ ] Are metadata values strings?
- [ ] Is the main skill reasonably concise, using references when appropriate?

## Structure

- [ ] Is the objective clear?
- [ ] Is the scope clear?
- [ ] Does it say when to use it?
- [ ] Does it say when not to use it?
- [ ] Are expected inputs identified?
- [ ] Are pre-conditions identified?
- [ ] Is there an operational procedure?
- [ ] Is the expected output clear?
- [ ] Are constraints explicit?
- [ ] Are human approval boundaries explicit?
- [ ] Are verification steps defined?
- [ ] Are interactions with other skills documented?
- [ ] Is uncertainty/failure handling defined?

## Consistency

- [ ] Does it avoid contradicting known project governance?
- [ ] Does it avoid unnecessary duplication?
- [ ] Does it avoid converting assumptions into decisions?
- [ ] Does it avoid silently depending on an undefined technology?
- [ ] Does it separate universal rules from agent-specific adapters?

## Operational quality

- [ ] Can an agent determine when to activate it?
- [ ] Can an agent determine when not to activate it?
- [ ] Does the workflow produce a verifiable result?
- [ ] Does it define when the agent must stop for human approval?

## Traceability

- [ ] Is the reason for the skill or change known?
- [ ] Are affected skills/files identified?
- [ ] Can meaningful changes be connected to Git history?
- [ ] Are pending decisions explicitly marked?

## Result

If a mandatory check fails:

- fix it before adoption when possible;
- otherwise keep the skill `proposed`;
- document the unresolved failure;
- do not treat the skill as authoritative.
