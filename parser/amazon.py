# encoding: utf-8

from pyquery import PyQuery

from parser import Parser

URL = 'https://www.amazon.co.jp/s'

class Amazon(Parser):

    def do_search(self, word):
        res = self.get(URL, { 'k': word })
        doc = PyQuery(res.text)
        results = []
        for item in doc(".s-result-item"):
            result = {}
            item = PyQuery(item)
            price = item('.a-price-whole')
            if not price:
                continue
            result['title'] = item('.a-section.a-spacing-none').eq(0).find('h2').text()
            result['url'] = 'https://www.amazon.co.jp' + item('a').eq(0).attr('href')
            result['img'] = item('img').attr('src')
            result['price'] = int(price.text().replace(',', ''))
            results.append(result)
        return results
