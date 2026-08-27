---
name: project-governance
description: Governa autoridade, decisões, evidências, escopo e aprovação humana no trabalho assistido por IA do projeto. Use quando um agente precisar determinar se uma ação está autorizada, se uma decisão está definida ou pendente, se há evidência suficiente ou se deve interromper para aprovação humana.
metadata:
  project-version: "1.0.0"
  project-status: "defined"
  project-category: "governance"
  project-scope: "project-wide"
  agent-agnostic: "true"
---

# Project Governance

## 1. Objetivo

Estabelecer as regras universais de governança que limitam e orientam o trabalho realizado por agentes de IA no projeto.

Esta skill existe para impedir que hipóteses, propostas, exemplos, inferências ou informações incompletas sejam tratadas como decisões aprovadas e para garantir que o agente:

- atue somente dentro do escopo autorizado;
- verifique evidências quando a tarefa depender do estado atual do projeto;
- preserve decisões já aprovadas;
- identifique quando uma decisão humana é necessária;
- mantenha rastreabilidade proporcional ao impacto da mudança.

Esta skill governa autoridade e limites. Procedimentos de domínio pertencem às respectivas skills.

## 2. Escopo

Esta skill é transversal ao projeto e se aplica quando o trabalho de um agente envolver:

- decisões ou propostas que possam alterar o estado oficial do projeto;
- requisitos, arquitetura, tecnologias, modelo de dados, processo ou funcionalidade;
- necessidade de distinguir fato observado, inferência e proposta;
- verificação de evidências existentes antes de agir;
- conflito entre fontes aparentemente autoritativas;
- expansão de escopo;
- necessidade de aprovação humana;
- preservação de rastreabilidade de mudanças relevantes.

Ela define **como determinar se uma ação pode prosseguir**, mas não define **como executar o trabalho técnico ou de processo de cada domínio**.

## 3. Quando utilizar

Utilize esta skill quando for necessário determinar pelo menos um dos seguintes pontos:

- se uma ação já está autorizada;
- se uma informação representa decisão vigente ou apenas proposta;
- se o estado atual do projeto precisa ser verificado antes da execução;
- se uma mudança ultrapassa o escopo autorizado;
- se uma ação exige aprovação humana;
- se duas fontes relevantes entram em conflito;
- se uma melhoria adjacente pode ser executada ou deve ser apenas proposta;
- quais evidências e informações de rastreabilidade devem acompanhar uma mudança relevante.

Skills de domínio devem tratá-la como dependência transversal quando essas condições ocorrerem.

## 4. Quando não utilizar

Não utilize esta skill como substituta de uma skill de domínio para:

- criar, alterar, validar, dividir, consolidar, depreciar ou remover skills;
- definir ou refinar requisitos;
- tomar ou documentar decisões arquiteturais;
- implementar funcionalidades;
- criar ou executar testes;
- revisar código;
- executar Scrum;
- operar Issues, branches, commits, Pull Requests ou merges;
- realizar auditoria completa do projeto.

A criação e manutenção de skills pertence a `skill-authoring`.

Procedimentos específicos de requisitos, arquitetura, implementação, testes, Scrum, GitHub, auditoria e tecnologias pertencem às respectivas skills quando existirem.

## 5. Entradas esperadas

Utilize, quando relevantes e disponíveis:

1. solicitação humana atual;
2. documentação aprovada do projeto;
3. skills oficiais aplicáveis;
4. decisões de produto, arquitetura ou processo já registradas;
5. arquivos e configuração atuais do repositório;
6. Issues, Pull Requests e demais evidências de trabalho;
7. resultados de testes, validações ou inspeções;
8. propostas existentes, mantendo-as explicitamente separadas de decisões vigentes.

Não presuma a existência, o conteúdo ou o estado de uma evidência que não tenha sido verificada.

## 6. Pré-condições

Antes de executar uma ação governada por esta skill:

1. identifique exatamente o trabalho solicitado;
2. identifique as fontes conhecidas que governam esse trabalho;
3. determine quais decisões materiais já existem;
4. identifique se a ação depende do estado atual do projeto;
5. verifique se a ação cruza uma fronteira de aprovação humana;
6. identifique limitações de acesso que impeçam verificação necessária.

Se uma informação essencial estiver ausente, aplique o tratamento de incerteza desta skill em vez de inventá-la.

## 7. Procedimento

1. **Delimite a ação.** Determine o que foi solicitado e quais partes do projeto podem ser afetadas.
2. **Identifique as fontes aplicáveis.** Localize regras, decisões e evidências relevantes já disponíveis.
3. **Classifique o estado das decisões.** Use o vocabulário oficial definido por `skill-authoring`: `Defined`, `Proposed`, `Pending Decision` e `Not Currently Applicable`. As definições desses estados permanecem canônicas em `skill-authoring`.
4. **Verifique a autoridade.** Consulte [Limites de aprovação humana](references/HUMAN_APPROVAL_BOUNDARIES.md) e identifique o que pode ser executado e o que depende de decisão humana.
5. **Verifique evidências.** Quando a tarefa depender do estado atual do projeto, inspecione a fonte relevante quando houver acesso e diferencie fato observado de inferência.
6. **Execute somente a parte autorizada.** Continue o trabalho que estiver dentro do escopo e não estiver bloqueado por aprovação, conflito ou evidência essencial ausente.
7. **Separe proposta de decisão.** Melhorias, alternativas e mudanças não autorizadas podem ser recomendadas, mas devem permanecer explicitamente propostas.
8. **Preserve rastreabilidade proporcional.** Para mudanças relevantes, mantenha informação suficiente para relacionar motivo, origem, alteração e verificação, sem criar burocracia para mudanças triviais.
9. **Exponha bloqueios.** Quando necessário, indique claramente o que foi concluído, o que permanece proposto, o que depende de decisão humana e o que não pôde ser verificado.
10. **Interrompa somente o necessário.** Se um conflito ou decisão pendente bloquear apenas parte do trabalho, continue as partes independentes que permaneçam autorizadas.

