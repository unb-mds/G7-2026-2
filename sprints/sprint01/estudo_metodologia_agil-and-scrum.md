# 📚 Guia Completo: Metodologias Ágeis e Framework Scrum

## Introdução: O que é Scrum?

Scrum é um **framework ágil** que fornece um conjunto de práticas, eventos e artefatos para organizar o desenvolvimento de projetos de forma iterativa e incremental. Diferente das metodologias tradicionais (cascata), o Scrum permite adaptação rápida às mudanças, entregas frequentes de valor e melhoria contínua.

Scrum é baseado em **empirismo** e **lean thinking**, permitindo que equipes complexas entreguem produtos de forma eficiente e previsível.

---

## 1. Metodologias Ágeis: Fundamentos

### 1.1 O que são Metodologias Ágeis?

Metodologias Ágeis são abordagens de desenvolvimento que **enfatizam adaptabilidade, colaboração e entrega incremental** ao invés de planos rígidos e prazos fixos.

As metodologias ágeis surgiram como resposta aos problemas do método cascata (waterfall), onde mudanças tardias eram custosas e o feedback do cliente chegava apenas no final.

### 1.2 Diferenças: Abordagem Tradicional vs. Ágil

| Aspecto | Tradicional (Cascata) | Ágil |
|--------|----------------------|------|
| **Planejamento** | Completo no início | Iterativo e adaptável |
| **Mudanças** | Difíceis e custosas | Bem-vindas e esperadas |
| **Feedback** | Apenas no final | Contínuo |
| **Entregas** | Uma única, ao final | Frequentes e incrementais |
| **Documentação** | Extensa | Essencial e concisa |
| **Equipe** | Especialistas isolados | Auto-organizada e multidisciplinar |

### 1.3 O Manifesto Ágil

O **Manifesto Ágil** (2001) define os valores fundamentais do desenvolvimento ágil:

**Nós valorizamos:**

1. **Indivíduos e interações** mais que processos e ferramentas
2. **Software funcionando** mais que documentação abrangente
3. **Colaboração com o cliente** mais que negociação de contratos
4. **Responder a mudanças** mais que seguir um plano

**Os 12 Princípios Ágeis:**

1. Satisfazer o cliente através da entrega contínua de software de valor
2. Abraçar mudanças de requisitos, mesmo no final do desenvolvimento
3. Entregar software funcionando frequentemente (semanas/meses)
4. Colaboração diária entre desenvolvedores e stakeholders
5. Projetos devem ser construídos com pessoas motivadas
6. Comunicação face a face é o melhor método
7. Software funcionando é a principal medida de progresso
8. Processo ágil promove desenvolvimento sustentável
9. Excelência técnica e bom design aumentam a agilidade
10. Simplicidade é essencial
11. Melhores arquiteturas surgem de equipes auto-organizadas
12. Refletir regularmente e ajustar comportamentos para melhorar

---

## 2. Framework Scrum: Conceitos Fundamentais

### 2.1 O que é Scrum?

Scrum é um **framework leve e iterativo** baseado em três pilares fundamentais:

- **Transparência:** Aspectos significativos do processo são visíveis
- **Inspeção:** Monitoramento regular do progresso e ajustes
- **Adaptação:** Ajustes rápidos baseados na inspeção

### 2.2 Os Pilares do Scrum

#### Transparência
- Todas as informações sobre o produto, progresso e processo devem ser visíveis
- Todos compartilham o mesmo entendimento sobre o que está sendo feito
- Falhas são descobertas rapidamente

#### Inspeção
- Acompanhar regularmente o progresso
- Identificar problemas e variações
- Adaptar-se às mudanças
- Eventos: Sprint Review, Retrospective, Daily Scrum

#### Adaptação
- Ajustar o processo baseado na inspeção
- Modificar o produto conforme feedback
- Otimizar continuamente o trabalho e a forma de trabalhar

### 2.3 Os Valores do Scrum

