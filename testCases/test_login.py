import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import readConfig
import datetime
import pdb


class Test_001_Login():
    # pdb.set_trace()
    url = readConfig.getApplicationUrl()
    username = readConfig.getUserName()
    password = readConfig.getPassword()
    # timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # def test_homepagetitle(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     expected_title = "Your store. Login"
    #     actual_title = self.driver.title
    #     assert actual_title == expected_title
    #     self.driver.close()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        # expected_title = "Dashboard / nopCommerce administration"
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("D:\\Python\\GitHub\\UI_Automation\\Screenshots\\" + "test_login.png")
            # self.driver.close()
            assert False



