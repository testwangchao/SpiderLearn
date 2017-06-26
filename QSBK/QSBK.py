#!/usr/bin/env python
#coding:utf-8
import requests,re
class reqUrl:
    response = requests.get("https://www.qiushibaike.com/8hr/page/1/?s=4994641")
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
        items = re.findall('''<div class="author clearfix">.*?alt="(.*?)".*?class="articleGender womenIcon">(.*?)</div>.*?class="content">.*?<span>(.*?)</span>.*?</a>(.*?)<div class="stats".*?"single-clear"></div>(.*?)</div>''',self.getHtml,re.S)
        return items
        for item in items:
            haveImg = re.search('img',item[3])
            if not haveImg:
                print item[4]

if __name__ == '__main__':
    print reqUrl().getText[0][4].strip('\n')

    #print re.search("[^>\n].*",a).group().strip(u"：")
