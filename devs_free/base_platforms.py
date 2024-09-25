from abc import ABC


class BasePlatform(ABC):
    """Base Platform OS class.
    all managers classes should inherit from this class.
    this class contain global information that should every
    manager class know.
    """

    # DNS CONFIG
    dns_config_file = "devs_free_dns.json"
    dns_default_config = {
        "default-ethernet-interface": None,
        "all-ethernet-interfaces": [],
        "internet": {
            "servers": {
                "name": None,
                "ip": []
            },
            "fetched-at": None,
        }
    }

    docker_config_file = "devs_free_docker.json"
    docker_default_config = {
        "mirror-url": None,
        "internet": {
            "registries": {
                "name": None,
                "register-url": []
            },
            "fetched-at": None,
        }
    }

    # APT CONFIG
    apt_config_file = "devs_free_apt.json"
    apt_default_config = {
        "mirror-url": None,
        "internet": {
            "mirrors":{
                "name": None,
                "links": []
            },
            "fetched-at": None,
        }
    }

    # PIP CONFIG
    pip_config_file = "devs_free_pip.json"
    pip_default_config = {
        "mirror-url": None,
        "internet": {
            "mirrors": {
                "name": None,
                "url": []
            },
            "fetched-at": None,
        }
    }
