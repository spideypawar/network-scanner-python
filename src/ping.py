import subprocess


def ping_host(ip):
    result = subprocess.run(
        ["ping", "-n", "1", "-w", "300", ip],
        capture_output=True,
        text=True
    )

    return result.returncode == 0