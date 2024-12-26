'''
Author: Daisy
Tugas:
Buat Automation untuk setiap button dan handlenya yg untuk web demoqa.com/alert
buat d repo github ya.'''


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.maximize_window()

url = "https://demoqa.com/alerts"

driver.get(url)

#----------------------------------------------------------------------------------
#1) handle 1st alert button - "Click Button to see alert"
driver.find_element(By.ID,"alertButton").click()
sleep(1)
driver.switch_to.alert.accept()
sleep(2)

#----------------------------------------------------------------------------------
#2) handle 2nd alert button - "On button click, alert will appear after 5 seconds"
driver.find_element(By.ID,"timerAlertButton").click()
try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    print(f"Alert text: {driver.switch_to.alert.text}") 
    sleep(1)
    driver.switch_to.alert.accept()
    sleep(2)

except TimeoutException:
    print("Timeout: Elemen tidak muncul dalam batas waktu!")

#----------------------------------------------------------------------------------
#3) handle 3rd alert button - "On button click, confirm box will appear"

#step 1 - try click OK in alert
driver.find_element(By.ID,"confirmButton").click()
sleep(1)
driver.switch_to.alert.accept()
sleep(2)

#step 2 - try click Cancel in alert
driver.find_element(By.ID,"confirmButton").click()
sleep(1)
driver.switch_to.alert.dismiss()
sleep(2)

#----------------------------------------------------------------------------------
#4) handle 4th alert button- "On button click, prompt box will appear"
driver.find_element(By.ID,"promtButton").click()
driver.switch_to.alert.send_keys("Daisy")
driver.switch_to.alert.accept()
sleep(2)

driver.close()
