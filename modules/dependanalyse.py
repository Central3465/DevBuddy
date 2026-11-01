import os

def find_dependencies(path):
    dependencies = []
    with os.scandir(path) as entries:
        for entry in entries:
            if not entry.is_file():
                continue

            if entry.name.endswith(('.txt', '.toml')):
                print(f"Success: {entry.name}")
                dependencies.append(entry.name)
    return dependencies

def scan_txt(file):
    print(f"\nScanning {file}...\n")

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line and not line.startswith("#"):
                print(line)


def scan_toml(file):
    print(f"\nScanning {file}...\n")

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            if "dependencies" in line.lower():
                print(line.strip())