| Valor | Significado |
|-------|-------------|
| **Compromisso** | A equipe se compromete com os objetivos do Sprint |
| **Foco** | Concentrar-se no trabalho da Sprint e objetivo principal |
| **Abertura** | Ser aberto sobre o trabalho, desafios e impedimentos |
| **Respeito** | Respeitar as capacidades e autonomia dos colegas |
| **Coragem** | Coragem para fazer o certo, enfrentar desafios, admitir erros |

---

## 3. Papéis no Scrum

O Scrum define **três papéis principais** que formam o Scrum Team:

### 3.1 Product Owner (Dono do Produto)

**Responsabilidades:**

- **Visão do Produto:** Define a visão clara do que o produto deve ser
- **Gerenciar o Product Backlog:**
  - Criar, manter e priorizar histórias
  - Definir os critérios de aceitação
  - Ordenar por valor de negócio
- **Comunicação:**
  - Intermediário entre stakeholders e equipe
  - Esclarecer dúvidas sobre requisitos
- **Garantir Valor:** Assegurar que o produto entrega máximo valor
- **Decisões:** Tomar decisões rápidas sobre o produto

**Características:**
- Disponível para a equipe
- Empoderado para tomar decisões
- Conhecimento profundo do domínio

### 3.2 Scrum Master

**Responsabilidades:**

- **Facilitador:** Facilita eventos do Scrum (não comanda)
- **Remover Impedimentos:** Ajuda a equipe a superar obstáculos
- **Coaching:** Ensina os princípios e práticas do Scrum
- **Proteção:** Protege a equipe de interrupções e distrações
- **Melhoria Contínua:** Facilita retrospectivas e melhorias

**Características:**
- Líder serviçal (não ditador)
- Facilitador, não gerenciador
- Promove auto-organização

### 3.3 Developers (Time de Desenvolvimento)

**Responsabilidades:**

- **Estimar:** Estimar o esforço das histórias
- **Comprometimento:** Estabelecer o Sprint Goal realista
- **Desenvolvimento:** Criar o produto durante a Sprint
- **Qualidade:** Manter altos padrões de qualidade
- **Auto-organização:** Decidir como executar o trabalho
- **Transparência:** Manter o trabalho visível

**Características:**
- Multidisciplinar (código, testes, design, etc.)
- Auto-organizado (sem hierarquias)
- Responsável pelos resultados da Sprint

---

## 4. Sprint: O Coração do Scrum

### 4.1 O que é uma Sprint?

Uma **Sprint** é um período de tempo fixo (geralmente **1 a 4 semanas**, comumente **2 semanas**) durante o qual a equipe trabalha para completar um conjunto de tarefas e entregar um incremento de produto potencialmente utilizável.

**Características de uma Sprint:**

- **Timeboxed:** Duração fixa (não deve mudar durante a Sprint)
- **Iterativa:** Múltiplas Sprints ocorrem até a conclusão do projeto
- **Incremental:** Cada Sprint entrega algo de valor (incremento)
- **Previsível:** As pessoas sabem o que esperar

### 4.2 Ciclo de Vida da Sprint

```
┌─────────────────────────────────────────────────────────┐
│                     SPRINT (1-4 semanas)                │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  [Sprint Planning]  --->  [Sprint Backlog]  --->  Daily Scrum
│        ↓                      ↓                       ↓
│    Definir             Trabalho                Síncronia &
│    Objetivo            Começar              Impedimentos
│                                                 ↓
│                          [Sprint Review] <--- Incremento
│                             ↓
│                         Demo do
│                         Produto
│                             ↓
│                    [Sprint Retrospective]
│                             ↓
│                      Melhorias para
│                      próxima Sprint
│                                                           │
└─────────────────────────────────────────────────────────┘
```

---

## 5. Eventos do Scrum (Cerimônias)

Scrum define **5 eventos** que criam regularidade e minimizam a necessidade de outros encontros.

### 5.1 Sprint Planning (Planejamento da Sprint)

**Objetivo:** Definir o que será feito durante a Sprint e como será realizado.

