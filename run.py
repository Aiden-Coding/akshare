from sanic import Sanic
from web.stockApi import stockApi

app = Sanic("ak_share")
app.blueprint(stockApi)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
