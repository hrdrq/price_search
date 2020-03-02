# encoding: utf-8
import re

from pyquery import PyQuery

from parser import Parser

URL = "http://s.kakaku.com/search_results/{word}/"

class Kakaku(Parser):

    def do_search(self, word):
        res = self.get(URL.format(word=word))
        doc = PyQuery(res.text)
        results = []
        for item in doc('.p-result_item'):
            result = {}
            item = PyQuery(item)
            price = re.sub("[¥〜,]", "", item(".p-item_price_num").text())
            if not price:
                continue
            result['price'] = int(price)
            result['title'] = item('.p-item_name').text()
            result['url'] = item('a').eq(0).attr('href')
            result['img'] = item('img').eq(0).attr('src')
            results.append(result)    
    
        return results
