
import socket
import urllib.request
import urllib.error

HOST = "www.google.com"
URL = "https://www.google.com"

# Check 1: DNS resolution
print(f"Checking DNS resolution for {HOST}...")

try:
    addresses = socket.getaddrinfo(
        HOST,
        443,
        type=socket.SOCK_STREAM
    )

    unique_ips = sorted({
        result[4][0] for result in addresses
    })

    print("DNS resolution: SUCCESS")

    for ip in unique_ips:
        print(f"  Resolved IP: {ip}")

except socket.gaierror as error:
    print(f"DNS resolution: FAILED ({error})")
    raise SystemExit(1)


# Check 2: HTTPS connectivity
print(f"\nChecking HTTPS endpoint {URL}...")

try:
    request = urllib.request.Request(
        URL,
        method="HEAD",
        headers={
            "User-Agent": "HybridDatacenterHealthCheck/1.0"
        }
    )

    with urllib.request.urlopen(request, timeout=10) as response:
        print(f"HTTPS request: SUCCESS (HTTP {response.status})")

except urllib.error.HTTPError as error:
    print(f"HTTPS responded with HTTP status: {error.code}")

except (urllib.error.URLError, TimeoutError, OSError) as error:
    print(f"HTTPS request: FAILED ({error})")
