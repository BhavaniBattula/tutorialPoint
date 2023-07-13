import pytest
from selenium import webdriver
@pytest.fixture()
def setup(browser):
   if browser == 'chrome':
      driver= webdriver.Chrome()
      driver.maximize_window()
      print("launching chrome browser...")
   elif browser == 'firefox' :
        driver = webdriver.firefox()
       print("launching firefox browser...")
   else:
       driver = webdriver.Chrome()
       driver.maximize_window()
       return driver


def pytest_addpotion(parser)
       parser.addoption("--broswer")
@pytest.fixture()
def browser (request)
    return request.config.getoption("--browser")
