# Projeto Tech News

## Contexto

Projeto criado durante o módulo de ciência da computação do curso da [Trybe](https://www.betrybe.com/).
Tech News é um programa criado para fazer raspagem de dados no site de notícias da Trybe (https://blog.betrybe.com). Além de coletar as informações e jogar num banco de dados NoSQL (no caso, MongoDB), faz a busca de notícias por título, data, tag ou categoria, e faz um top 5 de noticias e de categorias.

## Tecnologias utilizadas

- Python
- MongoDB

# Como rodar

Na sua máquina você deve ter:
>
> - Python3
> - MongoDB
> - Docker e Docker-compose


1. Clone o repositório e acesse a pasta com o comando:
* `git clone git@github.com:ruancunha/project-tech-news.git && cd project-tech-news`
2. Crie o ambiente virtual para o projeto:
* `python3 -m venv .venv && source .venv/bin/activate`
3. Instale as dependências:
* `python3 -m pip install -r dev-requirements.txt`
4. Monte o container Docker:
* `docker-compose up -d mongodb`
5. Use o comando para iniciar:
* `tech-news-analyzer`

> :warning:**_ATENÇÃO_**:warning: a conexão com o MongoDB foi desconfigurada ao transportar o projeto para o novo repositório. Correção do problema em breve

## Próximos passos (Roadmap)

- [ ]  Corrigir a conexão com o MongoDB
- [X]  Adicionar instruções de instalação e execução local
- [ ]  Hospedar e disponibilizar online
- [ ]  Criar testes
