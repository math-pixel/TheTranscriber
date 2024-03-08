import time
import inspect


class DLog:
    RED = "\033[31m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    YELLOW_BG = "\033[43m"  # Fond jaune
    GREEN = "\033[32m"
    BOLD = "\033[1m"
    GRAY = "\033[90m"

    def __init__(self):
        pass

    @staticmethod
    def goodbiglog(message):
        space = '='*len(message)
        print(DLog.buildStr(space, DLog.GREEN))
        print(DLog.buildStr(message, DLog.GREEN))
        print(DLog.buildStr(space, DLog.GREEN))


    @staticmethod
    def errorbiglog(message):
        space = '!'*len(message)
        print(DLog.buildStr(space, DLog.RED))
        print(DLog.buildStr(message, DLog.RED))
        print(DLog.buildStr(space, DLog.RED))

    @staticmethod
    def goodlog(message):
        print(DLog.buildStr(message, DLog.GREEN))

    @staticmethod
    def error(message):
        print(DLog.buildStr(message, DLog.RED))

    @staticmethod
    def warning(message):
        print(DLog.buildStr(message, DLog.YELLOW))

    @staticmethod
    def infos(message):
        print(DLog.buildStr(message, DLog.RESET))

    @staticmethod
    def buildStr(message, color):
        return DLog.GRAY + str(round(time.time(), 3)) + DLog.RESET + ": " + DLog.get_function_name(inspect.stack()[2]) + color + str(message) + DLog.RESET

    @staticmethod
    def get_function_name(function):
        # ChatGPT code mdr
        caller_frame = function
        caller_function = caller_frame.function
        caller_class = caller_frame.frame.f_locals.get('self',
                                                       None).__class__.__name__ if 'self' in caller_frame.frame.f_locals else None
        return DLog.BOLD + str(caller_class) + "." + caller_function + "() ==== > " + DLog.RESET
