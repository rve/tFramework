import re
import traceback
from paste import httpserver

class application:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def GET_index(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Welcome!\n"

    def GET_hello(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello world!\n"
    
    def notfound(self):
        status = '404 Not Found'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Not Found\n"
    urls = [
        ("/", "index"),
        ("/hello/(.*)", "hello")
    ]

    def __iter__(self):
        path = self.environ['PATH_INFO']
        method = self.environ['REQUEST_METHOD']
            
        for pattern, name in self.urls:
            m = re.match('^' + pattern + '$', path)
            if m:
                # pass the matched groups as arguments to the function
                args = m.groups()
                funcname = method.upper() + "_" + name
                func = getattr(self, funcname)
                return func(*args)
                    
        return self.notfound()

    def GET_hello(self, name):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello %s!\n" % name       
if __name__ == '__main__':
    httpserver.serve(application, host='127.0.0.1', port='8080')
