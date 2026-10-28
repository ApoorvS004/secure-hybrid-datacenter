# Hybrid Datacenter IP Addressing Plan

## 1. Objective

Define a proposed IPv4 addressing scheme for the AWS VPC and private datacenter. The design uses private IPv4 ranges and avoids overlap between the two environments.

## 2. Proposed Address Allocation

| Environment | CIDR | Purpose |
|---|---|---|
| AWS VPC | 10.20.0.0/16 | Cloud network address space |
| AWS public subnet | 10.20.1.0/24 | Internet-facing entry point |
| AWS private subnet | 10.20.2.0/24 | Internal application workloads |
| Private datacenter | 10.30.0.0/16 | On-premises network |

## 3. Design Rationale

- Private IPv4 addresses are reusable across independent networks.
- The AWS VPC uses a /16 prefix to provide room for multiple subnets.
- The initial public and private subnets use /24 prefixes for simplicity.
- The datacenter uses a separate /16 range to avoid overlap with the AWS VPC.
- The proposed address ranges must be checked against existing networks before deployment.

## 4. Routing Requirements

- AWS resources within the VPC use local VPC routing.
- Traffic destined for 10.30.0.0/16 must use the selected hybrid connectivity path.
- The datacenter must have a return route for the AWS network.
- Security rules must explicitly permit the intended traffic.

## 5. Security Principles

- Do not expose internal databases directly to the public internet.
- Allow only required source ranges, destination ranges, protocols, and ports.
- Use an appropriate secure connectivity mechanism, such as a site-to-site VPN.
- Treat routing and security policy as separate controls.

## 6. Status and Limitations

This is a proposed logical design, not deployed infrastructure. Address overlap, subnet sizing, availability-zone placement, routing, and connectivity requirements must be validated before implementation.

## 7. Routing and Traffic Flow

AWS application: 10.20.2.10
Datacenter database: 10.30.1.20
AWS route: 10.30.0.0/16 → hybrid VPN
Datacenter return route: 10.20.0.0/16 → hybrid VPN
Both directions must be allowed by the relevant security controls.