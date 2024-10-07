class Singleton:

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self, value: str = None) -> None:
        self.value = value
