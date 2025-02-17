import random
import string
import cherrypy
import json

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """
            <html>
                <head></head>
                    <body>
                        <form method="GET" action="generate">
                            <input type="text" value="10" name="length" />
                            <button type="submit">~Let's Go!~</button>
                        </form>
                    </body>
            </html> 
        """

    # 127.0.0.1:8080/generate?length=5
    @cherrypy.expose
    def generate(self, length=5):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    # 127.0.0.1:8080/json
    @cherrypy.expose
    def json(self):
        res = "Pong"
        return json.dumps(
            {"Ping": res}
        )

    # 127.0.0.1:8080/json
    @cherrypy.expose
    def display(self):
        return cherrypy.session['mystring']

if __name__ == "__main__":
    conf = {
        '/': {
            'tools.sessions.on': True
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf )