# encoding: utf-8

import requests

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36")

class Parser:

    def get(self, url, params):
        r = requests.get(url, params=params, headers={ 'User-Agent': UA })
        return r

    def do_search(self, word):
        pass

    def search(self, word):
        try:
            results = self.do_search(word)
            return {"status": 'success', "results": results}
        except Exception as e:
            return {"status": 'error', "error_detail": str(e)}

    @property
    def d(self):
        import pdb
        return pdb.set_trace
