from ping import ping_host
from report import save_report
import time


def scan_network(network):
    online_devices = 0
    online_ips = []

    total_ips = 254

    print("\nScanning...\n")

    start_time = time.time()

    for i in range(1, 255):
        ip = f"{network}.{i}"

        print(f"Scanning {i}/{total_ips}: {ip}")

        if ping_host(ip):
            print(f"✅ {ip}")
            online_devices += 1
            online_ips.append(ip)

    end_time = time.time()
    time_taken = end_time - start_time

    print("\n-----------------------------------")
    print("Scan Complete")
    print(f"Devices Found: {online_devices}")
    print(f"Time Taken: {time_taken:.2f} seconds")

    save_report(online_ips, online_devices, time_taken)

    print("\n💾 Results saved to scan_results.txt")