import os, sys
import time 
import scanner as scanner
import constants as cs


class eagle:
    def __init__(self) -> None:
        self.hosts = []
        self.hosts_down = []
        self.ip_range = ""

    def run_command(self, command):
        command_parts = command.split()  # Split the command and arguments
        base_command = command_parts[0]  # Extract the base command

        if base_command == "help":
            cs.constants.help()

        elif base_command == "clear":
            print("\033c")
            self.controller()

        elif base_command == "exit":
            sys.exit()

        elif base_command == "hosts":
            self.show_hosts()

        elif base_command == "alarm":
            self.alarm()

        elif base_command == "scan":
            # Check if there are arguments
            if len(command_parts) > 1:
                if command_parts[1] == "--range" and len(command_parts) > 2:
                    ip_range = command_parts[2]
                    self.ip_range = ip_range
                else:
                    print("\nInvalid scan command. Usage: scan --range <IP range>")
                    return
            else:
                print("\nMissing IP range argument for scan command. Usage: scan --range <IP range>")
                return

            devices = scanner.scanner().scanner(ip_range)
            self.hosts = devices
            if len(self.hosts) == 0:
                print(f"{cs.bold_red}No hosts found :({cs.reset}")

            else:
                print("\n")
                print(f"{'IP Address':<15} {'MAC Address':<18} {'Device Name':<20} {'State':<10}")
                print("="*63)
                for device in devices:
                    print(f"{device['ip']:<15} {device['mac']:<18} {device['name']:<20} {device['state']:<10}")

        else:
            print(f"Command not found: {base_command}")

    def show_hosts(self):
            
            devices = self.hosts
            self.hosts = devices

            if len(self.hosts) == 0:
                print(f"{cs.bold_red}No hosts found :({cs.reset}")
            else:
                print("\n")
                print(f"{'IP Address':<15} {'MAC Address':<18} {'Device Name':<20} {'State':<10}")
                print("="*63)
                for device in devices:
                    print(f"{device['ip']:<15} {device['mac']:<18} {device['name']:<20} {device['state']:<10}")


    def alarm(self):
        while True:
            devices = scanner.scanner().scanner(self.ip_range)
            ips_array = [host['ip'] for host in devices]


            missing_hosts = [host for host in self.hosts if host['ip'] not in ips_array]
            self.hosts_down = missing_hosts
            if len(self.hosts_down) == 0:
                    print(f"{cs.bold_green}No faults :){cs.reset}")
            else:
                print("\n")
                print(f"{'IP Address':<15} {'MAC Address':<18} {'Device Name':<20} {'State':<10}")
                print("="*63)
                for device in self.hosts_down:
                    print(f"{cs.bold_red}{device['ip']:<15} {device['mac']:<18} {device['name']:<20} {'down':<10} {cs.reset}")  
            time.sleep(1)

    def controller(self):
        while True:
            user_input = input(f"\n{cs.bold_pink}eagle-> {cs.reset}")
            self.run_command(user_input)

    def main(self):
        cs.constants.intro()
        self.controller()

if __name__ == "__main__":
    eagle().main()
