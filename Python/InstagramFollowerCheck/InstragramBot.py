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
    
    def followersInformation(self) -> dict:
        return self.api.user_followers(self.userId, self.token)
    
    def followingInformation(self) -> dict:
        return self.api.user_following(self.userId, self.token)
    
    def followUsernameSets(self) -> tuple:
        followingSet : set = {user["username"] for user in self.followingInformation()["users"]}
        followersSet : set = {user["username"] for user in self.followersInformation()["users"]}

        return followingSet, followersSet
    
    def unfollowersList(self) -> list:
        followingSet, followersSet = self.followUsernameSets()
        
        unfollowersSet : set = followingSet.difference(followersSet)
        unfollowersList : list = sorted(list(unfollowersSet))

        return unfollowersList
    
    def friendsList(self) -> list:
        followingSet, followersSet = self.followUsernameSets()

        friendsSet : set = followingSet.intersection(followersSet)
        friendsList : set = sorted(list(friendsSet))

        return friendsList
