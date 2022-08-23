from bdd.controllers.dummy_controller import DummyController
from bdd.controllers.input import Input
from bdd.controllers.radio import Radio
from bdd.page_objects.base_page import BasePage


class WebPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.first_name = Input(driver=self._driver, css_locator="[name='firstname']")
        self.last_name = Input(driver=self._driver, css_locator="[name='lastname']")
        self.gender_radio_option = "[id='sex-{0}']"
        self.experience = "[id='exp-{0}']"
        self.date_picker = Input(driver=self._driver, css_locator="[id='datepicker']")
        self.download_link = "//a[text()='{0}']"

    def set_first_name(self, value):
        self.first_name.send(value)

    def set_last_name(self, value):
        self.last_name.send(value)

    def set_gender(self, value):
        value = "0" if "male" in value else "1"
        ele = Radio(driver=self._driver, css_locator=self.gender_radio_option.format(value))
        ele.click()

    def set_experience(self, value):
        value = str(int(value)-1)
        ele = Radio(driver=self._driver, css_locator=self.experience.format(value))
        ele.click()

    def set_date(self, value):
        self.date_picker.click()
        self.date_picker.send(value)

    def click_download_link(self, value):
        ele = DummyController(driver=self._driver, xpath_locator=self.download_link.format(value))
        ele.click()
        self.wait_until_page_loads()

    def check_target_page_loaded(self, url):
        try:
            return self._driver.current_url == url
        except Exception as err:
            raise Exception(f"Error {err} at {__name__}")
