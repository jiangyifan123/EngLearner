import requests
from lxml import etree
from bs4 import BeautifulSoup
import os
import re

class LSpider:
    def __init__(self):
        self.url = 'https://toefl.kmf.com/listen/ets/order/'
    
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
    
    def get_all(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        div = soup.find('div', class_="origin-hidden-page original-cont")
        all_eng = div.find_all('p', class_="sentence-content")
        all_chinese = div.find_all('div', class_ = "translation-box")
        all_time = div.select('div .orgin-content.js-orgin-content.original-en')
        if len(all_time) != 0:
            all_time = [x.get('data-time') for x in all_time]
        else:
            all_time = []
        if len(all_chinese) != 0:
            all_chinese = [x.text for x in all_chinese]
        else:
            all_chinese = []
        if len(all_eng) != 0:
            all_eng = [x.text for x in all_eng]
        else:
            all_eng = []
        return (all_eng, all_chinese, all_time)

    def get_url(self):
        menu_url = []
        for i in range(12):
            url = self.url + '%d/0' % i
            menu_url.append(url)
        return menu_url
    
    def get_listen_url(self, menu_url):
        html = self.get_html(menu_url)
        soup = BeautifulSoup(html, 'lxml')
        urls = soup.select("a.listen-exam-link.button-style.js-listen-link")
        texts = soup.select("a.practice-title.js-practice-title")
        if len(urls) != 0:
            urls = [(t.text, 'https://toefl.kmf.com' + x.get('href')) for t, x in zip(texts, urls)]
        return urls

if __name__ == "__main__":
    spider = LSpider()
    # all_eng, all_chinese, all_time = spider.get_all(spider.url)
    menu = spider.get_url()
    urls = spider.get_listen_url(menu[0])
    all_eng, all_chinese, all_time = spider.get_all(urls[0][1])
    print(all_time)