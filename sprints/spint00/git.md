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



