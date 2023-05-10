from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    # use this method name!
    def do_GET(self):
        message = "Hello"
        self.send_response(200)  # HTTP code
        self.send_header('Content-type', 'text/plain')  # define the content type
        self.end_headers()  # add a blank line
        self.wfile.write(message.encode())  # write the message
