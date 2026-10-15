# Network Fundamentals for a Secure Hybrid Datacenter

## 1. Objective

Understand how a packet travels between a client, an application hosted in a public cloud, and a service hosted in a private datacenter.

## 2. Core Concepts

### IP Address
An IP address identifies a network interface or endpoint within an IP network.

### Subnet
A subnet defines a range of IP addresses within a network.

### Router
A router forwards packets between networks using routing information.

### Firewall
A firewall enforces rules governing which network traffic is allowed or denied.

### Port
A port identifies a transport-layer endpoint associated with a service, such as HTTPS on TCP port 443.

## 3. Example Scenario

A faculty member accesses a cloud-hosted research application. The application retrieves records from a database in the university's private datacenter.

Questions to investigate:

1. What is the source IP address?
2. What is the destination IP address?
3. Which routers forward the packet?
4. Where are firewall rules evaluated?
5. How is the return traffic routed?
6. What prevents an unrelated application from accessing the database?

## 4. Security Goal

Permit only the necessary communication between the research application and the private database while blocking unauthorized access from unrelated workloads.

## 5. Learning Notes

Add explanations, diagrams, commands, observations, and test results as the project progresses.
