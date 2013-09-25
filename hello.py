from paste import httpserver

class application:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello world!!\n"
        
if __name__ == '__main__':
    httpserver.serve(application, host='127.0.0.1', port='8080')
