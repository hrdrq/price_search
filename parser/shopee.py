# encoding: utf-8
import re

from pyquery import PyQuery

from parser import Parser

LIST_URL = 'https://rtapi.ruten.com.tw/api/search/v3/index.php/core/prod'
DETAIL_URL = 'https://rtapi.ruten.com.tw/api/prod/v2/index.php/prod'
ITEM_URL = 'https://goods.ruten.com.tw/item/show?'
URL = 'https://shopee.tw/api/v2/search_items/?by=relevancy&keyword={word}&limit=50&newest=0&order=desc&page_type=search&version=2'
IMG_URL = 'https://cf.shopee.tw/file/'

class Shopee(Parser):

    def do_search(self, word):
        res = self.get(URL.format(word=word), headers={ 'referer': 'https://shopee.tw/search' }).json()
        results = [{
            "title": r['name'],
            "url": 'https://shopee.tw/{}-i.{}.{}'.format(r['name'], r['shopid'], r['itemid']),
            "img": IMG_URL + r['image'],
            "price": r['price'] // 100000
            } for r in res['items'] if r['currency'] == "TWD"][:50]
        return results

