"""
 * devs free ( developers free ) OSS
 * author: github.com/alisharify7
 * email: alisharifyofficial@gmail.com
 * license: see LICENSE for more details.
 * Copyright (c) 2023 - ali sharifi
 * https://github.com/alisharify7/devs_free
"""

from abc import ABC


class BasePlatform(ABC):
    """Base Platform OS class.
    all managers classes should inherit from this class.
    this class contain global information that should every
    manager class knew.

    this class contains config files + structure for each
    manager class (DNS, PIP, APT, etc).
    """

    # global DNS CONFIG file + structure
    DNS_CONFIG_FILE_NAME = "devs_free_dns.json"
    DNS_DEFAULT_CONFIG = {
        "main-interface": None,
        "all-interfaces": [],
        "cache": {
            "servers": {"name": None, "ip": []},
            "fetched-at": None,
        },
    }

    # global DNS CONFIG file + structure
    DOCKER_CONFIG_FILE_NAME = "devs_free_docker.json"
    DOCKER_DEFAULT_CONFIG = {
        "mirror-url": None,
        "internet": {
            "cache": {"name": None, "link": []},
            "fetched-at": None,
        },
    }

    # global APT CONFIG file + structure
    APT_CONFIG_FILE_NAME = "devs_free_apt.json"
    APT_DEFAULT_CONFIG = {
        "mirror-url": None,
        "internet": {
            "cache": {"name": None, "link": []},
            "fetched-at": None,
        },
    }

    # global PIP CONFIG file + structure
    PIP_CONFIG_FILE_NAME = "devs_free_pip.json"
    PIP_DEFAULT_CONFIG = {
        "mirror-url": None,
        "internet": {
            "cache": {"name": None, "link": []},
            "fetched-at": None,
        },
    }
