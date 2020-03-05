from flask import Flask, request

from parser.amazon import Amazon
from parser.kakaku import Kakaku
from parser.mercari import Mercari
from parser.rakuma import Rakuma
from parser.ruten import Ruten
from parser.shopee import Shopee

app = Flask(__name__)

@app.route('/api/search/<platform>')
def search(platform):
    word = request.args.get('word')
    return globals()[platform]().search(word)

app.run(port=5000)