## 8. Saída esperada

Quando a governança precisar aparecer explicitamente na resposta, apresente apenas os elementos relevantes:

- **Estado**: decisões `Defined`, `Proposed`, `Pending Decision` ou `Not Currently Applicable`;
- **Trabalho autorizado**: o que pode prosseguir;
- **Aprovação necessária**: o que não pode se tornar efetivo ainda;
- **Evidência ou limitação**: o que foi verificado e o que permanece não verificado;
- **Próxima ação permitida**: o próximo passo dentro da autoridade existente.

Não force esse formato quando a verificação de governança puder ser aplicada sem acrescentar informação útil à resposta.

## 9. Restrições

Esta skill nunca deve:

- inventar requisitos, decisões de produto ou estado do projeto;
- transformar proposta, exemplo, hipótese ou inferência em decisão vigente;
- escolher silenciosamente uma tecnologia estrutural ainda não definida;
- alterar silenciosamente arquitetura ou decisões substanciais de modelo de dados;
- ampliar escopo adicionando funcionalidade não autorizada;
- substituir uma decisão aprovada apenas porque outra alternativa parece melhor;
- considerar silêncio ou ausência de objeção como aprovação humana;
- resolver conflito entre fontes autoritativas por suposição;
- executar uma ação reservada à aprovação humana como se já estivesse autorizada;
- redefinir procedimentos específicos de outras skills;
- alterar as regras que limitam sua própria autoridade fora do processo definido por `skill-authoring`;
- duplicar extensamente regras cuja fonte canônica pertença a outra skill.

## 10. Aprovação humana

A lista project-wide de ações sujeitas a aprovação humana está em:

[Limites de aprovação humana](references/HUMAN_APPROVAL_BOUNDARIES.md)

O agente pode analisar, reunir evidências, comparar alternativas, recomendar opções, preparar alterações para revisão quando isso não tornar uma decisão pendente efetiva, validar e reportar.

O agente não pode tratar uma ação sujeita a aprovação como decidida ou efetivá-la sem autorização humana explícita.

Alterações futuras nesta skill ou em suas fronteiras de aprovação devem seguir `skill-authoring` e permanecer `Proposed` até nova aprovação humana.

## 11. Verificações

Antes de considerar válida uma ação governada por esta skill, verifique:

- [ ] As fontes relevantes foram identificadas quando disponíveis.
- [ ] Fatos observados, inferências e propostas estão separados.
- [ ] Os estados de decisão foram preservados sem promoção silenciosa.
- [ ] A ação permanece dentro do escopo autorizado.
- [ ] As fronteiras de aprovação humana foram respeitadas.
- [ ] Conflitos entre fontes foram expostos em vez de resolvidos por suposição.
- [ ] Evidências necessárias foram verificadas ou a limitação foi declarada.
- [ ] Decisões aprovadas existentes foram preservadas.
- [ ] A rastreabilidade exigida é proporcional ao impacto.
- [ ] Regras específicas de outras skills foram referenciadas em vez de duplicadas.

## 12. Interação com outras skills

### `skill-authoring`

`skill-authoring` é a fonte canônica para criação, alteração, validação, versionamento, aprovação, divisão, consolidação, depreciação e remoção de skills.

`project-governance` não substitui esse ciclo. Ela fornece as regras project-wide de autoridade, decisão, evidência, escopo e aprovação humana que as demais skills devem respeitar, inclusive durante o trabalho sobre o sistema de skills, sem redefinir as regras específicas de `skill-authoring`.

### Skills de domínio

Skills de requisitos, arquitetura, implementação, testes, revisão, Scrum, GitHub, tecnologias e outras áreas devem:

- executar seus próprios procedimentos;
- consultar `project-governance` para limites universais de autoridade;
- manter regras específicas de domínio em sua própria fonte canônica;
- não enfraquecer unilateralmente fronteiras project-wide já aprovadas.

### Skills ainda não oficiais

Nomes ou responsabilidades de skills futuras não são tratados por esta skill como decisões vigentes.

Quando uma skill futura assumir um procedimento hoje não definido, `project-governance` deve apenas encaminhar a responsabilidade, sem copiar seu workflow.

## 13. Tratamento de incerteza e falhas

Se informação necessária estiver ausente:

1. identifique exatamente a lacuna;
2. determine se ela bloqueia a ação;
3. continue trabalho independente quando possível;
4. classifique decisão material não resolvida como `Pending Decision`;
5. não crie um valor padrão apenas para concluir a tarefa.

Se uma fonte necessária não puder ser acessada:

- marque o ponto correspondente como não verificado;
- não faça afirmações factuais que dependam dessa verificação;
- prossiga apenas quando a falta de evidência não comprometer a validade da ação.

Se fontes relevantes entrarem em conflito:

1. identifique as fontes e a regra conflitante;
2. aplique uma hierarquia somente se ela já estiver oficialmente definida;
3. não escolha uma fonte por preferência ou conveniência;
4. interrompa apenas a ação afetada;
5. solicite decisão humana quando o conflito impedir continuidade segura.
