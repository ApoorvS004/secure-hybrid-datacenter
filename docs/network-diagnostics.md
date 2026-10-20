# Network Diagnostics Tool

## Purpose

The network diagnostics tool checks whether a target hostname can be resolved through DNS and whether an HTTPS endpoint is reachable.

It provides a basic health report that can help identify common connectivity problems.

## Checks Performed

### 1. DNS Resolution

The tool uses Python's `socket.getaddrinfo()` to resolve the target hostname into IP addresses.

- **PASS:** DNS resolution succeeded.
- **FAIL:** The hostname could not be resolved.

### 2. HTTPS Connectivity

The tool sends an HTTPS `HEAD` request using Python's `urllib` library.

- **PASS:** The server returned a successful response.
- **INFO:** The server returned an HTTP error response, indicating that an HTTP response was received.
- **FAIL:** A connection, timeout, or other network-level error prevented the request from completing.

### 3. Timing Measurements

The tool measures DNS resolution time and HTTPS request duration using `time.perf_counter()`.

These measurements help compare repeated runs. HTTPS duration is not pure network latency: it can include connection setup, TLS negotiation, server processing, and response overhead.

## How to Run

From the project root, run:

```bash
python3 scripts/network_check.py
```

## How to Run Tests

Run the automated unit tests with:

```bash
python3 -m unittest discover -s tests -v
```

The tests mock DNS and HTTPS behavior, allowing success and failure scenarios to be tested without depending on real network conditions.

## Current Limitations

- The tool checks one configured hostname.
- It does not continuously monitor connectivity.
- It does not diagnose packet loss or identify the precise cause of a network failure.
- A successful HTTPS request does not establish that every network service is healthy.
- The results represent a basic connectivity check, not a complete production monitoring system.
