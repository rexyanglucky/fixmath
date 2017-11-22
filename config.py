#! /usr/bin/python
# encoding: utf-8
'''
系统的全局配置参数与URL
'''

import web

FIX_MATH_CONFIG = web.storage(
    name="fixMath",                                                 #fixmath名称
    url="https://www.fixmath.com",                                  #fixmath域名
    keywords="ajorm.com,zh-cn.vip,fixmath.com,luyuhai.com",         #fixmath关键字
    description="fixMath---将部分复杂的数学原理转化为计算机方面的应用",    #fixmath介绍
    port=int(web.os.getenv('PORT') or 8080),                        #默认端口
    author="Mr.Lu",                                                 #作者
    template_dir="template",                                        #模板位置
    home_url="/",                                                   #首页
    static_url="/static",                                           #静态文件位置
    calculus_url="/zh-cn/calculus/",                                #微积分位置
    favicon_url="/favicon.ico",                                     #fixmath图标位置
    init_day="2017/11/21",                                          #fixmath初始化day
    init_time="19:27:25",                                           #fixmath初始化time
    locale="beijing china",                                         #fixmath地点
    cache=False,                                                    #fixmath缓存
    debug=True                                                      #fixmath调试
)

web.config.port = FIX_MATH_CONFIG.port
web.config.debug = FIX_MATH_CONFIG.debug
RENDER = web.template.render(FIX_MATH_CONFIG.template_dir, cache=FIX_MATH_CONFIG.cache)

web.template.Template.globals['config'] = FIX_MATH_CONFIG
web.template.Template.globals['render'] = RENDER

URLS = (
    FIX_MATH_CONFIG.home_url, 'controller.Home', #首页
    FIX_MATH_CONFIG.calculus_url + 'the-first-volume(.*)', 'controller.TheFirstVolume', #微积分
    FIX_MATH_CONFIG.calculus_url + 'the-last-volume(.*)', 'controller.TheLastVolume',
)
