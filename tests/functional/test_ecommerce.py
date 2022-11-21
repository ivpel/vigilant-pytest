import pytest

from vigilant.driver.vigilant_driver import VigilantDriver
from pom.login_page import LoginPage
from pom.category_list_page import CategoryListPage
from pom.cart_page import CartPage
from pom.checkout_page import CheckoutPage


@pytest.fixture(scope="module")
def driver():
    vd = VigilantDriver()
    yield vd
    vd.quit()


def test_login(driver):
    login_page = LoginPage(driver)

    driver.get_page('/')
    login_page.fill_in_and_login()
    driver.assertions.see_in_url('/inventory.html')


def test_add_product_from_clp(driver):
    clp = CategoryListPage(driver)

    driver.assertions.see(
        clp.PRODUCT_CARD + '[1]')  # +[1] is Xpath trick to say that we looking for FIRST available element with this selector
    driver.click(clp.ADD_TO_CART_BUTTON + '[1]')
    driver.assertions.see_text('Remove')


def test_complete_order(driver):
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Go to cart page and assert correct url
    driver.click(cart.CART_ICON_LINK)
    driver.assertions.see_in_url('/cart.html')

    # From cart page go to checkout and complete it
    driver.click(cart.CHECKOUT_BUTTON)
    driver.assertions.see_in_url('/checkout-step-one.html')

    # Fill personal info and go to Second step
    checkout.fill_personal_info()
    driver.click(checkout.CONTINUE_BUTTON)
    driver.assertions.see_in_url('checkout-step-two.html')

    # Place order
    driver.click(checkout.FINISH_BUTTON)
    driver.assertions.see_in_url('/checkout-complete.html')
