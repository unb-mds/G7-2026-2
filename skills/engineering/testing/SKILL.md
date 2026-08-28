---
name: testing
description: Planeja, prepara, executa e avalia verificações de software com base em comportamentos e critérios autorizados. Use em atividades de teste, criação ou alteração autorizada de testes, execução de verificações e análise de resultados durante o desenvolvimento.
metadata:
  project-version: "1.0.0"
  project-status: "defined"
  project-category: "engineering"
  project-scope: "software-testing-and-verification"
  agent-agnostic: "true"
---

# Testing

## 1. Objective

Estabelecer um procedimento reutilizável para verificar software de forma rastreável, usando somente comportamentos, critérios e decisões que possuam fonte autorizada, sem transformar suposições, testes existentes ou escolhas de ferramenta em requisitos do projeto.

## 2. Scope

Esta skill governa a atividade de teste e verificação quando o trabalho envolve uma ou mais destas responsabilidades:

- identificar o comportamento que precisa ser verificado e sua fonte;
- planejar verificações compatíveis com as decisões já definidas pelo projeto;
- inspecionar testes existentes e sua relação com fontes autorizadas;
- criar ou alterar testes quando essa responsabilidade estiver explicitamente autorizada;
- executar testes e outras verificações definidas ou já suportadas pelo projeto;
- analisar e classificar resultados;
- registrar evidências suficientes para reprodução e handoff;
- encaminhar falhas ou decisões para a responsabilidade apropriada.

Esta skill não define requisitos, critérios de aceite, estratégia global de testes, arquitetura, ferramentas, frameworks, cobertura mínima, comandos oficiais ou política de integração contínua.

## 3. When to use

Use esta skill quando a tarefa exigir:

- verificar se uma implementação satisfaz comportamento autorizado;
- preparar ou revisar a abordagem de verificação de uma mudança;
- criar ou alterar testes quando isso estiver dentro do escopo autorizado da tarefa;
- executar testes existentes ou verificações definidas pelo projeto;
- investigar um resultado de teste para distinguir falha do produto, do teste, do ambiente ou falta de informação;
- produzir evidências de verificação para continuidade do fluxo de desenvolvimento.

## 4. When not to use

Não use esta skill como fonte primária para:

- definir ou alterar requisitos e critérios de aceite;
- implementar silenciosamente a correção de um defeito encontrado;
- tomar decisões arquiteturais;
- escolher ou introduzir uma tecnologia de teste ainda não aprovada;
- definir políticas de qualidade, cobertura ou CI inexistentes;
- realizar code review como atividade principal;
- alterar o sistema de skills.

Quando outra skill oficial possuir a responsabilidade canônica, siga-a e mantenha aqui apenas o handoff necessário.

## 5. Expected inputs

Use as fontes disponíveis e autorizadas para a tarefa, conforme aplicável:

- requisito, critério de aceite, especificação ou comportamento esperado aprovado;
- descrição da mudança ou objetivo de verificação;
- implementação a ser verificada;
- testes existentes;
- decisões técnicas e arquiteturais relevantes;
- ferramentas, comandos, ambientes e procedimentos de teste já definidos pelo projeto;
- evidências de execuções anteriores;
- limites explícitos da tarefa e de alteração de código.

Testes existentes são artefatos de verificação e não devem ser tratados automaticamente como fonte de requisito.

## 6. Pre-conditions

Antes de executar a atividade:

1. identifique o objetivo da verificação;
2. identifique a fonte autorizada do comportamento esperado, quando a tarefa depender de comportamento esperado;
3. determine quais mecanismos de teste ou verificação já estão definidos ou disponíveis no projeto;
4. confirme se a tarefa autoriza criação ou alteração de código de teste quando isso for necessário;
5. identifique decisões ausentes que possam impedir uma verificação válida.

Se uma informação essencial estiver ausente, registre-a como `Pending Decision` ou ausência de informação e não invente o valor necessário.

## 7. Procedure

1. **Delimite o alvo da verificação.** Identifique o componente, comportamento, mudança ou risco que a tarefa pede para verificar.
2. **Localize a fonte do comportamento esperado.** Relacione cada verificação relevante a requisito, critério, especificação, decisão aprovada ou outra fonte autorizada disponível.
3. **Inspecione os testes existentes.** Determine o que já é coberto, quais premissas os testes utilizam e se essas premissas possuem autoridade suficiente para a tarefa. Não converta automaticamente um teste existente em requisito.
4. **Selecione as verificações.** Use mecanismos, níveis e ferramentas já definidos pelo projeto ou compatíveis com a tarefa sem introduzir decisão estrutural nova. Se a seleção exigir uma estratégia, ferramenta ou critério ainda não definido, escale a decisão em vez de estabelecê-la silenciosamente.
5. **Prepare testes quando autorizado.** Crie ou altere código de teste somente quando a tarefa ou uma regra oficial atribuir essa responsabilidade ao trabalho de testing. Mantenha o teste coerente com a fonte autorizada e não codifique comportamento inventado.
6. **Execute as verificações.** Use comandos, ambiente e procedimentos definidos ou já estabelecidos no projeto. Não invente um comando oficial nem introduza dependência estrutural nova apenas para concluir a atividade.
7. **Classifique cada resultado relevante.** Diferencie, com base nas evidências disponíveis:
   - verificação aprovada;
   - possível falha do produto;
   - possível falha ou inadequação do teste;
   - falha de ambiente, ferramenta ou preparação;
   - resultado inconclusivo por ausência ou conflito de informação.
