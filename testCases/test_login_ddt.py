import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtility
import time


class Test_002_ddt_Login:
    baseURL = ReadConfig.getApplicationUrl()
    path = "D:\\Python\\GitHub\\UI_Automation\\TestData\\login_details.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtility.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtility.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtility.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtility.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    self.lp.clicklogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
                    time.sleep(2)
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");



