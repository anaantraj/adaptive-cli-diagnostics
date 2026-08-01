#importing self referential modules
from modules import system_info, input_validator, permissions_demo, config_writer, health_check


def show_menu():
    print("\n===== Adaptive CLI System Diagnostics =====")
    print("1. Show system summary")
    print("2. Show environment variables")
    print("3. Run health check")
    print("4. Permissions demo")
    print("5. Configure network settings")
    print("6. View saved config")
    print("0. Exit")


def configure_network():
    ip = input_validator.get_valid_ip()
    port = input_validator.get_valid_port()

    settings = {
        "ip": ip,
        "port": port,
        "os": system_info.get_os_type(),
    }
    config_writer.write_config(settings)


def main():
    print(f"Running on {system_info.get_os_type()}")

    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            system_info.print_system_summary()
        elif choice == "2":
            key = input("Filter by keyword (blank for default view): ").strip()
            system_info.print_env_vars(key if key else None)
        elif choice == "3":
            health_check.run_check()
        elif choice == "4":
            permissions_demo.run_demo()
        elif choice == "5":
            configure_network()
        elif choice == "6":
            config_writer.print_config()
        elif choice == "0":
            print("Exiting.")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
