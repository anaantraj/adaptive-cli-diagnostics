def validate_ip(ip_str):
    parts = ip_str.strip().split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True


def validate_port(port_str):
    port_str = port_str.strip()
    if not port_str.isdigit():
        return False
    port = int(port_str)
    return 0 < port <= 65535


def validate_threshold(value_str, min_val=0, max_val=100):
    value_str = value_str.strip()
    try:
        value = float(value_str)
    except ValueError:
        return None
    if min_val <= value <= max_val:
        return value
    return None


def get_valid_ip(prompt="Enter IP address: "):
    while True:
        ip = input(prompt)
        if validate_ip(ip):
            return ip
        print("Invalid IP format. Try again (e.g. 192.168.1.1)")


def get_valid_port(prompt="Enter port number: "):
    while True:
        port = input(prompt)
        if validate_port(port):
            return int(port)
        print("Invalid port. Must be a number between 1 and 65535.")


def get_valid_threshold(prompt="Enter threshold (0-100): "):
    while True:
        raw = input(prompt)
        result = validate_threshold(raw)
        if result is not None:
            return result
        print("Invalid value. Enter a number between 0 and 100.")
