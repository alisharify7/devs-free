"""
 * devs free ( developers free ) OSS
 * author: github.com/alisharify7
 * email: alisharifyofficial@gmail.com
 * license: see LICENSE for more details.
 * Copyright (c) 2023 - ali sharifi
 * https://github.com/alisharify7/devs_free
"""

import platform
import pyfiglet
from devs_free.common_lib.colors import colors


def detect_platform():
    if platform.system() == "Windows":
        return "windows"
    elif platform.system() == "Linux":
        return "linux"
    elif platform.system() == "Darwin":
        return "mac"
    else:
        return "unsupported OS"


def print_app_typography():
    print(
        f"{colors.bg.green}{colors.fg.red} * devs-free is a CLI tool to help you develop easily and freely. * {colors.reset}"
    )
    pyfiglet.print_figlet(f"Devs free", font="starwars", colors="GREEN")
    print(
        f"{colors.fg.red} * Github: https://github.com/alisharify7/devs-free * {colors.reset}"
    )
    print(f"{colors.fg.red} * Author: alisharifyofficial@gmail.com * {colors.reset}")
    print(
        f"{colors.fg.red} * Website: https://github.com/alisharify7/devs-free * {colors.reset}"
    )
