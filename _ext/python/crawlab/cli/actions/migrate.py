from argparse import Namespace

from pymongo import MongoClient

from crawlab.actions.migrate import migrate
from crawlab.actions.migrate_no_upgrade import migrate_no_upgrade


def cli_migrate(args: Namespace):
    # mongo settings
    mongo_host = args.mongo_host
    mongo_port = args.mongo_port
    mongo_db_name = args.mongo_db
    mongo_username = args.mongo_username
    mongo_password = args.mongo_password
    mongo_auth_source = args.mongo_auth_source
    no_upgrade = args.no_upgrade
    source_filer_address = args.source_filer_address
    target_filer_address = args.target_filer_address

    # mongo client
    mongo_client = MongoClient(host=mongo_host, port=mongo_port, username=mongo_username, password=mongo_password,
                               authSource=mongo_auth_source)

    # mongo db
    mongo_db = mongo_client[mongo_db_name]

    if no_upgrade:
        # migrate (no upgrade)
        migrate_no_upgrade(mongo_db=mongo_db, source_filer_address=source_filer_address,
                           target_filer_address=target_filer_address)

    else:
        # migrate
        migrate(mongo_db=mongo_db)
