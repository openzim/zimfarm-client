class OAuth2Error(Exception):
    def __init__(self, error:str, description: str):
        self.error = error
        self.description = description
