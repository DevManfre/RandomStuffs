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
    
    def followersDict(self) -> dict:
        """
        Return a dict contains all information about every single followers.
        """

        return self.api.user_followers(self.userId, self.token)
    
    def followingsDict(self) -> dict:
        """
        Return a dict contains all information about every single following.
        """

        return self.api.user_following(self.userId, self.token)
    
    def unfollowersList(self) -> list:
        followers : set = {user["username"] for user in self.followersDict()["users"]}
        following : set = {user["username"] for user in self.followingsDict()["users"]}

        unfollowers : list = sorted(list(following.difference(followers)))

        return unfollowers
    
    def friendsList(self) -> list:
        followers : set = {user["username"] for user in self.followersDict()["users"]}
        following : set = {user["username"] for user in self.followingsDict()["users"]}

        friends : list = sorted(list(following.intersection(followers)))

        return friends
