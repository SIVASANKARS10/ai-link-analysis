
import ipaddress
import socket
from urllib.parse import urlparse


def validate_url(url: str) -> bool:
    try:
        parsed = urlparse(url)

        if parsed.scheme not in ("http", "https"):
            return False

        if not parsed.hostname:
            return False

        hostname = parsed.hostname.lower()

        if hostname in ("localhost", "localhost.localdomain"):
            return False

        try:
            ip = ipaddress.ip_address(hostname)

            if not ip.is_global:
                return False

        except ValueError:
            addresses = socket.getaddrinfo(
                hostname,
                None,
                type=socket.SOCK_STREAM
            )

            if not addresses:
                return False

            for address in addresses:
                ip = ipaddress.ip_address(address[4][0])

                if not ip.is_global:
                    return False

        return True

    except (ValueError, socket.gaierror, OSError):
        return False
