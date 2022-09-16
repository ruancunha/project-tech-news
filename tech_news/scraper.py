import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Função para colher os dados da página
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
          url,
          headers={"user-agent": "Fake user-agent"},
          timeout=3)

        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Captura os links de cada notícia
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    result = []
    for article in selector.css(".entry-preview"):
        link = article.css("h2 a::attr(href)").get()
        result.append(link)

    return result


# Captura o botão que passa para a próxima página
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    result = selector.css(".next::attr(href)").get()
    if result:
        return result
    else:
        return None


# Captura as informações da notícia
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    result = {}
    result["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    result["title"] = selector.css("h1.entry-title::text").get().strip()
    result["timestamp"] = selector.css(".meta-date::text").get()
    result["writer"] = selector.css("span.author a::text").get()
    try:
        result["comments_count"] = int(selector.css(
          ".post-comments h5.title-block::text").re(r"\d+")[0])
    except IndexError:
        result["comments_count"] = 0

    result["summary"] = "".join(
      selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
      ).strip()

    result["tags"] = selector.css(".post-tags li a::text").getall()
    result["category"] = selector.css("span.label::text").get()

    return result


# Captura quantas noticias o usuário solicitou
#  e lança os dados delas no banco de dados
def get_tech_news(amount):
    html = fetch("https://blog.betrybe.com")
    html_list = scrape_novidades(html)
    result = []
    counter = 0
    while len(html_list) < int(amount):
        next = scrape_next_page_link(html)
        html = fetch(next)
        html_list.extend(scrape_novidades(html))

    while counter < int(amount):
        article = fetch(html_list[counter])
        result.append(scrape_noticia(article))
        counter += 1

    create_news(result)
    return result
