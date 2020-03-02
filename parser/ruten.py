# encoding: utf-8
import re

from pyquery import PyQuery

from parser import Parser

LIST_URL = 'https://rtapi.ruten.com.tw/api/search/v3/index.php/core/prod'
DETAIL_URL = 'https://rtapi.ruten.com.tw/api/prod/v2/index.php/prod'
ITEM_URL = 'https://goods.ruten.com.tw/item/show?'
IMG_URL = 'https://c.rimg.com.tw'

class Ruten(Parser):

    def do_search(self, word):
        list_res = self.get(LIST_URL, { 'q': word }).json()
        ids = [row['Id'] for row in list_res['Rows']]
        list_res = self.get(DETAIL_URL, { 'id': ','.join(ids) }).json()
        results = [{
            "title": r['ProdName'],
            "url": ITEM_URL + r['ProdId'],
            "img": IMG_URL + r['Image'],
            "price": r['PriceRange'][0]
        } for r in list_res if r['Currency'] == "TWD"]
        return results

