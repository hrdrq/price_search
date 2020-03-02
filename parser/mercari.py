# encoding: utf-8
import re

from pyquery import PyQuery

from parser import Parser

URL = 'https://www.mercari.com/jp/search/'

class Mercari(Parser):

    def do_search(self, word):
        res = self.get(URL, { 'keyword': word })
        doc = PyQuery(res.text)
        results = []
        for item in doc("section.items-box"):
            result = {}
            item = PyQuery(item)
            result['title'] = item('h3.items-box-name').text()
            result['url'] = item('a').attr('href')
            result['img'] = item('img').attr('data-src')
            result['price'] = int(re.sub("[¥,]", "", item(".items-box-price").text()))
            results.append(result)    
        return results

