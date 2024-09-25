import click
from devs_free.dns_manager.main import dns
from devs_free.config_manager import config
from devs_free.utils import print_app_typography

@click.group()
def devs():
    """main control switch"""
    pass

@devs.command()
def about():
    click.echo(print_app_typography())

devs.add_command(dns)
devs.add_command(config)


