---
name: implementation
description: Orienta a execução de mudanças de código do projeto a partir de requisitos e decisões aprovadas. Use ao implementar funcionalidades, correções ou refatorações autorizadas sem redefinir requisitos, arquitetura ou tecnologia.
metadata:
  project-version: "1.0.0"
  project-status: "defined"
  project-category: "engineering"
  project-scope: "implementation"
  agent-agnostic: "true"
---

# Implementation

## 1. Objective

Orientar agentes a transformar trabalho de implementação já autorizado em mudanças de código coerentes, limitadas ao escopo e verificáveis, sem assumir responsabilidades de requisitos, arquitetura, tecnologia, testes, revisão ou governança.

## 2. Scope

Esta skill é responsável por:

- compreender o objetivo de implementação e os critérios já definidos;
- inspecionar o código e o contexto técnico diretamente afetados;
- realizar a menor mudança coerente necessária para atender ao trabalho autorizado;
- preservar comportamento aprovado fora do escopo da mudança;
- executar verificações de implementação que já estejam definidas e disponíveis;
- registrar arquivos alterados, verificações realizadas, riscos, bloqueios e handoffs.

Ela não define requisitos, arquitetura, tecnologias, estratégia de testes, critérios de revisão, documentação de produto ou fluxo de Git/GitHub.

## 3. When to use

Use esta skill quando existir uma tarefa autorizada que exija alteração de código, configuração diretamente necessária à implementação ou refatoração explicitamente incluída no escopo.

Ative-a somente quando houver informação suficiente para identificar o comportamento esperado e as decisões técnicas que limitam a implementação.

## 4. When not to use

Não use esta skill para:

- descobrir, negociar ou redefinir requisitos;
- criar ou alterar decisões arquiteturais;
- escolher silenciosamente linguagem, framework, biblioteca, banco de dados ou outra tecnologia estrutural;
- definir política, estratégia ou cobertura de testes;
- executar o processo de code review;
- definir branch, commit, push, Pull Request ou fluxo Scrum/GitHub;
- criar regras de governança do projeto ou do sistema de skills.

Quando uma dessas responsabilidades surgir durante a implementação, encaminhe-a à skill responsável e preserve a implementação como bloqueada apenas quando a decisão for necessária para continuar.

## 5. Expected inputs

Use, quando disponíveis:

1. tarefa, requisito ou mudança autorizada;
2. critérios de aceite ou comportamento esperado já definidos;
3. decisões arquiteturais relevantes;
4. diretrizes tecnológicas aplicáveis;
5. código e arquivos afetados;
6. comandos de build, análise estática ou outras verificações já definidos pelo projeto;
7. restrições e aprovações estabelecidas pela governança do projeto.

Informação ausente não deve ser inventada.

## 6. Pre-conditions

Antes de alterar código:

1. confirme que a implementação está autorizada;
2. confirme que o objetivo e o limite da mudança são compreensíveis;
3. consulte as fontes canônicas relevantes de requisitos, arquitetura, tecnologia e governança quando existirem;
4. identifique decisões pendentes que possam bloquear a mudança;
5. preserve comportamento aprovado que não faça parte do escopo.

Se uma decisão essencial estiver ausente, pare a parte afetada da implementação e solicite a decisão apropriada.

## 7. Procedure

1. Identifique o comportamento esperado, o escopo autorizado e os critérios já definidos.
2. Inspecione o código e os arquivos diretamente relacionados antes de modificar qualquer conteúdo.
3. Consulte as decisões arquiteturais e diretrizes tecnológicas aplicáveis sem reinterpretá-las como novas decisões.
4. Identifique riscos, dependências e decisões pendentes que possam alterar a implementação.
5. Implemente a menor mudança coerente necessária para atender ao objetivo autorizado.
6. Evite refatorações amplas ou mudanças colaterais que não sejam necessárias ao trabalho atual.
7. Se surgir necessidade de alterar requisito, arquitetura, tecnologia ou escopo, interrompa a parte afetada e encaminhe a decisão à responsabilidade correta.
8. Execute somente verificações técnicas já definidas e disponíveis para a implementação; não invente comandos nem políticas de qualidade.
9. Registre o que foi alterado, o resultado das verificações executadas, limitações conhecidas, riscos restantes e handoffs necessários.
10. Entregue a mudança para as etapas responsáveis por testes, revisão, documentação ou fluxo de repositório conforme aplicável.

