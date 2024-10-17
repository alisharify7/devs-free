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
    all dns manager classes should inherit from this class,
    and implement the all methods that this class contain.
    """

    def get_all_ethernet_interfaces(self):
        raise NotImplemented()

    def get_main_ethernet_interfaces(self):
        raise NotImplemented()

    def get_current_username(self):
        raise NotImplemented()

    def does_config_exist(self):
        raise NotImplemented()

    def get_config_dir(self):
        raise NotImplemented()

    def create_config_file(self):
        raise NotImplemented()

    def get_config_file(self):
        raise NotImplemented()

    def update_config_file(self, config_object: dict):
        raise NotImplemented()

    def set_up_init_config(self):
        raise NotImplemented()