**Quando:** No início de cada Sprint
**Duração:** 4 horas para Sprint de 2 semanas (2 horas/semana de Sprint)
**Participantes:** Todo o Scrum Team
**Output:** Sprint Backlog + Sprint Goal

**Atividades:**

1. **Parte 1 - O QUE (1ª metade):**
   - Product Owner apresenta as histórias prioritárias
   - Discussão e esclarecimento de dúvidas
   - Equipe entende os requisitos
   - Seleciona histórias que pode completar

2. **Parte 2 - COMO (2ª metade):**
   - Equipe quebra as histórias em tarefas técnicas
   - Estima o esforço de cada tarefa
   - Define a estratégia técnica
   - Estabelece o Sprint Goal

**Exemplo de Sprint Goal:**
> "Implementar autenticação de usuários com segurança de senha de forma que os usuários possam acessar a plataforma com conta pessoal"

### 5.2 Daily Scrum (Reunião Diária)

**Objetivo:** Sincronizar a equipe e identificar impedimentos.

**Quando:** Todos os dias, no mesmo horário
**Duração:** Máximo 15 minutos
**Participantes:** Developers (PO e SM opcionais)
**Local:** Presencial ou virtual

**Estrutura - Cada desenvolvedor responde:**

1. **O que fiz ontem** para atingir o Sprint Goal?
2. **O que farei hoje** para atingir o Sprint Goal?
3. **Há impedimentos** bloqueando meu progresso?

**Anti-padrões:**
- ❌ Reunião de status com o gerente
- ❌ Resolvendo problemas durante a reunião
- ❌ Relatórios detalhados
- ✅ Sincronização rápida e identificação de bloqueios

### 5.3 Sprint Review (Revisão da Sprint)

**Objetivo:** Inspecionar o incremento entregue e obter feedback dos stakeholders.

**Quando:** No final da Sprint
**Duração:** 2 horas para Sprint de 2 semanas
**Participantes:** Todo o Scrum Team + Stakeholders
**Output:** Feedback para próxima Sprint, possíveis mudanças no Product Backlog

**Atividades:**

1. **Demonstração do Produto:**
   - Mostrar o que foi completado
   - Funcionando, não slides
   - Interativo - stakeholders testam

2. **Discussão:**
   - Como o incremento atingiu o objetivo?
   - O que falta?
   - Mudanças de requisitos?

3. **Próximos Passos:**
   - Prioridades para próxima Sprint
   - Ajustes no Product Backlog

**Importante:** A revisão é sobre o PRODUTO, não sobre a performance da equipe!

### 5.4 Sprint Retrospective (Retrospectiva da Sprint)

**Objetivo:** A equipe reflete sobre como trabalha e identifica melhorias.

**Quando:** Após a Sprint Review, antes da próxima Sprint Planning
**Duração:** 1,5 horas para Sprint de 2 semanas
**Participantes:** Scrum Team (sem stakeholders externos)
**Output:** Ações de melhoria para próximas Sprints

**Estrutura Comum - "Retro de 3 Colunas":**

```
┌──────────────┬──────────────┬──────────────┐
│      ✅      │      ⚠️      │      ❌      │
│   O que deu  │  O que pode  │   O que não  │
│      bem     │   melhorar   │      deu     │
├──────────────┼──────────────┼──────────────┤
│ Colaboração  │ Testes antes │ Falta de     │
│ Código clean │ de subir     │ planejamento │
│ Entrega no   │ Docs sem     │ Dependências │
│ prazo        │ atualização  │ externas     │
└──────────────┴──────────────┴──────────────┘
```

**Ações de Melhoria:**
- Escolher 1-3 itens para melhorar
- Ser específico (não genérico)
- Atribuir responsável
- Monitorar na próxima Sprint

---

## 6. Artefatos do Scrum

Artefatos são informações visíveis que representam o trabalho e o valor a ser entregue.

### 6.1 Product Backlog

**O que é:**
Uma lista **priorizada**, **dinâmica** e **ordenada** de tudo que pode ser feito no produto.

