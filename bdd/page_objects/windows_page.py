from bdd.controllers.button import Button
from bdd.controllers.frame import Frame
from bdd.controllers.input import Input
from bdd.page_objects.base_page import BasePage
from bdd.win_objects.file_open_dialog import FileDialogObject


class WindowsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.input_button = Button(driver=self._driver, xpath_locator="//button[@id='myFile']")
        self.selected_file = Input(driver=self._driver, xpath_locator="//input[@id='txtFile']")
        self.download_file_iframe = Frame(driver=self._driver, css_locator="iframe[id='iframeResult']")
        self.download_fie_button = Button(driver=self._driver, xpath_locator="//a")

    def click_upload_file_button(self):
        self.input_button.click()

    def get_selected_file_text(self):
        return self.selected_file.get_attr("value")

    def upload_a_file(self, file_name):
        fdo = FileDialogObject(self._driver.title)
        fdo.set_file_name(file_name)
        fdo.click_open_button()

    def download_file(self):
        self.download_file_iframe.switch_to_iframe()
        self.download_fie_button.click()
