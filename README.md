# Legião Bot - Bot externo de Raid

Ferramenta educacional para testes controlados e estudo de desenvolvimento de bots no Discord.

## AVISO IMPORTANTE (LEIA COM ATENÇÃO)

Este projeto foi desenvolvido exclusivamente para **fins educacionai**s, **pesquisa e testes em ambientes controlados**.

Permitido apenas em:
- Servidores que você possui
- Ambientes de desenvolvimento ou teste com autorização explícita

Proibido:
- Usar em servidores de terceiros
- Realizar spam, raid ou qualquer tipo de perturbação
- Violar os Termos de Serviço do Discord

Os autores não se responsabilizam por qualquer uso indevido do software.

FUNCIONALIDADES

- Interface com painel interativo (botões)
- Suporte a múltiplos idiomas (Português, Inglês e Russo)
- Sistema de persistência de preferências do usuário (JSON)
- Comandos Slash (/panel)
- Views persistentes
- Tratamento básico de rate limits
- Sistema de verificação de acesso

USO RESPONSÁVEL

Este bot deve ser utilizado apenas como ferramenta de aprendizado e testes em servidores próprios. Recomendamos fortemente:

- Testar apenas em servidores de desenvolvimento
- Manter rate limiting ativo
- Registrar logs de uso
- Nunca usar contra comunidades sem autorização

INSTALAÇÃO

1. Clone o repositório:
git clone https://github.com/SEU_USUARIO/legiao-bot.git
cd legiao-bot

2. Instale as dependências:
pip install discord.py

3. Substitua as coisas:
TOKEN = ""
PROTECTED_SERVER_ID =
INVITE_LINK = ""

4. Execute o bot:
python main.py

COMO USAR

1. Convide o bot para o seu servidor de testes
2. Use o comando: /panel
3. Selecione seu idioma
4. Utilize o painel interativo

Observação: O bot possui uma proteção para não funcionar dentro do servidor oficial (configurável).

TECNOLOGIAS UTILIZADAS

- Python 3.10+
- discord.py
- JSON para persistência
- Discord Slash Commands
- Discord UI Views

LICENÇA

Este projeto está licenciado sob a MIT License.

TERMOS LEGAIS

Ao utilizar este software, você concorda que:

- É responsável por todas as ações realizadas com o bot
- Vai utilizá-lo apenas em ambientes autorizados
- Cumprirá com os Termos de Serviço do Discord e leis aplicáveis

CONTRIBUIÇÕES

Contribuições são bem-vindas! Sinta-se à vontade para abrir Issues ou Pull Requests com melhorias, correções de bugs ou novas funcionalidades educacionais.

OBJETIVO DO PROJETO

Fornecer um recurso educacional para desenvolvedores que desejam aprender sobre:
- Desenvolvimento de bots Discord
- Interface interativa (discord.ui)
- Internacionalização (i18n)
- Boas práticas de rate limiting
- Arquitetura de aplicações com discord.py

Feito com fins educacionais. Use com responsabilidade.
