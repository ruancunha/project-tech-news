import sys
# from tech_news.scraper import get_tech_news
# from tech_news.analyzer.search_engine import (
#   search_by_title,
#   search_by_date,
#   search_by_category,
#   search_by_tag
# )


def populate_db():
    print("Digite quantas notícias serão buscadas:")


def get_by_title():
    print("Digite o título:")


def get_by_date():
    print("Digite a data no formato aaaa-mm-dd:")


def get_by_tag():
    print("Digite a tag:")


def get_by_category():
    print("Digite a categoria:")


def end_script():
    print("Encerrando script")


def option_director(option):
    menu = [
      populate_db,
      get_by_title,
      get_by_date,
      get_by_tag,
      get_by_category,
      "top 5 noticias",
      "top 5 categorias",
      end_script
    ]
    try:
        if not 0 <= int(option) <= 7:
            print("Opção inválida", file=sys.stderr)
        else:
            menu[int(option)]()

    except ValueError:
        print("Opção inválida", file=sys.stderr)


# Requisito 12
def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.", sep='', end="")

    option = input()

    return option_director(option)
