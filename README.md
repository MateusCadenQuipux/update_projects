
# Atualizador - Projetos GA

Um atualizador para os projetos do GA , realizando git pull de todos os projetos e gerando os seus JARs.7

# Avisos
11/06/2024 - 09:19 -- O projeto de alertas está com problema de circular reference. Por enquanto, utilizaremos a branch brasil, que está com uma versão anterior sem este problema.

# Como utilizar
1. Mudar os caminhos em pathscaminhos.json para os caminhos da sua máquina. Caso um projeto seu esteja dentro do basexxxx-frontimplementacionplugins, adicione o nome do serviço dentro dos plugins do projeto. Caso contrário, remova-o.
2. Após qualquer mudança do arquivo pathscaminhos.json, rode o arquivo pathsupdate-caminhos.py.
3. Com os caminhos configurados, rode o updatesgit_pull.py para realizar o git pull de todos os projetos, além de um gulp dist daqueles que sejam frontend. Lembre-se de ter acesso a estes projetos no git e ter a VPN da colombia conectada.
4. Rode o updatesclean_install.py para gerar o JAR de todos os projetos (Em desenvolvimento)
5. Verifique os logs das operações acima dentro de logs.

# Observações
Não é necessário rodar ambos git pull e clean install, basta utilizar aqueles que sejam necessários para você no momento!

