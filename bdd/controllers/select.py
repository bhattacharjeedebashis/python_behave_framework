from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from bdd.controllers.base_controller import BaseController


class SelectDropdown(BaseController):

    def __init__(self, driver, css_locator=None, xpath_locator=None, locator=None, parent=None):
        super().__init__(driver, parent)
        self._driver = driver

        if not (css_locator or locator or xpath_locator):
            raise ValueError(f"Element label name or locator is missing in controller class {__name__}")

        if locator:
            self._locator = locator
        elif css_locator:
            self._locator = (By.CSS_SELECTOR, css_locator)
        elif xpath_locator:
            self._locator = (By.XPATH, xpath_locator)

    def open(self):
        self.click()

    def select_by_value(self, value, open_=False):
        try:
            self.wait_till_element_is_not_displayed(timeout=2)
            if open_:
                self.click()
            ele = Select(self.get_element())
            ele.select_by_value(value=value)
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")

    def select_by_index(self, value, open_=False):
        try:
            self.wait_till_element_is_not_displayed(timeout=2)
            if open_:
                self.click()
            ele = Select(self.get_element())
            ele.select_by_index(index=value)
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")

    def select_by_visible_text(self, value, open_=False):
        try:
            self.wait_till_element_is_not_displayed(timeout=2)
            if open_:
                self.click()
            ele = Select(self.get_element())
            ele.select_by_visible_text(text=value)
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")

    def get_selected_value(self):
        try:
            self.wait_till_element_is_not_displayed(timeout=2)
            ele = Select(self.get_element())
            return ele.first_selected_option
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")
