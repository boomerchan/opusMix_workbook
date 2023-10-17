import http.server
import socketserver
import argparse

parser = argparse.ArgumentParser(description='HTTP Server')
parser.add_argument('--port', type=int, help='specify the port number', default=7865)
args = parser.parse_args()

PORT = args.port

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()