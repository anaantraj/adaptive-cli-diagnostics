import platform
import os
import sys


def get_os_type():
    return platform.system()


def print_system_summary():
    print("\n--- System Summary ---")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor() or 'unknown'}")


def print_env_vars(filter_key=None):
    print("\n--- Environment Variables ---")
    count = 0
    for key, value in os.environ.items():
        if filter_key and filter_key.lower() not in key.lower():
            continue
        print(f"{key} = {value}")
        count += 1
        if count >= 15 and not filter_key:
            print("... (truncated, use filter to narrow down)")
            break


def is_windows():
    return get_os_type() == "Windows"
