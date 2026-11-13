"""Tiny health-check service used to demonstrate a signed, SBOM-attested container image."""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"status": "ok", "version": os.getenv("APP_VERSION", "dev")}).encode()
        self.send_response(200 if self.path in ("/", "/health") else 404)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
