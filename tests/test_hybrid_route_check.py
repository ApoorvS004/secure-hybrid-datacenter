
import unittest

from scripts.hybrid_route_check import (
    find_best_route,
    aws_routes,
    datacenter_routes,
)


class TestHybridRoutes(unittest.TestCase):

    def test_aws_to_datacenter_route(self):
        route = find_best_route("10.30.1.20", aws_routes)
        self.assertEqual(route[1], "hybrid-vpn")

    def test_datacenter_to_aws_return_route(self):
        route = find_best_route("10.20.2.10", datacenter_routes)
        self.assertEqual(route[1], "hybrid-vpn")


if __name__ == "__main__":
    unittest.main()
