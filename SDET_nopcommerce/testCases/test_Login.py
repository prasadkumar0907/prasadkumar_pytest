from selenium import webdriver
import pytest
from pageObjects.LoginPage import Login


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, set_up):
        self.driver = set_up
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        # self.driver.close()
        if actual_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_LoginPage(self, set_up):
        self.driver = set_up
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        # self.driver.close()
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
