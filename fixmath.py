#!/usr/bin/env python
# encoding: utf-8

'''
程序入口
'''

import config

if __name__ == "__main__":
    config.web.application(config.URLS, globals()).run()
