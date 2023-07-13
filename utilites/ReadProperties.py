import configparser
config = configparser.RawConfigParser()
config.read("C:\\Users\\bathu\\PycharmProjects\\tutorialPoint\\configaration\\config.ini")
class Readconfig:
    @staticmethod
    def getApplicationURL():
        URL  = config.get('common userinfo', 'base url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common userinfo','username')
        return username
    @staticmethod
    def getpassword():
        password = config.get('common userinfo','password')
        return password


