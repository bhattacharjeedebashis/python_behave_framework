from selenium.webdriver.common.by import By

from bdd.controllers.base_controller import BaseController
from bdd.controllers.dummy_controller import DummyController
from bdd.controllers.input import Input


class DropDown(BaseController):

    BASE_LOC = ".//mat-form-field[.//span//label[normalize-space()='{}']]"

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

        self.search_input = Input(driver=self._driver, label=label)
        self.options_elements = DummyController(
            driver=self._driver, xpath_locator=".//mat-option|.//div[contains(@class, 'pac-container pac-logo')]")
        self.options_xpath = ".//mat-option[normalize-space()={}]|" \
                             ".//option[normalize-space()={}]|" \
                             ".//div[@class='pac-item' and normalize-space()={}]"

    def open(self):
        self.click()

    def search(self, value):
        self.search_input.send(value=value)

    def select(self, value, open_dropdown=True, scroll=False):
        if open_dropdown:
            self.open()
        ele = DummyController(driver=self._driver, xpath_locator=self.options_xpath.format(value))
        ele.wait_till_element_is_not_displayed(timeout=2)
        if scroll:
            self._driver.execute_script('arguments[0].scrollTop=300', self.get_element())
        ele.click()

    def get_search_value(self):
        ele = DummyController(driver=self._driver, xpath_locator=".//input", parent=self._locator)
        return ele.get_attr("value")

    def get_selected_value(self):
        ele = DummyController(driver=self._driver, xpath_locator=".//mat-select", parent=self._locator)
        return ele.get_text()

    def scroll_option_to_center(self):
        self._driver.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center"})',
                                    self.get_element())
