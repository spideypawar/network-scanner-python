import socket


def save_report(online_devices_info, online_devices, time_taken):
    with open("scan_results.txt", "w") as file:
        file.write("NETWORK SCANNER RESULTS\n")
        file.write("=======================\n\n")
        file.write("Online Devices\n")
        file.write("-----------------------\n")

        for ip, hostname in online_devices_info:
            file.write(f"{ip} ({hostname})\n")

        file.write("\n-----------------------\n")
        file.write(f"Devices Found: {online_devices}\n")
        file.write(f"Time Taken: {time_taken:.2f} seconds\n")