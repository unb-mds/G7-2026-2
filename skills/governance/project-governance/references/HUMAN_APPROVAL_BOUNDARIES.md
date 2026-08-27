# Project Governance — Limites de aprovação humana

## 1. Estado desta referência

Esta referência integra a versão `1.0.0` de `project-governance`, com estado `defined`.

Ela é a fonte project-wide para as fronteiras de aprovação humana abaixo. Regras específicas do ciclo de vida das skills continuam pertencendo a `skill-authoring`.

## 2. Objetivo

Manter em um único local a lista project-wide de ações que exigem aprovação humana, evitando que cada skill de domínio repita as mesmas fronteiras de autoridade.

A aprovação humana autoriza a decisão correspondente; ela não substitui os procedimentos técnicos, de processo ou de registro definidos pelas skills de domínio.

## 3. Ações sujeitas a aprovação humana

Exigem aprovação humana explícita:

- alterar a arquitetura da aplicação ou criar/alterar uma decisão arquitetural permanente;
- alterar requisito já aprovado;
- substituir tecnologia já aprovada;
- adicionar tecnologia estrutural importante ao projeto;
- realizar `merge`;
- fechar Issue relevante quando o fechamento representar aceite ou conclusão oficial do trabalho;
- modificar substancialmente o modelo de dados;
- alterar regras do processo Scrum;
- modificar `Definition of Done` ou `Definition of Ready`;
- remover funcionalidade do produto;
- tomar decisão de produto;
- alterar regras project-wide de governança.

Para criação, alteração, aprovação, consolidação, depreciação ou remoção de skills, aplique também as fronteiras específicas definidas pela fonte canônica `skill-authoring`.

## 4. O que o agente pode fazer antes da aprovação

Antes da decisão humana, o agente pode:

- identificar que uma decisão é necessária;
- reunir e verificar evidências;
- comparar alternativas;
- explicar vantagens, desvantagens, impactos e riscos;
- recomendar uma opção;
- preparar uma proposta ou alteração para revisão quando essa preparação não tornar a decisão efetiva;
- executar partes independentes do trabalho que já estejam autorizadas.

## 5. O que não constitui aprovação

A aprovação deve ser explícita.

Não infira aprovação a partir de:

- silêncio ou ausência de objeção;
- aprovação anterior de assunto diferente;
- recomendação produzida por um agente;
- conveniência de implementação;
- comportamento padrão de uma ferramenta;
- existência de código ou arquivo já preparado;
- continuidade de uma conversa sem manifestação inequívoca de aceite.

## 6. Ambiguidade

Se houver dúvida razoável sobre uma ação estar ou não dentro de uma fronteira de aprovação:

1. descreva a ação e seu impacto;
2. não a torne efetiva;
3. classifique a decisão como `Pending Decision`;
4. solicite aprovação humana apenas para a parte afetada;
5. continue trabalho independente que permaneça autorizado.

Não invente limites quantitativos globais para termos como "relevante", "substancial" ou "estrutural". Skills de domínio podem tornar esses critérios mais objetivos quando houver decisão oficial para isso.

## 7. Limites de skills de domínio

Skills de domínio podem acrescentar restrições de aprovação próprias quando justificadas e oficialmente adotadas.

Elas não podem enfraquecer unilateralmente uma fronteira project-wide aprovada.

## 8. Registro da aprovação

O mecanismo operacional exato para registrar aprovações no GitHub permanece `Pending Decision`.

Uma futura skill de processo pode estabelecer esse procedimento sem alterar, por esse motivo, as fronteiras de autoridade desta referência.
