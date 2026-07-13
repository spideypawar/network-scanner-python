from ping import ping_host
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

    print("\n-----------------------------------")
    print("Scan Complete")
    print(f"Devices Found: {online_devices}")
    print(f"Time Taken: {end_time - start_time:.2f} seconds")

    with open("scan_results.txt", "w") as file:
        file.write("NETWORK SCANNER RESULTS\n")
        file.write("=======================\n\n")
        file.write("Online Devices\n")
        file.write("-----------------------\n")

        for ip in online_ips:
            file.write(ip + "\n")

        file.write("\n-----------------------\n")
        file.write(f"Devices Found: {online_devices}\n")
        file.write(f"Time Taken: {end_time - start_time:.2f} seconds\n")

    print("\n💾 Results saved to scan_results.txt")