**Características:**

- **Propriedade:** Product Owner é responsável
- **Priorização:** Ordenado por valor de negócio
- **Dinâmico:** Muda conforme o produto evolui
- **Vivo:** Continuamente refinado
- **Não é estático:** Novos itens surgem, prioridades mudam

**Estrutura:**

```
Prioridade | ID   | Título              | Estimativa | Descrição
-----------|------|---------------------|------------|----------
1          | P-01 | Autenticação        | 13 pts     | Usuário pode...
2          | P-02 | Dashboard           | 8 pts      | Exibir dados...
3          | P-03 | Relatório mensal    | 5 pts      | Gerar PDF...
4          | P-04 | Integração API      | 21 pts     | Conectar com...
```

**Product Goal:**
A visão de longo prazo do produto. Todos os Sprints trabalham para atingir esse objetivo.

Exemplo:
> "Criar uma plataforma de gerenciamento de tarefas colaborativa que melhore a produtividade das equipes em 40%"

### 6.2 Sprint Backlog

**O que é:**
Um **subconjunto do Product Backlog** selecionado para a Sprint **MAIS as tarefas técnicas** para implementá-lo.

**Características:**

- **Propriedade:** Time de Desenvolvimento
- **Criado em:** Sprint Planning
- **Previsível:** Contém apenas o que pode ser feito
- **Descritivo:** Detalha COMO fazer, não só O QUÊ
- **Visível:** Todo o time vê o andamento em tempo real

**Exemplo:**

```
História: "Como usuário, quero fazer login com email e senha"
├── Tarefa: Criar formulário de login
├── Tarefa: Implementar validação
├── Tarefa: Integrar com banco de dados
├── Tarefa: Implementar recuperação de senha
├── Tarefa: Testes unitários
└── Tarefa: Documentar API

Sprint Goal: "Implementar autenticação segura"
```

**Sprint Goal:**
Descrito durante o Planning, é o objetivo que une todas as histórias da Sprint.

Características:
- Único e claro
- Alcançável em uma Sprint
- Motivador
- Pode ser ajustado se necessário

### 6.3 Incremento (Produto Potencialmente Entregável)

**O que é:**
Todo o trabalho **completado** durante a Sprint, **pronto para usar** (Done).

**Características:**

- **Acumulativo:** Cada Sprint adiciona ao incremento anterior
- **Pronto:** Atende à "Definition of Done"
- **Potencialmente entregável:** Pode ir para produção
- **Testado:** Sem defeitos conhecidos

**Exemplo de Incremento (fim da Sprint 1):**
- ✅ Tela de login funcionando
- ✅ Validação de senha implementada
- ✅ Testes passando
- ✅ Documentação atualizada

---

## 7. Conceitos Essenciais

### 7.1 Definition of Done (Definição de Pronto)

**O que é:**
Uma **lista de verificação** que define quais critérios uma história/tarefa deve atender para ser considerada **completa**.

**Exemplos:**

```
✅ Código implementado
✅ Testes unitários escritos e passando (>80% cobertura)
✅ Code review aprovado
✅ Sem bugs conhecidos
✅ Documentação atualizada
✅ Testado em ambiente de staging
✅ Integrado na branch main
✅ Descrito na Sprint Review
```

**Importância:**
- Garante qualidade consistente
- Evita retrabalho
- Comunicação clara
- Confiança no incremento

### 7.2 Definition of Ready (Definição de Pronto para Começar)

**O que é:**
Critérios que uma história deve atender **ANTES** de entrar na Sprint.

**Exemplos:**

```
✅ Descrição clara e completa
✅ Critérios de aceitação definidos
✅ Estimada pelo time
✅ Sem dependências bloqueantes
✅ Testável
✅ Aceita pelo Product Owner
```

### 7.3 Histórias de Usuário (User Stories)

**O que é:**
Uma descrição concisa de uma funcionalidade **do ponto de vista do usuário**.

**Formato Padrão:**

