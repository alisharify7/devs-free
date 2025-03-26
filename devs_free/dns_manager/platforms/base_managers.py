"""
 * devs free ( developers free ) OSS
 * author: github.com/alisharify7
 * email: alisharifyofficial@gmail.com
 * license: see LICENSE for more details.
 * Copyright (c) 2023 - ali sharifi
 * https://github.com/alisharify7/devs_free
"""

from abc import ABC
from devs_free.base_platforms import BasePlatform


class BasePlatformDNS(BasePlatform, ABC):
    """
    Base DNS manager class.
    all dns manager classes should inherit from this class no matter what Dev type they are,
    and they should implement the all methods that this class contain.
    """

    @staticmethod
    def get_all_ethernet_interfaces():
        """get all available Ethernet interfaces on the current platform."""
        raise NotImplemented()

    def get_main_ethernet_interfaces(self):
        """get current selected Ethernet interfaces on the current platform."""
        raise NotImplemented()

    @staticmethod
    def get_current_username():
        """get current user of the OS."""
        raise NotImplemented()

    def does_config_exist(self):
        """check config file exists."""
        raise NotImplemented()

    def get_config_dir(self):
        """get config dir."""
        raise NotImplemented()

    def create_config_file(self):
        """create config file in config dir."""
        raise NotImplemented()

    def get_config_file(self):
        """get config content from config file."""
        raise NotImplemented()

    def update_config_file(self, config_object: dict):
        """update config file in config file."""
        raise NotImplemented()

    def set_up_init_config(self):
        """setup init config for startup. runs only once in the beginning the app"""
        raise NotImplemented()
