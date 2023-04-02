import schedule as sh


def do_something():
    print("lets take a tea break!")


sh.every(1).seconds.do(do_something)
sh.every().minute.at(":17").do(do_something)
sh.every().hour.do(do_something)
sh.every().day.at("10:30").do(do_something)
sh.every().monday.do(do_something)
sh.every().friday.at("18:00").do(do_something)


while True:
    sh.run_pending()
