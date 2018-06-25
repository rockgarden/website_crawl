# futu5.com webdriver_Safari

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.36'
}


driver = webdriver.Safari()

def login(login_url, login_name, login_password):
    """
    使用 webdriver Safari
    :param login_url:
    :param login_name:
    :param login_password:
    :return:
    """
    # driver = webdriver.Safari()
    driver.get(login_url)
    time.sleep(1)

    login_tab = driver.find_element_by_class_name('active')
    # print(login_tab.text)
    login_tab.click()

    login_form = driver.find_element_by_id("loginFormWrapper")

    account_input = login_form.find_element_by_name('email')
    # print(account_input.get_property("placeholder"))
    password_input = login_form.find_element_by_name('password')
    # print(password_input.get_property("placeholder"))
    submit = login_form.find_element_by_class_name('ui-submit ui-form-submit')  # ui-submitting ui-form-submitting
    auto_login_checkbox = login_form.find_element_by_name('autologin')
    print(password_input.get_property("placeholder"))

    account_input.clear()
    password_input.clear()

    account_input.send_keys(login_name)
    password_input.send_keys(login_password)

    # TODO: An element command could not be completed because the element is not visible on the page.
    # auto_login_checkbox.click()

    submit.click()
    time.sleep(5)

    futu_cookies = driver.get_cookies()
    driver.close()
    return futu_cookies


def sign_in_for_credits(credits_url):
    driver.get(credits_url)
    time.sleep(1)
    sign_box = driver.find_element_by_id("signBox")
    login_form = driver.find_element_by_name("loginFormWrapper")


def req_by_cookie(cookies):
    cookie_dict = dict()
    for cookie in cookies:
        cookie_dict[cookie['name']] = cookie['value']
    return cookie_dict


