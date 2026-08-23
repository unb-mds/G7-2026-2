Guia Completo de Git e GitHub

Introdução: o que é Git?

Git é um sistema de controle de versão distribuído. Ele registra o histórico de alterações de um projeto, permitindo:

Voltar a versões anteriores do código
Trabalhar em paralelo com outras pessoas sem sobrescrever o trabalho alheio
Rastrear quem alterou o quê e quando

Diferente de um controle de versão centralizado, no Git cada máquina tem uma cópia completa do repositório (histórico incluído), não só os arquivos atuais.


git --version   # verifica se o git está instalado

Conceitos básicos do Git

Antes de usar os comandos, é importante entender as áreas de trabalho do Git:

Área	O que é
Working Directory	Seus arquivos no dia a dia, onde você edita
Staging Area (Index)	"Área de espera" com o que será incluído no próximo commit
Repository (.git)	Histórico de commits já salvos

Fluxo geral:

Working Directory --(git add)
--> Staging Area --(git commit)
--> Repository

Outros conceitos-chave:

Repositório (repo): pasta versionada pelo Git
Commit: um "snapshot" (foto) do projeto em um momento específico
Branch: uma linha independente de desenvolvimento
HEAD: ponteiro para o commit/branch atual
commit 3 — Instalação e configuração

Instalação (Linux/Debian):



sudo apt update
sudo apt install git

Após instalar, configure seu nome e e-mail (usados em todo commit que você fizer):



git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"

Ver as configurações atuais:

git config --list

Criando repositórios

Para transformar uma pasta em um repositório Git:

git init

Isso cria uma pasta oculta .git/ que guarda todo o histórico e configurações do repositório.

Para verificar o estado atual do repositório (arquivos modificados, novos, etc.):


git status

Colocando arquivos no stage

Depois de criar ou modificar arquivos, eles ficam como "não rastreados" ou "modificados". Para movê-los para a staging area:


git add nome-do-arquivo.txt   # adiciona um arquivo específico
git add .                     # adiciona todos os arquivos modificados/novos

Verifique o que está no stage com:

git status


Fazendo commits

Um commit registra permanentemente o que está no stage no histórico do repositório.


git commit -m "Mensagem descrevendo a alteração"

Boas práticas para mensagens de commit:

Escreva no imperativo: "Adiciona validação de formulário" (não "Adicionado")
Seja claro e objetivo
Um commit deve representar uma mudança lógica coesa

Ver o histórico de commits:

git log
git log --oneline   # versão resumida, uma linha por commit

Desfazendo commits

Existem várias formas de desfazer um commit, dependendo do que você precisa:


git commit --amend            # corrige/edita o último commit (mensagem ou conteúdo)

git reset --soft HEAD~1       # desfaz o commit, mantém alterações no stage
git reset --mixed HEAD~1      # desfaz o commit, mantém alterações no working directory (padrão)
git reset --hard HEAD~1       # desfaz o commit E descarta as alterações (cuidado, é destrutivo)

git revert <hash-do-commit>   # cria um novo commit que desfaz as mudanças de um commit específico
# (seguro para usar em histórico já compartilhado)

gitignore

O .gitignore informa ao Git quais arquivos ou pastas devem ser ignorados.

É comum ignorar:

Dependências;
Arquivos de build;
Logs;
Arquivos temporários;
Arquivos de configuração local;
Credenciais;
Variáveis de ambiente.

Arquivo que já está sendo rastreado

Se um arquivo já foi adicionado ao Git, simplesmente colocá-lo no .gitignore não faz o Git parar de rastreá-lo.

git rm --cached nome-do-arquivo

Criando branches

Branches permitem desenvolver funcionalidades isoladamente, sem afetar a branch principal (geralmente main ou master).

bash
git branch                     # lista as branches existentes
git branch nome-da-branch      # cria uma nova branch
git checkout nome-da-branch    # muda para a branch
git checkout -b nome-da-branch # cria e já muda para a branch (atalho)

# Forma mais atual (Git >= 2.23):


git switch nome-da-branch
git switch -c nome-da-branch   # cria e muda

Fundindo branches (merge)

Depois de terminar o trabalho em uma branch, você pode juntá-la de volta à branch principal:

git checkout main
git merge nome-da-branch

Tipos de merge:

Fast-forward: quando não houve divergência, o ponteiro só avança
Merge commit (3-way): quando as branches divergiram, o Git cria um commit específico para juntar as duas

Após o merge, se a branch não for mais necessária:

git branch -d nome-da-branch

Iniciando com GitHub

GitHub é uma plataforma de hospedagem de repositórios Git na nuvem, usada para colaboração.

Conectando um repositório local a um repositório remoto no GitHub:


git remote add origin https://github.com/usuario/repositorio.git
git remote -v                      # lista os remotos configurados

git push -u origin main            # envia os commits locais para o GitHub (-u define o upstream)

Para trazer um repositório do GitHub para a máquina local:

git clone https://github.com/usuario/repositorio.git_

Simulando múltiplos devs

Ao trabalhar em equipe, é comum usar duas pastas locais (ou clones) simulando "devs" diferentes para praticar o fluxo colaborativo:


git pull origin main     # traz e já integra as atualizações do remoto
git fetch origin         # apenas baixa as atualizações, sem integrar automaticamente

Fluxo típico de trabalho em equipe:

git pull para atualizar antes de começar a trabalhar
Criar uma branch para a sua tarefa
Fazer commits normalmente
Enviar (git push) a branch para o GitHub
Abrir um Pull Request para revisão

Fazendo Pull Request (PR)

Pull Request é uma solicitação para que as alterações de uma branch sejam revisadas e integradas a outra (geralmente main).

Fluxo geral:


git checkout -b minha-feature
# ... altera arquivos, faz commits ...
git push -u origin minha-feature

Depois, no GitHub:

Acesse o repositório
Clique em "Compare & pull request"
Descreva as alterações feitas
Aguarde revisão/aprovação
Faça o merge do PR na branch principal

PRs facilitam revisão de código, discussão sobre as mudanças e histórico organizado de contribuições.



