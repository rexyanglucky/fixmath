#! /usr/bin/python
# encoding: utf-8
'''
控制器
'''

import config
import fixmathproperty
import model

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
        parames = model.BasePara()
        parames.mathjax = False
        return RENDER.home(parames)

class TheFirstVolume(object):
    '''
    微积分
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = model.BasePara()
        parames.keyword = "Calculus"
        parames.description = "研究的基本对象是定义在实数集上的函数"
        parames.currentmodule = fixmathproperty.CurrentPage().calculus
        parames.bannerstylename = fixmathproperty.CurrentStyleName().the_first_volume
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
        parames = model.BasePara()
        parames.keyword = "Calculus"
        parames.description = "研究的基本对象是定义在实数集上的函数"
        parames.currentmodule = fixmathproperty.CurrentPage().calculus
        parames.bannerstylename = fixmathproperty.CurrentStyleName().the_last_volume
        return RENDER.modules.calculus.the_last_volume(parames)
