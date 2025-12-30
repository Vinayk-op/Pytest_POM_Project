from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    email_field = (By.ID, "input-email")
    password_field = (By.ID, "input-password")
    login_button = (By.XPATH, "//input[@value='Login']")
    warning_message = (By.XPATH, "//div[@id='account-login']/div[1]")

    def enter_email(self, email):
        self.send_keys(self.email_field, email)

    def enter_password(self, password):
        self.send_keys(self.password_field, password)

    def click_login(self):
        self.click_element(self.login_button)

    def login_to_application(self,email_address_text,password_text):
        self.enter_email(email_address_text)
        self.enter_password(password_text)
        return self.click_login()

    def retrieve_warning_message(self):
        return self.get_text(self.warning_message)





