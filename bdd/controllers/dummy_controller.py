from selenium.webdriver.common.by import By

from bdd.controllers.base_controller import BaseController


class DummyController(BaseController):

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

    def send(self, value):
        self.wait_till_element_is_not_displayed()
        ele = self.get_all_elements()
        self.scroll_element_to_center()
        ele.send_keys(value)
