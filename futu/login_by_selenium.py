# futu5.com webdriver_Safari

import time

import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CrawlFutu(object):

    def __init__(self, ):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/58.0.3029.110 Safari/537.36'
        }
        self.driver = webdriver.Safari()

    def login(self, login_url, login_name, login_password):
        """
        login function
        :param login_url:
        :param login_name:
        :param login_password:
        :return:
        """
        self.driver.get(login_url)
        time.sleep(1)

        # tab切换 div 确认选择 login href
        # <div class="navs-slider"><a href="#login" class="active">登录</a>
        login_tab = self.driver.find_element_by_class_name('active')
        login_tab.click()

        # 获取父元素 login from
        login_form = self.driver.find_element_by_id("loginFormWrapper")

        # 获取子元素 帐号元素
        account_input = login_form.find_element_by_name('email')
        password_input = login_form.find_element_by_name('password')
        # 填充帐号信息
        account_input.clear()
        password_input.clear()
        account_input.send_keys(login_name)
        password_input.send_keys(login_password)

        # 获取子元素 自动login
        auto_login_checkbox = login_form.find_element_by_name('autologin')
        # TODO: An element command could not be completed because the element is not visible on the page.
        # auto_login_checkbox.click()

        # 获取子元素 提交
        submit = login_form.find_element_by_class_name('ui-submit ui-form-submit')  # ui-submitting ui-form-submitting
        submit.click()

        time.sleep(5)

        futu_cookies = self.driver.get_cookies()

        return futu_cookies

    def sign_in_for_credits(self, credits_url):
        self.driver.get(credits_url)
        time.sleep(5)

        # # 获取元素 签到
        # sign_box = driver.find_element_by_id("signBox")
        # print(sign_box)
        # sign_box.click()

        # 获取元素 签到
        sign_href = self.driver.find_element_by_id("signIn")
        if sign_href.get_attribute('class') != "signIn none":
            sign_href.click()

    def post_article(self, article_url):
        # 获取父元素 myTasks
        my_tasks = self.driver.find_element_by_name("myTasks")
        items = my_tasks.find_elements_by_class_name("item")
        print("积分任务数:", len(items))

        # 获取子元素 发贴任务
        # <a name="gotoWork" title="发表牛牛圈" class="btn btn2 " href="https://www.futunn.com/nnq">立即发表</a>
        posting = my_tasks.find_element_by_css_selector("[title=牛牛圈精华内容]")
        if posting.get_attribute('class') != "btn btn2 none":
            posting.click()

        # 通过检查元素是否被加载来检查是否跳转网页，其中10的解释：10秒内每隔0.5毫秒扫描1次页面变化，直到指定的元素
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'publishFeedWrapper')))

        # 获取元素 发表帖子
        pub_post = self.driver.find_element_by_id("publishFeedWrapper").find_element_by_link_text("发表帖子")
        pub_post.click()

        # TODO: 弹出新窗口,须要重新获取 url
        self.driver.get(article_url)

        # TODO: 通过检查元素是否被加载来检查是否跳转网页
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'futuEditorWrapper')))

        title_input = self.driver.find_element_by_class_name("inputTxtWrapper").find_element_by_class_name("inputTxt")
        title_input.send_keys("rockgarden")

        # 切入 iframe
        self.driver.switch_to.frame("ueditor_0")
        content_input = self.driver.find_element_by_class_name("view")
        print(content_input.get_attribute('innerHTML'))
        content_input.send_keys("涨涨涨！")
        # 切出 iframe
        self.driver.switch_to().defaultContent()

    def req_by_cookie(self, cookies):
        cookie_dict = dict()
        for cookie in cookies:
            cookie_dict[cookie['name']] = cookie['value']
        return cookie_dict


def job(name, p):
    url = "https://passport.futu5.com/"
    credits_url = "https://www.futunn.com/account/credits-task"
    mobile_credits_task_url = "https://mobile.futunn.com/credits#/task"
    article_url = "https://www.futunn.com/nnq/article"

    object = CrawlFutu()

    cookies = object.login(url, name, p)

    # print(cookies)

    object.sign_in_for_credits(credits_url)

    time.sleep(5)

    # object.post_article()

    object.driver.close()


if __name__ == '__main__':
    username = "rockgarden@sina.com"  # input('请输入用户名:\n')
    password = "freestar"  # input('请输入密码:\n')
    schedule.every().day.at("8:30").do(job, username, password)
