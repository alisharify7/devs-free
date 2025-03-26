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
    dns_config_file = "devs_free_dns.json"
    dns_default_config = {
        "main-interface": None,
        "all-interfaces": [],
        "cache": {
            "servers": {"name": None, "ip": []},
            "fetched-at": None,
        },
    }

    # global DNS CONFIG file + structure
    docker_config_file = "devs_free_docker.json"
    docker_default_config = {
        "mirror-url": None,
        "internet": {
            "cache": {"name": None, "link": []},
            "fetched-at": None,
        },
    }

    # global APT CONFIG file + structure
    apt_config_file = "devs_free_apt.json"
    apt_default_config = {
        "mirror-url": None,
        "internet": {
            "cache": {"name": None, "link": []},
            "fetched-at": None,
        },
    }

    # global PIP CONFIG file + structure
    pip_config_file = "devs_free_pip.json"
    pip_default_config = {
        "mirror-url": None,
        "internet": {
            "cache": {"name": None, "link": []},
            "fetched-at": None,
        },
    }
