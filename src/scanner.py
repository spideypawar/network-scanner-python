from ping import ping_host
from report import save_report
from hostname import get_hostname
import time


def scan_network(network):
    online_devices = 0
    online_devices_info = []

    total_ips = 254

    print("\nScanning...\n")

    start_time = time.time()

    for i in range(1, 255):
        ip = f"{network}.{i}"

        print(f"Scanning {i}/{total_ips}: {ip}")

        if ping_host(ip):
            hostname = get_hostname(ip)

            print(f"✅ {ip} ({hostname})")

            online_devices += 1
            online_devices_info.append((ip, hostname))

    end_time = time.time()
    time_taken = end_time - start_time

    print("\n-----------------------------------")
    print("Scan Complete")
    print(f"Devices Found: {online_devices}")
    print(f"Time Taken: {time_taken:.2f} seconds")

    save_report(online_devices_info, online_devices, time_taken)

    print("\n💾 Results saved to scan_results.txt")