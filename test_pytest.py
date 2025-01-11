'''
Author: Daisy
Tugas:
Buat Automation test untuk per-login-an dari web berikut.
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.firefox.options import Options
import pytest 

@pytest.fixture
def browser():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)

    driver.implicitly_wait(5)
    driver.maximize_window()

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.get(url)

    yield driver

    driver.close()


data_login_valid = [
    ('Admin', 'admin123', 'Dashboard')
]

@pytest.mark.parametrize('username, password, valuetoverify', data_login_valid)
def test_login_happyflow(username, password, valuetoverify, browser):
    # page login
    browser.find_element(By.NAME,"username").send_keys("Admin")
    browser.find_element(By.NAME, "password").send_keys("admin123")
    browser.find_element(By.CSS_SELECTOR, "button.orangehrm-login-button").click()

    current_url = browser.current_url
    title = browser.find_element(By.CSS_SELECTOR, "h6.oxd-topbar-header-breadcrumb-module").text

    assert current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    assert title == valuetoverify
    

data_login_invalid = [
    ('Admin', 'salah', 'Invalid credentials'),
    ('salah', 'admin123', 'Invalid credentials'),
    ('salah', 'salah', 'Invalid credentials'),
    ('Admin', '', 'Required')
]

@pytest.mark.parametrize('username, password, err_msg', data_login_invalid)
def test_negative_login(username, password, err_msg, browser):
    '''
    scenarios:
    Login dengan-
    [scenario 1] username correct - pass wrong
    [scenario 2] username wrong - pass correct
    [scenario 3] username wrong - pass wrong
    [scenario 4] username correct - pass empty
    '''

    # page login
    browser.find_element(By.NAME,"username").send_keys(username)
    browser.find_element(By.NAME, "password").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "button.orangehrm-login-button").click()    

    try:
        # 1st check: is "Invalid credentials" element present?
        error = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-alert-content-text"))).text
    
    except TimeoutException:
        try:
            # if "Invalid credentials" not present, then check the "Required" element
            error = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-input-group__message"))).text

        except TimeoutException:
            print("kedua error elements ga ada")

    assert error == err_msg

