from requests_html import AsyncHTMLSession


asession = AsyncHTMLSession()


async def get_pythonorg():
    r = await asession.get("https://python.org/")
    return r


async def get_reddit():
    r = await asession.get("https://reddit.com/")
    return r


async def get_google():
    r = await asession.get("https://google.com/")


results = asession.run(get_pythonorg, get_reddit, get_google)
# results

for result in results:
    print(result)
