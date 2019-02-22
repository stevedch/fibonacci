import tornado.ioloop
import tornado.web
from jinja2 import Environment, FileSystemLoader

# Load template file templates/site.html
from utils import nth_succession

templateLoader = FileSystemLoader(searchpath='templates/')
templateEnv = Environment(loader=templateLoader)


# Handler for main page
class MainController(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        template = templateEnv.get_template('main.html')
        render = template.render()
        self.write(render)


# Handler for main page
class FibonacciController(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, ):
        nth = self.request.query_arguments.get('nth')[0]
        successions = nth_succession(int(nth))
        template = templateEnv.get_template('fibonacci.html')
        render = template.render(successions=successions)
        self.write(render)


# Assign handler to the server root  (127.0.0.1:PORT/)
application = tornado.web.Application([
    (r'/', MainController),
    (r'/fibonacci/', FibonacciController),
])

PORT = 8080
if __name__ == "__main__":
    # Setup the server

    application.listen(PORT)
    print('Server up  http://127.0.0.1:{}/'.format(PORT))
    tornado.ioloop.IOLoop.instance().start()