8. **Investigue sem ultrapassar o escopo.** Reexecute ou isole verificações quando isso puder esclarecer a causa sem alterar silenciosamente requisitos, arquitetura ou implementação. Uma correção do produto deve ser encaminhada para a responsabilidade apropriada, salvo se a tarefa atual também autorizar explicitamente essa implementação.
9. **Registre evidências.** Informe o alvo verificado, a fonte do comportamento esperado, a verificação executada, o contexto relevante, o resultado observado e as limitações que afetem a conclusão.
10. **Faça o handoff.** Encaminhe defeitos de implementação, ambiguidades de requisito, decisões arquiteturais ou tecnológicas e outros bloqueios à skill ou decisão responsável quando ela existir.

## 8. Expected output

A atividade deve produzir, conforme aplicável:

- escopo efetivamente verificado;
- fontes usadas para determinar o comportamento esperado;
- testes criados ou alterados, quando autorizados;
- verificações ou comandos efetivamente executados;
- resultados observados;
- classificação das falhas ou incertezas;
- evidências suficientes para reprodução ou revisão;
- limitações e decisões pendentes;
- handoff necessário para continuidade do trabalho.

A conclusão deve distinguir entre "a atividade de testing foi concluída" e "o produto está apto a avançar". A segunda afirmação depende dos critérios oficiais do fluxo do projeto, quando existirem.

## 9. Constraints

Nunca:

- invente requisito, critério de aceite ou comportamento esperado;
- use um teste existente como autoridade suficiente sem analisar sua fonte;
- escolha silenciosamente framework, ferramenta, estratégia, ambiente ou tecnologia de teste ainda não definidos;
- estabeleça cobertura mínima, quantidade de testes ou métrica de aprovação sem fonte oficial;
- altere arquitetura para facilitar testes sem autorização apropriada;
- corrija silenciosamente código de produção quando a tarefa estiver limitada à verificação;
- modifique testes apenas para fazer uma execução passar quando isso contrariar a fonte autorizada;
- declare um defeito do produto quando a evidência não distinguir adequadamente produto, teste, ambiente e informação ausente;
- declare verificações que não foram executadas;
- trate resultado inconclusivo como sucesso.

## 10. Human approval

Esta skill pode orientar e executar atividades de teste que estejam dentro do escopo autorizado da tarefa e das decisões já definidas pelo projeto.

Pare e solicite decisão humana, ou faça handoff para a responsabilidade canônica, quando for necessário:

- definir ou alterar comportamento esperado;
- criar critério de aceite inexistente;
- estabelecer estratégia ou política de testes;
- introduzir framework, ferramenta ou dependência estrutural nova;
- definir cobertura mínima ou outro gate de qualidade;
- alterar arquitetura;
- resolver conflito entre fontes autorizadas;
- decidir uma fronteira de responsabilidade entre `testing` e outra skill que ainda não esteja definida.

Esta versão foi aprovada humanamente e é autoritativa no escopo que define. Decisões explicitamente pendentes continuam pendentes e não são promovidas por esta aprovação.

## 11. Verification

Antes de concluir a atividade de testing, verifique:

- [ ] o alvo da verificação está identificado;
- [ ] a fonte do comportamento esperado foi identificada ou sua ausência foi registrada;
- [ ] não foi introduzido requisito ou critério de aceite sem fonte;
- [ ] testes existentes não foram tratados automaticamente como requisitos;
- [ ] qualquer criação ou alteração de teste estava autorizada;
- [ ] somente verificações realmente executadas foram declaradas como executadas;
- [ ] resultados relevantes foram classificados com base em evidência;
- [ ] falhas de produto, teste, ambiente e informação insuficiente não foram confundidas silenciosamente;
- [ ] evidências e limitações relevantes foram registradas;
- [ ] decisões pendentes e handoffs necessários estão explícitos.

## 12. Interaction with other skills

- `requirements`: deve permanecer fonte canônica para requisitos e critérios de aceite quando essa skill existir e possuir essa responsabilidade. `testing` consome essas informações; não as redefine.
- `implementation`: pode receber handoff quando a verificação indicar correção de código de produção. A responsabilidade por criar ou alterar código de teste deve seguir a divisão oficialmente definida entre as skills; enquanto ela não estiver disponível ou aprovada, não presuma essa fronteira.
- `code-review`: revisa mudanças segundo sua responsabilidade própria quando disponível; `testing` fornece evidências de execução e não substitui review.
- `architecture`: recebe decisões que impliquem alteração arquitetural ou restrições estruturais não resolvidas.
- `technology-guidelines`: deve ser consultada quando houver orientação tecnológica oficial para ferramentas, frameworks, comandos ou ambientes de teste.
- `project-governance`: prevalece nas regras globais de autoridade, decisão e aprovação quando disponível.
- `documentation`: pode receber handoff quando resultados ou mudanças exigirem atualização documental conforme regras próprias.
- skills de processo do fluxo de desenvolvimento: determinam gates, estados e critérios de avanço quando essas regras estiverem definidas.
- `skill-authoring`: governa mudanças estruturais nesta skill e no sistema de skills.

Não duplique aqui regras cuja fonte canônica esteja em outra skill oficial.

## 13. Handling uncertainty and failures

Quando houver informação ausente, conflitante ou resultado inesperado:

1. registre o que é conhecido e a fonte utilizada;
2. identifique exatamente o dado, decisão ou evidência que falta;
3. determine se ainda existe uma verificação válida que possa ser realizada sem inventar informação;
4. execute somente a parte não bloqueada;
5. classifique o restante como inconclusivo, bloqueado ou `Pending Decision`, conforme aplicável;
6. encaminhe a decisão para a responsabilidade apropriada;
7. não altere silenciosamente produto, teste, requisito, arquitetura ou tecnologia para eliminar a incerteza.

Uma falha de teste isolada não é, por si só, prova de defeito do produto. A conclusão deve considerar a autoridade do comportamento esperado, a validade do teste e as condições de execução.
