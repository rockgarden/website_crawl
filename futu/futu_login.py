

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login(login_url, login_name, login_password):
    driver = webdriver.Safari()
    driver.get(login_url)
    time.sleep(1)

    login_tab = driver.find_element_by_class_name('active')
    print(login_tab.text)
    login_tab.click()

    account_input = driver.find_element_by_class_name('u-input').find_element_by_name('email')
    password_input = driver.find_element_by_class_name('u-input').find_element_by_name('password')
    submit = driver.find_element_by_id('loginFormWrapper').find_element_by_class_name('ui-submit ui-form-submiti')

    account_input.clear()
    password_input.clear()
    account_input.send_keys(login_name)
    password_input.send_keys(login_password)

    submit.click()
    time.sleep(5)

    cookies = driver.get_cookies()
    driver.close()
    return cookies


if __name__ == '__main__':
    url = 'https://passport.futu5.com'
    name = input('请输入用户名:\n')
    password = input('请输入密码:\n')
    cookies = login(url, name, password)
    print(cookies)
