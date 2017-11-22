#! /usr/bin/python
# encoding: utf-8

'''
实体类
'''

import fixmathproperty

class BasePara(object):
    '''
    页面的公共参数类
    '''

    title = "fixmath"                                             #页面的title
    keyword = ""                                                  #banner的关键字
    description = ""                                              #banner的描述
    mathjax = True                                                #是否数学公式加载
    currentmodule = fixmathproperty.CurrentPage().home            #高亮显示字符串
    bannerstylename = fixmathproperty.CurrentStyleName().home     #页面样式banner名称
