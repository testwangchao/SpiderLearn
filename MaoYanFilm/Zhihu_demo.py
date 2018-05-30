import requests
import re
from time import sleep
base_url = "http://maoyan.com/board/4?offset={0}"
headers = {
    "Host": "maoyan.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
}


def get_one_page(url):
    rep = requests.get(url, headers=headers)
    if rep.status_code == 200:
        return rep.text
    return None

def get_data(rep):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?title="(.*?)".*?src="(http.*?)".*?star.*?：(.*?)</p>.*?：(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>', re.S)
    result = re.findall(pattern, rep)
    return result


def main(page):
    url = base_url.format(page)
    data = get_data(get_one_page(url))
    for i in data:
        yield {
            "index": i[0],
            "film_name": i[1],
            "icon": i[2],
            "star": i[3].strip(),
            "time": i[4].strip(),
            "score": "{0}{1}".format(i[5],i[6])
        }


if __name__ == '__main__':

    for page in range(10):
        data = main(str(page*10))
        while True:
            try:
                a = next(data)
            except StopIteration:
                break
            print(a)

