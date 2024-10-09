import re
import subprocess
import os
import json
import pathlib
from devs_free.dns_manager.base_platforms import BasePlatformDNS


import questionary


class Windows(BasePlatformDNS):
    @staticmethod
    def get_all_ethernet_interfaces():
        # Using `ip link show` to get interface details
        patterns = r"^\d+: (.+):"
        output = subprocess.check_output(["ip", "link", "show"]).decode()
        result = re.findall(patterns, output, re.MULTILINE)

        # Filter out non-ethernet interfaces
        ethernet_interfaces = [iface for iface in result if "eth" in iface or "en" in iface]
        return ethernet_interfaces

    def get_selected_ethernet_interfaces(self):
        if not self.does_config_exist():
            self.set_up_init_config()

        with open(self.get_config_dir() / BasePlatformDNS.config_file, "r") as f:
            data = json.load(fp=f)
        return data['dns']['default-ethernet-interface']

    @staticmethod
    def get_current_username():
        """get current username"""
        command = 'whoami'
        output = subprocess.check_output([command]).decode('utf-8')
        return str(output.rsplit("\\")[-1]).strip()

    def does_config_exist(self):
        """check if config file exists or not"""
        return os.path.exists(self.get_config_dir() / BasePlatformDNS.config_file)

    def get_config_dir(self):
        """get config directory"""
        return pathlib.Path(f"C:\\Users\\{Windows.get_current_username()}")

    def create_config_file(self):
        """create config file """
        with open(file=str(self.get_config_dir() / BasePlatformDNS.config_file), mode="w") as f:
            json.dump(BasePlatformDNS.base_config, fp=f)

    def get_config_file(self):
        if not self.does_config_exist():
            raise RuntimeError("config file does not exist")

        with open(file=str(self.get_config_dir() / BasePlatformDNS.config_file), mode="r") as f:
            return json.load(f)

    def update_config_file(self, config_object: dict):
        with open(self.get_config_dir() / BasePlatformDNS.config_file, "w") as f:
            json.dump(config_object, fp=f)

    def set_up_init_config(self):
        interfaces = Windows.get_all_ethernet_interfaces()
        selected_interface = questionary.select(
            choices=interfaces,
            message="Select your main ethernet interface"
        ).ask()

        if self.does_config_exist():
            config_object = self.get_config_file()
        else:
            self.create_config_file()
            config_object = self.get_config_file()

        config_object['default-ethernet-interface'] = selected_interface
        self.update_config_file(config_object=config_object)