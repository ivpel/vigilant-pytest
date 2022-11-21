from .base_page import BasePage


class CategoryListPage(BasePage):

    PRODUCT_CARD = '//div[@class="inventory_item"]'
    PRODUCT_NAME = '//div[@class="inventory_item_name"]'
    ADD_TO_CART_BUTTON = '//button[text()="Add to cart"]'
    PRODUCT_PRICE = '//div[@class="inventory_item_price"]'

    def __init__(self, driver):
        super().__init__(driver)
