import os

CONFIG_PATH = os.path.join("config", "default_config.txt")


def write_config(settings):
    with open(CONFIG_PATH, "w") as f:
        for key, value in settings.items():
            f.write(f"{key}={value}\n")
    print(f"\nConfig written to {CONFIG_PATH}")


def read_config():
    if not os.path.exists(CONFIG_PATH):
        print("No config file found yet.")
        return {}

    settings = {}
    with open(CONFIG_PATH, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "=" not in line:
                continue
            key, value = line.split("=", 1)
            settings[key] = value
    return settings


def print_config():
    settings = read_config()
    if not settings:
        return
    print("\n--- Current Config ---")
    for key, value in settings.items():
        print(f"{key}: {value}")
