# G7 — Avaliação de Disciplinas (UnB MDS)

## Sobre o projeto

- Disciplina: Métodos de Desenvolvimento de Software (MDS), UnB — professora Carla Rocha.
- Objetivo: aplicativo web de avaliação de disciplinas + professores da UnB, com dados públicos extraídos do SIGAA.
- Equipe: G7, 6 integrantes, Scrum com sprints semanais.

## Stack atual (em migração)

- **Backend:** FastAPI + Uvicorn + Python 3.12. Migrando de Django (pedido da professora, por separação insuficiente entre front e back no Django).
- **Frontend:** ainda não decidido (proposta em avaliação: HTML/CSS/JS puro consumindo a API via `fetch`).
- **Banco de dados:** PostgreSQL via Docker Compose. ORM ainda pendente de aprovação — ver `skills/technology/fastapi/SKILL.md`.
- **Scraping SIGAA:** páginas públicas, sem autenticação (referência: `unb-mds/SuaGradeUnB`).

## Como este projeto usa Skills

Antes de qualquer tarefa, verifique se existe uma skill relevante dentro de `skills/<categoria>/<nome>/SKILL.md`:

- `skills/governance/` — regras de como as skills são criadas, revisadas e validadas. Leia `skill-authoring` antes de criar uma skill nova.
- `skills/process/` — Scrum, fluxo de GitHub, requisitos (ainda a criar).
- `skills/engineering/` — padrões de implementação, testes (ainda a criar).
- `skills/technology/` — guias por tecnologia (`docker`, `fastapi`).

Compare a tarefa pedida com a `description` de cada `SKILL.md` dessas pastas antes de agir. Se uma skill for aplicável, leia o arquivo inteiro e siga as instruções nela antes de gerar código ou configuração.

## Convenções gerais

- Segredos nunca são commitados: variáveis sensíveis ficam em `.env` (fora do Git), lidas via `python-decouple`.
- Fluxo de Git: GitHub Flow — sempre branch de feature + Pull Request, nunca push direto na `main`.
- Nomenclatura: entidades de domínio em português (`Avaliacao`, `Usuario`, `Turma`), estrutura técnica (routers, schemas, etc.) em inglês.

## Estado atual (Sprint 0)

- Migração de Django para FastAPI em andamento numa branch dedicada (`chore/migrate-to-fastapi`).
- Skill `docker`: status `proposed`, aguardando aprovação humana.
- Skill `fastapi`: status `proposed`, aguardando aprovação humana. Decisões pendentes: ORM/banco de dados, divisão `backend/` + `frontend/`.
