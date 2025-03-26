"""
 * devs free ( developers free ) OSS
 * author: github.com/alisharify7
 * email: alisharifyofficial@gmail.com
 * license: see LICENSE for more details.
 * Copyright (c) 2023 - ali sharifi
 * https://github.com/alisharify7/devs_free
"""
import re
import os
import json
import typing
import pathlib
import subprocess

import questionary
from devs_free.dns_manager.platforms.base_managers import BasePlatformDNS


class Windows(BasePlatformDNS):
    """Window DNS manager base class"""

    @staticmethod
    def get_all_ethernet_interfaces() -> typing.List[str]:
        """this method returns all available ethernet interfaces
        Using `netsh interface show interface`
        extract all available ethernet interfaces using regex from output of the command.

        https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh-contexts
        https://stackoverflow.com/questions/61918509/using-netsh-to-find-an-interface-name-and-define-it-as-a-variable-in-a-batch-fil
        https://superuser.com/questions/619786/use-commandline-to-show-disabled-network-interfaces-in-windows-mobile-broadban
        """
        output = subprocess.check_output(
            ["netsh", "interface", "show", "interface"]
        ).decode()
        # Regex pattern to extract interface names
        pattern = r"^\s*Enabled\s+Connected\s+Dedicated\s+(.+)$"

        # Extract interface names
        interfaces = re.findall(pattern, output, re.MULTILINE)
        interfaces = [str(interface).strip() for interface in interfaces]
        return interfaces

    def get_main_ethernet_interfaces(self) -> str:
        """this method returns user selected (main) ethernet interfaces"""
        if not self.does_config_exist():
            self.set_up_init_config()

        data = self.get_config_file()
        return data["main-interface"]

    @staticmethod
    def get_current_username() -> str:
        """get os current username

        https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/whoami
        """
        command = "whoami"
        output = subprocess.check_output([command]).decode("utf-8")
        return str(output.rsplit("\\")[-1]).strip()

    def does_config_exist(self) -> bool:
        """check if config file exists or not"""
        return os.path.exists(self.get_config_dir() / self.DNS_CONFIG_FILE_NAME)

    def get_config_dir(self) -> pathlib.Path:
        """get config directory
        config dir in windows is
        C:/users/<current user's username>/devs_free/
        """
        conf_dir = pathlib.Path(
            f"C:\\Users\\{Windows.get_current_username()}\\devs_free\\"
        )
        if not os.path.exists(conf_dir):
            os.mkdir(conf_dir)
        return conf_dir

    def create_config_file(self):
        """create dns config file from base default config"""
        with open(
            file=str(self.get_config_dir() / self.DNS_CONFIG_FILE_NAME), mode="w"
        ) as f:
            json.dump(self.DNS_DEFAULT_CONFIG, fp=f)

    def get_config_file(self):
        """get dns config file content"""
        if not self.does_config_exist():
            self.create_config_file()

        with open(
            file=str(self.get_config_dir() / BasePlatformDNS.DNS_CONFIG_FILE_NAME), mode="r"
        ) as f:
            return json.load(f)

    def update_config_file(self, config_object: dict):
        """update config file with new config"""
        with open(self.get_config_dir() / BasePlatformDNS.DNS_CONFIG_FILE_NAME, "w") as f:
            json.dump(config_object, fp=f)

    def set_up_init_config(self):
        """this method initializes DNS config file"""
        interfaces = Windows.get_all_ethernet_interfaces()
        selected_interface = questionary.select(
            choices=interfaces, message="Select your main ethernet interface"
        ).ask()

        if not self.does_config_exist():
            self.create_config_file()

        config_object = self.get_config_file()
        config_object["main-interface"] = selected_interface
        self.update_config_file(config_object=config_object)
