class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, to_visit: list = [], downloaded: list = [], queue_to_parse: list = []):
        self.queue_to_parse = queue_to_parse
        self.to_visit = to_visit
        self.downloaded = downloaded

