import configparser
import os


def get_scrapy_cfg():
    cp = configparser.ConfigParser()
    cp.read('scrapy.cfg')
    return cp

