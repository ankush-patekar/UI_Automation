import logging
import pdb

class LogGen:
    # pdb.set_trace()
    @staticmethod
    def loggen():
        logging.basicConfig(filename="D:\\Python\\GitHub\\UI_Automation\\Logs\\automaton.logs",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
