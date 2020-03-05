# encoding: utf-8
import re

from pyquery import PyQuery

from parser import Parser

URL = 'https://ja.valutafx.com/TWD-JPY.htm'

class Rate(Parser):

    def do_search(self, word):
        res = self.get(URL).text
        doc = PyQuery(res)
        rate = float(doc('.rate-value').text())
        return rate
