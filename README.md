# price_search

Renewal of [priceSearch](https://github.com/hrdrq/priceSearch)

Get and compare prices of productions in EC sites in Japan and Taiwan.

Developed with Flask and Vue.js.

### Demo
[https://jp-tw-price-search.herokuapp.com/](https://jp-tw-price-search.herokuapp.com/)

### Screenshot
![](https://raw.githubusercontent.com/hrdrq/price_search/master/screenshot.png)

### Install
```
pipenv install
npm install
```

### Development
```
python server.py
npm run serve
```

### Production
```
npm run build
gunicorn server:app
```
