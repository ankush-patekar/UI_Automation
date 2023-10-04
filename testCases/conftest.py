from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("D:\\Python\\GitHub\\UI_Automation\\chromedriver_117.0.5938.89")
        '''
        webdriver kept at Python installed location(C:\sers\ankush.patekar\AppData\Local\Programs\Python\Python310\Scripts)
        So no need to give executable path
        '''
        # driver = webdriver.Chrome()
    elif browser == 'firefox':
        pro_path = "C:\\Users\\ankush.patekar\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\qfdwn80q.default"
        options = Options()
        options.set_preference('profile', pro_path)
        service = Service("D:\\Python\\GitHub\\UI_Automation\\geckodriver")
        driver = Firefox(service=service, options=options)
        '''
         webdriver kept at Python installed location(C:\sers\ankush.patekar\AppData\Local\Programs\Python\Python310\Scripts)
        So no need to give executable path
        '''
        # driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge("D:\\Python\\GitHub\\UI_Automation\\msedgedriver")
        # driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):           # This will get value from CLI
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):                         # This will return browser value to setup method
    return request.config.getoption('--browser')


#################### pyTest HTML Report ######################

#hook for adding environment info to html report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Hybrid Framework Practice"
    config.stash[metadata_key]["Module Name"] = "Customer"
    config.stash[metadata_key]["Tester"] = "Ankush Patekar"

def pytest_metadata(metadata):
    metadata.pop("plugins", None)
