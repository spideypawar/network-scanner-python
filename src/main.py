import ipaddress
from ping import ping_host

ips = [
    "127.0.0.1",
    "8.8.8.8",
    "1.1.1.1",
    "192.168.1.1"
]

print("===================================")
print("      NETWORK SCANNER v1")
print("      Developed by Spidey")
print("===================================")

for ip in ips:
    print(f"\nScanning {ip}...")

    if ping_host(ip):
        print("✅ Device is Online")
    else:
        print("❌ Device is Offline")