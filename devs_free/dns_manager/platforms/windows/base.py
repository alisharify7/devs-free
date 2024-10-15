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
import pathlib
import subprocess

import questionary
from devs_free.dns_manager.base_platforms import BasePlatformDNS




class Windows(BasePlatformDNS):
    """Window DNS manager base class"""
    @staticmethod
    def get_all_ethernet_interfaces():
        """this method returns all available ethernet interfaces
        Using `ip link show`
        """
        interfaces = []
        output = subprocess.check_output(["ipconfig", "/all"]).decode()
        for line in output.splitlines():
            if line.startswith("Ethernet adapter"):
                line = line.replace(":", "")
                interfaces.append(line)

        return interfaces

    def get_main_ethernet_interfaces(self):
        """this method returns user selected (main) ethernet interfaces"""
        if not self.does_config_exist():
            self.set_up_init_config()

        with open(self.get_config_dir() / BasePlatformDNS.dns_config_file, "r") as f:
            data = json.load(fp=f)
        return data['main-interface']

    @staticmethod
    def get_current_username():
        """get os current username"""
        command = 'whoami'
        output = subprocess.check_output([command]).decode('utf-8')
        return str(output.rsplit("\\")[-1]).strip()

    def does_config_exist(self):
        """check if config file exists or not"""
        return os.path.exists(self.get_config_dir() / BasePlatformDNS.dns_config_file)

    def get_config_dir(self):
        """get config directory"""
        conf_dir = pathlib.Path(f"C:\\Users\\{Windows.get_current_username()}\\devs_free\\")
        if os.path.exists(conf_dir):
            return conf_dir
        else:
            os.mkdir(conf_dir)
            return conf_dir

    def create_config_file(self):
        """create dns config file from base default config """
        with open(file=str(self.get_config_dir() / BasePlatformDNS.dns_config_file), mode="w") as f:
            json.dump(BasePlatformDNS.dns_default_config, fp=f)

    def get_config_file(self):
        """get dns config file content"""
        if not self.does_config_exist():
            raise RuntimeError("config file does not exist")

        with open(file=str(self.get_config_dir() / BasePlatformDNS.dns_config_file), mode="r") as f:
            return json.load(f)

    def update_config_file(self, config_object: dict):
        """update config file with new config """
        with open(self.get_config_dir() / BasePlatformDNS.dns_config_file, "w") as f:
            json.dump(config_object, fp=f)

    def set_up_init_config(self):
        """this method initializes DNS config file"""
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

        config_object['main-interface'] = selected_interface
        self.update_config_file(config_object=config_object)