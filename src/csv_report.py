import csv
import os


def save_csv(online_devices_info):
    os.makedirs("reports", exist_ok=True)

    with open("reports/scan_results.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["IP Address", "Hostname"])

        for ip, hostname in online_devices_info:
            writer.writerow([ip, hostname])