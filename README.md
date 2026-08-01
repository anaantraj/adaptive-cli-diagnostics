# Adaptive CLI System Diagnostics & Configuration Tool
# Author: Anaant Raj | CSE3011 Python Programming | MIT License 

A lightweight command-line tool for inspecting your system, running quick health checks, and managing local config, all from one interactive menu. No dependencies, no setup, just Python.

## Features

- **System summary** — OS, Python version, architecture, processor info
- **Environment variable inspector** — browse or filter by keyword
- **Health check** — evaluate CPU/memory/disk usage against warning and critical thresholds
- **Permissions demo** — build and manipulate Unix-style rwx flags using bitwise operations
- **Network config** — validate and persist IP/port settings to a local config file
- **Config viewer** — read back whatever you've saved

## Getting started

```bash
git clone https://github.com/yourusername/adaptive-cli-diagnostics.git
cd adaptive-cli-diagnostics
python main.py
```

Pure standard library, so nothing to install and no dependencies to handle!

## Demo

```
Running on Linux

===== Adaptive CLI System Diagnostics =====
1. Show system summary
2. Show environment variables
3. Run health check
4. Permissions demo
5. Configure network settings
6. View saved config
0. Exit
Select an option: 1

--- System Summary ---
OS: Linux 6.18.5
Python version: 3.12.3
Machine: x86_64
Processor: x86_64

Select an option: 3

--- Health Check (enter simulated usage %) ---
CPU usage %: 85
Memory usage %: 92
Disk usage %: 60

Results:
- Critical: CPU and memory both under heavy load.

Select an option: 4

--- Permissions Demo (bitwise ops) ---
Allow read? (y/n): y
Allow write? (y/n): n
Allow execute? (y/n): y
Permission value: 5 (binary: 0b101)
Permission string: r-x
Flipped (XOR with 111): -w-

Select an option: 5
Enter IP address: 192.168.1.10
Enter port number: 8080

Config written to config/default_config.txt

Select an option: 6

--- Current Config ---
ip: 192.168.1.10
port: 8080
os: Linux
```

## Project structure

```
.
├── main.py                     # entry point, menu loop
├── modules/
│   ├── system_info.py          # OS detection, env vars
│   ├── input_validator.py      # IP/port/threshold validation
│   ├── health_check.py         # usage threshold evaluation
│   ├── permissions_demo.py     # bitwise rwx permission simulation
│   └── config_writer.py        # read/write local config
├── config/
│   └── default_config.txt      # saved settings
└── requirements.txt
```

## Requirements

Python 3.6+. No third-party packages.

## License

MIT
