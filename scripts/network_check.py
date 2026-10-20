
import socket
import urllib.request
import urllib.error
import time

HOST = "www.google.com"
URL = f"https://{HOST}"


def check_dns(host):
    print(f"\nChecking DNS resolution for {host}...")

    try:
        start_time = time.perf_counter()

        addresses = socket.getaddrinfo(
            host,
            443,
            type=socket.SOCK_STREAM
)

        elapsed = time.perf_counter() - start_time
        print(f"DNS resolution time: {elapsed * 1000:.2f} ms")
        addresses = socket.getaddrinfo(
            host,
            443,
            type=socket.SOCK_STREAM
        )

        unique_ips = sorted({
            result[4][0] for result in addresses
        })

        print("[PASS] DNS resolution")

        for ip in unique_ips:
            print(f"  IP address: {ip}")

        return True

    except socket.gaierror as error:
        print(f"[FAIL] DNS resolution: {error}")
        return False


def check_https(url):
    print(f"\nChecking HTTPS endpoint {url}...")

    request = urllib.request.Request(
        url,
        method="HEAD",
        headers={
            "User-Agent": "HybridDatacenterHealthCheck/1.0"
        }
    )

    try:
        start_time = time.perf_counter()

        with urllib.request.urlopen(request, timeout=10) as response:
            elapsed = time.perf_counter() - start_time
            print(f"HTTPS request time: {elapsed * 1000:.2f} ms")
            print(f"[PASS] HTTPS request (HTTP {response.status})")
            return True
        with urllib.request.urlopen(
            request,
            timeout=10
        ) as response:
            print(f"[PASS] HTTPS request (HTTP {response.status})")
            return True

    except urllib.error.HTTPError as error:
        print(
            f"[INFO] Server responded with HTTP {error.code}"
        )
        return True

    except (urllib.error.URLError, TimeoutError, OSError) as error:
        print(f"[FAIL] HTTPS request: {error}")
        return False


def main():
    print("=== Network Health Report ===")
    print(f"Target: {HOST}")

    dns_ok = check_dns(HOST)

    if dns_ok:
        https_ok = check_https(URL)
    else:
        print("\n[SKIP] HTTPS check because DNS failed")
        https_ok = False

    print("\n=== Summary ===")

    if dns_ok and https_ok:
        print("Overall result: HEALTHY")
    else:
        print("Overall result: UNHEALTHY")


if __name__ == "__main__":
    main()
