from getpass import getpass

import click

from core.client import client
from core.config import config


@click.group()
def cli():
    pass


@click.command('login', help='login to Crawlab platform and get token')
@click.option('--username', '-u')
@click.option('--password', '-p')
def login(username=None, password=None):
    if username is not None:
        config.data.username = username
    if password is not None:
        config.data.username = password
    # config.data.username = input('Please enter your username: ')
    # config.data.password = getpass('Please enter your password: ')
    config.save()
    client.update_token()


@click.command('config', help='set the config info')
@click.option('--username', '-u')
@click.password_option('--password', '-p')
def config_(username=None, password=None):
    if username is not None:
        config.data.username = username
    if password is not None:
        config.data.username = password
    config.save()
    print('config has been saved')


@click.command('check', help='check the Crawlab connection and update token')
def check():
    client.update_token()


@click.command('nodes', help='list the nodes')
def nodes():
    client.list_nodes()


@click.command('spiders', help='list the spiders')
def spiders():
    client.list_spiders()


@click.command('schedules', help='list the schedules')
def schedules():
    client.list_schedules()


if __name__ == '__main__':
    cli.add_command(login)
    cli.add_command(check)
    cli.add_command(config_)
    cli.add_command(spiders)
    cli.add_command(nodes)
    cli.add_command(schedules)

    cli()
