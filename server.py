from http.server import CGIHTTPRequestHandler, HTTPServer
import socket

address = socket.gethostbyname(socket.gethostname())
print("IP address: " + address)
handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin', '/htbin']  # this is the default
server = HTTPServer(('', 8000), handler)
server.serve_forever()