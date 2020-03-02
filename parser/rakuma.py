# encoding: utf-8
import re

from pyquery import PyQuery

from parser import Parser

URL = 'https://fril.jp/search/{word}'

class Rakuma(Parser):

    def do_search(self, word):
        res = self.get(URL.format(word=word))
        doc = PyQuery(res.text)
        results = []
        for item in doc(".item-list .item"):
            result = {}
            item = PyQuery(item)
            result['title'] = item('.item-box__item-name').text()
            result['url'] = item('a').eq(0).attr('href')
            result['img'] = item('img').eq(1).attr('src')
            result['price'] = int(re.sub("[¥￥,]", "", item('.item-box__item-price').text()))
            results.append(result)    
        return results

