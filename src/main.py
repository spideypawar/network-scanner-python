from ping import ping_host

print("===================================")
print("      NETWORK SCANNER v3")
print("      Developed by Spidey")
print("===================================")

network = input("Enter network (Example: 192.168.1): ")

online_devices = 0

print("\nScanning...\n")

for i in range(1, 255):
    ip = f"{network}.{i}"

    if ping_host(ip):
        print(f"✅ {ip}")
        online_devices += 1

print("\n-----------------------------------")
print("Scan Complete")
print(f"Devices Found: {online_devices}")