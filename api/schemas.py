#!/usr/bin/env python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Load the JSON records
with open("sms_records.json", "r") as f:
    transactions = json.load(f)

def save_transactions():
    with open("sms_records.json", "w") as f:
        json.dump(transactions, f, indent=2)

# Give each transaction an ID if it doesn’t have one
for i, tx in enumerate(transactions, start=1):
    tx.setdefault("id", i)


class SimpleAPI(BaseHTTPRequestHandler):

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    # GET: list all or one by ID
    def do_GET(self):
        if self.path == "/transactions":
            self._set_headers()
            self.wfile.write(json.dumps(transactions).encode())
        elif self.path.startswith("/transactions/"):
            try:
                tx_id = int(self.path.split("/")[-1])
                tx = next((t for t in transactions if t["id"] == tx_id), None)
                if tx:
                    self._set_headers()
                    self.wfile.write(json.dumps(tx).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Not found"}).encode())
            except ValueError:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid ID"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    # POST: add new transaction
    def do_POST(self):
        if self.path == "/transactions":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_tx = json.loads(post_data)

            # Assign a new ID
            new_tx["id"] = max(t["id"] for t in transactions) + 1 if transactions else 1
            transactions.append(new_tx)

            save_transactions()   # 🔹 persist change

            self._set_headers(201)
            self.wfile.write(json.dumps(new_tx, indent=2).encode("utf-8"))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode("utf-8"))

    def do_PUT(self):
        path_parts = self.path.strip("/").split("/")
        if len(path_parts) == 2 and path_parts[0] == "transactions":
            try:
                tx_id = int(path_parts[1])
                tx = next((t for t in transactions if t["id"] == tx_id), None)
                if not tx:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Transaction not found"}).encode("utf-8"))
                    return

                content_length = int(self.headers["Content-Length"])
                put_data = self.rfile.read(content_length)
                updated_tx = json.loads(put_data)

                tx.update(updated_tx)

                save_transactions()   # 🔹 persist change

                self._set_headers(200)
                self.wfile.write(json.dumps(tx, indent=2).encode("utf-8"))

            except ValueError:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid ID"}).encode("utf-8"))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode("utf-8"))

    def do_DELETE(self):
        path_parts = self.path.strip("/").split("/")
        if len(path_parts) == 2 and path_parts[0] == "transactions":
            try:
                tx_id = int(path_parts[1])
                global transactions
                transactions = [t for t in transactions if t["id"] != tx_id]

                save_transactions()   # 🔹 persist change

                self._set_headers(204)
                self.wfile.write(b"")
            except ValueError:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid ID"}).encode("utf-8"))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode("utf-8"))

def run(port=8000):
    server = HTTPServer(("", port), SimpleAPI)
    print(f"🚀 Server running at http://localhost:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
