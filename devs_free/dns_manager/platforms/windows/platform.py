"""
 * devs free ( developers free ) OSS
 * author: github.com/alisharify7
 * email: alisharifyofficial@gmail.com
 * license: see LICENSE for more details.
 * Copyright (c) 2023 - ali sharifi
 * https://github.com/alisharify7/devs_free
"""

import re
import typing
import subprocess

import click
from .base import Windows as WindowsBase


class Windows(WindowsBase):
    """Win64 DNS manager class."""

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
                return "Error: Could not parse current DNS information."

        except subprocess.CalledProcessError as e:
            return f"Error retrieving current DNS servers: {e}"

    def set_dns(self, dns_servers: list):
        """Set the DNS server on the system."""
        self.unset_dns(self.get_current_dns())
        selected_ethernet_interface = self.get_main_ethernet_interfaces()
        try:
            for index, ip in enumerate(dns_servers):
                command = [
                    "netsh",
                    "interface",
                    "ip",
                    "add",
                    "dns",
                    f"name=\"{selected_ethernet_interface}\"",
                    f"address=\"{ip}\"",
                    f"index={index}",
                ]
                out = subprocess.run(command, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(f"Error in setting DNS servers: {e}")

    def unset_dns(self, dns_servers: list):
        """Unset the DNS server on the system."""
        selected_ethernet_interface = self.get_main_ethernet_interfaces()
        for dns in dns_servers:
            try:
                command = [
                    "netsh",
                    "interface",
                    "ip",
                    "delete",
                    "dns",
                    f"name=\"{selected_ethernet_interface}\"",
                    f"address=\"{dns}\"",
                ]
                out = subprocess.run(command, capture_output=True)
            except subprocess.CalledProcessError as e:
                print(f"Error in setting DNS servers: {e}")