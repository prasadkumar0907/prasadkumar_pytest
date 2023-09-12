from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class _visibility_of_element_located(visibility_of_element_located):

    def __call__(self, driver):
        displayed = super().__call__(driver)
        if isinstance(displayed, WebElement):
            return displayed.is_enabled()
        else:
            return False


def _wait(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        locator = args[1]
        w = WebDriverWait(instance.driver, 20)
        v = _visibility_of_element_located(locator)
        w.until(v)
        return func(*args, **kwargs)
    return wrapper



