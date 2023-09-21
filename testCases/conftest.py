import webdriver_manager.chrome
from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome("D:\\Python\\GitHub\\UI_Automation\\chromedriver")
    return driver
