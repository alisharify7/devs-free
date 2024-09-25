import os
import re
import json
import pathlib
import subprocess
from abc import ABC

import questionary

from devs_free.base_platforms import BasePlatform
from devs_free.exception import NotInstalledError

class PlatformBaseDNS(BasePlatform, ABC):
    def get_all_ethernet_interfaces(self):
        pass

    def get_selected_ethernet_interfaces(self):
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


