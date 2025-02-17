import string
import random
import cherrypy

class HelloWorld(object):

    # 127.0.0.1:8080/index
    @cherrypy.expose
    def index(self):
        return "Hello World, Oleksandr!"

    # 127.0.0.1:8080/generate
    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))


if __name__ == "__main__":
    cherrypy.quickstart( HelloWorld() )