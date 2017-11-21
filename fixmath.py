#! /usr/bin/python
# encoding: utf-8

'''
程序入口
'''

import web
from config import URLS


if __name__ == "__main__":
    web.application(URLS, globals()).run(web.config.port)
