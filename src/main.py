from ping import ping_host

print("===================================")
print("      NETWORK SCANNER v1")
print("      Developed by Spidey")
print("===================================")

network = input("Enter network (Example: 192.168.1): ")

for i in range(1, 255):
    ip = f"{network}.{i}"

    print(f"\nScanning {ip}...")

    if ping_host(ip):
        print("✅ Device is Online")
    else:
        print("❌ Device is Offline")