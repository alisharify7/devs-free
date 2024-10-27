"""
 * devs free ( developers free ) OSS
 * author: github.com/alisharify7
 * email: alisharifyofficial@gmail.com
 * license: see LICENSE for more details.
 * Copyright (c) 2023 - ali sharifi
 * https://github.com/alisharify7/devs_free
"""

import json
from time import sleep

import click
import questionary

from devs_free.decorators import dns_config_required
from devs_free.dns_manager.utils import get_dns_servers
from devs_free.utils import detect_platform

from devs_free.dns_manager.platforms.linux.platform import Linux
from devs_free.dns_manager.platforms.windows.platform import Windows


@click.group()
def dns():
    pass


@dns.command(help="list all avialable dns servers from upstream server.")
@click.option(
    "-s",
    "--save",
    help="save the result in the cache db",
    required=False,
    default="yes",
    type=str,
    show_default=True,
)
@dns_config_required
def list():
    """get list of all available dns servers"""
    with click.progressbar(length=100, label="fetching data ...") as bar:
        for _ in range(10):
            bar.update(10)
            sleep(0.2)

    dns_server_list = get_dns_servers()  # get data from internet
    name_dns_server_mapper = dict()
    for each in dns_server_list:
        name_dns_server_mapper[each["name"]] = each

    servers = [server["name"] for server in dns_server_list]
    user_selected_dns = questionary.select(
        message="available DNS servers",
        choices=servers,
    ).ask()

    selected_dns = name_dns_server_mapper[user_selected_dns]
    click.echo(click.style(text=f"servers: {' , '.join(selected_dns['servers'])}"))
    click.echo(
        click.style(text=f"rate: {' 🌟  ' * (selected_dns['rate'] + 1)}", overline="")
    )
    click.echo(click.style(text=f"category: {', '.join(selected_dns['tags'])}"))


@dns.command()
@dns_config_required
def status(): ...


@dns.command()
@dns_config_required
def disconnect(): ...


@dns.command()
@dns_config_required
def connect():
    """connect to a dns server"""
    platform = detect_platform()
    if platform == "unsupported OS":
        raise RuntimeError("unsupported OS.")

    with click.progressbar(length=100, label="fetching data ...") as bar:
        for _ in range(10):
            bar.update(10)
            sleep(0.2)

    dns_server_list = get_dns_servers()  # get data from internet
    name_dns_server_mapper = dict()
    for each in dns_server_list:
        name_dns_server_mapper[each["name"]] = each

    servers = [server["name"] for server in dns_server_list]
    user_selected_dns = questionary.select(
        message="select your DNS server",
        choices=servers,
    ).ask()

    selected_dns = name_dns_server_mapper[user_selected_dns]
    click.echo(click.style(text=f"servers: {' , '.join(selected_dns['servers'])}"))
    click.echo(
        click.style(text=f"rate: {' 🌟  ' * (selected_dns['rate'] + 1)}", overline="")
    )
    click.echo(click.style(text=f"category: {', '.join(selected_dns['tags'])}"))

    if platform == "windows":
        print(Windows().set_dns(selected_dns["servers"]))
    elif platform == "linux":
        print(Linux().set_dns(selected_dns["servers"]))
    else:
        raise NotImplemented("sorry :(")


@dns.command()
@dns_config_required
def active():
    """showing current active dns server."""
    platform = detect_platform()
    if platform == "unsupported OS":
        raise RuntimeError("unsupported OS.")

    if platform == "windows":
        dns_servers = Windows().get_current_dns()
    elif platform == "linux":
        dns_servers = Linux().get_current_dns()
    else:  # mac
        raise NotImplemented("sorry :(")

    click.echo(click.style("*" * 50, fg="green"))
    for index, srv in enumerate(dns_servers):
        click.echo(click.style(f"\t[Server {index+1}]: ", fg="red"), nl=False)
        click.echo(click.style(srv, fg="blue"))
    click.echo(click.style("*" * 50, fg="green"), nl=False)


@dns.command()
@dns_config_required
def show_config():
    """showing dns config file."""
    platform = detect_platform()
    if platform == "unsupported OS":
        raise RuntimeError("unsupported OS.")

    if platform == "windows":
        config_file = Windows().get_config_file()
    elif platform == "linux":
        config_file = Linux().get_config_file()
    else:  # mac
        raise NotImplemented("sorry :(")

    click.echo(click.style("*" * 50, fg="green"))
    click.echo(message=json.dumps(config_file["dns"], indent=4))
    click.echo(click.style("*" * 50, fg="green"), nl=False)
