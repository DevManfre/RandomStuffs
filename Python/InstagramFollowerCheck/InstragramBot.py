from instagram_private_api import Client

class InstagramBot:
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
    
    def unfollowersList(self) -> list:
        followingSet = {user["username"] for user in self.followingInformation()["users"]}
        followersSet = {user["username"] for user in self.followersInformation()["users"]}
        
        unfollowersSet = followingSet.difference(followersSet)
        unfollowersList = sorted(list(unfollowersSet))

        return unfollowersList
    
    def fanList(self) -> list:
        followingSet = {user["username"] for user in self.followingInformation()["users"]}
        followersSet = {user["username"] for user in self.followersInformation()["users"]}

        fanSet = followingSet.intersection(followersSet)
        fanList = sorted(list(fanSet))

        return fanList
