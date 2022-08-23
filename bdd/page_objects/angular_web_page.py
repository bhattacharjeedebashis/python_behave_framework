from bdd.controllers.button import Button
from bdd.controllers.dummy_controller import DummyController
from bdd.controllers.input import Input
from bdd.controllers.select import SelectDropdown
from bdd.page_objects.base_page import BasePage


class AngularWebPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.first_operand = Input(driver=self._driver, css_locator="input[ng-model='first']")
        self.second_operand = Input(driver=self._driver, css_locator="input[ng-model='second']")
        self.operator = SelectDropdown(driver=self._driver, css_locator="select[ng-model='operator']")
        self.go_button = Button(driver=self._driver, css_locator="button[id='gobutton']")
        self.operation_result_expression = DummyController(driver=self._driver,
                                                           xpath_locator="//table/tbody/tr[1]/td[2]")
        self.operation_result_value = DummyController(driver=self._driver, xpath_locator="//table/tbody/tr[1]/td[3]")
        self.result_loader = DummyController(driver=self._driver, css_locator="h2[class='ng-binding']")

    def set_first_operand(self, value):
        self.first_operand.send(value)

    def set_second_operand(self, value):
        self.second_operand.send(value)

    def select_operator(self, value):
        self.operator.select_by_visible_text(value=value, open_=True)

    def submit_operation(self):
        self.go_button.click()
        self.operation_result_value.wait_till_element_is_not_displayed()

    def get_result_expression(self):
        return self.operation_result_expression.get_text()

    def get_result_value(self):
        return self.operation_result_value.get_text()
