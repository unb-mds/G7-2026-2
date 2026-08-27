---
name: architecture
description: Analisa questões arquiteturais e prepara propostas rastreáveis com base em requisitos, restrições, decisões e evidências autorizadas. Use quando uma dúvida ou mudança puder criar, alterar ou reavaliar uma decisão estrutural com impacto sistêmico sem que a própria análise torne a decisão efetiva.
metadata:
  project-version: "1.0.0"
  project-status: "defined"
  project-category: "engineering"
  project-scope: "software-architecture-analysis"
  agent-agnostic: "true"
---

# Architecture

## 1. Objective

Estabelecer um procedimento reutilizável para analisar questões de arquitetura de software, relacionando problemas estruturais a requisitos, restrições, decisões e evidências autorizadas, avaliando impactos e alternativas de forma proporcional e produzindo recomendações rastreáveis sem transformar análise em aprovação, implementação ou escolha tecnológica silenciosa.

## 2. Scope

Esta skill é responsável por:

- determinar se uma questão pertence realmente à responsabilidade de arquitetura;
- identificar o problema ou força arquitetural que motiva a análise;
- localizar requisitos, restrições e decisões autorizadas aplicáveis;
- inspecionar a arquitetura existente e seu contexto quando isso for necessário para compreender a questão;
- distinguir fatos observados, requisitos, restrições, decisões vigentes, hipóteses, alternativas, escolhas tecnológicas e detalhes de implementação;
- identificar impactos estruturais e sistêmicos de manter ou alterar uma decisão;
- avaliar alternativas materialmente relevantes usando apenas critérios sustentados por fontes autorizadas;
- explicitar trade-offs, consequências, riscos, incertezas e dependências;
- preparar uma proposta arquitetural rastreável ou recomendar, de forma fundamentada, que nenhuma mudança arquitetural seja realizada;
- identificar evidências adicionais, decisões humanas e handoffs necessários para continuidade.

Esta skill não define requisitos, escolhe tecnologias estruturais sem fonte autorizada, implementa decisões, governa testing, executa code review, define o formato documental oficial das decisões nem estabelece o fluxo de Git/GitHub.

## 3. When to use

Use esta skill quando a tarefa envolver uma questão que possa criar, alterar, substituir ou reavaliar uma decisão estrutural persistente do sistema, especialmente quando a resposta puder afetar múltiplas partes, contratos, responsabilidades, fluxos de dados, integrações ou restrições relevantes além de um detalhe local de implementação.

Use também quando `implementation`, `testing` ou `code-review` identificar uma dúvida cuja resolução dependa de nova análise arquitetural ou da alteração de uma decisão arquitetural existente.

Uma mudança não se torna arquitetural apenas por ser grande, difícil ou tecnicamente interessante. Se decisões existentes já determinarem a estrutura necessária e restar apenas executar uma mudança local, a responsabilidade principal pertence à skill adequada, como `implementation`.

## 4. When not to use

Não use esta skill como substituta para:

- descobrir, negociar ou redefinir requisitos, critérios de aceite ou requisitos não funcionais;
- escolher linguagem, framework, biblioteca, banco de dados, serviço externo, plataforma ou infraestrutura quando a atividade for primariamente uma escolha tecnológica;
- aplicar uma tecnologia já definida em uma mudança local de código;
- implementar diretamente uma decisão arquitetural;
- criar ou alterar testes como parte implícita da análise;
- revisar uma mudança de código como atividade principal;
- produzir documentação sem existir uma questão arquitetural a analisar;
- transformar toda refatoração ou reorganização local em decisão arquitetural;
- aprovar uma proposta arquitetural ou tornar uma decisão permanente efetiva.

Quando outra responsabilidade for necessária, faça o handoff correspondente em vez de absorvê-la silenciosamente.

## 5. Expected inputs

Use, conforme disponíveis e aplicáveis:

1. problema, solicitação, risco ou necessidade que motivou a análise;
2. requisitos e critérios de aceite autorizados relacionados;
3. requisitos não funcionais autorizados, quando existirem e forem relevantes;
4. decisões arquiteturais vigentes e propostas relacionadas;
5. diretrizes tecnológicas aplicáveis;
6. documentação, código, configuração, contratos, modelo de dados e integrações necessários para compreender o estado atual;
7. evidências de `testing`, `code-review`, incidentes, medições ou outras verificações relevantes;
8. restrições de escopo, autoridade e aprovação definidas pela governança do projeto.

