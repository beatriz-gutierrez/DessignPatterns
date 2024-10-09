from connector import Connector
from port import FTPPort

class FTPConnector(Connector):
    """
    A concrete connector that creates a FTP connector and sets in runtime all its attributes
    """
    def protocol_factory_method(self) -> str:
        return 'ftp'

    def port_factory_method(self):
        return FTPPort()

    def parse(self, content):
        """
        Parses ftp content
        """
        lines = content.split('\n')
        filenames = []

        for line in lines:
            # ftp format has 8 columns
            splitted_line = line.split(None, 8)
            if len(splitted_line) == 9:
                filenames.append(splitted_line[-1])
        
        return '\n'.join(filenames)
        