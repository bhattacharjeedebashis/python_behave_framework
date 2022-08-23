import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from helper.helper_base import HelperFunc


def get_browser(browser):
    if browser == "chrome":
        chrome_options = __get_chrome_options()
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        return HelperFunc(driver)


def __get_chrome_options():
    options = ChromeOptions()
    options.binary_location = os.environ.get('CHROME_BINARY_PATH')
    chrome_options = [
        '--no-sandbox',
        '--disable-dev-shm-usage',
        '--disable-setuid-sandbox',
        '--window-size=1920x1080',
        '--remote-debugging-port=9220'
    ]
    for option in chrome_options:
        options.add_argument(option)

    return options