Código legado, configuração existente ou testes existentes podem servir como evidência do estado atual, mas não devem ser tratados automaticamente como fonte normativa de requisito ou decisão.

## 6. Pre-conditions

Antes de produzir uma recomendação arquitetural:

1. delimite a questão que será analisada e o escopo afetado;
2. confirme que existe um problema, força ou decisão estrutural real a avaliar;
3. identifique as fontes autorizadas que podem fornecer requisitos, restrições, decisões e critérios relevantes;
4. verifique decisões arquiteturais existentes relacionadas quando as fontes estiverem acessíveis;
5. separe informação observada, inferência e proposta;
6. identifique decisões ausentes ou conflitos que possam impedir uma comparação válida.

Nem toda informação precisa estar resolvida para iniciar a análise. Quando uma lacuna material impedir uma conclusão sustentada, preserve-a como `Pending Decision` ou limitação e não invente um valor para completar o trabalho.

## 7. Procedure

1. **Classifique a questão.** Determine se a tarefa exige análise de uma decisão estrutural persistente ou se pertence principalmente a requirements, tecnologia, implementation, testing, code-review, documentação ou processo. Se não for arquitetural, registre o motivo e faça o handoff apropriado.
2. **Defina o problema arquitetural.** Descreva o contexto, a força, o risco ou a necessidade que exige análise. Não substitua um problema ausente por preferência técnica, tendência de mercado ou desejo genérico de "melhorar a arquitetura".
3. **Identifique fontes e estados.** Localize requisitos, restrições, decisões e evidências aplicáveis e preserve seus estados como `Defined`, `Proposed`, `Pending Decision` ou `Not Currently Applicable` quando essa classificação for relevante.
4. **Inspecione o estado atual.** Examine apenas o contexto necessário para compreender a decisão existente, seus limites e dependências. Não trate a simples existência de código como aprovação normativa da arquitetura encontrada.
5. **Separe tipos de informação.** Distinga, conforme aplicável, requisito, restrição, decisão arquitetural, escolha tecnológica, detalhe de implementação, hipótese, fato observado e evidência. Não converta uma categoria em outra por conveniência.
6. **Determine impactos relevantes.** Analise as áreas que a decisão pode afetar, como componentes, módulos, interfaces, contratos, fluxos de dados, persistência, integrações e requisitos não funcionais autorizados. Não invente dimensões de qualidade ou metas que não possuam fonte.
7. **Construa alternativas de forma proporcional.** Considere alternativas materialmente relevantes quando existirem. Não force múltiplas opções artificiais quando apenas uma alternativa sustentada for conhecida, mas também não trate a primeira ideia como decisão automática quando outras opções relevantes estiverem disponíveis.
8. **Compare usando critérios autorizados.** Relacione alternativas somente a critérios sustentados por requisitos, restrições, decisões ou evidências aplicáveis. Se um critério necessário ainda não estiver definido, registre a dependência em vez de criar um critério por preferência pessoal.
9. **Preserve a fronteira tecnológica.** A análise pode identificar capacidades ou dependências tecnológicas necessárias e avaliar consequências arquiteturais de tecnologias já definidas. Quando a decisão exigir escolher ou substituir tecnologia estrutural ainda não autorizada, registre a dependência e encaminhe-a à fonte responsável por tecnologia.
10. **Use evidências sem absorver outras skills.** Resultados de `testing`, findings de `code-review` e informações de implementação podem sustentar ou enfraquecer hipóteses arquiteturais. Se for necessária nova prova de conceito, spike, alteração de código ou verificação, proponha a necessidade e faça handoff para a responsabilidade apropriada; não execute essa mudança como parte implícita de `architecture`.
11. **Formule a conclusão.** A análise pode concluir que: nenhuma mudança arquitetural é justificável; existe uma recomendação pronta para aprovação; são necessárias mais evidências; existe uma decisão pendente; ou a questão não pertence à arquitetura.
12. **Prepare a proposta rastreável.** Quando houver recomendação de mudança, registre informação suficiente para relacionar problema, fontes, critérios, alternativas, justificativa, trade-offs, impactos, riscos, incertezas, decisões pendentes, evidências e áreas afetadas. Não force ADR ou outro formato específico sem fonte oficial que o exija.
13. **Verifique a fronteira de aprovação.** Uma recomendação ou artefato preparado permanece proposta até a aprovação exigida pela governança. Não trate análise concluída, concordância técnica ou artefato pronto como decisão arquitetural aprovada.
14. **Faça o handoff.** Após a decisão humana necessária, encaminhe mudanças de código para `implementation`, verificações para `testing`, revisão de mudanças para `code-review`, escolhas tecnológicas para a responsabilidade canônica e registros documentais ou de processo para suas respectivas fontes.

