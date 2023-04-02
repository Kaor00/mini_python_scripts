import snowballstemmer


r = snowballstemmer.RussianStemmer()
print(r.stemWord('гуглить'))
print(r.stemWord('Утонченый'))

e = snowballstemmer.EnglishStemmer()
print(e.stemWord('Education'))
print(e.stemWord('Programming'))
print(e.stemWord('presentation'))
