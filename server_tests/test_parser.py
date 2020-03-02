# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, patch, PropertyMock

import vcr

from parser.amazon import Amazon

def check(res):
    if res['status'] != 'success':
        return False
    for item in res['results']:
        if not item['title']:
            return False
        if not isinstance(item['price'], int):
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
