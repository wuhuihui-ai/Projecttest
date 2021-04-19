from time import sleep

import yaml
from selenium import webdriver


class TestCookies:
    def test_get_cookies(self):
        # 复用浏览器，直接在当前页面操作
        opt1 = webdriver.ChromeOptions()
        opt1.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt1)
        driver.implicitly_wait(10)
        driver.find_element_by_id("menu_contacts").click()
        cookies = driver.get_cookies()
        with open("./data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookies, f)

    def test_start_login(self):
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("./data.yaml", encoding="UTF-8") as f:
            data = yaml.safe_load(f)
            for cookie in data:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(10)