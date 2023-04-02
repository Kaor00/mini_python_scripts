from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service(executable_path='/hполный путь')
driver = webdriver.Chrome(service=s)

options = webdriver.ChromeOptions()

options.add_argument('--user-data-dir=./User_data')
options.add_argument('--profile-directory=./User_data/Profile_1')
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

driver.get("https://google.com")

driver.close()
driver.quit()

# не верно работает
