import click


@click.group()
def config():
    """config manager"""
    pass


@config.command()
def show():
    print("config")
