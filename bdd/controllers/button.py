from selenium.webdriver.common.by import By

from bdd.controllers.base_controller import BaseController


class Button(BaseController):

    BASE_LOC = ".//button[normalize-space()=\"{}\"]"

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

    def is_button_displayed(self):
        try:
            return self.is_element_displayed()
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")

    def is_button_disabled(self):
        try:
            _expected_classes = ["mat-button-disabled"]
            classes = self.get_attr("class")
            disabled = self.get_attr("disabled")
            if disabled or classes in _expected_classes:
                return True
            return False
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")
