# :abcd: Projeto Segurança da Informação 
[![](https://img.shields.io/badge/python-v3.8-blue)](https://github.com/DevExpress/testcafe) ![](https://img.shields.io/badge/docker%20build-automated-066da5)

## Membros:
 - Maicon Silva - [Github](https://github.com/maiconandsilva);
 - Andre Rodrigues - [Github](https://github.com/Andrerodrigues0018);
 - William Barreto - [Github](https://github.com/WilliamBarretoH);
 - Gabriel Costa - [Github](https://github.com/c0sta);
 - Raphael Ribeira - [Github](https://github.com/raphariibeira);
 - Pablo Gabriel - [Github](https://github.com/PGabriel-MB);
 - Gustavo Robert - [Github](https://github.com/gu-robert);
 - Mauro Toshiuki - [Github](https://github.com/maurosakugawa).

## Objetivos: :dart:

Projeto designado à matéria de Segurança da Informação, lecionado pelo professor Eduardo Sakaue, trouxe consigo o desafio de implementar uma solução para tópicos abordados na Lei Geral de Proteção de Dados (LGPD).

A Lei Geral de proteção de Dados, de caráter Multidisciplinar e extraterritorial, é a legislação que regula a coleta, armazenamento, tratamento e compartilhamento de dados pessoais, impondo um padrão mais elevado de proteção e penalidades significativas para o não cumprimento da norma. Ela é um marco legal de grande impacto, englobando instituições públicas e privadas.

Essa lei surge com a finalidade de proteger direitos fundamentais, como:

- Privacidade;
- Autodeterminação informativa;
- Liberdade de expressão, de informação, de comunicação e de opinião;
- Inviolabilidade da intimidade da honra e da imagem;
- Desenvolvimento econômico, tecnológico e a inovação;
- A livre iniciativa, a livre concorrência e a defesa do consumidor;
- Direitos humanos: o livre desenvolvimento da personalidade, dignidade e o exercício da cidadania pelas pessoas naturais.

## Abordagem :mag:

> Estudo de caso sobre Anonimização de Dados sensíveis dos clientes da Dell Store usando [PostgreSQL](https://www.postgresql.org/) 

Seguindo um conceito para maior seguranca dos dados, nesse projeto foi feito uma pseudoanonimizacao na base de dados, que consiste em separar dados sensiveis do cliente dos dados de estatisticas para a empresa, armazenando-os em bancos diferentes resultando em mais seguranca na base de dados dos clientes, pois o mesmo conta com mais criptografia. 

Com isso e possivel acessar e alterar dados estatisticos sem a necessidade de violar a privacidade dos clientes. Tambem, facilitando a exclusao dos dados do cliente, quando o mesmo a solicita, pois conseguimos desvincular seus dados sensiveis dos dados importantes para a empresa.  


## :cd: Dependências

Esta versão requer o Docker e Docker-Compose. Se você está utilizando o Windows [clique aqui](https://docs.docker.com/docker-for-windows/install/).

``` bash
docker-compose version 1.27.4
Docker version 19.03.13
```
#### Principais bibliotecas Python usadas

| Biblioteca | Versão                               |
|-------|--------------------------------------|
| cryptography | 3.2.1 |
| Flask     | 1.1.2                      |
| Flask-SQLAlchemy    | 2.4.4 |
| Flask-WTF | 0.14.3 |
| Jinja2    | 2.11.2             |
| psycopg2     | 2.8.6                  |
| SQLAlchemy    | 1.3.19        |
| SQLAlchemy-Utils | 0.36.8 |
| WTForms-Alchemy | 0.17.0 |

##  :rocket: Inicialização 

``` bash
# Executar aplicação pela primeira vez 
docker-compose up --build -d

# Executar
docker-compose up -d

# URL de acesso 
url: http://127.0.0.1/
```
## :gear: Processo de Desenvolvimento
Como framework de desenvolvimento dessa aplicação foi aplicada o Scrum - Metodologia Ágil de Desenvolvimento de softwares, e as entregas desse projeto foram
divididas em sprints, e para controle dessas, foram utilizados ferramentas como o Nosso [Board no Trello](https://trello.com/b/PyOFWkYC/si) e também nossa Planilha de [BurnDown](https://docs.google.com/spreadsheets/d/1tDluxMUywgS5cD-ZQRGEMXdzJRsSD_wp/edit#gid=699714556).


### Sprint 1
**Destinada à pesquisas e à configuração inicial do projeto.**

- [x] Inicialização do projeto.
- [x] Configuração do ambiente em Docker (serviços de banco de dados e aplicação Flask)

### Sprint 2
**Destinada à criação de rotas e telas principais.**

- [x] Exclusão de usuário com técnica de anonimização
- [x] Rota de listagem dos dados dos clientes pós anonimização.

### Sprint 3
**Destinada à criação de rotas e telas para registro e autenticação.**
g
- [x] Rota para criar conta, login e visualizar dados
- [x] Rota de requisição para deletar conta de usuário (para anonimizar e pseudonomizar)

### Sprint 4
**Destinada à Pseudonimizacao dos dados do usuário/cliente através de requisição e criação de máscaras após requisição para deletar conta (anonimização com fim analítico).**

- [x] Pseudonimização dos dados do usuário
- [x] Aplicar máscaras para os campos e-mail e telefone
- [x] Aplicar máscaras para visualização de dados pessoais na conta do usuario

### [Sprint 5](https://github.com/maiconandsilva/LGPD-compliant-website/milestone/1)
_A partir da sprint 5 o gerenciamento das tarefas mudou para o [Kanban](https://github.com/maiconandsilva/LGPD-compliant-website/projects/1?fullscreen=true) e o [Milestones com Issues](https://github.com/maiconandsilva/LGPD-compliant-website/milestones) do Github._

**Destinada à [revisão da documentação](https://github.com/maiconandsilva/LGPD-compliant-website/issues/5) e à funcionalidade de [solicitação de relatório](https://github.com/maiconandsilva/LGPD-compliant-website/issues/3).**

- [Tarefas abertas](https://github.com/maiconandsilva/LGPD-compliant-website/milestone/1)
- [Tarefas fechadas](https://github.com/maiconandsilva/LGPD-compliant-website/milestone/1?closed=1)

### [Sprint 6](https://github.com/maiconandsilva/LGPD-compliant-website/milestone/2)
**Destinada à correção de bugs, implementação final de telas e demonstração do projeto.**

- [Tarefas abertas](https://github.com/maiconandsilva/LGPD-compliant-website/milestone/2)
- [Tarefas fechadas](https://github.com/maiconandsilva/LGPD-compliant-website/milestone/2?closed=1)

## :anchor: Fontes
- Exemplo da Empresa Dell Store de [Banco de dados ](https://linux.dell.com/dvdstore/) utilizado para anonimização.

## :lock: Licença

Consulte o arquivo [LICENSE](LICENSE) para obter os direitos e limitações da licença (FATEC).

