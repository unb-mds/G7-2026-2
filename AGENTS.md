# G7 — Instruções para agentes

Este arquivo funciona apenas como bootstrap para agentes que trabalham neste repositório.

As regras canônicas do projeto estão em `skills/`. Este arquivo não substitui nem duplica essas regras.

## Agent Skills

Antes de executar uma tarefa, verifique se existe uma skill aplicável em:

- `skills/governance/`
- `skills/process/`
- `skills/engineering/`
- `skills/technology/`

Compare a tarefa com a `description` das skills relevantes.

Quando uma skill for aplicável:
1. leia seu `SKILL.md` integralmente;
2. leia as referências necessárias;
3. siga suas instruções antes de alterar código ou configuração.

Para criação, alteração, validação, promoção ou gerenciamento de Agent Skills, leia primeiro:

- `skills/governance/skill-authoring/SKILL.md`
- `skills/governance/project-governance/SKILL.md`

e as referências aplicáveis.

As regras encontradas nas skills canônicas têm precedência sobre este arquivo.

## Aprovação humana

Não transforme uma skill de `proposed` para `defined` sem aprovação humana explícita.

Não execute commit, push, Pull Request ou merge sem solicitação ou autorização explícita.

Operações Git destrutivas exigem confirmação humana explícita.

## Portabilidade

Preserve o caráter agent-agnostic das skills.

Regras universais do projeto devem permanecer em `skills/`, e não ser transferidas para configurações específicas do Codex.