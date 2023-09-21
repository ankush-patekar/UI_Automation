import configparser

confprsr = configparser.RawConfigParser()
confprsr.read("D:\\Python\\GitHub\\UI_Automation\\Configurations\\config.ini")

class readConfig():

    @staticmethod
    def getApplicationUrl():
        baseurl = confprsr.get('common info', 'url')
        return baseurl

    @staticmethod
    def getUserName():
        username = confprsr.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = confprsr.get('common info', 'password')
        return password
