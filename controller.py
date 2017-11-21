#! /usr/bin/python
# encoding: utf-8
'''
控制器
'''

import config


RENDER = config.RENDER
CONFIG = config.FIX_MATH_CONFIG


class Home(object):
    '''
    加载首页
    '''
    def GET(self):
        '''
        返回视图
        '''
        parames = {"title" : "fixmath"}
        return RENDER.home(parames)
