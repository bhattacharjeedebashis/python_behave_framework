from selenium.webdriver.common.by import By

from bdd.controllers.base_controller import BaseController


class Accordion(BaseController):

    BASE_LOC = ".mat-expansion-panel-header[.//span[contains(text(), '{}')]]"

    def __init__(self, driver, label=None, xpath_locator=None, css_locator=None, locator=None, parent=None):
        super().__init__(driver, parent)
        self.label = label
        self._driver = driver

        if not (label or css_locator or locator):
            raise ValueError(f"Element label name or locator is missing in controller class {__name__}")

        if locator:
            self._locator = locator
        elif css_locator:
            self._locator = (By.CSS_SELECTOR, self.BASE_LOC.format(label))
        elif xpath_locator:
            self._locator = (By.XPATH, self.BASE_LOC.format(label))

    def is_accordion_expanded(self):
        try:
            expanded = self.get_attr('aria-expanded')
            return bool(expanded == "true")
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")

    def expand(self):
        try:
            if self.is_accordion_expanded():
                log.debug(f"Accordion '{self.label}' is already expanded")
            else:
                ele = self._get_web_element()
                ele.click()
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")
