from operator import itemgetter
from tech_news.database import search_news


# Requisito 10
def top_5_news():
    news = search_news({})
    result = sorted(news, key=itemgetter('comments_count'), reverse=True)
    if len(result) > 5:
        result = result[:5]

    return [(article["title"], article["url"])for article in result]


# Requisito 11
def top_5_categories():
    return ["category1", "category2"]
