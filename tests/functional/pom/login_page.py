from .base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = '//input[@id="user-name"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//input[@id="login-button"]'

    USERNAME_DATA = 'standard_user'
    PASSWORD_DATA = 'secret_sauce'

    def __init__(self, driver):
        super().__init__(driver)

    def fill_in_and_login(self):
        self.driver.fill_field(self.USERNAME_INPUT, self.USERNAME_DATA)
        self.driver.fill_field(self.PASSWORD_INPUT, self.PASSWORD_DATA)
        self.driver.click(self.LOGIN_BUTTON)