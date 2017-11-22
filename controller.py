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
        parames.title = "fixMath"
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
        parames.title = "the-first-volume"
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
        parames.title = "the-last-volume"
        parames.keyword = "Calculus"
        parames.description = "研究的基本对象是定义在实数集上的函数"
        parames.currentmodule = fixmathproperty.CurrentPage().calculus
        parames.bannerstylename = fixmathproperty.CurrentStyleName().the_last_volume
        return RENDER.modules.calculus.the_last_volume(parames)

class RealNumbers(object):
    '''
    实数及其性质
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = model.BasePara()
        parames.title = "real-numbers-and-their-properties"
        parames.keyword = ""
        parames.description = "研究的基本对象是定义在实数集上的函数"
        parames.currentmodule = fixmathproperty.CurrentPage().calculus
        parames.bannerstylename = fixmathproperty.CurrentStyleName().real_numbers
        return RENDER.modules.calculus.real_numbers(parames)

class InequalityWith(object):
    '''
    从数轴上看，数 `a` 的绝对值 `|a|` 就是点 `a` 到原点的距离
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = model.BasePara()
        parames.title = "inequality-with-absolute-value"
        parames.keyword = ""
        parames.description = "从数轴上看，数 `a` 的绝对值 `|a|` 就是点 `a` 到原点的距离"
        parames.currentmodule = fixmathproperty.CurrentPage().calculus
        parames.bannerstylename = fixmathproperty.CurrentStyleName().inequality_with
        return RENDER.modules.calculus.inequality_with(parames)
