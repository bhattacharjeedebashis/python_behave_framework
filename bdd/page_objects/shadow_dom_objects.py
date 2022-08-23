from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from bdd.controllers.dummy_controller import DummyController
from bdd.page_objects.base_page import BasePage


class ShadowRootObject(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.book_root = DummyController(driver=self._driver, xpath_locator="//book-app[@apptitle='BOOKS']")
        self.book_root_input = (By.CSS_SELECTOR, "input[id=input]")
        self.download_root = DummyController(driver=self._driver, locator=(By.TAG_NAME, "downloads-manager"))
        self.download_toolbar = (By.CSS_SELECTOR, "downloads-toolbar")
        self.cr_toolbar = (By.CSS_SELECTOR, "cr-toolbar")
        self.toolbar_header = (By.CSS_SELECTOR, "div[id=leftSpacer]>h1")
        self.toolbar_search_field = (By.CSS_SELECTOR, "cr-toolbar-search-field")
        self.search_field = (By.CSS_SELECTOR, "input[id=searchInput]")

    def enter_value_into_book_input(self, value):
        root_element = self.book_root.get_element()
        element_list = [self.book_root_input]
        final_element = self.__get_element_from_shadow_root(root_element, element_list)
        final_element.send_keys(value)

    def enter_value_into_chrome_input(self, value):
        root_element = self.download_root.get_element()
        element_list = [self.download_toolbar, self.cr_toolbar, self.toolbar_search_field, self.search_field]
        final_element = self.__get_element_from_shadow_root(root_element, element_list)
        final_element.send_keys(value)

    def get_toolbar_header(self):
        root_element = self.download_root.get_element()
        element_list = [self.download_toolbar, self.cr_toolbar, self.toolbar_header]
        final_element = self.__get_element_from_shadow_root(root_element, element_list)
        return final_element.text

    def __get_element_from_shadow_root(self, root_element, element_list):
        final_element = root_element
        for ele in element_list:
            final_element = self.__expand_root_element(final_element)
            final_element = final_element.find_element(*ele)
        return final_element

    def __expand_root_element(self, element):
        dictionary = self._driver.execute_script('return arguments[0].shadowRoot', element)
        return WebElement(self._driver, dictionary['shadow-6066-11e4-a52e-4f735466cecf'], w3c=True)

