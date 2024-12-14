from selenium import webdriver
from time import sleep

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.maximize_window()


urlList = ['https://tiket.com'
        ,'https://tokopedia.com'
        ,'https://orangsiber.com'
        ,'https://idejongkok.com'
        ,'https://kelasotomesyen.com']

for url in urlList:
    driver.get(url)
    title = driver.title
    print(f'{url} - {title}')

driver.close()
