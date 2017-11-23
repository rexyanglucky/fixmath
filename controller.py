#!/usr/bin/env python
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

class AlgebraIndex(object):
    '''
    研究线性空间（向量空间）、模和其上的线性变换以及与之有关的问题
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = model.BasePara()
        parames.title = "algebra"
        parames.keyword = "Algebra"
        parames.description = "研究线性空间（向量空间）、模和其上的线性变换以及与之有关的问题"
        parames.currentmodule = fixmathproperty.CurrentPage().algebra
        parames.bannerstylename = fixmathproperty.CurrentStyleName().algebra
        return RENDER.modules.algebra.index(parames)

class GeometryIndex(object):
    '''
    借助于解析式进行图形研究的几何学，定义图形的概念与参数
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = model.BasePara()
        parames.title = "Analytic Geometry"
        parames.keyword = "Analytic Geometry"
        parames.description = "借助于解析式进行图形研究的几何学，定义图形的概念与参数"
        parames.currentmodule = fixmathproperty.CurrentPage().geometry
        parames.bannerstylename = fixmathproperty.CurrentStyleName().geometry
        return RENDER.modules.geometry.index(parames)

class SourceIndex(object):
    '''
    AsciiMath
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = model.BasePara()
        parames.title = "AsciiMath"
        parames.keyword = ""
        parames.description = ""
        parames.currentmodule = fixmathproperty.CurrentPage().source
        parames.bannerstylename = fixmathproperty.CurrentStyleName().source
        return RENDER.modules.source.index(parames)

class GameIndex(object):
    '''
    Game
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = model.BasePara()
        parames.mathjax = False
        parames.title = "Game"
        parames.keyword = ""
        parames.description = ""
        parames.currentmodule = fixmathproperty.CurrentPage().game
        parames.bannerstylename = fixmathproperty.CurrentStyleName().game
        return RENDER.modules.game.index(parames)

class SvgIndex(object):
    '''
    SVG
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = model.BasePara()
        parames.mathjax = False
        parames.title = "SVG"
        parames.keyword = ""
        parames.description = ""
        parames.currentmodule = fixmathproperty.CurrentPage().svg
        parames.bannerstylename = fixmathproperty.CurrentStyleName().svg
        return RENDER.modules.svg.index(parames)

class WikiIndex(object):
    '''
    WIKI
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = model.BasePara()
        parames.mathjax = False
        parames.title = "WIKI"
        parames.keyword = ""
        parames.description = ""
        parames.currentmodule = fixmathproperty.CurrentPage().wiki
        parames.bannerstylename = fixmathproperty.CurrentStyleName().wiki
        return RENDER.modules.wiki.index(parames)

class ProfileIndex(object):
    '''
    用户中心
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = model.BasePara()
        parames.mathjax = False
        parames.title = "用户中心"
        parames.keyword = ""
        parames.description = "用户中心"
        parames.currentmodule = fixmathproperty.CurrentPage().profile
        parames.bannerstylename = fixmathproperty.CurrentStyleName().profile
        return RENDER.modules.profile.index(parames)

class DonateIndex(object):
    '''
    捐助中心
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = model.BasePara()
        parames.mathjax = False
        parames.title = "捐助中心"
        parames.keyword = ""
        parames.description = ""
        parames.currentmodule = fixmathproperty.CurrentPage().home
        parames.bannerstylename = fixmathproperty.CurrentStyleName().home
        return RENDER.donate(parames)

class AboutIndex(object):
    '''
    关于我们
    '''
    def GET(self, url):
        '''
        返回视图
        '''
        if url in ['', '/']:
            pass
        parames = model.BasePara()
        parames.mathjax = False
        parames.title = "关于我们"
        parames.keyword = ""
        parames.description = ""
        parames.currentmodule = fixmathproperty.CurrentPage().home
        parames.bannerstylename = fixmathproperty.CurrentStyleName().home
        return RENDER.about(parames)
