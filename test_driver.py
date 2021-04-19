from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDriver():
    def setup(self):
        self.driver = webdriver.Edge(executable_path='D:\wuhuihui\Installation package\driver\msedgedriver.exe')
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(3)

    # def teardown(self):
    #     self.driver.quit()

    def test_method(self):
        # self.driver.find_element(By.ID, "s-top-left")
        # self.driver.find_element(By.XPATH, '//*[@id="s-top-left"//a[1]]')
        # self.driver.find_element(By.CSS_SELECTOR, '#s-top-left a:nth-child(3)')
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_css_selector("#su").click()

        ele = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "MeterSphere - 开源自动化测试平台")))
        self.driver.find_element_by_link_text("MeterSphere - 开源自动化测试平台").click()
        assert ele
