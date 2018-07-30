#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-07-12 01:59:33
# Project: ChinaMobileProcurementBiddingSite

from pyspider.libs.base_handler import *
import re
import base64
import json
import time


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=4 * 60)
    # on_start方法每4小时执行一次
    def on_start(self):
        url = 'https://b2b.10086.cn/b2b/main/listVendorNotice.html?noticeType=2'
        # noticeType=2 采购公告

        date = time.strftime("%Y-%m-%d", time.localtime())
        # 获取当前日期

        data = {
            'page.currentPage': 1,
            'page.perPageSize': 200,
            'noticeBean.sourceCH': '',
            'noticeBean.source': '',
            'noticeBean.title': '',
            'noticeBean.startDate': date,
            'noticeBean.endDate': date
        }
        # 构造POST参数

        # 用于创建一个爬取任务，url 为目标地址，callback 为抓取到数据后的回调函数
        self.crawl(url, callback=self.index_page, method="POST", data=data)
        print(self.index_page)

    @config(age=10 * 24 * 60 * 60)
    # 设置任务的有效期限，告诉scheduler这个request过期时间是10天
    def index_page(self, response):
        # response.doc 为 pyquery 对象，用来方便地抓取返回的html文档中对应标签的数据
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    # 设定任务优先级
    # 返回一个 dict 对象作为结果，自动保存到 resultdb
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }

