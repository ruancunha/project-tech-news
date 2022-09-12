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

    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    result = selector.css(".next::attr(href)").get()
    if result:
        return result
    else:
        return None


# Requisito 4
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


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
