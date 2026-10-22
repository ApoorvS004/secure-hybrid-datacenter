
import ipaddress


def find_best_route(destination, routes):
    destination = ipaddress.ip_address(destination)
    best_route = None

    for network_text, next_hop in routes:
        network = ipaddress.ip_network(network_text)

        if destination in network:
            if (
                best_route is None
                or network.prefixlen > best_route[0].prefixlen
            ):
                best_route = (network, next_hop)

    return best_route


routes = [
    ("0.0.0.0/0", "internet-gateway"),
    ("10.30.0.0/16", "hybrid-vpn"),
    ("10.30.1.0/24", "specific-network"),
]

destination = "8.8.8.8"
best_route = find_best_route(destination, routes)

if best_route is not None:
    print(f"Destination: {destination}")
    print(f"Selected route: {best_route[0]}")
    print(f"Next hop: {best_route[1]}")
else:
    print("No matching route found")