## 8. Expected output

O resultado deve ser proporcional ao impacto da questão e permitir compreender por que a conclusão foi alcançada. Inclua, quando aplicável:

- problema ou contexto arquitetural;
- escopo efetivamente analisado;
- fontes, requisitos, restrições e decisões relevantes;
- fatos e evidências utilizadas;
- alternativas materialmente relevantes consideradas, ou a razão para não haver comparação útil entre múltiplas opções;
- critérios autorizados utilizados na análise;
- recomendação, incluindo a possibilidade de manter a arquitetura atual;
- justificativa e trade-offs;
- impactos e consequências conhecidas, positivas e negativas;
- riscos e incertezas;
- áreas, componentes, contratos, dados ou integrações afetados;
- decisões ainda pendentes;
- evidências adicionais necessárias;
- condição de aprovação ou handoff necessária para continuidade.

Esse conjunto é um contrato mínimo de informação, não um formulário obrigatório. Use um formato mais simples quando ele preservar a rastreabilidade necessária.

Quando a recomendação for manter a arquitetura atual, limite a conclusão ao problema e ao escopo analisados. Não apresente essa conclusão como prova de que a arquitetura inteira do sistema é ideal ou definitivamente correta.

## 9. Constraints

Durante a atividade de arquitetura, nunca:

- invente requisito, critério de aceite, requisito não funcional ou restrição arquitetural;
- trate preferência pessoal, tendência tecnológica ou conveniência de implementação como critério autorizado;
- escolha silenciosamente estilo arquitetural, linguagem, framework, biblioteca, banco de dados, serviço externo, infraestrutura ou plataforma;
- transforme tecnologia existente no código em decisão arquitetural apenas por existir;
- trate código legado como fonte normativa automática;
- altere modelo de dados, contratos, APIs, integrações ou estrutura do sistema sem considerar as fontes e aprovações aplicáveis;
- transforme detalhe local de implementação ou toda refatoração em decisão arquitetural;
- altere código, testes ou configuração para validar uma hipótese como parte implícita desta skill;
- redesenhe partes do sistema sem relação demonstrável com o problema analisado;
- force alternativas artificiais ou critérios inexistentes apenas para completar uma comparação;
- considere uma proposta como decisão aprovada;
- considere análise concluída como aprovação automática;
- considere ausência de mudança recomendada como prova de correção global da arquitetura;
- replique extensamente regras cuja fonte canônica pertença a outra skill.

## 10. Human approval

Esta skill pode analisar, reunir e verificar evidências, comparar alternativas, recomendar uma opção e preparar uma proposta ou alteração explicitamente marcada como não efetiva.

Siga `project-governance` para as fronteiras universais de autoridade. Em particular, criar ou alterar uma decisão arquitetural permanente exige aprovação humana explícita. Mudanças substanciais de modelo de dados e outras ações listadas pela governança também preservam suas próprias fronteiras de aprovação.

Antes dessa aprovação, a recomendação deve permanecer `Proposed` ou a decisão material deve permanecer `Pending Decision`, conforme o caso.

Esta skill não autoriza implementar silenciosamente a recomendação. Quando uma decisão arquitetural for aprovada e exigir alteração de código, configuração ou estrutura executável, faça handoff para `implementation` e para as demais skills aplicáveis.

Esta versão foi aprovada humanamente e é autoritativa no escopo que define. Essa aprovação da skill não aprova automaticamente nenhuma proposta arquitetural produzida por ela; decisões materiais continuam sujeitas às fronteiras de `project-governance`.

Quando existir um mecanismo oficial para registrar decisões ou aprovações, utilize a fonte canônica correspondente. A skill não inventa ADR obrigatório, local de arquivo, status documental ou procedimento de Git/GitHub ausente.

