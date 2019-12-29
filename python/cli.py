from getpass import getpass

import click

from core.config import config


@click.group()
def cli():
    pass


@click.command()
def login():
    config.data.username = input("Please enter your username: ")
    config.data.password = getpass("Please enter your password: ")
    config.save()


if __name__ == '__main__':
    cli.add_command(login)
    cli()
