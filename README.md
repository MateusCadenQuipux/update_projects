
# Atualizador - Projetos GA

Um atualizador para os projetos do GA , realizando git pull de todos os projetos e gerando os seus JARs.7

## Avisos
18/06/2024 - 16:37 - Mateus Caden -- O projeto de alertas voltou para a branch development!
11/06/2024 - 09:19 - Mateus Caden -- O projeto de alertas está com problema de circular reference. Por enquanto, utilizaremos a branch brasil, que está com uma versão anterior sem este problema.

## Como utilizar
1. Mudar os caminhos em /paths/caminhos.json para os caminhos da sua máquina. Caso um projeto seu esteja dentro do basexxxx-front/implementacion/plugins, adicione o nome do serviço dentro dos plugins do projeto. Caso contrário, remova-o.
2. Após qualquer mudança do arquivo /paths/caminhos.json, rode o arquivo /paths/update-caminhos.py.
3. Com os caminhos configurados, rode o /updates/git_pull.py para realizar o git pull de todos os projetos, além de um gulp dist daqueles que sejam frontend. Lembre-se de ter acesso a estes projetos no git e ter a VPN da colombia conectada.
4. Rode o /updates/clean_install.py para gerar o JAR de todos os projetos **(Em desenvolvimento)**
5. Verifique os logs das operações acima dentro de /logs.

## Observações
Não é necessário rodar ambos git pull e clean install, basta utilizar aqueles que sejam necessários para você no momento!

Legendas para as urls dentro do /paths/caminhos.json
	1. base_url -> caminho ate as pastas do BO e FrontOffice
	2. bo -> caminhos entre base_url e a pasta com os projetos do bo
	3. frontoffice -> caminho entre base_url e a pasta com os projetos do frontoffice

