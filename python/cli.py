from getpass import getpass

import click

from core.client import client
from core.config import config


@click.group()
def cli():
    pass


@click.command('login', help='login to Crawlab platform and get token')
@click.option('--username', '-u')
@click.password_option('--password', '-p', confirmation_prompt=False)
@click.option('--api_address', '-a')
def login(username=None, password=None, api_address=None):
    if username is not None:
        config.data.username = username
    if password is not None:
        config.data.password = password
    if api_address is not None:
        config.data.api_address = api_address
    config.save()
    client.update_token()


@click.command('config', help='set the config info')
@click.option('--username', '-u')
@click.password_option('--password', '-p', confirmation_prompt=False)
@click.option('--api_address', '-a')
def config_(username=None, password=None, api_address=None):
    if username is not None:
        config.data.username = username
    if password is not None:
        config.data.password = password
    if api_address is not None:
        config.data.api_address = api_address
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


@click.command('tasks', help='list the tasks')
@click.option('--number', '-n', help='number of tasks')
def schedules(number=None):
    client.list_tasks(number)


if __name__ == '__main__':
    cli.add_command(login)
    cli.add_command(check)
    cli.add_command(config_)
    cli.add_command(spiders)
    cli.add_command(nodes)
    cli.add_command(schedules)

    cli()
