from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self._driver = driver

    def pres_tab_key(self):
        ActionChains(self._driver).send_keys(Keys.TAB).perform()

    def pres_backspace_key(self):
        ActionChains(self._driver).send_keys(Keys.BACKSPACE).perform()

    def pres_ctrl_a_key(self):
        ActionChains(self._driver).send_keys(Keys.CONTROL, "a").perform()

    def switch_window(self, tab_index):
        if len(self._driver.window_handles) > 0:
            self._driver.switch_to_window(tab_index)

    def wait_until_page_loads(self):
        page_state = self._driver.execute_script('return document.readyState;')
        while page_state != 'complete':
            page_state = self._driver.execute_script('return document.readyState;')

