import pickle


# Model
class Url(object):

    @classmethod
    def shorten(cls, full_url: str) -> str:
        """Shortens full url."""

        instance = cls()
        instance.full_url = full_url
        instance.short_url = instance.__create_short_url()

        Url.__save_url_mapping(instance)

        return instance

    @classmethod
    def get_by_short_url(cls, short_url: str) -> str:
        """Retrieves full url from short url."""

        url_mapping = Url.__load_url_mapping()
        return url_mapping.get(short_url)

    def __create_short_url(self) -> str:
        """Creates short url, saves it and returns it."""

        last_short_url = Url.__load_last_short_url()
        short_url = self.__increment_string(last_short_url)
        Url.__save_last_short_url(short_url)

        return short_url

    def __increment_string(self, string: str) -> str:
        """Increments string, that is:
        a -> b
        z -> aa
        az -> ba
        empty string -> a
        """

        if string == "":
            return "a"

        last_char = string[-1]

        if last_char != "z":
            return string[:-1] + chr(ord(last_char) + 1)

        return self.__increment_string(string[:-1]) + "a"

    @staticmethod
    def __load_last_short_url() -> str:
        """Loads last short url from file."""
        try:
            return pickle.load(open("last_short.p", "rb"))
        except IOError:
            return ""

    @staticmethod
    def __save_last_short_url(url: str):
        """Saves last short url to file."""
        pickle.dump(url, open("last_short.p", "wb"))

    @staticmethod
    def __load_url_mapping():
        """Returns short_url to Url instance mapping."""
        try:
            return pickle.load(open("short_to_url.p", "rb"))
        except IOError:
            return {}

    @staticmethod
    def __save_url_mapping(instance):
        """Saves short_url to Url instance mapping."""
        short_to_url = Url.__load_url_mapping()
        short_to_url[instance.short_url] = instance
        pickle.dump(short_to_url, open("short_to_url.p", "wb"))
