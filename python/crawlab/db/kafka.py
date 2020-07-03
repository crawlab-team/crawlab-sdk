import json

from kafka import KafkaProducer

from crawlab.utils.config import get_data_source, get_collection


def get_producer():
    ds = get_data_source()
    if ds.get('username') is not None:
        return KafkaProducer(
            sasl_mechanism="PLAIN",
            security_protocol='SASL_PLAINTEXT',
            sasl_plain_username=ds.get('username'),
            sasl_plain_password=ds.get('password'),
            bootstrap_servers=f'{ds.get("host")}:{ds.get("port")}'
        )
    else:
        return KafkaProducer(
            bootstrap_servers=ds.get('host').split(',')
        )


def send_msg(item):
    producer = get_producer()
    producer.send(get_collection(), json.dumps(item))
