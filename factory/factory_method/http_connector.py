from connector import Connector
from bs4 import BeautifulStoneSoup
from port import HHTPort, HTTPSecurePort

class HTTPConnector(Connector):
    """
    A concrete connector that creates a HTTP connector and sets in runtime all its attributes
    """
    def protocol_factory_method(self) -> str:
        if self.is_secure:
            return 'https'
        return 'http'

    def port_factory_method(self):
        if self.is_secure:
            return HTTPSecurePort()
        return HHTPort()

    def parse(self, content):
        """
        Parses web content
        """
        filenames = []
        soup = BeautifulStoneSoup(content)
        links = soup.table.findAll('a')
        for link in links:
            filenames.append(link['href'])

        return '\n'.join(filenames)
