---
name: code-review
description: Revisa alterações de código de forma rastreável contra fontes autorizadas do projeto, identificando findings verificáveis, riscos e lacunas sem assumir responsabilidades de implementação, testing ou decisão arquitetural. Use ao inspecionar diffs, commits, branches ou Pull Requests antes de sua continuidade no fluxo de desenvolvimento.
metadata:
  project-version: "1.0.0"
  project-status: "defined"
  project-category: "engineering"
  project-scope: "code-change-review"
  agent-agnostic: "true"
---

# Code Review

## 1. Objective

Revisar alterações de código por meio de um procedimento reutilizável que confronte a mudança com fontes autorizadas do projeto, identifique problemas verificáveis e comunique findings acionáveis, preservando as fronteiras de implementação, testing, arquitetura e aprovação humana.

## 2. Scope

Esta skill é responsável por:

- delimitar o conjunto de alterações que será revisado;
- identificar quais fontes disponíveis possuem autoridade para avaliar a mudança;
- inspecionar o diff e, quando necessário, o contexto de código relacionado;
- identificar defeitos, regressões, riscos e inconsistências sustentados por evidência;
- verificar conformidade com requisitos, decisões arquiteturais e diretrizes técnicas somente quando essas fontes estiverem definidas e disponíveis;
- utilizar resultados de testes e outras verificações como evidência, sem assumir o workflow de `testing`;
- distinguir findings verificáveis de sugestões opcionais;
- registrar incertezas, lacunas de evidência e limitações da revisão;
- encaminhar trabalho para a responsabilidade apropriada quando a revisão revelar necessidade de correção, testing adicional, decisão arquitetural ou decisão humana.

A revisão termina na avaliação e comunicação do resultado. Alterar diretamente código ou testes não faz parte desta skill quando ela estiver sendo executada exclusivamente como `code-review`.

## 3. When to use

Use esta skill quando houver uma alteração de código identificável a ser inspecionada, como:

- diff ou patch;
- commit ou conjunto de commits;
- branch com mudanças;
- Pull Request;
- alteração localizada apresentada para revisão antes de seguir no fluxo de desenvolvimento.

Use também quando for necessário reavaliar uma alteração depois que findings anteriores tiverem sido tratados, desde que o objetivo continue sendo revisão e não implementação.

## 4. When not to use

Não use esta skill como substituta para:

- implementar ou corrigir código;
- criar, alterar ou executar uma estratégia completa de testes;
- definir requisitos, critérios de aceite ou comportamento esperado;
- criar ou alterar decisões arquiteturais;
- escolher tecnologias, linters, formatadores ou ferramentas ainda não definidos;
- definir padrões de código ou qualidade inexistentes;
- aprovar ou rejeitar um Pull Request quando essa autoridade pertence ao processo de revisão ou aprovação do projeto;
- realizar refatoração apenas por preferência estilística.

Quando outra responsabilidade for necessária, registre o handoff em vez de absorvê-la silenciosamente.

## 5. Expected inputs

Utilize, conforme disponíveis:

1. a alteração a revisar e sua referência de escopo;
2. a intenção declarada da mudança, Issue, requisito ou critério autorizado relacionado;
3. código relacionado necessário para compreender impacto e contratos existentes;
4. decisões arquiteturais aplicáveis;
5. diretrizes técnicas ou padrões oficiais aplicáveis;
6. evidências de `testing`, análise estática ou outras verificações já produzidas;
7. contexto do fluxo de desenvolvimento que defina responsabilidades ou critérios de continuidade.

Ausência de uma dessas fontes não autoriza inventar seu conteúdo.

## 6. Pre-conditions

Antes de concluir uma revisão:

- o alvo da revisão deve ser identificável;
- deve ser possível determinar quais partes da alteração foram efetivamente inspecionadas;
- fontes aplicáveis devem ser identificadas antes de serem tratadas como regras;
- conflitos entre fontes não devem ser resolvidos silenciosamente;
- quando o comportamento esperado depender de informação indisponível, essa parte da revisão deve ser marcada como não verificada.

Se o material disponível não permitir uma revisão útil, registre a limitação e interrompa a conclusão da revisão em vez de produzir findings especulativos.

