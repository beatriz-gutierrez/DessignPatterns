from abc import ABC, abstractmethod
from urllib.request import urlopen


class Connector(ABC):
    """
    Abstract class to connect to remote reource. 
    This class provides two factory methods for creating protocol and port that must be implemented by concrete connectors.
    """
    def __init__(self, is_secure):
        self.is_secure = is_secure
        self.port = self.port_factory_method()
        self.protocol = self.protocol_factory_method()

    @abstractmethod
    def parse(self):
        """
        Parses web content. Abstract method to be implemented by concrete connectors.
        """
        pass

    def read(self, host, path):
        """
        A generic method for reading web content.
        """
        url = self.protocol + '://' + host + str(self.port) + path
        print(f"Connecting to {url}")
        return urlopen(url, timeout=2).read()
    
    @abstractmethod
    def protocol_factory_method(self) -> str:
        """
        A factory method that must be implemented by concrete connectors.
        """
        pass

    @abstractmethod
    def port_factory_method(self):
        """
        A factory method that must be implemented by concrete connectors.
        """
        pass



