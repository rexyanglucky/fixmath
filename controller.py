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
        parames = {"title" : "fixmath", "mathJax" : False}
        return RENDER.home(parames)

class TheFirstVolume(object):
    '''
    微积分
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        parames = {"title" : "", "mathJax" : False}
        return RENDER.modules.calculus.the_first_volume(parames)

class TheLastVolume(object):
    '''
    下集
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = {"title" : "", "mathJax" : False}
        return RENDER.modules.calculus.the_last_volume(parames)
