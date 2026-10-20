
import socket
import sys
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock
from urllib.error import URLError

# Make the scripts directory importable.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import network_check


class NetworkCheckTests(unittest.TestCase):

    @patch("network_check.socket.getaddrinfo")
    def test_dns_success(self, mock_getaddrinfo):
        mock_getaddrinfo.return_value = [
            (None, None, None, None, ("192.0.2.10", 443))
        ]

        result = network_check.check_dns("example.com")

        self.assertTrue(result)

    @patch("network_check.socket.getaddrinfo")
    def test_dns_failure(self, mock_getaddrinfo):
        mock_getaddrinfo.side_effect = socket.gaierror(
            "Name resolution failed"
        )

        result = network_check.check_dns("invalid.example")

        self.assertFalse(result)

    @patch("network_check.urllib.request.urlopen")
    def test_https_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_urlopen.return_value.__enter__.return_value = mock_response

        result = network_check.check_https(
            "https://example.com"
        )

        self.assertTrue(result)

    @patch("network_check.urllib.request.urlopen")
    def test_https_connection_failure(self, mock_urlopen):
        mock_urlopen.side_effect = URLError(
            "Connection failed"
        )

        result = network_check.check_https(
            "https://example.com"
        )

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
