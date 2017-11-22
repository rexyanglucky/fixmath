#! /usr/bin/python
# encoding: utf-8

'''
实体类
'''

import config


CONFIG = config.FIX_MATH_CONFIG


class BasePara(object):
    '''
    参数类
    '''
    title = CONFIG.description
    mathjax = True
    highlight = ""
    