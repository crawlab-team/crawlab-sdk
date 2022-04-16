import argparse

from cli.actions.config import config_func
from cli.constants import CLI_ACTION_UPLOAD, CLI_ACTION_LOGIN, CLI_DEFAULT_API_ADDRESS, CLI_DEFAULT_API_USERNAME, \
    CLI_DEFAULT_API_PASSWORD, CLI_ACTION_CONFIG
from cli.actions.login import login
from cli.actions.upload import upload

# root parser
root_parser = argparse.ArgumentParser(description='CLI tool for Crawlab')

# sub-parsers
subparsers = root_parser.add_subparsers()

# login parser
login_parser = subparsers.add_parser(CLI_ACTION_LOGIN)
login_parser.add_argument('--api_address', '-a', help='HTTP URL of API address of Crawlab',
                          default=CLI_DEFAULT_API_ADDRESS, type=str)
login_parser.add_argument('--username', '-u', help='Username for logging in Crawlab', default=CLI_DEFAULT_API_USERNAME,
                          type=str)
login_parser.add_argument('--password', '-p', help='Password for logging in Crawlab', default=CLI_DEFAULT_API_PASSWORD,
                          type=str)
login_parser.set_defaults(func=login, action=CLI_ACTION_LOGIN)

# upload parser
upload_parser = subparsers.add_parser(CLI_ACTION_UPLOAD)
upload_parser.add_argument('--dir', '-d', help='Local directory of spider to upload. Default: current directory',
                           default=None, type=str)
upload_parser.add_argument('--create', '-c', help='Whether to create a new spider. Default: false', action='store_true',
                           default=False)
upload_parser.add_argument('--name', '-n', help='Spider name if creating a new spider. Default: directory name',
                           type=str)
upload_parser.add_argument('--id', '-i', help='Spider ID if uploading to an existing spider.',
                           type=str)
upload_parser.add_argument('--col_name', '-C',
                           help='Spider results collection name if creating a new spider. Default: results_<spider_name>',
                           type=str)
upload_parser.add_argument('--cmd', '-m',
                           help='Spider execute command if creating a new spider. Default: echo "hello crawlab"',
                           default='echo "hello crawlab"')
upload_parser.set_defaults(func=upload, action=CLI_ACTION_UPLOAD)

# config parser
config_parser = subparsers.add_parser(CLI_ACTION_CONFIG)
config_parser.add_argument('--set', '-s', type=str)
config_parser.add_argument('--unset', '-u', type=str)
config_parser.set_defaults(func=config_func, action=CLI_ACTION_CONFIG)


def main():
    args = root_parser.parse_args()
    if not hasattr(args, 'func'):
        root_parser.print_help()
        return
    try:
        args.func(args)
    except Exception as e:
        if getattr(args, 'action') == CLI_ACTION_LOGIN:
            login_parser.print_help()
        elif getattr(args, 'action') == CLI_ACTION_UPLOAD:
            upload_parser.print_help()
        elif getattr(args, 'action') == CLI_ACTION_CONFIG:
            config_parser.print_help()
        else:
            root_parser.print_help()


if __name__ == '__main__':
    main()
