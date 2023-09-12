from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """BY locators OR-object repository"""
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "loginBtn")
    SIGNUP = (By.LINK_TEXT, "Sign in with Google")

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """page actions for login page"""

    """this is used to get page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """this is used to login to the app"""
    def login(self, username, password):
        self.enter_text(self.EMAIL, username)
        self.enter_text(self.PASSWORD, password)
        self.click_element(self.LOGIN)

