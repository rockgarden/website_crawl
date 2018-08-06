# https://passport.futu5.com/?target=https%3A%2F%2Fmy.futu5.com%2Faccount
# https://www.futunn.com/account/credits-task

# https://www.futunn.com/site/sign-in
#
#
# class ="frBox01" id="signBox" uid="294152" >
# < a href = "javascript:;" class ="signIn none" id="signIn" > 签到领6积分 < / a >

# https://webkit.org/blog/6900/webdriver-support-in-safari-10/

# Safari的WebDriver支持默认关闭，所以要配置Safari
# Safari的WebDriver支持默认关闭。要启用WebDriver支持，请执行以下操作：
#
# 确保“开发”菜单可用。可以通过打开Safari首选项（菜单栏中的Safari>偏好设置）打开，然后打开“ 高级”选项卡，并确保选中菜单栏中的“ 显示开发”菜单复选框。
# 在开发菜单中启用远程自动化。这通过菜单栏中的Develop> Allow Remote Automation来切换。
# 授权  safaridriver启动webdriverd托管本地Web服务器的服务。要允许此操作，请/usr/bin/safaridriver手动运行一次并完成身份验证提示。
# 直接前往该目录，双击执行，如果用命令行之行会报错（报错原因待研究）

import time
import unittest

from selenium import webdriver


class CrawlFutuTest(unittest.TestCase):
    url = "https://passport.futu5.com/"
    credits_url = "https://www.futunn.com/account/credits-task"
    mobile_credits_task_url = "https://mobile.futunn.com/credits#/task"
    article_url = "https://www.futunn.com/nnq/article"

    name = "rockgarden@sina.com"  # input('请输入用户名:\n')
    password = "freestar"  # input('请输入密码:\n')

    driver = webdriver.Safari()

    def test_setup_module(self):
        CrawlFutuTest.driver = webdriver.Safari()

    def test_feature_credits_task_page_sign_in(self):
        self.driver.get("https://www.futunn.com/account/credits-task")

        sign_box = self.driver.find_element_by_id("signBox")
        print(sign_box)
        sign_href = self.driver.find_element_by_id("signIn")
        print(sign_href)
        # value = sign_box.get_attribute("value")
        # sign_box.click()
        #
        # value = sign_box.get_attribute("value")
        # self.assertTrue(len(value) > 0)
        # sign_box.submit()
        #
        # # Count the results.
        # feature_count = self.shown_feature_count()
        # self.assertTrue(len(feature_count) > 0)

    def test_login(self):
        self.driver.get(self.url)
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
        account_input.send_keys(self.name)
        password_input.send_keys(self.password)

        # 获取子元素 自动login
        auto_login_checkbox = login_form.find_element_by_name('autologin')
        # TODO: An element command could not be completed because the element is not visible on the page.
        # auto_login_checkbox.click()

        # 获取子元素 提交
        submit = login_form.find_element_by_class_name('ui-submit ui-form-submit')  # ui-submitting ui-form-submitting
        submit.click()

        time.sleep(5)

    def test_post_article(self):
        driver.get(self.article_url)
        title_input = driver.find_element_by_class_name("inputTxtWrapper")
        print(title_input.get_attribute())

        # find_element_by_tag_name("textarea")  # .find_element_by_name("title")
        title_input.send_keys("rockgarden")
        content_input = driver.find_element_by_css_selector("[contenteditable=true]")
        content_input.send_keys("涨涨涨！")

    def test_shown_feature_count(self):
        return len(self.driver.execute_script("return document.querySelectorAll('li.feature:not(.is-hidden)')"))

    def test_teardown_module(self):
        CrawlFutuTest.driver.quit()


if __name__ == '__main__':
    unittest.main
