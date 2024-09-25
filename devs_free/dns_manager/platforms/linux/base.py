import os
import re
import json
import pathlib
import subprocess

import questionary

from devs_free.dns_manager.base_platforms import BasePlatformDNS
from devs_free.exception import NotInstalledError
from devs_free.base_platforms import BasePlatform

class Linux(BasePlatformDNS):
    """
    Base Linux DNS manager class.
    don't use this class directly, use `devs_free.dns_manager.linux.Linux` instead.
    """
    def __init__(self):
        super().__init__()

        # check requirement apps are installed (grep, nmcli).
        output = subprocess.getoutput("grep --version")
        if "grep (GNU grep)" not in output:
            raise NotInstalledError("`grep` is not installed. install it using\napt-get install grep")

        output = subprocess.getoutput("nmcli --version")
        if "nmcli tool," not in output:
            raise NotInstalledError("`nmcli` is not installed.")

    @staticmethod
    def get_all_ethernet_interfaces():
        """this method returns all available ethernet interfaces."""
        regex_patterns = r"^Ethernet adapter (.*):"
        output = subprocess.check_output(
            ["ipconfig", ]
        ).decode()
        result = re.findall(regex_patterns, output, re.MULTILINE)
        return result

    def get_selected_ethernet_interfaces(self):
        if not self.does_config_exist():
            self.set_up_init_config()

        with open(self.get_config_dir() / BasePlatform.dns_config_file, "r") as f:
            data = json.load(fp=f)
        return data['default-ethernet-interface']

    @staticmethod
    def get_current_username():
        """get current username"""
        command = 'whoami'
        output = subprocess.check_output([command]).decode('utf-8')
        return str(output.rsplit("\\")[-1]).strip()

    def get_config_dir(self):
        """get config directory"""
        return pathlib.Path(f"/home/{self.get_current_username()}/.config/devs-free/")

    def does_config_exist(self):
        """check if config file exists or not"""
        return os.path.exists(self.get_config_dir() / BasePlatform.dns_config_file)

    def create_config_file(self):
        """create config file """
        if not os.path.exists(self.get_config_dir()):
            os.makedirs(self.get_config_dir())
        with open(file=str(self.get_config_dir() / BasePlatform.dns_config_file), mode="w") as f:
            json.dump(BasePlatform.dns_base_config, fp=f)

    def get_config_file(self):
        if not self.does_config_exist():
            raise RuntimeError("config file does not exist")

        with open(file=str(self.get_config_dir() / BasePlatform.dns_config_file), mode="r") as f:
            return json.load(f)

    def update_config_file(self, config_object: dict):
        with open(self.get_config_dir() / BasePlatform.dns_config_file, "w") as f:
            json.dump(config_object, fp=f)

    def set_up_init_config(self):
        # get default interface
        interfaces = Linux.get_all_ethernet_interfaces()
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