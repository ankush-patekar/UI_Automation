import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:

    lnkCustomers_menu_css = ".has-treeview:nth-child(4) > .nav-link > p"
    lnkCustomers_menuitem_css = ".menu-is-opening .nav-item:nth-child(1) p"
    btnAddnew_linktxt = "Add new"
    txtEmail_id = "Email"
    txtPassword_id = "password"
    txtFirstname_id = "FirstName"
    txtLastName_id = "LastName"
    txtGenderMale_id = "Gender_Male"
    txtGenderFemale_id = "Gender_Female"
    txtDateOfBirth_id = "DateOfBirth"
    txtCompany_id = "Company"
    txtIsTaxExempt_id = "IsTaxExempt"
    # txtNewsletter_css = ".k-state-hover > .k-multiselect-wrap"
    lstbxcustomerroles_css = "#customer-info > div.card-body > div:nth-child(10) > div.col-md-9 > div > div.input-group > div"
    lstitemcustomerroleRegistered_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[4]'
    lstitemcustomerroleAdministrator_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[1]'
    lstitemcustomerroleFM_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[2]'
    lstitemcustomerroleGuest_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[3]'
    lstitemcustomerroleVendors_xpath = '//*[@id="a743548a-0644-4168-ab07-9d4aa70c3739"]'
    txtVendorId_id = "VendorId"
    chkIsTaxExempt_xpath = '//*[@id="IsTaxExempt"]'
    btnsave_xpath = '/html/body/div[3]/div[1]/form/div[1]/div/button[1]'
    alertmsg_xpath = '/html/body/div[3]/div[1]/div[1]'

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.CSS_SELECTOR, self.lnkCustomers_menu_css).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.CSS_SELECTOR, self.lnkCustomers_menuitem_css).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.LINK_TEXT, self.btnAddnew_linktxt).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setPassword(self):
        self.driver.find_element(By.ID, self.txtPassword_id)

    def setFirstName(self, Name):
        self.driver.find_element(By.ID, self.txtFirstname_id).send_keys(Name)

    def setLastName(self, SurName):
        self.driver.find_element(By.ID, self.txtFirstname_id).send_keys(SurName)

    def setDOB(self, DOB):
        self.driver.find_element(By.ID, self.txtDateOfBirth_id).send_keys(DOB)

    def setGender(self, Gender):
        if Gender == "Male":
            self.driver.find_element(By.ID, self.txtGenderMale_id).click()
        elif Gender == "Female":
            self.driver.find_element(By.ID, self.txtGenderFemale_id).click()

    def setIsTaxExempt(self):
        chkbox = self.driver.find_element(By.XPATH, self.chkIsTaxExempt_xpath)
        if not chkbox.is_selected():
            chkbox.click()
        else:
            print("Already selected")

    def setVendor(self, value):
        DD = Select(self.driver.find_element(By.ID, self.txtVendorId_id))
        DD.select_by_visible_text(value)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.CSS_SELECTOR, self.lstbxcustomerroles_css).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
        if role == "Administrator":
            # self.driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitemcustomerroleAdministrator_xpath)
        elif role == "Fourm Moderators":
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitemcustomerroleFM_xpath)
        elif role == "Gusest":
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitemcustomerroleGuest_xpath)
        # elif role == "Registered":
        #     self.lstitem = self.driver.find_element(By.XPATH, self.lstitemcustomerroleRegistered_xpath)
        elif role == "Vendors":
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitemcustomerroleVendors_xpath)
        else:
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitemcustomerroleRegistered_xpath)

        self.driver.execute_script("arguments[0].click();", self.lstitem)

    def clicksavebtn(self):
        self.driver.find_element(By.XPATH, self.btnsave_xpath).click()

    def alertMsg(self):
        msg = self.driver.find_element(By.XPATH, self.alertmsg_xpath).text
        return msg

