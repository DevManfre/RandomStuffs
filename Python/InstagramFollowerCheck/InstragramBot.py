from instagram_private_api import Client

class InstagramBot:
    def __init__(self, username : str, password : str):
        self.username : str = username
        self.password : str = password
        self.api : Client = Client(username, password)
        self.token : str = self.api.generate_uuid()
        self.userId : str = self.api.authenticated_user_id
    