```
Como [tipo de usuário]
Quero [ação/funcionalidade]
Para que [benefício/razão]

Critérios de Aceitação:
□ Critério 1
□ Critério 2
□ Critério 3
```

**Exemplo:**

```
Como usuário registrado
Quero filtrar tarefas por categoria
Para que eu consiga encontrar rapidamente meu trabalho

Critérios de Aceitação:
□ Dropdown com categorias disponíveis
□ Lista atualiza ao selecionar categoria
□ "Todas as categorias" é seleção padrão
□ Funciona em mobile também
```

**Características (INVEST):**

- **I**ndependent (Independente de outras histórias)
- **N**egotiable (Detalhes podem ser negociados)
- **V**aluable (Entrega valor ao usuário)
- **E**stimable (Time consegue estimar)
- **S**mall (Cabe em uma Sprint)
- **T**estable (Critérios de aceitação claros)

### 7.4 Critérios de Aceitação

**O que é:**
Condições específicas que definem quando uma história está completa e correta.

**Características:**

- Mensuráveis
- Testáveis
- Livres de ambiguidade
- Do ponto de vista do usuário

**Exemplo - Bom:**
```
✅ Quando usuário clica em "Esqueci Senha"
   E insere um email válido
   Então uma mensagem de confirmação é exibida
   E um email com link de recuperação é enviado em até 5 minutos
```

**Exemplo - Ruim:**
```
❌ Implementar funcionalidade de recuperação de senha
   (Vago, não testável)
```

### 7.5 Estimativa e Pontuação

**Por que estimar?**

- Planejar quantas histórias cabem na Sprint
- Entender a complexidade do trabalho
- Criar previsibilidade
- Identificar histórias muito grandes

**Técnicas de Estimativa:**

#### Planning Poker
1. Cada pessoa recebe cartas com números (0, 1, 2, 3, 5, 8, 13, 21, ?)
2. Discutem a história
3. Todos mostram a carta simultaneamente
4. Se divergirem muito, discutem e re-estimam

#### T-Shirt Sizes
P (Pequeno), M (Médio), G (Grande), XG (Extra Grande)

#### Fibonacci
0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
(Números crescentes indicam maior incerteza)

**Velocity (Velocidade):**
A quantidade de pontos que a equipe consegue completar por Sprint.

Exemplo:
- Sprint 1: 34 pontos completados → Velocity = 34
- Sprint 2: 36 pontos completados → Velocity = 36
- Sprint 3: 32 pontos completados → Velocity = 32
- Média = 34 pontos por Sprint

### 7.6 Priorização

**Técnicas de Priorização:**