## 7. Procedure

1. **Delimite o escopo.** Identifique o diff, commits, arquivos, trechos ou versão que compõem a revisão e registre exclusões relevantes.
2. **Identifique a intenção da mudança.** Localize a descrição, requisito, Issue ou outra fonte que explique o objetivo da alteração. Se a intenção não estiver disponível, não a reconstrua por suposição.
3. **Identifique as fontes de autoridade.** Determine quais requisitos, decisões arquiteturais, contratos, diretrizes técnicas e regras de processo realmente se aplicam. Registre fontes ausentes ou conflitantes.
4. **Inspecione a alteração e o contexto necessário.** Leia o diff e amplie para código relacionado quando isso for necessário para avaliar fluxo de dados, chamadas, estados, contratos, efeitos colaterais ou impacto fora do trecho modificado.
5. **Procure problemas verificáveis.** Verifique, conforme sustentado pelas fontes disponíveis, defeitos funcionais, regressões, violações de contratos existentes, inconsistências com decisões definidas, riscos concretos introduzidos pela alteração e impactos não tratados.
6. **Considere evidências de testing e automação.** Use resultados existentes para apoiar ou enfraquecer uma hipótese de problema. Não trate sucesso de testes como prova geral de correção e não assuma que um teste existente é requisito sem fonte que lhe dê essa autoridade.
7. **Valide cada finding antes de reportá-lo.** Confirme que há localização ou alteração afetada, problema observável, justificativa, impacto ou risco e evidência suficiente. Quando aplicável, indique a regra, comportamento ou decisão autorizada que sustenta o finding e a condição necessária para considerá-lo resolvido.
8. **Separe finding de sugestão.** Trate como finding apenas o que puder ser sustentado como problema ou risco verificável. Melhorias sem obrigação autorizada podem ser apresentadas como sugestões opcionais e não devem ser convertidas em defeitos obrigatórios.
9. **Trate incerteza explicitamente.** Se uma suspeita depender de contexto ausente ou interpretação não confirmada, busque evidência adicional quando disponível. Se continuar incerta, registre-a como dúvida ou limitação, não como finding confirmado.
10. **Registre o resultado.** Liste findings confirmados, sugestões opcionais relevantes, lacunas de verificação e handoffs necessários. É válido concluir com zero findings.
11. **Determine a conclusão da atividade de review.** A revisão pode ser marcada como concluída para o escopo declarado quando o escopo planejado foi inspecionado, findings estão sustentados, limitações relevantes foram registradas e handoffs foram identificados. Isso não significa que o código esteja comprovadamente correto nem que o Pull Request esteja aprovado.

## 8. Expected output

O resultado deve permitir rastrear o que foi revisado e por quê. Inclua, de forma proporcional ao tamanho da mudança:

- escopo efetivamente revisado;
- fontes autorizadas utilizadas;
- findings, que podem ser inexistentes;
- para cada finding, informação suficiente para localizar o problema, compreender a justificativa, o impacto ou risco e a evidência disponível;
- sugestões opcionais separadas de findings, quando úteis;
- pontos não verificados, incertezas ou limitações;
- handoffs necessários para `implementation`, `testing`, arquitetura, processo ou decisão humana;
- indicação de revisão concluída ou incompleta para o escopo declarado.

Não é obrigatório impor um formulário rígido quando uma comunicação mais simples preservar essas propriedades.

## 9. Constraints

Durante `code-review`, não:

- invente requisitos, critérios de aceite ou comportamento esperado;
- invente padrões de código, qualidade, segurança ou arquitetura;
- trate preferência pessoal como regra do projeto;
- crie uma escala de severidade ou prioridade sem fonte autorizada;
- escolha silenciosamente ferramentas de análise, linters ou formatadores;
- transforme refatoração opcional em finding obrigatório sem justificativa verificável;
- considere ausência de findings como prova de correção;
- considere ausência de findings como aprovação automática de Pull Request;
- altere diretamente código ou testes enquanto operar exclusivamente sob esta skill;
- crie ou modifique testes como parte implícita da revisão;
- trate a existência de um teste como requisito por si só;
- crie ou modifique decisões arquiteturais;
- resolva conflito entre fontes autorizadas por preferência própria;
- declare como verificado algo que não foi efetivamente inspecionado.

