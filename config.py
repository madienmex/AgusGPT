class Config:
    def __init__(self):
        self.api_key = None

    def set_api_key(self, key):
        self.api_key = key

    def get_api_key(self):
        return self.api_key

config = Config()
