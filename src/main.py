import ipaddress
from ping import ping_host

print("===================================")
print("     NETWORK SCANNER v1")
print("      Developed by Spidey")
print("===================================")

ip = input("Enter an IP address: ")

try:
    ipaddress.ip_address(ip)

    if ping_host(ip):
        print("✅ Device is Online")
    else:
        print("❌ Device is Offline")

except ValueError:
    print("❌ Invalid IP Address")