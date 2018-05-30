import requests
import re

base_url = "http://maoyan.com/board/4?offset=0"
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
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>', re.S)
    result = re.findall(pattern, rep)
    return result


def main():
    print(get_data(get_one_page(base_url)))


if __name__ == '__main__':
    main()