## 11. Verification

Antes de concluir a análise, verifique:

- [ ] a questão foi classificada como arquitetural com justificativa ou encaminhada para outra responsabilidade;
- [ ] o problema arquitetural e o escopo analisado estão explícitos;
- [ ] requisitos, restrições e requisitos não funcionais utilizados possuem fonte autorizada ou sua ausência foi registrada;
- [ ] decisões arquiteturais existentes relevantes foram consideradas quando acessíveis;
- [ ] código, configuração e testes existentes não foram tratados automaticamente como autoridade normativa;
- [ ] alternativas foram consideradas de forma proporcional, sem opções artificiais;
- [ ] critérios de comparação possuem fonte autorizada;
- [ ] nenhuma tecnologia estrutural foi escolhida silenciosamente;
- [ ] trade-offs, impactos, riscos e incertezas relevantes estão registrados;
- [ ] nenhuma alteração de código ou teste foi executada como parte implícita da análise arquitetural;
- [ ] recomendações permanecem propostas até a aprovação aplicável;
- [ ] análise concluída não foi convertida em aprovação automática;
- [ ] a possibilidade de manter a arquitetura atual foi considerada quando sustentada pelas evidências;
- [ ] decisões pendentes, limitações e handoffs estão explícitos.

## 12. Interaction with other skills

### `project-governance`

É a fonte project-wide de autoridade, evidência, escopo e aprovação humana. `architecture` aplica essas fronteiras e não as redefine.

### `requirements`

Quando disponível como fonte canônica, fornece requisitos, critérios de aceite e requisitos não funcionais autorizados. `architecture` consome essas definições e não as inventa nem redefine.

### `technology-guidelines`

Quando disponível como fonte canônica, governa escolhas e diretrizes tecnológicas. `architecture` pode identificar capacidades necessárias, dependências e consequências estruturais, mas não substitui a responsabilidade de definir ou trocar tecnologia estrutural.

### `implementation`

Recebe mudanças de código, configuração ou estrutura executável decorrentes de decisões já autorizadas. `architecture` termina na análise, proposta, aprovação necessária e handoff; não absorve a implementação.

### `testing`

Pode fornecer evidências para avaliar uma hipótese arquitetural e receber necessidades de verificação. `architecture` não define estratégia de testes nem cria testes como parte implícita da análise.

### `code-review`

Pode identificar uma possível violação ou necessidade de nova decisão arquitetural e encaminhá-la para esta skill. `architecture` não substitui a revisão do diff nem transforma um finding em decisão sem análise e aprovação apropriadas.

### `documentation`

Quando existir uma fonte canônica para documentação, ela deve governar formato, localização e manutenção dos registros. `architecture` define a informação necessária para uma proposta rastreável, mas não inventa um formato documental oficial.

### Skills de processo e Pull Request

Governam estados, registros operacionais, aprovações formais e fluxo Git/GitHub quando essas regras estiverem definidas. Uma recomendação arquitetural pronta não equivale, por si só, a aprovação ou integração no repositório.

### `skill-authoring`

Governa alterações estruturais nesta ou em outras skills. Questões de arquitetura do próprio sistema de skills retornam a essa responsabilidade quando envolverem a governança das skills.

## 13. Handling uncertainty and failures

Quando informação necessária estiver ausente:

1. identifique a lacuna e sua fonte esperada;
2. determine qual parte da análise ela bloqueia;
3. continue somente a análise independente que permaneça válida sem suposições;
4. classifique decisão material não resolvida como `Pending Decision` quando aplicável;
5. não invente requisito, critério, restrição, tecnologia ou decisão para preencher a lacuna;
6. registre a evidência ou decisão necessária para continuar.

Quando fontes relevantes entrarem em conflito:

1. identifique as fontes e o ponto de conflito;
2. aplique precedência somente quando ela estiver oficialmente definida;
3. não escolha uma fonte por preferência técnica;
4. interrompa apenas a parte afetada;
5. encaminhe a resolução à autoridade apropriada.

Quando a análise não encontrar justificativa suficiente para alterar a arquitetura, registre a manutenção da decisão ou estrutura atual como recomendação limitada ao escopo analisado. Quando a evidência for insuficiente até mesmo para essa conclusão, registre o resultado como inconclusivo em vez de inferir estabilidade ou correção.
