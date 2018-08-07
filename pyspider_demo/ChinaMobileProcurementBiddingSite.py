#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-07-12 01:59:33
# Project: ChinaMobileProcurementBiddingSite

from pyspider.libs.base_handler import *
from pyquery import PyQuery as pq
import re
import base64
import json
import time


class Handler(BaseHandler):
    crawl_config = {
        "headers": {
            "User-Agent": "Mozilla/5.0 (X11;Linux x86_64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/66.0.3359.181 Safari/537.36"
        }
    }

    @every(minutes=4 * 60)
    # on_start方法每4小时执行一次
    def on_start(self):
        # noticeType=2 采购公告
        url = 'https://b2b.10086.cn/b2b/main/listVendorNoticeResult.html?noticeBean.noticeType=2'
        # 获取当前日期
        date = time.strftime("%Y-%m-%d", time.localtime())
        # 构造POST参数
        data = {
            'page.currentPage': 1,
            'page.perPageSize': 200,
            'noticeBean.sourceCH': '',
            'noticeBean.source': '',
            'noticeBean.title': '',
            'noticeBean.startDate': date,
            'noticeBean.endDate': date
        }
        # 用于创建一个爬取任务，url 为目标地址，callback 为抓取到数据后的回调函数
        self.crawl(url, callback=self.index_page, method="POST", data=data)

    @config(age=10 * 24 * 60 * 60)
    # 设置任务的有效期限，告诉scheduler这个request过期时间是10天
    def index_page(self, response):
        # 公告详情uri
        uri = "https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeBean.id="
        # response.doc 为 pyquery 对象，用来方便地抓取返回的html文档中对应标签的数据
        print(len(response.doc("tr")))
        for each in response.doc("tr").items():
            # 过滤无效数据
            if each.attr("onclick"):
                notice_id = each.attr("onclick").split("'")[1]
                href = uri + notice_id
                self.crawl(href, callback=self.detail_page)

    @config(priority=2)
    # 设定任务优先级
    # 返回一个 dict 对象作为结果，自动保存到 resultdb
    def detail_page(self, response):
        # 去除无效元素 script
        result = response.doc.remove('script')

        topics = {
            '项目名称': '解析失败',
            '招标人': '解析失败',
            '招标代理机构': '无',
            '采购内容概况': '解析失败',
            '投标截止时间': '解析失败',
        }

        # 无用内容列表
        useless_topics = ['免责声明', '发布公告的媒介', '电子采购应答规则']
        # 项目概况相关主题列表
        project_overview_topics = ['项目概况与招标范围', '项目概况', '招标范围', '项目概况与招标内容',
                                   '采购说明', '采购内容', '采购内容及相关内容', '采购项目概况', '采购货物的名称', '采购项目的名称',
                                   '工程概况与比选内容', '比选项目的名称',]
        # 截止日期正则表达式
        deadline_pattern = re.compile('截止时间(.*)(\d+)年(\d{1,2})月(\d{1,2})日')
        # 日期正则表达式 年月日上午时
        date_pattern = re.compile('(\d+)年(\d{1,2})月(\d{1,2})日(.*)(\d{1,2})时')
        # 无效字符字典
        useless_char = dict.fromkeys(ord(c) for c in u"\xa0\n\t_ ")

        # 去除空元素
        tr_items = result('#mobanDiv > table tr').items()
        tr_items_nonzero = []
        for item in tr_items:
            # print(item('span').length)
            if item('span').length > 0:
                tr_items_nonzero.append(item)

        # !提取--URL
        topics['url'] = response.url

        # !提取--项目名称
        topics['项目名称'] = result('h1').text()

        # !提取--招标人
        last_tr = tr_items_nonzero[-1]
        last_tr_span_text = pq(pq(last_tr)('span')[0]).text()
        print('\n', last_tr_span_text)
        if last_tr_span_text.count("："):
            text = last_tr_span_text.split("：")[1]
            if text.count('/'):
                topics['招标人'] = text.split("/")[0]
                topics['招标代理机构'] = text.split("/")[1]
            else:
                topics['招标人'] = text

        # !提取--采购内容概况
        for each in tr_items_nonzero:
            # 设置默认值
            span_list = list(each('tr > td > span').items())
            if len(span_list) > 0:
                topic = span_list[0].text().split('、')[1]
                if topic in project_overview_topics:
                    print("\n", topic)
                    topics['采购内容概况'] = pq(each).clone().remove('table')('div').text().translate(useless_char)

        # !提取--其它主题
        for each in result('#mobanDiv > table tr').items():
            span = each('tr > td > span')
            # 过滤无主题内容
            if span.length > 0:
                topic = pq(span[0]).text().split('、')[1]
                if topic not in (useless_topics + project_overview_topics):
                    print(topic)
                    len_p = each('p').length
                    len_div = each('div').length
                    # print("\n p 元素: ", len_p, "\n div 元素: ", len_div)
                    infos = []
                    items = []
                    if len_p > 0:
                        items = each('p').items()
                    else:
                        if len_div > 0:
                            items = each('div').items()

                    for item in items:
                        text = item.clone().text().translate(useless_char)
                        # !提取--投标截止时间
                        deadline = deadline_pattern.findall(text)
                        if len(deadline) > 0:
                            # print('投标截止时间: ', deadline)
                            for m in date_pattern.finditer(text):
                                topics['投标截止时间'] = m.group()
                        else:
                            infos.append(text)
                    topics[topic] = infos
                    # print(infos)
        print(topics)
        return {
            "url": response.url,
            "项目名称": topics['项目名称'],
            "招标人": topics['招标人'],
            "招标代理机构": topics['招标代理机构'],
            "投标截止时间": topics['投标截止时间'],
            "采购内容概况": topics['采购内容概况'],
        }


