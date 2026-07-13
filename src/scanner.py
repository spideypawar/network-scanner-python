from ping import ping_host


def scan_network(network):
    online_devices = 0
    online_ips = []

    print("\nScanning...\n")

    for i in range(1, 255):
        ip = f"{network}.{i}"

        if ping_host(ip):
            print(f"✅ {ip}")
            online_devices += 1
            online_ips.append(ip)

    print("\n-----------------------------------")
    print("Scan Complete")
    print(f"Devices Found: {online_devices}")

    with open("scan_results.txt", "w") as file:
        file.write("NETWORK SCANNER RESULTS\n")
        file.write("=======================\n\n")
        file.write("Online Devices\n")
        file.write("-----------------------\n")

        for ip in online_ips:
            file.write(ip + "\n")

        file.write("\n-----------------------\n")
        file.write(f"Devices Found: {online_devices}\n")

    print("\n💾 Results saved to scan_results.txt")