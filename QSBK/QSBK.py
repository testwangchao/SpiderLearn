#!/usr/bin/env python
#coding:utf-8
import requests,re
class reqUrl:
    response = requests.get("https://www.qiushibaike.com/8hr/page/2/?s=4994641")
    #获取状态码
    @property
    def getcode(self):
        print self.response.status_code
    #获取页面HTML
    @property
    def getHtml(self):
        return self.response.content.decode('utf-8')
    #匹配段子
    @property
    def getText(self):
        return re.findall('''<div class="article block untagged mb15.*?>.*?<div.*?clearfix">.*?(<a.*?alt=.*?</a>).*?<a href.*?</a>.*?(<div.*?</div>).*?(<div class="content".*?<span>.*?</span>.*?</div>)''',self.getHtml,re.S)
if __name__ == '__main__':
    print reqUrl().getText