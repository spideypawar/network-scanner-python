from scanner import scan_network

print("===================================")
print("      NETWORK SCANNER v4")
print("      Developed by Spidey")
print("===================================")

network = input("Enter IP or Network (Example: 192.168.1 or 192.168.1.8): ").strip()

parts = network.split(".")

if len(parts) == 4:
    network = ".".join(parts[:3])

scan_network(network)