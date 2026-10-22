# Python Route Simulator

## Purpose
Simulate IPv4 route selection using longest-prefix matching.

## How it works
- Accepts a destination IP and a routing table.
- Checks which networks contain the destination.
- Selects the matching route with the longest prefix.
- Returns None if no route matches.

## Example routes
- 0.0.0.0/0 -> internet-gateway
- 10.30.0.0/16 -> hybrid-vpn
- 10.30.1.0/24 -> specific-network

## Testing
Run all project tests with:
python3 -m unittest discover -s tests -v

## Limitations
This is a learning simulator, not a production router.
It does not model route metrics, interface states, or actual packet forwarding.