## 8. Expected output

A execução deve produzir:

- uma mudança de implementação coerente com o trabalho autorizado;
- indicação dos arquivos e comportamentos alterados;
- evidências das verificações realmente executadas;
- decisões pendentes e bloqueios ainda existentes;
- riscos ou limitações conhecidos;
- handoffs necessários para outras skills.

Não declare testes, revisão, build ou qualquer verificação como aprovados quando não tiverem sido realmente executados.

## 9. Constraints

Nunca:

- invente requisitos ou critérios de aceite;
- transforme uma proposta ou hipótese em decisão definida;
- altere arquitetura silenciosamente;
- escolha tecnologia estrutural ainda não definida;
- expanda o escopo sem autorização;
- faça refatoração ampla apenas por conveniência;
- replique regras cuja fonte canônica pertence a outra skill;
- ignore uma decisão pendente necessária para continuar;
- declare sucesso de verificações não executadas.

## 10. Human approval

Esta skill não cria novas fronteiras universais de aprovação.

Siga as aprovações definidas pela governança do projeto. Durante a implementação, interrompa a parte afetada e solicite decisão humana quando continuar exigir:

- redefinir requisito ou critério de aceite;
- alterar decisão arquitetural;
- escolher tecnologia estrutural ainda não definida;
- ampliar materialmente o escopo autorizado;
- contrariar uma decisão ou regra canônica existente.

Trabalho não afetado pela decisão pendente pode continuar quando isso for seguro e não gerar retrabalho relevante.

## 11. Verification

Antes do handoff, confirme:

- [ ] a mudança corresponde ao trabalho autorizado;
- [ ] não houve expansão silenciosa de escopo;
- [ ] decisões arquiteturais conhecidas foram respeitadas;
- [ ] diretrizes tecnológicas conhecidas foram respeitadas;
- [ ] verificações disponíveis e aplicáveis foram executadas ou a ausência foi registrada;
- [ ] nenhuma verificação não executada foi declarada como aprovada;
- [ ] decisões pendentes continuam explícitas;
- [ ] arquivos alterados, riscos, limitações e handoffs estão registrados.

## 12. Interaction with other skills

- `project-governance`: fonte das regras globais de autoridade, aprovação, escopo e evidência. Esta skill deve obedecê-la sem duplicar suas regras.
- `requirements`: fonte do comportamento esperado, requisitos e critérios de aceite. `implementation` consome essas definições e não as redefine.
- `architecture`: fonte das decisões estruturais. Necessidades de mudança arquitetural devem retornar a essa responsabilidade.
- `technology-guidelines`: fonte das tecnologias e convenções técnicas já definidas. `implementation` aplica essas diretrizes, mas não cria novas escolhas estruturais.
- `testing`: recebe a implementação para as atividades de teste que lhe pertencem. A divisão exata sobre criação ou manutenção de código de teste deve seguir a definição canônica dessa skill quando estiver disponível.
- `code-review`: recebe a mudança concluída para revisão; `implementation` não substitui o processo de revisão.
- `documentation`: recebe impactos documentais quando a mudança exigir atualização fora do escopo direto da implementação.
- `scrum-github`: governa rastreabilidade operacional, branch, commit, push e Pull Request quando aplicável.
- `skill-authoring`: governa qualquer mudança estrutural nesta ou em outras skills.

## 13. Handling uncertainty and failures

Quando faltar informação:

1. identifique exatamente o que está ausente;
2. determine se a lacuna bloqueia toda a implementação ou apenas uma parte;
3. continue somente o trabalho não afetado quando isso não exigir suposições;
4. registre a lacuna como decisão pendente quando exigir decisão humana;
5. encaminhe a questão à skill responsável;
6. não alegue conclusão completa enquanto houver bloqueio essencial.

Quando houver conflito entre fontes canônicas, identifique as fontes conflitantes e siga a hierarquia de governança definida. Se não existir resolução autorizada, solicite decisão humana antes de continuar a parte afetada.