if __name__ == '__main__':
    url = 'https://www.futunn.com/account/credits-task'  # 'https://passport.futu5.com'
    name = input('请输入用户名:\n')
    password = input('请输入密码:\n')
    cookies = login(url, name, password)


    print(cookies)
    '''
    [
    {'domain': '.futu5.com', 'secure': False, 'expiry': 1592972626000, 'httpOnly': False, 
    'value': 'GA1.2.1718183655.1529900626', 
    'path': '/', 
    'name': '_ga'}, 
    {'domain': '.futu5.com', 'secure': False, 'expiry': 1529900686000, 'httpOnly': False, 
    'value': '1', 
    'path': '/', 
    'name': '_gat_UA-71722593-2'}, 
    {'domain': '.futu5.com', 'secure': False, 'expiry': 1529987026000, 'httpOnly': False, 
    'value': 'GA1.2.1253191714.1529900626', 
    'path': '/', 
    'name': '_gid'}, 
    {'domain': '.futu5.com', 'secure': False, 'expiry': 1545625425000, 'httpOnly': False, 
    'value': '164352eeef2794-0e50f0543e29098-1c451b26-1fa400-164352eeef3704', 
    'path': '/', 
    'name': 'UM_distinctid'}, 
    {'domain': 'www.futu5.com', 'secure': False, 'expiry': 1545625425000, 'httpOnly': False, 
    'value': '1830070412-1529899130-https%253A%252F%252Fpassport.futu5.com%252F%7C1529899130', 
    'path': '/', 
    'name': 'CNZZDATA1000431642'}, 
    {'domain': '.futu5.com', 'secure': False, 'expiry': 2160620624000, 'httpOnly': False, 
    'value': '1529900620159683', 
    'path': '/', 
    'name': 'cipher_device_id'}, 
    {'domain': '.futu5.com', 'secure': False, 'expiry': 1529902423000, 'httpOnly': False, 
    'value': 'e3f43d42-ab25-4cbf-acd9-44fead42b7bf_true', 
    'path': '/', 
    'name': 'a4201d90f5554adf_gr_session_id'}, 
    {'domain': 'www.futu5.com', 'secure': False, 'expiry': 1845260623000, 'httpOnly': False, 
    'value': '15299006237521214', 
    'path': '/', 
    'name': 'FUTU_TOOL_STAT_UNIQUE_ID'}, 
    {'domain': 'www.futu5.com', 'secure': False, 'expiry': 1529900653000, 'httpOnly': False, 
    'value': '3606278cd1af9b84d7c855b0e7f3ad06', 
    'path': '/', 
    'name': 'tgw_l7_route'}, 
    {'domain': '.futu5.com', 'secure': True, 'expiry': 1529987022000, 'httpOnly': True, 
    'value': '294152', 
    'path': '/', 
    'name': 'uid'}, 
    {'domain': '.futu5.com', 'secure': True, 'expiry': 1529987022000, 'httpOnly': True, 
    'value': 'HAvS6Nu6mBlZzPWm%2FR986rmXtxWq3Oy2%2FSoheZQ8rA5eRNz%2BnDVNPv2zqAaD1vEe%2FxfXG2BSRLEvgMgafbzJzcqU76hMaVZmnlVdpD5jspn6gfQK6fyc9g5BirRlYIlj', 
    'path': '/', 
    'name': 'web_sig'}, 
    {'domain': '.futu5.com', 'secure': False, 'expiry': 1624508620000, 'httpOnly': False, 
    'value': '6c5c4166-494b-4183-866c-3a52ecca7451', 
    'path': '/', 
    'name': 'gr_user_id'}
    ]
    
    [
    {'domain': '.futunn.com', 'secure': False, 'expiry': 253402300799000, 'httpOnly': False, 
    'value': '1529905462395451', 'path': '/', 
    'name': 'cipher_device_id'}, 
    {'domain': '.futunn.com', 'secure': False, 'expiry': 1545630261000, 'httpOnly': False, 
    'value': '1643578b8091c3-0a321f108cac338-1c451b26-1fa400-1643578b80a5cd', 'path': '/', 
    'name': 'UM_distinctid'}, 
    {'domain': 'www.futunn.com', 'secure': False, 'expiry': 1545630261000, 'httpOnly': False, 
    'value': '153811847-1529901959-https%253A%252F%252Fpassport.futu5.com%252F%7C1529901959', 'path': '/', 
    'name': 'CNZZDATA1256186977'}, 
    {'domain': 'www.futunn.com', 'secure': False, 'expiry': 1845265461000, 'httpOnly': False, 
    'value': '15299054605994544', 'path': '/', 
    'name': 'FUTU_TOOL_STAT_UNIQUE_ID'}, 
    {'domain': '.futunn.com', 'secure': False, 'expiry': 0, 'httpOnly': True, 
    'value': 'thgjkpmqj1s77pia114fqg2fm0', 'path': '/', 
    'name': 'PHPSESSID'}, 
    {'domain': '.futunn.com', 'secure': False, 'expiry': 1531201459000, 'httpOnly': True, 
    'value': 'HPkgWCP0D7cxmVz%2FlMRGIk%2FJwUBhPTEwMDAwNTM4JmI9MjAxMTM2Jms9QUtJRENXblN2cWJ4UDkza3lYdW55ZTNNYXVJUWp2angydFlEJmU9MTUzMjQ5NzQ1OSZ0PTE1Mjk5MDU0NTkmcj0yNjc2MzAyNTkmdT0mZj0%3D', 'path': '/', 
    'name': 'ci_sig'}, 
    {'domain': '.futunn.com', 'secure': False, 'expiry': 1531201459000, 'httpOnly': True, 
    'value': '294152', 'path': '/', 
    'name': 'uid'}, 
    {'domain': '.futunn.com', 'secure': False, 'expiry': 1531201459000, 'httpOnly': True, 
    'value': 'rvLpevWQeiWzaEQm4WyR1geRp%2F9ZMPFc7g1x3CuZk6JAQeQ994We0d%2B8HO4H1IeKVJ2%2BbyGf5UP1R0MD9PXRBZOHpa5xmsI6jzyfFMWVFovo1sUze2aIP%2F4tTOXDLx7i', 'path': '/', 
    'name': 'web_sig'}, 
    {'domain': 'www.futunn.com', 'secure': False, 'expiry': 0, 'httpOnly': True, 
    'value': '3ozpClqD-BOqf0UDGzVzWv1yeArcf1Lu', 'path': '/', 
    'name': '_csrf'}, 
    {'domain': 'www.futunn.com', 'secure': False, 'expiry': 1529906355000, 'httpOnly': False, 
    'value': '7587343559275141d1207d24944b360a', 'path': '/', 
    'name': 'tgw_l7_route'}
    ]

    '''
