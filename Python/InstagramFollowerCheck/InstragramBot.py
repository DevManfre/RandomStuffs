from instagram_private_api import Client
import logging
import coloredlogs
import json
import codecs
import os


class InstagramBot:
    """
    Implementantion for instagram_private_api
    The init method accepts 2 params: username and password so it can have:
    - api -> the logged client using the given username and password;
    - token, userId -> used for many intragram_private_api function;
    - logger -> used for debugging in the terminal.
    """

    def __init__(self, username: str, password: str, rememberLogin: bool = False):
        paths = {
            "CACHE": "cache.json",
            "CREDENTIALS": "credentials.json"
        }

        # Logger Settings
        self.logger = logging.getLogger(username)
        coloredlogs.install(
            level='DEBUG',
            logger=self.logger,
            fmt="%(asctime)s %(hostname)s %(name)s %(levelname)s    \t%(message)s"
        )

        # Client settings
        if os.path.isfile(paths["CACHE"]) and os.path.isfile(paths["CREDENTIALS"]):
            self.logger.debug(f"Loading cache files")

            cache, credentials = self.loadLogin(paths)

            # Reuse auth settings
            self.api = Client(
                credentials["username"],
                credentials["password"],
                settings=cache
            )
            self.token = credentials["token"]
            self.userId = credentials["userId"]
        else:
            # Create new client
            self.logger.info(f"Creating a client for \033[01m{username}\033[0m")
            self.api: Client = Client(username, password)
            self.token: str = self.api.generate_uuid()
            self.userId: str = self.api.authenticated_user_id

            if rememberLogin:
                self.logger.debug(f"Creating cache files")
                self.saveLogin(paths)

    def __followInformationList(self, callingFunction) -> list:
        """
        Function called from followersInformationList and followingInformationList to
        avoid repeated lines of code.
        Given one param function (instagram_private_api.Client.user_followers or
        instagram_private_api.Client.user_following) the main function returns
        a list with all pagination together (composed respectively of followers or
        following).
        """

        self.logger.debug(
            f"Calling the API method \033[01m{callingFunction.__name__}\033[0m")

        results: dict = callingFunction(self.userId, self.token)
        followInfo: list = results["users"]
        try:
            nextMaxId: str = results["next_max_id"]
        except:
            # Error -> 0 follow, that is an empty followInfo list
            return followInfo

        # Get others pagination
        while nextMaxId:
            results = callingFunction(
                self.userId, self.token, max_id=nextMaxId)
            followInfo.extend(results["users"])
            try:
                nextMaxId = results["next_max_id"]
            except Exception:
                # If exception occurs, it means there isn't other paginations
                nextMaxId = None

        return followInfo

    def __combinatedUsernameList(self, callingFunction) -> list:
        """
        Function called from unfollowersUsernamesList and friendsUsernamesList to
        avoid repeated lines of code.
        Given one param function (set.difference or set.intersection) the main
        function returns a list composed of followers and following assembled by
        the given function).
        """

        followers: set = set(self.followersUsernamesList())
        following: set = set(self.followingUsernamesList())

        results: list = list(callingFunction(following, followers))

        return sorted(results)

    def followersInformationList(self) -> list:
        """
        Returns a list of dicts. Each dict is a follower with many information.
        """

        return self.__followInformationList(self.api.user_followers)

    def followingInformationList(self) -> list:
        """
        Returns a list of dicts. Each dict is a following with many information.
        """

        return self.__followInformationList(self.api.user_following)

    def followersUsernamesList(self) -> list:
        """
        Return a sorted list contains the followers usernames.
        """

        self.logger.info("Getting the follower list")
        return sorted([follower["username"] for follower in self.followersInformationList()])

    def followingUsernamesList(self) -> list:
        """
        Return a sorted list contains the following usernames.
        """

        self.logger.info("Getting the following list")
        return sorted([following["username"] for following in self.followingInformationList()])

    def unfollowersUsernamesList(self) -> list:
        """
        Returns the following that isn't followers, thas is unfollowers.
        """

        self.logger.info("Getting the unfollower list")
        return self.__combinatedUsernameList(set.difference)

    def friendsUsernamesList(self) -> list:
        """
        Returns the following that is followers, thas is friends.
        """

        self.logger.info("Getting the friends list")
        return self.__combinatedUsernameList(set.intersection)

    def saveLogin(self, paths) -> None:
        def toJson(pythonObject):
            if isinstance(pythonObject, bytes):
                return {
                    '__class__': 'bytes',
                    '__value__': codecs.encode(pythonObject, 'base64').decode()
                }

        with open(paths["CACHE"], 'w') as cacheFile:
            json.dump(self.api.settings, cacheFile, default=toJson)
        with open(paths["CREDENTIALS"], "w") as credentialsFile:
            json.dump(
                {
                    "username": self.api.username,
                    "password": self.api.password,
                    "token": self.token,
                    "userId": self.userId
                },
                credentialsFile,
                default=toJson
            )

    def loadLogin(self, paths) -> tuple:
        def fromJson(jsonObject):
            if '__class__' in jsonObject and jsonObject['__class__'] == 'bytes':
                return codecs.decode(jsonObject['__value__'].encode(), 'base64')
            return jsonObject

        cachedSettings = credentials = {}

        with open(paths["CACHE"]) as file_data:
            cachedSettings = json.load(file_data, object_hook=fromJson)
        with open(paths["CREDENTIALS"]) as file_data:
            credentials = json.load(file_data, object_hook=fromJson)

        return cachedSettings, credentials
