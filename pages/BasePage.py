from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def send_keys(self, locator, text):
        """
        Sends keys to the element located by the given locator.
        :param locator: locator of the element
        :param text: msg to be sent to the element
        :return: None
        """
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        """
        Clicks the element located by the given locator.
        :param locator: locator of the element
        :return: None
        """
        element = self.get_element(locator)
        element.click()

    def get_text(self, locator):
        """
        Retrieves the text of the element located by the given locator.
        :param locator: locator of the element
        :return: text of the element
        """
        return self.get_element(locator).text

    def is_element_displayed(self, locator):
        """
        Checks if the element located by the given locator is displayed.
        :param locator: locator of the element
        :return: True if the element is displayed, False otherwise
        """
        return self.get_element(locator).is_displayed()

    def get_element(self, locator, timeout=10):
        """
        Retrieves the web element located by the given locator.
        :param locator: locator of the element
        :param timeout: maximum wait time in seconds
        :return: web element otherwise raises TimeoutException
        """
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def get_elements(self, locator, timeout=10):
        """
        Retrieves the list of web elements located by the given locator.
        :param locator: locator of the elements
        :param timeout: maximum wait time in seconds
        :return: list of web elements otherwise raises TimeoutException
        """
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def select_dropdown_by_text(self, locator, text):
        """
        Selects an option from a dropdown by visible text.
        :param locator: locator of the dropdown option elements
        :param text: visible text of the option to be selected
        :return: None or raises Exception if option not found
        """
        options = self.get_elements(locator)
        for option in options:
            if option.text.lower() == text.lower():
                option.click()
                break
        else:
            raise Exception(f"Option with text '{text}' not found in dropdown.")

    def select_dropdown_by_partial_text(self, locator, partial_text):
        """
        Selects an option from a dropdown by partial visible text.
        :param locator: locator of the dropdown option elements
        :param partial_text: partial visible text of the option to be selected
        :return: None or raises Exception if option not found
        """
        options = self.get_elements(locator)
        for option in options:
            if partial_text.lower() in option.text.lower():
                option.click()
                break
        else:
            raise Exception(f"Option containing text '{partial_text}' not found in dropdown.")


