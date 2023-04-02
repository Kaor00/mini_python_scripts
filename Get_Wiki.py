import wikipedia


wikipedia.set_lang("ru")
print(wikipedia.summary("Elon Musk"))
print(wikipedia.summary("Python"))

lv = wikipedia.page("Las Vegas")

print(lv.title)
print(lv.url)
print(lv.content)
