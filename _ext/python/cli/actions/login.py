from cli.config import config
from cli.client.request import http_post
from cli.constants import CLI_DEFAULT_CONFIG_KEY_USERNAME, CLI_DEFAULT_CONFIG_KEY_PASSWORD, \
    CLI_DEFAULT_CONFIG_KEY_API_ADDRESS, CLI_DEFAULT_CONFIG_KEY_TOKEN


def login(args):
    url = f'{args.api_address}/login'
    try:
        res = http_post(url, {
            'username': args.username,
            'password': args.password,
        })
        print('logged-in successfully')
    except Exception as e:
        print(e)
        return

    token = res.json().get('data')
    config.set(CLI_DEFAULT_CONFIG_KEY_USERNAME, args.username)
    config.set(CLI_DEFAULT_CONFIG_KEY_PASSWORD, args.password)
    config.set(CLI_DEFAULT_CONFIG_KEY_API_ADDRESS, args.api_address)
    config.set(CLI_DEFAULT_CONFIG_KEY_TOKEN, token)
    config.save()
