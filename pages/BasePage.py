from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def send_keys(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def get_text(self, locator):
        return self.get_element(locator).text

    def is_element_displayed(self, locator):
        return self.get_element(locator).is_displayed()

    def get_element(self, locator, timeout=10):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

