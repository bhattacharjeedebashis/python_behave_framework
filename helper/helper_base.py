import base64

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HelperFunc(object):
    __TIMEOUT = 10

    def __init__(self, driver):
        super(HelperFunc, self).__init__()
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
        self._driver = driver

    def open(self, url):
        self._driver.get(url)

    def maximize(self):
        self._driver.maximize_window()

    def close(self):
        self._driver.quit()

    def get_driver(self):
        return self._driver

    def capture_screenshot(self, context, name):
        self._driver.save_screenshot('reports/screenshots/'+name+'.png')
        data_base64 = base64.b64encode(open('reports/screenshots/'+name+'.png', "rb").read())
        data = data_base64.decode("utf-8").replace("\n", "")
        context.embed(mime_type="image/png", data=data, caption=name)

    # # Helper functions that are used to identify the web locators in Selenium Python tutorial
    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def find_by_css(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, xpath)))
