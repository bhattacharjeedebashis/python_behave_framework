from selenium.webdriver.common.by import By

from bdd.controllers.base_controller import BaseController


class ProgressBar(BaseController):

    BASE_LOC = ".//loader-progress//div"

    def __init__(self, driver, parent=None):
        super().__init__(driver, parent=parent)
        self._locator = (By.XPATH, self.BASE_LOC)

    def wait_till_progress_bar_appear(self, timeout=20):
        self.wait_till_element_is_not_displayed(timeout=timeout)

    def wait_till_progress_bar_disappear(self, timeout=20):
        self.wait_till_element_is_displayed(timeout=timeout)
