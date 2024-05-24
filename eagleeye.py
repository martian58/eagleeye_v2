import os, sys
import scanner as scanner
import constants as cs

def run_command(command):
    if command == "help":
        cs.constants.help()

    elif command == "clear":
        print("\033c")
        controller()

    elif command == "exit":
        sys.exit()

    elif command == "scan":
        devices = scanner.eagle().scanner()
        print(f"{'IP Address':<15} {'MAC Address':<18} {'Device Name':<20} {'State':<10}")
        print("="*63)
        for device in devices:
            print(f"{device['ip']:<15} {device['mac']:<18} {device['name']:<20} {device['state']:<10}")

    else:
        print(f"Command not found: {command}")
def controller():
    while True:
        user_input = input(f"{cs.bold_pink}eagle--> {cs.reset}")
        run_command(user_input)

def main():
    controller()

if __name__ == "__main__":
    main()
