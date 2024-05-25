import nmap
import socket

class scanner:
    def __init__(self) -> None:
        self.hosts = []
        self.hosts_down = []

    def get_devices(self,ip_range):
        # Initialize the nmap scanner
        nm = nmap.PortScanner()
        # Perform a ping scan (no root privileges required)
        nm.scan(hosts=ip_range, arguments='-sn -T4')

        devices = []

        for host in nm.all_hosts():
            device_info = {
                "ip": host,
                "mac": nm[host]['addresses'].get('mac', 'Unknown'),
                "name": self.get_device_name(host),
                "state": nm[host].state()
            }
            devices.append(device_info)

        return devices

    def get_device_name(self,ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except socket.herror:
            return "Unknown"

    def scanner(self,ip_range):
        # ip_range = "192.168.100.0/24"  # Modify this to match your network's IP range
        devices = self.get_devices(ip_range)
        self.hosts = devices
        return devices
    
    def get_down_hosts(self):
        devices = self.get_devices()

if __name__ == "__main__":
    eagle.scanner()
