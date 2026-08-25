---
name: skill-authoring
description: Creates, reviews, updates, splits, merges, deprecates, and validates project skills. Use whenever the team proposes a new skill, changes an existing skill, audits the skill system, or decides whether a reusable instruction should become a skill.
metadata:
  project-version: "1.0.0"
  project-status: "defined"
  project-category: "governance"
  project-scope: "project-wide"
  agent-agnostic: "true"
---

# Skill Authoring

## 1. Objective

Govern the creation and maintenance of all project skills so they remain reusable, coherent, traceable, low in redundancy, and portable across compatible AI agents.

This skill is the primary source of truth for skill-authoring rules.

## 2. Scope

Use this skill to:

- create a new skill;
- change an existing skill;
- decide whether an instruction deserves a skill;
- split or merge skills;
- deprecate or remove skills;
- validate skill structure;
- detect overlap or conflicting skill rules;
- change the official skill template;
- adapt universal skill rules to agent-specific discovery or invocation.

Do not use it to perform product implementation, requirements work, code review, testing, Scrum execution, or architecture work except when those activities concern the skill system itself.

## 3. Decision states

Use these project states when relevant:

- **Defined**: approved and authoritative.
- **Proposed**: prepared but not yet authoritative.
- **Pending Decision**: requires a human decision.
- **Not Currently Applicable**: known but not needed now.

Never silently convert a proposal, assumption, or pending decision into a defined rule.

## 4. Expected inputs

Gather the available information about:

1. the recurring problem to solve;
2. the expected reusable behavior;
3. related existing skills;
4. relevant governance rules;
5. relevant technical or process decisions;
6. agents expected to use the skill;
7. example trigger tasks;
8. human approval boundaries.

If an essential decision is unknown, mark it as `Pending Decision`. Do not invent it.

## 5. Pre-conditions

Before changing the skill system:

1. inspect relevant existing skills;
2. identify the current source of truth for overlapping rules;
3. determine whether the request is already covered;
4. identify required human decisions;
5. preserve unrelated approved behavior.

If relevant skill files cannot be inspected, do not claim that no overlap exists.

## 6. Choose the action

Classify the request as exactly one of:

- `CREATE`
- `EXTEND`
- `SPLIT`
- `MERGE`
- `DEPRECATE`
- `NO-SKILL`

### CREATE

Create a skill when the responsibility is reusable, has a clear purpose and triggers, has distinct enough procedure, has clear boundaries, and can evolve without excessive coupling.

### EXTEND

Extend an existing skill when the new behavior belongs to the same domain, shares similar triggers, and separation would mainly create duplication.

### SPLIT

Split a skill when it mixes independent responsibilities, has very different triggers, contains incompatible procedures, or has become unnecessarily large or difficult to maintain.

### MERGE

Merge skills when they substantially duplicate triggers, rules, or workflow and do not justify independent evolution.

### DEPRECATE

Deprecate a skill when its responsibility has intentionally been replaced or is no longer valid. Check dependencies before removal.

### NO-SKILL

Do not create a skill for one-off tasks, tiny conventions, task-specific instructions, ordinary documentation, or behavior already covered elsewhere.

## 7. Single source of truth

Each project rule should have one primary authoritative source.

When authoring skills:

1. place the full rule in the correct source;
2. reference it elsewhere instead of copying it;
3. avoid duplicating large rules in `CLAUDE.md`, `AGENTS.md`, or equivalent files;
4. report conflicts rather than choosing silently;
5. keep agent-specific adapters minimal.

Duplicate content only when technically necessary and explicitly justified.

## 8. Agent independence

Separate:

1. universal project behavior;
2. agent-specific discovery, invocation, and tooling configuration.

A Claude, Codex, or other agent limitation must not silently redefine a universal project rule.

## 9. Agent Skills compatibility

Every project skill must follow the portable Agent Skills structure.

Minimum:

```text
<skill-name>/
└── SKILL.md
```

Optional:

