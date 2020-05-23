import requests
from lxml import etree
from bs4 import BeautifulSoup
import os
import re

class RSpider:
    def __init__(self):
        self.url = 'http://www.kekenet.com/Article/media/economist/'
    
    def get_html(self, url):
        try:
            # print(url)
            html = requests.get(url=url)
            html.encoding = 'utf-8'
            if html.status_code == 200:
                # print(html.text)
                return html.text
            else:
                return None
        except Exception as e:
            print(e.args)

    def get_list_text(self, url):
        html = self.get_html(url)
        tree = etree.HTML(html)
        xp = '//*[@id="menu-list"]/li'
        ul = tree.xpath(xp)
        ans = []
        for li in ul:
            li = li.xpath('h2/a[2]')[0]
            url = li.get('href')
            title = li.get('title')
            ans.append({"url": url, "title": title})
        return ans
    
    def get_mp3(self, url):
        url = re.sub('/\w+/', '/mp3/', url)
        # print(url)
        html = requests.get(url)
        html.encoding = 'utf-8'
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'lxml')
            ans = soup.find_all('a', href = re.compile('http://k6.kekenet.com/Sound/'))
            if len(ans) != 0:
                return ans[0].get('href')
            else:
                return None
        else:
            return None
    
    def get_text(self, url):
        html = self.get_html(url)
        tree = etree.HTML(html)
        xp = '//*[@id="article_eng"]/div//text()'
        div = tree.xpath(xp)
        eng = ""
        chinese = ""
        if len(div) != 0:
            for value in div:
                if value == '' or value == '\n':
                    continue
                if isChinese(value):
                    chinese += value + '\n'
                else:  
                    eng += value + '\n'
        return (chinese, eng)
    
    def get_all(self, url):
        return (self.get_text(url), self.get_mp3(url))

def isChinese(s):
    flag = 0
    for i in s:
        if '\u4e00' <= i <= '\u9fff':
            flag = 1
            break
    return flag

if __name__ == "__main__":
    spider = RSpider()
    ans = spider.get_list_text(spider.url)
    for i in ans:
        print(spider.get_all(i['url'])[1])