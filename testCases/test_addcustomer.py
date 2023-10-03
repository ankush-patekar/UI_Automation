import time
import pytest
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.addCustomer import AddCustomer
import random
import string
import pdb

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    # pdb.set_trace()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addCustomer(self, setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()
        self.email = random_genrator() + '@gmail.com'
        print(self.email)
        self.addcust.setEmail(self.email)
        self.addcust.setGender('Male')
        self.addcust.setVendor("Vendor 2")
        self.addcust.setIsTaxExempt()
        self.addcust.setCustomerRoles("Registered")
        self.addcust.clicksavebtn()

        self.logger.info("************* Saving customer info **********")
        self.logger.info("********* Add customer validation started *****************")

        if 'The new customer has been added successfully.' in self.addcust.alertMsg():
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")

def random_genrator(size=8, chars = string.ascii_lowercase + string.digits ):
    return "".join(random.choice(chars) for x in range(size))