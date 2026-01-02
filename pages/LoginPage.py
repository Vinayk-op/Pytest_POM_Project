from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    email_field = (By.ID, "Email")
    password_field = (By.ID, "Password")
    login_button = (By.XPATH, "//*[@class='button-1 login-button']")
    page_title = (By.XPATH, "//title")
    warning_message = (By.XPATH, "//*[@id='admin-notifications']//span")

    def enter_email(self, email):
        self.send_keys(self.email_field, email)

    def enter_password(self, password):
        self.send_keys(self.password_field, password)

    def click_login(self):
        self.click_element(self.login_button)

    def login_to_application(self,email_address_text,password_text):
        """
        Logs in to the application using the provided email and password.
        :param email_address_text:
        :param password_text:
        :return: 1 if login is successful, 0 otherwise
        """
        try:
            self.enter_email(email_address_text)
            self.enter_password(password_text)
            self.click_login()
            title = self.get_text(self.page_title)
            if title == "Dashboard / nopCommerce administration":
                print("Login successful.")
                return 1
        except Exception as e:
            print("Exception occurred while logging in to application: ", str(e))
            return 0

    def retrieve_warning_message(self):
        return self.get_text(self.warning_message)





