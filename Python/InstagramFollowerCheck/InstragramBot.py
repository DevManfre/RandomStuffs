from instagram_private_api import Client

class InstagramBot:
    """
    Implementantion for instagram_private_api
    The init method accepts 2 params: username and password so it can have:
    - api -> the logged client using the given username and password;
    - token, userId -> used for many intragram_private_api function
    """

    def __init__(self, username : str, password : str):
        self.username : str = username
        self.password : str = password
        self.api : Client = Client(username, password)
        self.token : str = self.api.generate_uuid()
        self.userId : str = self.api.authenticated_user_id

    def __followInformationList(self, callingFunction) -> list:
        """
        Function called from followersInformationList and followingInformationList to
        avoid repeated lines of code.
        Given one param function (instagram_private_api.Client.user_followers or 
        instagram_private_api.Client.user_following) the main function returns
        a list with all pagination together (composed respectively of followers or
        following).
        """

        results : dict = callingFunction(self.userId, self.token)
        followInfo : list = results["users"]
        nextMaxId : str = results["next_max_id"]
        
        # Get others pagination
        while nextMaxId:
            results = callingFunction(self.userId, self.token, max_id=nextMaxId)
            followInfo.extend(results["users"])
            try:
                nextMaxId = results["next_max_id"]
            except Exception:
                # If exception occurs, it means there isn't other paginations
                nextMaxId = None

        return followInfo

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

        return sorted([follower["username"] for follower in self.followersInformationList()])
    
    def followingUsernamesList(self) -> list:
        """
        Return a sorted list contains the following usernames.
        """

        return sorted([following["username"] for following in self.followingInformationList()])

    def unfollowersUsernamesList(self) -> list:
        """
        Returns the following that isn't followers, thas is unfollowers.
        """

        followers : set = set(self.followersUsernamesList())
        following : set = set(self.followingUsernamesList())

        unfollowers : list = list(following.difference(followers))

        return sorted(unfollowers)
    
    def friendsUsernamesList(self) -> list:
        """
        Returns the following that is followers, thas is friends.
        """

        followers : set = set(self.followersUsernamesList())
        following : set = set(self.followingUsernamesList())

        unfollowers : list = list(following.intersection(followers))

        return sorted(unfollowers)
