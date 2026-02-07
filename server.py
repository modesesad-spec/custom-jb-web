import http.server
import socketserver
import json
import os

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/config.json':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            with open('config.json', 'r') as f:
                self.wfile.write(f.read().encode())
        else:
            super().do_GET()

print(f"Server berjalan di http://localhost:{PORT}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()