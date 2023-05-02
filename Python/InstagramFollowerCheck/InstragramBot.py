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

    def followersInformationList(self) -> list:
        """
        Returns a list of dicts. Each dict is a follower with many information.
        """

        # Get first pagination
        results : dict = self.api.user_followers(self.userId, self.token)
        followersInfo : list = results["users"]
        nextMaxId : str = results["next_max_id"]
        
        # Get others pagination
        while nextMaxId:
            results = self.api.user_followers(self.userId, self.token, max_id=nextMaxId)
            followersInfo.extend(results["users"])
            try:
                nextMaxId = results["next_max_id"]
            except Exception:
                # If exception occurs, it means there isn't other paginations
                nextMaxId = None

        return followersInfo
