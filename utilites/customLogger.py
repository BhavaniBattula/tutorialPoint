import logging

class LogGneneration:

    @staticmethod
    def loginformation():
        logging.basicConfig(filename= "C:\\Users\\bathu\\PycharmProjects\\quicker\\logs\\automationlogs",format='%(astime)s:%(levelname)s%(message)s',datefmt='%m/%d/%y %I:%m: %S %p',force='true')
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        return log


