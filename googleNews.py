from GoogleNews import GoogleNews


news = GoogleNews(period="5d", lang="ru")
news.search("exchange")
result = news.result()

for i in result:
    print(f"Title: {i['title']}")
    print(f"Data/Time: {i['date']}")
    print(f"Description: {i['desc']}")
    print(f"Link: {i['link']}")
    print("#"*20)
