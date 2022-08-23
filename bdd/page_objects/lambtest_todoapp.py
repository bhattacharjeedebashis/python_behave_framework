from selenium.webdriver.common.by import By

from bdd.controllers.button import Button
from bdd.controllers.checkbox import CheckBox
from bdd.controllers.dummy_controller import DummyController
from bdd.controllers.input import Input
from bdd.page_objects.base_page import BasePage


class ToDoAppPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.li_one = CheckBox(driver=self._driver, locator=(By.NAME, 'li1'))
        self.li_two = CheckBox(driver=self._driver, locator=(By.NAME, 'li2'))
        self.item_name_input = Input(driver=self._driver, locator=(By.ID, 'sampletodotext'))
        self.add_button = Button(driver=self._driver, locator=(By.ID, 'addbutton'))
        self.result = DummyController(driver=self._driver, xpath_locator="//ul")

    def select_checkbox_one(self):
        self.li_one.check()

    def select_checkbox_two(self):
        self.li_two.check()

    def enter_item_name(self, value):
        self.item_name_input.send(value)

    def click_add_btn(self):
        self.add_button.click()

    def get_result(self):
        return self.result.get_text()
