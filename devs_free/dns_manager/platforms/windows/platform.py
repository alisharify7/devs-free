import json
import re
import subprocess
import typing
from .base import Windows as WindowsBase

import click

class Windows(WindowsBase):
    """Win64 DNS changer utils class."""

    def get_current_dns(self) -> typing.Union[typing.List[str], str]:
        """Retrieve the currently configured DNS servers."""
        try:
            pattern = r"Statically Configured DNS Servers:(.*)"
            output = subprocess.check_output(
                ["netsh", "interface", "ip", "show", "config", 'name="Ethernet"']
            ).decode()
            match = re.search(pattern, output, re.DOTALL)
            if match:
                txt = match.group(1).strip()
                ip_addresses = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", txt)
                if ip_addresses:
                    return ip_addresses
            else:
                return ("Error: Could not parse current DNS information.")

        except subprocess.CalledProcessError as e:
            return (f"Error retrieving current DNS servers: {e}")

    def set_dns(self, dns_servers: list):
        """Set the DNS server on the system."""
        try:
            # Use netsh command for setting DNS

            selected_ethernet_interface = self.get_selected_ethernet_interfaces()

            command = [
                "netsh",
                "interface",
                "ip",
                "set",
                "dns",
                f"name={selected_ethernet_interface}",
                "static",
                dns_servers[0],
            ]
            out = subprocess.run(command, capture_output=True)
            click.echo(out)

            command = [
                "netsh",
                "interface",
                "ip",
                "add",
                "dns",
                f"name={selected_ethernet_interface} ",
                "address="+dns_servers[-1],
                "index=2"
            ]
            out = subprocess.run(command, capture_output=True)
            click.echo(out)
        except subprocess.CalledProcessError as e:
            print(e)

    def unset_dns(self):
        """Unset the DNS server on the system."""
        try:
            # Use netsh command to reset DNS to automatic
            subprocess.run(
                [
                    "netsh",
                    "interface",
                    "ip",
                    "set",
                    "dns",
                    "name=",
                    "static",
                    "address=",
                ],
                check=True,
            )
            print("DNS server unset successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error unsetting DNS server: {e}")