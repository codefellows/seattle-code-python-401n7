from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
# new
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Take the url string, and create a dictionary of the parameters
        url = self.path  # this is the url string
        url_components = parse.urlsplit(url)  # is the SplitResult() object
        query_string_list = parse.parse_qsl(url_components.query)  # list of key value pair tuples, representing the query string
        dictionary = dict(query_string_list)

        # We can do stuff!
        print(dictionary)
        dictionary_api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{dictionary.get('word')}"
        print("dictionary_api_url is:", dictionary_api_url)
        response = requests.get(dictionary_api_url)
        data = response.json()
        # print("data is:", data)
        definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        print("definition is:", definition)

        # Forming the response
        message = f"The meaning of {dictionary.get('word')} is: {definition}"
        self.send_response(200)  # HTTP code
        self.send_header('Content-type', 'text/plain')  # define the content type
        self.end_headers()  # add a blank line
        self.wfile.write(message.encode())  # write the message


if __name__ == '__main__':
    server_address = ('localhost', 8000)  # use any available port
    httpd = HTTPServer(server_address, handler)  # httpd is a commonly used abbreviation for "HTTP Daemon"
    print(f'Starting httpd server on {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
