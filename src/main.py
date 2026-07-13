import ipaddress

print("===================================")
print("     NETWORK SCANNER v1")
print("      Developed by Spidey")
print("===================================")

ip = input("Enter an IP address: ")

try:
    ipaddress.ip_address(ip)
    print("✅ Valid IP Address")
except ValueError:
    print("❌ Invalid IP Address")