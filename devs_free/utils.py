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


def detect_platform() -> str:
    """this function return the type of the current platform OS"""
    if platform.system() == "Windows":
        return "windows"
    elif platform.system() == "Linux":
        return "linux"
    elif platform.system() == "Darwin":
        return "mac"
    else:
        return "unsupported OS"


def print_app_typography():
    print(f" * devs-free is a CLI tool to help you develop easily and freely. *")
    pyfiglet.print_figlet(f"Devs free", font="starwars", colors="GREEN")
    print(f" * Github: https://github.com/alisharify7/devs-free * ")
    print(f" * Author: alisharifyofficial@gmail.com * ")
    print(f"* Website: https://github.com/alisharify7/devs-free * ")
