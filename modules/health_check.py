def evaluate_health(cpu_usage, mem_usage, disk_usage):
    issues = []

    if cpu_usage > 80 and mem_usage > 80:
        issues.append("Critical: CPU and memory both under heavy load.")
    elif cpu_usage > 80 or mem_usage > 80:
        issues.append("Warning: high usage on CPU or memory.")

    if disk_usage >= 90:
        issues.append("Critical: disk almost full.")
    elif disk_usage >= 75:
        issues.append("Warning: disk usage getting high.")

    if not issues:
        issues.append("All systems normal.")

    return issues


def run_check():
    print("\n--- Health Check (enter simulated usage %) ---")
    from modules.input_validator import get_valid_threshold

    cpu = get_valid_threshold("CPU usage %: ")
    mem = get_valid_threshold("Memory usage %: ")
    disk = get_valid_threshold("Disk usage %: ")

    results = evaluate_health(cpu, mem, disk)
    print("\nResults:")
    for r in results:
        print(f"- {r}")
