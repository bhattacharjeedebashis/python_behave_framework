from time import sleep

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseController:
    """
    Base controller class to capture and define base web elements and their methods
    """
    FIELDS_TIMEOUT_SECONDS = 0.55

    def __init__(self, driver, parent=None):
        self._driver = driver
        self.__parent = None
        self.__locator = None
        self._parent = parent
        self._fields_timeout_seconds = self.FIELDS_TIMEOUT_SECONDS

    @property
    def _locator(self):
        return self.__locator

    @_locator.setter
    def _locator(self, locator):
        if not isinstance(locator, tuple):
            raise ValueError("Locator must be tuple (By.<CSS/XPATH/etc>, locator ")
        self.__locator = locator

    @property
    def _parent(self):
        return self.__parent

    @_parent.setter
    def _parent(self, parent):
        rules = (
            parent is None,
            isinstance(parent, BaseController),
            isinstance(parent, tuple)
        )
        if not any(rules):
            raise ValueError(f"Wrong parent value was given {parent}. Must be either None, subclass of baseControl"
                             f" or a locator")
        self.__parent = parent

    def _get_web_element(self, timeout=15):
        return self._get_parent_element(timeout).find_element(*self._locator)

    def _get_web_elements(self, timeout=15):
        return self._get_parent_element(timeout).find_elements(*self._locator)

    def _get_parent_element(self, timeout=15):
        if not self._parent:
            return self._driver
        if isinstance(self._parent, BaseController):
            parent_of_parent = self._parent._get_parent_element(timeout)
            return parent_of_parent.find_element(*self._parent._locator)
        elif isinstance(self._parent, tuple, list) and len(self._parent) == 2:
            return self._driver.find_element(*self._parent)
        else:
            raise ValueError(f"Wrong parent value was given {self._parent}. Must be either None, subclass of "
                             f"baseControl or a locator")

    def wait_till_element_is_not_displayed(self, timeout=20):
        wait = WebDriverWait(self._driver, timeout, poll_frequency=0.5)
        try:
            wait.until(EC.visibility_of_element_located(self._locator))
        except TimeoutException:
            pass

    def wait_till_element_is_displayed(self, timeout=20):
        wait = WebDriverWait(self._driver, timeout, poll_frequency=0.5)
        try:
            wait.until(EC.invisibility_of_element_located(self._locator))
        except TimeoutException:
            pass

    def wait_till_element_is_present(self, timeout=20):
        wait = WebDriverWait(self._driver, timeout, poll_frequency=0.5)
        try:
            wait.until(EC.presence_of_element_located(self._locator))
        except TimeoutException:
            pass

    def wait_till_iframe_is_displayed(self, timeout=20):
        wait = WebDriverWait(self._driver, timeout, poll_frequency=0.5)
        try:
            wait.until(EC.frame_to_be_available_and_switch_to_it(self._locator))
        except TimeoutException:
            pass

    def wait_till_element_is_clickable(self, timeout=20):
        wait = WebDriverWait(self._driver, timeout, poll_frequency=0.5)
        try:
            wait.until(EC.element_to_be_clickable(self._locator))
        except TimeoutException:
            pass

    def is_element_displayed(self, timeout=20, element=None):
        wait = WebDriverWait(self._driver, timeout, poll_frequency=0.5)
        try:
            element = self._get_web_element() if not element else element
            wait.until(EC.visibility_of(element))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def wait_implicitly(time=1):
        sleep(time)

    def scroll_element_to_center(self):
        self._driver.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center"})',
                                    self._get_web_element())

    def click(self, timeout=5):
        try:
            self.wait_till_element_is_clickable(timeout)
            ele = self._get_web_element()
            self.scroll_element_to_center()
            return ele.click()
        except Exception as err:
            raise ValueError(f"Error {err} at {__name__}")

    def get_attr(self, attribute_name, timeout=5):
        self.wait_till_element_is_not_displayed(timeout)
        ele = self._get_web_element()
        self.scroll_element_to_center()
        return ele.get_attribute(attribute_name)

    def get_text(self, timeout=5):
        self.wait_till_element_is_not_displayed(timeout)
        ele = self._get_web_element()
        self.scroll_element_to_center()
        return ele.text

    def javascript_click(self):
        return self._driver.execute_script('arguments[0].click()', self._get_web_element())

    def is_alert_displayed(self, timeout=2):
        wait = WebDriverWait(self._driver, timeout, poll_frequency=0.5)
        try:
            wait.until(EC.alert_is_present())
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def get_all_elements(self):
        return self._get_web_elements()

    def get_element(self):
        return self._get_web_element()

    def get_locator(self):
        return self._locator

    def is_element_present(self):
        try:
            return bool(len(self._get_web_elements()) > 0)
        except NoSuchElementException:
            return False
