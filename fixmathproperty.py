#! /usr/bin/python
# encoding: utf-8

'''
fixmath模块及页面属性
'''

class CurrentPage(object):
    '''
    模块枚举
    '''

    @property
    def home(self):
        '''
        首页
        '''
        return 0

    @property
    def calculus(self):
        '''
        微积分
        '''
        return 1

    @property
    def algebra(self):
        '''
        代数
        '''
        return 2

    @property
    def geometry(self):
        '''
        几何
        '''
        return 3

    @property
    def game(self):
        '''
        游戏
        '''
        return 4

    @property
    def svg(self):
        '''
        svg
        '''
        return 5

    @property
    def wiki(self):
        '''
        wiki
        '''
        return 6

    @property
    def profile(self):
        '''
        用户中心
        '''
        return 7

    @property
    def source(self):
        '''
        源
        '''
        return 8

class CurrentStyleName(object):
    '''
    定位当前页面的样式
    '''
    @property
    def home(self):
        '''
        首页
        '''
        return 0

    @property
    def the_first_volume(self):
        '''
        上集
        '''
        return 1

    @property
    def the_last_volume(self):
        '''
         下集
        '''
        return 2

    @property
    def real_numbers(self):
        '''
        研究的基本对象是定义在实数集上的函数
        '''
        return 3

    @property
    def inequality_with(self):
        '''
        从数轴上看，数 `a` 的绝对值 `|a|` 就是点 `a` 到原点的距离
        '''
        return 4

    @property
    def algebra(self):
        '''
        代数
        '''
        return 5

    @property
    def geometry(self):
        '''
        几何
        '''
        return 6

    @property
    def game(self):
        '''
        游戏
        '''
        return 7

    @property
    def svg(self):
        '''
        svg
        '''
        return 8

    @property
    def wiki(self):
        '''
        wiki
        '''
        return 9

    @property
    def profile(self):
        '''
        用户中心
        '''
        return 10

    @property
    def source(self):
        '''
        源
        '''
        return 11
