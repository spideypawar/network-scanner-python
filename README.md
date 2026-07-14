# 🌐 Network Scanner Pro

> A professional multithreaded network scanner built with Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-v1.0.0-success)

---

## 📖 Overview

Network Scanner Pro is a fast and lightweight command-line tool that scans devices on a local network, detects hostnames, and generates detailed scan reports in TXT and CSV formats.

This project was built to learn Python networking, multithreading, file handling, and CLI application development.

---

## ✨ Features

- ⚡ Fast multithreaded network scanning
- 🌐 Hostname detection
- 📄 TXT report generation
- 📊 CSV report generation
- 🎨 Professional colorized terminal interface
- 📁 View previous scan reports
- 📦 Windows executable (.exe)

---

## 📷 Screenshots

> Add screenshots inside the `screenshots/` folder.

- Main Menu
- Network Scanning
- Scan Results
- Previous Report

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/spideypawar/network-scanner-python.git
```

Go to the project folder:

```bash
cd network-scanner-python
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python src/main.py
```

Or run the Windows executable:

```text
dist/main.exe
```

---

## 📂 Project Structure

```text
network-scanner-python/
│
├── src/
│   ├── main.py
│   ├── scanner.py
│   ├── ping.py
│   ├── hostname.py
│   ├── report.py
│   ├── csv_report.py
│   └── utils.py
│
├── reports/
├── screenshots/
├── docs/
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🛠 Technologies Used

- Python 3
- Colorama
- ThreadPoolExecutor
- PyInstaller
- Git
- GitHub

---

## 📄 Reports

The application automatically generates:

- TXT Scan Report
- CSV Scan Report

Reports are stored inside the `reports/` directory.

---

## 🔮 Future Improvements

- Port Scanner
- MAC Address Detection
- Vendor Lookup
- Network Mapping
- GUI Version

---

## 👨‍💻 Author

**Harshit Pawar**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.