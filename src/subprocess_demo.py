import subprocess

result = subprocess.run(
    ["ping", "8.8.8.8"],
    capture_output=True,
    text=True
)

print(result.stdout)