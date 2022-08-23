from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from bdd.controllers.base_controller import BaseController


class Input(BaseController):

    BASE_LOC = ".//mat-form-field[.//label/span[normalize-space()=\"{}\"]]"

    def __init__(self, driver, css_locator=None, xpath_locator=None, locator=None, parent=None, label=None):
        super().__init__(driver, parent)
        self._driver = driver

        if not (css_locator or locator or xpath_locator or label):
            raise ValueError(f"Element label name or locator is missing in controller class {__name__}")

        if locator:
            self._locator = locator
        elif css_locator:
            self._locator = (By.CSS_SELECTOR, css_locator)
        elif xpath_locator:
            self._locator = (By.XPATH, xpath_locator)
        else:
            self._locator = (By.XPATH, self.BASE_LOC.format(label))

    def send(self, value, clear=False):
        try:
            self.wait_till_element_is_not_displayed()
            ele = self.get_element()
            self.scroll_element_to_center()
            if clear:
                self.clear_via_backspace()
            ele.send_keys(value)
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")

    def clear_via_backspace(self):
        try:
            length = len(self.get_attr("value"))
            if length > 0:
                ele = self.get_all_elements()
                for _ in range(length):
                    ele.send_keys(Keys.BACKSPACE)
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")

    def clear(self):
        try:
            ele = self.get_element()
            ele.clear()
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")

    def get_value(self):
        try:
            return self.get_attr("value")
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")
