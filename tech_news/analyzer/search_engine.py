from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)
    return [(article["title"], article["url"])for article in news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    query = {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}}
    news = search_news(query)
    return [(article["title"], article["url"])for article in news]


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    news = search_news(query)
    return [(article["title"], article["url"])for article in news]
