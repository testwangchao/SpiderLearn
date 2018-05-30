import requests
from lxml import etree


base_url = "http://maoyan.com/board/4?offset={0}"
headers = {
    "Host": "maoyan.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
}
def get_html():
    html = etree.HTML(requests.get(base_url.format('0'),headers=headers).text,etree.HTMLParser())
    result = html.xpath("//p[@class='star']/text()")
    for i in result:
        print(i.strip())

if __name__ == '__main__':
    get_html()