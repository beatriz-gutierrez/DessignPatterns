from http_connector import HTTPConnector
from ftp_connetor import FTPConnector
from urllib.error import URLError

if __name__=="__main__":
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'

    protocol = input(f'Connecting to {domain}. Which protocol to use? (0-http or 1-ftp): ')

    if protocol == '0':
        is_secure = bool(input('Use secure connection? (1-yes, 0-no): '))
        connector = HTTPConnector(is_secure=is_secure)
    else:
        connector = FTPConnector(is_secure=False)
    
    try:
        content = connector.read(domain, path)
    except URLError as e:
        print(f"Can't access resource with this method: {e}")
    else:
        print(connector.parse(content))