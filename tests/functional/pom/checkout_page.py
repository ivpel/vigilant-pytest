from .base_page import BasePage


class CheckoutPage(BasePage):
    # First step checkout
    FIRST_NAME = '//input[@id="first-name"]'
    LAST_NAME = '//input[@id="last-name"]'
    ZIP_CODE = '//input[@id="postal-code"]'
    CONTINUE_BUTTON = '//input[@id="continue"]'

    # Second step checkout
    FINISH_BUTTON = '//button[@id="finish"]'
    CANCEL_BUTTON = '//button[@id="cancel"]'

    # Checkout complete
    BACK_HOME_BUTTON = '//button[@id="back-to-products"]'

    def __init__(self, driver):
        super().__init__(driver)

    def fill_personal_info(self):
        self.driver.fill_field(self.FIRST_NAME, 'Test User')
        self.driver.fill_field(self.LAST_NAME, 'Lastname')
        self.driver.fill_field(self.ZIP_CODE, '01001')
