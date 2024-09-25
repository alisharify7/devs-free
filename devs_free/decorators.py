from functools import wraps

import click

from devs_free.utils import detect_platform
from devs_free.dns_manager.platforms import Linux

def dns_config_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        platform = detect_platform()
        if platform == "unsupported OS":
            raise RuntimeError("unsupported OS.")


        if platform == "windows":
            if not Windows().does_config_exist():
                click.echo(click.style("config not found !", fg="red"))
                click.echo(click.style("setup dns configuration", fg="red"))
                Windows().set_up_init_config()
        elif platform == "linux":
            if not Linux().does_config_exist():
                click.echo(click.style("config not found !", fg="red"))
                click.echo(click.style("setup dns configuration", fg="red"))
                Linux().set_up_init_config()
        else:
            raise NotImplemented()

        return f(*args, **kwargs)
    return inner