```text
<skill-name>/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

Every `SKILL.md` must begin with compatible YAML frontmatter containing at least:

```yaml
---
name: <skill-name>
description: <what the skill does and when to use it>
---
```

Rules:

- the directory name must match `name`;
- `name` uses lowercase letters, numbers, and hyphens;
- project-specific metadata belongs inside `metadata`;
- keep project metadata values as strings;
- keep the main `SKILL.md` focused;
- move detailed supporting material into `references/` when useful.

## 10. Repository organization

The canonical project source for skills is:

```text
skills/
├── governance/
├── process/
├── engineering/
└── technology/
```

Store each skill as:

```text
skills/<category>/<skill-name>/SKILL.md
```

Categories:

- `governance`: project and skill-system governance;
- `process`: requirements, Scrum, GitHub workflow, and related processes;
- `engineering`: implementation, testing, review, architecture, and quality;
- `technology`: technology-specific guidance.

Do not create a category for a single convenience case.

Tool-specific directories such as `.claude/skills/` or `.agents/skills/` are adapters to the canonical source, not independently maintained sources of truth.

The adapter strategy is defined separately from this skill.

## 11. Naming

Skill names must:

- use lowercase `kebab-case`;
- be concise and responsibility-oriented;
- match the skill directory name;
- not begin or end with a hyphen;
- not contain consecutive hyphens.

Prefer names such as:

- `skill-authoring`
- `project-governance`
- `code-review`
- `backend-python`

Avoid names based on people, agents, arbitrary numbers, vague words such as `helper`, or one temporary Issue.

## 12. Project metadata

Recommended portable frontmatter:

```yaml
---
name: <skill-name>
description: <what it does and when to use it>
metadata:
  project-version: "0.1.0"
  project-status: "proposed"
  project-category: "<category>"
  project-scope: "<scope>"
  agent-agnostic: "true"
