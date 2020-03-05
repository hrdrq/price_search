# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, patch, PropertyMock

import vcr

from parser.amazon import Amazon
from parser.kakaku import Kakaku
from parser.mercari import Mercari
from parser.rakuma import Rakuma
from parser.ruten import Ruten
from parser.shopee import Shopee
from parser.rate import Rate

def check(res):
    if res['status'] != 'success':
        return False
    if not len(res['results']):
        return False
    for item in res['results']:
        if not item['title']:
            print('title error', item)
            return False
        if not isinstance(item['price'], int):
            print('price error', item)
            return False
    
    return True

class ParserTest(unittest.TestCase):

    def setUp(self):
        self.word = 'Nikon COOLPIX W150'

    def test_amazon(self):
        parser = Amazon()
        with vcr.use_cassette('server_tests/vcr_cassettes/amazon.yaml'):
            res = parser.search(self.word)
        self.assertTrue(check(res))

    def test_kakaku(self):
        parser = Kakaku()
        with vcr.use_cassette('server_tests/vcr_cassettes/kakaku.yaml'):
            res = parser.search(self.word)
        self.assertTrue(check(res))
        
    def test_mercari(self):
        parser = Mercari()
        with vcr.use_cassette('server_tests/vcr_cassettes/mercari.yaml'):
            res = parser.search(self.word)
        self.assertTrue(check(res))

    def test_rakuma(self):
        parser = Rakuma()
        with vcr.use_cassette('server_tests/vcr_cassettes/rakuma.yaml'):
            res = parser.search(self.word)
        self.assertTrue(check(res))

    def test_ruten(self):
        parser = Ruten()
        with vcr.use_cassette('server_tests/vcr_cassettes/ruten.yaml'):
            res = parser.search(self.word)
        self.assertTrue(check(res))

    def test_shopee(self):
        parser = Shopee()
        with vcr.use_cassette('server_tests/vcr_cassettes/shopee.yaml'):
            res = parser.search(self.word)
        self.assertTrue(check(res))

    def test_rate(self):
        parser = Rate()
        with vcr.use_cassette('server_tests/vcr_cassettes/rate.yaml'):
            res = parser.search(self.word)
        self.assertTrue(isinstance(res['results'], float))

