from selenium import webdriver
from selenium.webdriver.common.by import By


class login:
    button_loginTotutorialspoin_Xpath = "//*[@id='navbarCollapse']/div[2]/div/a"
    textbox_emailId_xpath = "//input[@id='user_email']"
    textbox_password_xpath = "//input[@name='user_password']"
    button_login_Xpath = "//*[@id='user_login']"

    def __int__(self,driver):
        self.driver=driver


    def Clicklogintutorialspoint(self):
        self.driver.find_element(By.XPATH,self.button_logintutorialspointXpath).click()


    def enterUsername(self,username):
        self.driver.find_element(By.XPATH, self.textbox_emailId_xpath).send_keyes(username)

    def enterPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keyes(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
    