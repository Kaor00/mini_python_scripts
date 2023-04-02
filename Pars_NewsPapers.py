from newspaper import Article


article = Article(url="https://quote.ru/?utm_source=topline ")
article.download()
article.parse()

print(article.title)
print(article.authors)
print(article.publish_date)
print(article.text)

article.nlp()
print(article.keywords)

# Работает но странно
