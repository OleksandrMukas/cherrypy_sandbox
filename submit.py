import random
import string
import cherrypy
import json

class Generator(object):
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
        return ''.join(random.sample(string.hexdigits, int(length)))

    # 127.0.0.1:8080/json
    @cherrypy.expose
    def json(self):
        res = "Pong"
        return json.dumps(
            {"Ping": res}
        )

if __name__ == "__main__":
    cherrypy.quickstart( Generator() )