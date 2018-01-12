import tornado.ioloop
import tornado.web
import sys
import request

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        page = requests.get('http://www.londonstockexchange.com/exchange/prices-and-markets/stocks/indices/constituents-indices.html?index=UKX&industrySector=&page=1')
        self.write(page)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(sys.argv[1])
    tornado.ioloop.IOLoop.current().start()