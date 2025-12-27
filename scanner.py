# Import required modules for socket operations, multi-threading, and command-line argument parsing
import socket
import threading
import argparse
from logger import log_result

# Thread lock to ensure thread-safe operations when accessing shared resources
lock = threading.Lock()

def scan_port(host, port, timeout=1):
    """Scan a single port on the target host"""
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        # Attempt to connect to the host:port
        result = sock.connect_ex((host, port))
        sock.close()

        # Thread-safe printing and logging of results
        with lock:
            if result == 0:
                print(f"[OPEN] Port {port}")
                log_result(host, port, "OPEN")
            else:
                print(f"[CLOSED] Port {port}")
                log_result(host, port, "CLOSED")

    except socket.timeout:
        with lock:
            print(f"[TIMEOUT] Port {port}")
            log_result(host, port, "TIMEOUT")

    except Exception as e:
        with lock:
            print(f"[ERROR] Port {port} : {e}")
            log_result(host, port, "ERROR")


def start_scan(host, start_port, end_port):
    """Scan multiple ports using threading"""
    threads = []

    # Create a thread for each port in the range
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="TCP Port Scanner")
    parser.add_argument("--host", required=True, help="Target host or IP")
    parser.add_argument("--ports", required=True, help="Port or range (e.g. 80 or 1-1024)")
    args = parser.parse_args()

    # Parse port range or single port
    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
    else:
        start = end = int(args.ports)

    # Start the port scanning process
    start_scan(args.host, start, end)
