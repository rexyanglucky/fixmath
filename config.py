#! /usr/bin/python
# encoding: utf-8

'''
系统的全局配置参数与URL
'''

import web


FIX_MATH_CONFIG = web.storage(
    name="fixMath",
    url="https://www.fixmath.com",
    keywords="ajorm.com,zh-cn.vip,fixmath.com,luyuhai.com",
    description="将部分复杂的数学原理转化为计算机方面的应用",
    port=int(web.os.getenv('PORT') or 8080),
    author="Mr.Lu",
    template_dir="template",
    home_url="/",
    static_url="/static",
    url_suffix=".html",
    favicon_url="/favicon.ico",
    init_day="2017/11/21",
    init_time="19:27:25",
    cache=False,
    debug=True
)

web.config.port = FIX_MATH_CONFIG.port
web.config.debug = FIX_MATH_CONFIG.debug
RENDER = web.template.render(FIX_MATH_CONFIG.template_dir, cache=FIX_MATH_CONFIG.cache)

web.template.Template.globals['config'] = FIX_MATH_CONFIG
web.template.Template.globals['render'] = RENDER

URLS = (
    FIX_MATH_CONFIG.home_url, 'controller.Home'
)
