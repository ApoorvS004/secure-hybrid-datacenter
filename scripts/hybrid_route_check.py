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


aws_routes = [
    ("10.20.0.0/16", "local"),
    ("10.30.0.0/16", "hybrid-vpn"),
    ("0.0.0.0/0", "internet-gateway"),
]

datacenter_routes = [
    ("10.30.0.0/16", "local"),
    ("10.20.0.0/16", "hybrid-vpn"),
]


def check_connection(source, destination, routes, network_name):
    route = find_best_route(destination, routes)

    if route is None:
        print(f"[FAIL] No route from {network_name} to {destination}")
        return False

    print(f"[PASS] {network_name}: {destination} -> {route[1]}")
    return True


def main():
    print("=== Hybrid Route Validation ===")

    forward_ok = check_connection(
        "10.20.2.10", "10.30.1.20", aws_routes, "AWS"
    )

    return_ok = check_connection(
        "10.30.1.20", "10.20.2.10", datacenter_routes, "Datacenter"
    )

    print("\n=== Summary ===")
    if forward_ok and return_ok:
        print("Route validation: PASS")
    else:
        print("Route validation: FAIL")


if __name__ == "__main__":
    main()