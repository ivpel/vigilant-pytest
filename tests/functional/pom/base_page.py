from vigilant.driver.vigilant_driver import VigilantDriver


class BasePage:

    def __init__(self, driver):
        self.driver: VigilantDriver = driver