Se o projeto definir posteriormente alguma dessas políticas em sua fonte canônica, siga essa fonte por referência em vez de duplicá-la aqui.

## 10. Human approval

Esta skill autoriza inspeção, análise e comunicação de findings dentro do escopo disponível, mas não cria novas fronteiras universais de aprovação.

Siga `project-governance` para as ações que exigem aprovação humana e a skill de processo aplicável para decisões formais do fluxo de Pull Request. Se a revisão depender de uma decisão ainda não autorizada, interrompa apenas a parte afetada, registre a lacuna e faça o handoff apropriado.

Enquanto não houver fonte canônica que atribua à revisão autoridade de aprovação ou rejeição de Pull Request, a conclusão de `code-review` deve se limitar ao resultado técnico da inspeção. A ausência de findings não substitui aprovação humana nem decisões de processo.

## 11. Verification

Antes de concluir a revisão, verifique:

- [ ] o escopo efetivamente inspecionado está identificável;
- [ ] cada finding está ligado a uma alteração ou contexto concreto;
- [ ] cada finding possui justificativa e evidência suficientes para ser verificado;
- [ ] requisitos, padrões e decisões citados possuem fonte autorizada;
- [ ] sugestões opcionais não foram apresentadas como defeitos obrigatórios;
- [ ] incertezas e partes não verificadas estão explícitas;
- [ ] resultados de testing foram usados como evidência, não como substituto de análise;
- [ ] nenhuma decisão arquitetural ou tecnológica foi criada silenciosamente;
- [ ] a revisão não modificou código ou testes sob responsabilidade exclusiva de `code-review`;
- [ ] zero findings, quando aplicável, não foi convertido em prova de correção ou aprovação automática;
- [ ] handoffs e decisões humanas necessárias estão registrados.

## 12. Interaction with other skills

### `project-governance`

Siga suas regras globais aprovadas quando a skill estiver disponível. Não replique nesta skill regras universais cuja fonte canônica seja `project-governance`.

### `requirements`

Use requisitos e critérios autorizados como fonte para avaliar comportamento. `code-review` não cria nem redefine requisitos.

### `implementation`

`code-review` identifica e comunica problemas; mudanças no código pertencem a `implementation` salvo se outra regra canônica autorizar explicitamente um fluxo diferente.

### `testing`

Use evidências produzidas por `testing` quando disponíveis e encaminhe necessidades de verificação adicional. O desenho, criação, alteração e execução do workflow de testes permanecem fora desta skill salvo regra canônica em contrário.

### `architecture`

Avalie conformidade apenas contra decisões arquiteturais existentes e aplicáveis. Questões que exigem nova decisão ou mudança arquitetural devem ser encaminhadas para a responsabilidade de arquitetura e, quando necessário, aprovação humana.

### `technology-guidelines`

Aplique padrões técnicos apenas quando estiverem definidos nessa ou em outra fonte canônica aplicável. Ausência de guideline não autoriza criar um durante a revisão.

### Skills de processo e Pull Request

Critérios formais de aprovação, reviewers obrigatórios, branch protection e outras regras de fluxo pertencem à fonte de processo correspondente. Uma revisão tecnicamente concluída não implica aprovação formal do Pull Request.

## 13. Handling uncertainty and failures

Se informação relevante estiver ausente:

1. identifique exatamente o que falta;
2. determine quais partes da revisão continuam possíveis;
3. não invente a informação faltante;
4. revise apenas o que puder ser sustentado;
5. registre a parte não verificada;
6. encaminhe a decisão ou obtenção de evidência para a responsabilidade apropriada.

Se houver fontes conflitantes:

1. cite as fontes conflitantes;
2. verifique se existe precedência oficialmente definida;
3. não escolha silenciosamente entre elas;
4. solicite resolução humana ou do processo responsável quando necessário.

Se um finding perder sustentação durante a investigação, remova-o ou reclassifique-o como incerteza ou sugestão conforme a evidência. Não preserve um finding apenas porque ele foi levantado inicialmente.
