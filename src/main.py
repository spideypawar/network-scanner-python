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


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    while True:
        clear_screen()

        print(Fore.CYAN + "===================================")
        print(Fore.CYAN + "    NETWORK SCANNER PRO v1.0")
        print(Fore.WHITE + "      Developed by Harshit Pawar")
        print(Fore.GREEN + "          Version 1.0")
        print(Fore.CYAN + "===================================")

        print(Fore.GREEN + "1. Scan Network")
        print(Fore.YELLOW + "2. View Previous Report")
        print(Fore.RED + "3. Exit")

        choice = input(Fore.WHITE + "\nChoose an option: ")

        if choice == "1":
            network = input(
                Fore.WHITE
                + "\nEnter IP or Network (Example: 192.168.1 or 192.168.1.8): "
            ).strip()

            parts = network.split(".")

            if len(parts) == 4:
                network = ".".join(parts[:3])
                parts = network.split(".")

            if len(parts) != 3:
                print(Fore.RED + "\nInvalid network format!")
                input("\nPress Enter to continue...")
                continue

            scan_network(network)
            input("\nPress Enter to return to the menu...")

        elif choice == "2":
            clear_screen()
            show_previous_report()
            input("\nPress Enter to return to the menu...")

        elif choice == "3":
            confirm = input(
                Fore.YELLOW + "\nAre you sure you want to exit? (y/n): "
            ).lower()

            if confirm == "y":
                print(Fore.CYAN + "\nThank you for using Network Scanner Pro!")
                break

        else:
            print(Fore.RED + "\nInvalid option.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()