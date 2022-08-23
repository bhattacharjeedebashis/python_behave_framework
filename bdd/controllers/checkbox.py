from selenium.webdriver.common.by import By

from bdd.controllers.base_controller import BaseController


class CheckBox(BaseController):

    BASE_LOC = ".//mat-checkbox[.//span[normalize-space()={}]]"

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

    def check(self):
        try:
            if not self.is_checked():
                self.click()
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")

    def is_checked(self):
        try:
            classes = self.get_attr("class")
            return bool("mat-checkbox-checked" in classes)
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")
