import csv


def save_csv(online_devices_info):
    with open("scan_results.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["IP Address", "Hostname"])

        for ip, hostname in online_devices_info:
            writer.writerow([ip, hostname])