import tornado.ioloop
import tornado.web
import tornado.websocket

class ChatHandler(tornado.websocket.WebSocketHandler):
 clients = []

 def open(self):

  print('hoge')
  if self not in ChatHandler.clients:
   ChatHandler.clients.append(self)

 def on_message(self, message):
  for c in ChatHandler.clients:
   c.write_message(message)

 def on_close(self):
  if self in ChatHandler.clients:
   ChatHandler.clients.remove(self)

class MainHandler(tornado.web.RequestHandler):
 def get(self):
  self.render('main.html')

if __name__ == "__main__":
 application = tornado.web.Application([
  (r"/chat/main.html", MainHandler),
  (r"/chat/websocket", ChatHandler),
 ])
 print('hoge')
 application.listen(9000)
 print('hoge')
 tornado.ioloop.IOLoop.current().start()
 print('hoge')
