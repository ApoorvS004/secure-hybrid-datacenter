import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from route_simulator import find_best_route


class RouteSimulatorTests(unittest.TestCase):


    def test_default_route(self):
        routes = [("0.0.0.0/0", "internet-gateway")]

        result = find_best_route("8.8.8.8", routes)

        self.assertEqual(result[1], "internet-gateway")


    def test_no_matching_route(self):
        routes = [("10.30.0.0/16", "hybrid-vpn")]

        result = find_best_route("8.8.8.8", routes)

        self.assertIsNone(result)

    def test_specific_route_wins(self):
        routes = [
            ("0.0.0.0/0", "internet-gateway"),
            ("10.30.0.0/16", "hybrid-vpn"),
            ("10.30.1.0/24", "specific-network"),
        ]

        result = find_best_route("10.30.1.20", routes)

        self.assertEqual(result[1], "specific-network")


if __name__ == "__main__":
    unittest.main()