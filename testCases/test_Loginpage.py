import pytest
import time
from selenium import webdriver
from pageObjects.Loginpage import login
from utilites.ReadProperties import Readconfig
from utilites.customLogger import logGenaration

class Test_001_loginAcess
    baseURL  =  Readconfig.getApplicationurl()
    Username = Readconfig.username()
    Password = Readconfig.password()

    loginfo = logGenaration.loginformation()


    def test_homepageTittle(self,setup):
        self.driver = setup
        self.loginfo.info("##################test case started################")
        self.driver.get(self.baseURL)
        act_tittle =self.driver.title
        if act_tittle=="Online Courses and eBooks Library":
            assert True
            self.loginfo.info("##################test case passed################")
        else:
            self.driver.save_screenshort("C:\\Users\\bathu\\PycharmProjects\\tutorialPoint\\Screenshorts\\test_homepage tittle.png")
            self.loginfo.info("##################test case failed################")
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.loginfo.info("##################login TC started################")
        self.driver.get(self.baseURL)
        self.lp = login()
        self.lp.ClickTologintutorialspoin()
        self.lp.enterusername(self.username)
        self.lp.enterPassword(self.Password)
        self.lp.clicklogin()
        time.(5)
        act_tittle = self.driver.tittle
        if act_tittle == "Online Courses and eBooks Library":
        assert True
        self.loginfo.info("##################login TC passed################")
        else:
        self.driver.save_screenshort("C:\\Users\\bathu\\PycharmProjects\\tutorialPoint\\Screenshorts\\test_homepage")
        assert False
