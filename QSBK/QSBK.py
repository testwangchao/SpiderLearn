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
        #return items
        for item in items:
            haveImg = re.search('img',item[3])
            if not haveImg:
                haveHot = re.search('main-text',item[4])
                if haveHot:
                    hotText = re.search('<div class="main-text">(.*?)<div class="likenum">',item[4],re.S).group(1).strip(u'\n：')
                    print u"作者:%s,年龄:%s,内容:%s,神评:%s"%(item[0].strip('\n'),item[1].strip('\n'),item[2].strip('\n'),hotText)
                else:
                    print item[0].strip('\n'),item[1].strip('\n'),item[2].strip('\n')
if __name__ == '__main__':
    reqUrl().getText

    #print re.search("[^>\n].*",a).group().strip(u"：")