1. **MoSCoW:**
   - M (Must Have) - Essencial
   - S (Should Have) - Importante
   - C (Could Have) - Desejável
   - W (Won't Have) - Não fará agora

2. **Value vs Effort:**
```
Alto Valor + Baixo Esforço   → Fazer PRIMEIRO ⭐
Alto Valor + Alto Esforço    → Fazer depois
Baixo Valor + Baixo Esforço  → Preencher tempo
Baixo Valor + Alto Esforço   → Evitar
```

3. **Kano Model:**
   - Basics (higiênicos): Esperados
   - Performers: Diferenciais
   - Delighters: Surpresas positivas

---

## 8. Implementação Prática do Scrum

### 8.1 Fluxo Típico de uma Semana em Scrum

**Segunda-feira:**
- 09:00 - Sprint Planning (4h) - Definem o que será feito
- 13:00 - Time começa o trabalho

**Terça a Quinta:**
- 09:30 - Daily Scrum (15 min) - Sincronização
- Resto do dia - Desenvolvimento

**Sexta-feira:**
- 09:30 - Daily Scrum
- 14:00 - Sprint Review (2h) - Demonstram o que foi feito
- 16:00 - Sprint Retrospective (1,5h) - Refletem sobre melhorias
- Semana termina com planejamento pronto para semana que vem

### 8.2 Impedimentos Comuns

**Impedimento:** Algo bloqueando o progresso da equipe.

**Exemplos:**

- Falta de permissões de acesso
- Servidor de testes offline
- Dependência de outro time
- Ambiente não configurado
- Requisito pouco claro

**Ação do Scrum Master:**

1. Identificar o impedimento (na Daily)
2. Tirar do caminho rápido
3. Sugerir soluções
4. Rastrear até resolução

### 8.3 Problemas e Soluções

| Problema | Causa Raiz | Solução |
|----------|-----------|--------|
| Sprints não termina no prazo | Histórias muito grandes | Quebrar em histórias menores |
| Falta de qualidade | Pouco tempo para testes | Incluir testes na estimativa |
| Mudanças constantes | Product Owner não clarifica | Refinamento do Product Backlog |
| Equipe desorganizada | Falta de disciplina | Melhorar Daily + Retrospective |

---

## 9. Anti-padrões e Práticas Ruins

❌ **NÃO fazer:**

1. **Projeto em Cascata disfarçado de Scrum**
   - Todo planejamento no começo
   - Sem refinamento do backlog
   - Falta de feedback do cliente

2. **Daily Scrum como reunião de status com chefe**
   - Pessoas com medo de falar
   - Relatórios detalhados
   - Duração > 15 minutos

3. **Sprint como deadline rígido**
   - Empurrar histórias incompletas
   - Forçar mais itens que a capacidade
   - Comprometer qualidade

4. **Ignorar feedback da Retrospective**
   - Identificar problemas mas não agir
   - Mesmas reclamações todo Sprint
   - Sem melhorias visíveis

5. **Product Owner ausente**
   - Histórias mal definidas
   - Critérios de aceitação vagos
   - Feedback lento

---

## 10. Ferramentas para Scrum

### Opções Populares:

| Ferramenta | Tipo | Melhor Para |
|-----------|------|-------------|
| Jira | Cloud | Equipes grandes, empresariais |
| Trello | Kanban simples | Projetos pequenos, visuais |
| Asana | Gerenciamento | Múltiplos projetos |
| Azure DevOps | Completo | Microsoft stack |
| Miro | Colaborativa | Retrospectives, Planning |
| Notion | Flexível | Documentação + Tracking |
| GitHub Projects | Dev-focused | Equipes técnicas |

**Importante:** A ferramenta é só um meio. O importante é a prática do Scrum, não a tecnologia.

---


### Vídeos Educacionais

1. **[Scrum Fundamentos e Conceitos Principais](https://www.youtube.com/watch?v=1cVxiUtN6lc)**
   - Introdução completa aos conceitos e estrutura do Scrum
   - Pilares, valores e visão geral do framework

2. **[Eventos do Scrum: Sprint Planning, Daily, Review e Retrospective](https://www.youtube.com/watch?v=5ByWvpW2zw0)**
   - Detalhamento de todas as cerimônias
   - Como executar cada evento corretamente
   - Duração e participantes

3. **[Papéis no Scrum: Product Owner, Scrum Master e Desenvolvedores](https://www.youtube.com/watch?v=XfvQWnRgxG0&t=187s)**
   - Entendimento detalhado das responsabilidades
   - Características de cada papel
   - Como os papéis interagem

### Documentos Oficiais

- **Scrum Guide** (oficial): https://scrumguides.org/
- **Manifesto Ágil**: https://agilemanifesto.org/
- **Product Owner Accountability**: https://scrumguides.org/

---

## 🎯 Resumo: Os 5 W's do Scrum

| Pergunta | Resposta |
|----------|----------|
| **What (O quê)?** | Framework iterativo para entregar valor continuamente |
| **Who (Quem)?** | Product Owner, Scrum Master, Developers |
| **When (Quando)?** | Em Sprints de 1-4 semanas, eventos em dias específicos |
| **Where (Onde)?** | Em qualquer projeto complexo e adaptativo |
| **Why (Por quê)?** | Adaptar-se rápido, entregar valor, melhorar continuamente |

---

