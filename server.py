from flask import Flask, request, send_file

from parser.amazon import Amazon
from parser.kakaku import Kakaku
from parser.mercari import Mercari
from parser.rakuma import Rakuma
from parser.ruten import Ruten
from parser.shopee import Shopee
from parser.rate import Rate

app = Flask(__name__, static_folder='dist', static_url_path='')

@app.route('/api/search/<platform>')
def search(platform):
    word = request.args.get('word')
    return globals()[platform]().search(word)

@app.route('/api/rate')
def rate():
    return Rate().search(None)

@app.route('/')
def index():
    return send_file('dist/index.html')

app.run(port=5000)
