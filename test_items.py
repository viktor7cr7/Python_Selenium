import time
from selenium.webdriver.common.by import By

def test_check_language(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(10) #визуально проверяем что всё ОК
    #Проверяем наличие кнопки при помощи уникального класса
    check_button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert check_button == browser.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    print("OKAY")

