import os
import re
import json
import pathlib
import subprocess
import typing

import questionary

from devs_free.dns_manager.platforms.base_managers import BasePlatformDNS
from devs_free.exception import NotInstalledError
from devs_free.base_platforms import BasePlatform


class Linux(BasePlatformDNS):
    """
    Base Linux DNS manager class.
    don't use this class directly,
    """

    def __init__(self):
        """
        init method.
        user must install the following packages for interacting with dns and output commands.
            - grep
            - nmcli
        in this method we simply just checks user has the following packager installed in its own
        os or not.
        """
        super().__init__()

        # check requirement apps are installed (grep, nmcli).
        output = subprocess.getoutput("grep --version")
        if "grep (GNU grep)" not in output:
            raise NotInstalledError(
                "`grep` is not installed. install it using\napt-get install grep"
            )

        output = subprocess.getoutput("nmcli --version")
        if "nmcli tool," not in output:
            raise NotInstalledError("`nmcli` is not installed.")

    @staticmethod
    def get_all_ethernet_interfaces() -> typing.List[str]:
        """
        this method returns all available ethernet interfaces.
        :return: list of all available ethernet interfaces.
        :rtype: typing.List[str]
        """
        regex_pattern = r"( *(:?[\w-]{2,666}) *)"
        expected_output_regex_pattern = r"( *(DEVICE|TYPE|STATE|CONNECTION) *)"

        output = subprocess.check_output(["nmcli", "device", "status"]).decode()
        if not re.search(expected_output_regex_pattern, output, re.MULTILINE):
            raise Exception("an error occurred in fetching all ethernet interfaces")

        output = output.split("\n")

        interfaces = []
        for each in output:
            if each:
                row = ", ".join(each)
                interfaces.append(each)
        return interfaces

    def get_selected_ethernet_interfaces(self) -> str:
        """
        this method returns user selected ethernet interfaces.

        :return: selected ethernet interfaces.
        :rtype: str
        """
        if not self.does_config_exist():
            self.set_up_init_config()

        with open(self.get_config_dir() / BasePlatform.DNS_CONFIG_FILE_NAME, "r") as f:
            data = json.load(fp=f)
        return data["default-ethernet-interface"]

    @staticmethod
    def get_current_username():
        """get current username"""
        command = "whoami"
        output = subprocess.check_output([command]).decode("utf-8")
        return str(output.rsplit("\\")[-1]).strip()

    def get_config_dir(self):
        """get config directory"""
        return pathlib.Path(f"/home/{self.get_current_username()}/.config/devs-free/")

    def does_config_exist(self):
        """check if config file exists or not"""
        return os.path.exists(self.get_config_dir() / BasePlatform.DNS_CONFIG_FILE_NAME)

    def create_config_file(self):
        """create config file"""
        if not os.path.exists(self.get_config_dir()):
            os.makedirs(self.get_config_dir())
        with open(
            file=str(self.get_config_dir() / BasePlatform.DNS_CONFIG_FILE_NAME), mode="w"
        ) as f:
            json.dump(BasePlatform.dns_base_config, fp=f)

    def get_config_file(self):
        if not self.does_config_exist():
            raise RuntimeError("config file does not exist")

        with open(
            file=str(self.get_config_dir() / BasePlatform.DNS_CONFIG_FILE_NAME), mode="r"
        ) as f:
            return json.load(f)

    def update_config_file(self, config_object: dict):
        """update config file and replace new content with old content"""
        with open(self.get_config_dir() / BasePlatform.DNS_CONFIG_FILE_NAME, "w") as f:
            json.dump(config_object, fp=f)

    def set_up_init_config(self):
        """Set up init config"""
        # get default interface
        interfaces = Linux.get_all_ethernet_interfaces()

        selected_interface = questionary.select(
            choices=interfaces, message="Select your main ethernet interface"
        ).ask()

        if self.does_config_exist():
            config_object = self.get_config_file()
        else:
            self.create_config_file()
            config_object = self.get_config_file()

        config_object["main-interface"] = selected_interface
        self.update_config_file(config_object=config_object)
