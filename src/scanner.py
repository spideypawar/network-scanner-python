from concurrent.futures import ThreadPoolExecutor, as_completed
from ping import ping_host
from hostname import get_hostname
from report import save_report
import time


def scan_ip(ip):
    if ping_host(ip):
        hostname = get_hostname(ip)
        return (ip, hostname)
    return None


def scan_network(network):
    online_devices_info = []

    start_time = time.time()

    print("\nScanning...\n")

    ips = [f"{network}.{i}" for i in range(1, 255)]

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_ip, ip) for ip in ips]

        completed = 0

        for future in as_completed(futures):
            completed += 1
            print(f"Progress: {completed}/{len(ips)}", end="\r")

            result = future.result()

            if result:
                ip, hostname = result
                print(f"\n✅ {ip} ({hostname})")
                online_devices_info.append(result)

    end_time = time.time()
    time_taken = end_time - start_time

    print("\n-----------------------------------")
    print("Scan Complete")
    print(f"Devices Found: {len(online_devices_info)}")
    print(f"Time Taken: {time_taken:.2f} seconds")

    save_report(
        online_devices_info,
        len(online_devices_info),
        time_taken
    )

    print("\n💾 Results saved to scan_results.txt")