from scanner import scan_network
import os
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)


def show_previous_report():
    report_path = "reports/scan_results.txt"

    if os.path.exists(report_path):
        print(Fore.CYAN + "\n===== PREVIOUS REPORT =====\n")
        with open(report_path, "r") as file:
            print(file.read())
    else:
        print(Fore.RED + "\nNo previous report found.\n")


def main():
    while True:
        print(Fore.CYAN + "\n===================================")
        print(Fore.CYAN + "      NETWORK SCANNER PRO")
        print(Fore.CYAN + "      Developed by Spidey")
        print(Fore.CYAN + "===================================")

        print(Fore.GREEN + "1. Scan Network")
        print(Fore.YELLOW + "2. View Previous Report")
        print(Fore.RED + "3. Exit")

        choice = input(Fore.WHITE + "\nChoose an option: ")

        if choice == "1":
            network = input(
                Fore.WHITE + "\nEnter IP or Network (Example: 192.168.1 or 192.168.1.8): "
            ).strip()

            parts = network.split(".")

            if len(parts) == 4:
                network = ".".join(parts[:3])

            scan_network(network)

        elif choice == "2":
            show_previous_report()

        elif choice == "3":
            print(Fore.CYAN + "\nThank you for using Network Scanner Pro!")
            break

        else:
            print(Fore.RED + "\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()