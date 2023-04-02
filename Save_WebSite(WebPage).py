from pywebcopy import save_webpage, save_website


save_webpage(
    url="https://httpbin.org/",
    project_folder="/полный путь/Examples//",
    project_name="my_site",
    bypass_robots=True,
    debug=True,
    open_in_browser=True,
    delay=None,
    threaded=False,
)


save_website(
    url="https://httpbin.org/",
    project_folder="/полный путь/Examples//",
    project_name="my_website",
    bypass_robots=True,
    debug=True,
    open_in_browser=True,
    delay=None,
    threaded=False,
)
