from .base_page import BasePage


class CartPage(BasePage):
    CART_ICON_LINK = '//a[@class="shopping_cart_link"]'
    PRODUCT_PRICE = '//div[@class="inventory_item_price"]'
    PRODUCT_NAME = '//div[@class="inventory_item_name"]'
    REMOVE_PRODUCT = '//button[text()="Remove"]'
    CONTINUE_SHOPPING_BUTTON = '//button[@id="continue-shopping"]'
    CHECKOUT_BUTTON = '//button[@id="checkout"]'

    def __init__(self, driver):
        super().__init__(driver)
