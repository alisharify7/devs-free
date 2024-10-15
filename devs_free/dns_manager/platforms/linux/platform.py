import subprocess
from .base import Linux as LinuxBase

class Linux(LinuxBase):
    """A class for managing DNS settings on Linux."""
    def __init__(self):
        super().__init__()


    def get_current_dns(self):
        try:
            output = subprocess.getoutput("resolvectl | grep 'DNS Servers'")
            dns_servers = output.strip().split("DNS Servers: ")[-1].split()
            return dns_servers
        except subprocess.CalledProcessError as e:
            print(f"error  {e}")
            return None

    def set_dns(self, dns_servers):
        """Set the DNS server on the specified network interface.

        Args:
        """
        selected_ethernet_interface = self.get_selected_ethernet_interfaces()
        try:
            # Use nmcli command to set DNS
            subprocess.run(
                [
                    "nmcli",
                    "device",
                    "modify",
                    f"ifname={selected_ethernet_interface}",
                    f"ipv4.dns={dns_servers}",
                ]
            )
            print("DNS server set successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error setting DNS server: {e}")

    def unset_dns(self, interface="eth0"):
        """Unset the DNS server on the specified network interface.

        Args:
            interface (str): The name of the network interface (e.g., "eth0", "wlan0").
        """
        try:
            # Use nmcli command to reset DNS to automatic
            subprocess.run(
                ["nmcli", "device", "modify", f"ifname={interface}", "ipv4.dns=auto"]
            )
            print("DNS server unset successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error unsetting DNS server: {e}")