import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
          url,
          headers={"user-agent": "Fake user-agent"},
          timeout=3)

        # time.sleep(1) >> testar se funciona após
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    result = []
    for article in selector.css(".entry-preview"):
        link = article.css("h2 a::attr(href)").get()
        result.append(link)
        print(link)

    return result


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