---
```

Do not add metadata that has no practical use.

## 13. Versioning

Use semantic versioning for project skill behavior:

`MAJOR.MINOR.PATCH`

- `PATCH`: clarification or correction without meaningful behavior change.
- `MINOR`: backward-compatible new behavior.
- `MAJOR`: incompatible behavior, scope, or contract change.

A proposed skill may begin at `0.1.0`. Its first approved authoritative release may become `1.0.0`.

Git history remains the authoritative history of changes.

## 14. Required content

Every official skill must clearly define:

1. Objective
2. Scope
3. When to use
4. When not to use
5. Expected inputs
6. Pre-conditions
7. Procedure
8. Expected output
9. Constraints
10. Human approval
11. Verification
12. Interaction with other skills
13. Handling uncertainty and failures

Examples are optional.

Use [references/SKILL_TEMPLATE.md](references/SKILL_TEMPLATE.md) when creating a new skill.

## 15. Procedure

### Step 1 — State the recurring problem

Answer:

> What recurring project problem does this skill solve?

If there is no clear answer, choose `NO-SKILL`.

### Step 2 — Inspect existing skills

Check for similar responsibilities, duplication, dependencies, conflicts, and opportunities to extend an existing skill.

### Step 3 — Classify

Choose one action:

`CREATE`, `EXTEND`, `SPLIT`, `MERGE`, `DEPRECATE`, or `NO-SKILL`.

Give a short justification.

### Step 4 — Define boundaries

State what the skill owns, what it does not own, when its responsibility begins and ends, and which other skills receive related work.

### Step 5 — Identify unresolved decisions

Explicitly classify material decisions as Defined, Proposed, Pending Decision, or Not Currently Applicable.

### Step 6 — Write or update

For a new skill, use the official template.

For an existing skill:

1. read the current version and relevant references;
2. make the smallest coherent change;
3. preserve unrelated approved behavior;
4. update behavioral version when appropriate.

### Step 7 — Validate

Run [references/VALIDATION_CHECKLIST.md](references/VALIDATION_CHECKLIST.md).

If a compatible Agent Skills validator is available, run it as an additional check.

### Step 8 — Report impact

State:

- selected action;
- reason;
- files affected;
- skills affected;
- conflicts;
- pending decisions;
- approval required.

### Step 9 — Human approval

Governance-changing work remains Proposed until approved by a human.

### Step 10 — Record the change

When the GitHub workflow is defined, preserve proportionate traceability through the appropriate Issue, branch, commit, or Pull Request.

## 16. Expected output

When invoked, return the relevant parts of:

### Decision
One of `CREATE`, `EXTEND`, `SPLIT`, `MERGE`, `DEPRECATE`, `NO-SKILL`.

### Justification
The recurring problem and reason for the selected action.

### Impact
Affected skills, files, rules, and compatibility.

### Decision state
Relevant Defined, Proposed, Pending Decision, or Not Currently Applicable items.

### Proposed content
The new or changed skill when applicable.

### Validation
Checks performed and failures found.

### Approval
Whether the change is already authorized or must remain Proposed until human approval.

## 17. Constraints

Never:

- invent product requirements;
- invent architectural decisions;
- silently choose an undefined structural technology;
- create redundant skills for unnecessary granularity;
- duplicate extensive rules across skills;
- turn agent-specific behavior into universal behavior without justification;
- mark an unsupported decision as Defined;
- remove approved rules without impact analysis;
- change this governance model silently.

## 18. Human approval

Human approval is required to:

- make a new governance skill authoritative;
- change this `skill-authoring` skill;
- materially change the official skill template;
- change human approval boundaries;
- remove or deprecate an authoritative skill;
- merge skills when responsibility materially changes;
- alter central skill-governance rules;
- promote agent-specific behavior into a universal project rule.

Agents may inspect, analyze, prepare, and recommend these changes, but must not treat them as approved beforehand.

## 19. Verification

Before requesting adoption:

1. run the project validation checklist;
2. confirm the directory name matches `name`;
3. confirm `name` and `description` exist;
4. confirm `description` covers purpose and trigger context;
5. confirm project-specific metadata is under `metadata`;
6. confirm the skill does not unnecessarily duplicate another source;
7. confirm pending decisions remain explicit;
8. confirm approval boundaries are clear.

## 20. Interaction with other skills

### `project-governance`

When available, follow its approved global rules.

If a conflict exists, identify both sources and use any explicitly defined governance hierarchy. If no authoritative resolution exists, request human resolution.

### `project-audit`

The audit skill may use this skill to detect invalid structure, duplicated responsibilities, conflicting rules, missing approval, outdated adapters, or divergence between entry files and canonical skills.

### Domain skills

Requirements, implementation, testing, architecture, Scrum, and other domain skills may identify reusable gaps, but structural changes to the skill system must return to `skill-authoring`.

## 21. Handling uncertainty and failures

If information is missing:

1. do not invent it;
2. record the gap;
3. determine whether it blocks the task;
4. continue unaffected work when possible;
5. mark it Pending Decision;
6. state the exact human decision needed if blocked.

If skills conflict:

1. identify the conflicting rules and sources;
2. check for an approved hierarchy;
3. do not silently choose;
4. request human resolution when needed.

If validation is incomplete, report what was not checked and do not claim full validation.

## 22. Deprecation and removal

Before deprecating or removing a skill:

1. identify dependencies and references;
2. decide where remaining responsibilities move;
3. prevent broken references;
4. preserve rules still required;
5. explain the reason;
6. obtain human approval when required.

Recent lack of use alone is not sufficient reason for removal.

## 23. Self-modification rule

This skill must never silently change the rules that govern itself or the rest of the skill system.

Any proposed change to `skill-authoring` must:

1. explain the motivating problem;
2. identify affected rules;
3. identify impact on existing skills;
4. present the proposed new version;
5. pass validation;
6. remain Proposed until human approval.

This prevents an agent from autonomously changing the governance mechanism that constrains its own behavior.
