### DESCRIÇÃO DO PROJETO

Para a atividade foi selecionado um sistema de abertura e fechamento de chamados, desenvolvido utilizando HTML e Python, com as bibliotecas Flask disponíveis. O objetivo do trabalho é demonstrar de forma simplificada como é o funcionamento de uma arquitetura MVC de forma prática.

Foi definido que uma solução adequada de microserviço para o projeto seria a implementação de um sistema de envio de e-mails, responsável por notificar os usuários sempre que ocorressem atualizações no sistema — como a criação ou fechamento de chamados e o cadastro de novos usuários. O microserviço de envio de e-mails é acionado pelo sistema principal, desenvolvido com arquitetura MVC, sempre que um desses eventos é registrado. A comunicação ocorre de forma síncrona, por meio de uma requisição HTTP do tipo POST realizada pelo controller do Flask. Essa requisição envia um payload em formato JSON contendo informações como o e-mail do destinatário, o assunto e a mensagem a ser enviada. Ao receber a requisição, o microserviço processa os dados e realiza o envio do e-mail, retornando uma resposta com o status da operação para o sistema principal.

### INSTRUÇÕES

1. Instalação das bibliotecas python disponíveis no arquivo "requirements.txt" (Flask; Flask-SQLAlchemy; Flask-Login);
2. Utilizar o comando *python run.py* no terminal do VSCode para inicialização do servidor;
3. Abrir o link disponibilizado no terminal;
4. Utilizar as credenciais de usuário: **admin** e senha: **admin123**.

