from http.server import BaseHTTPRequestHandler, HTTPServer
import door_io_mock
import garage

class Server(BaseHTTPRequestHandler):
    garage = None
    with open("public/index.html", "r") as f:
        html = bytes(f.read(), "utf-8")
    with open("public/index.js", "r") as f:
        js = bytes(f.read(), "utf-8")
    ok = bytes("ok", "utf-8")
    
    def set_door_io(abstract_door_io):
        Server.garage = garage.Garage(abstract_door_io)
    
    def run(port):
        addr = ('127.0.0.1', port)
        httpd = HTTPServer(addr, Server)
        httpd.serve_forever()
    
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(Server.html)
        elif self.path == "/index.js":
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(Server.js)
        elif self.path == "/api/toggle":
            self.send_response(200)
            Server.garage.toggle()
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(Server.ok)
        else:
            self.send_response(404)
        return

if __name__ == "__main__":
    Server.set_door_io(door_io_mock.Door())
    Server.run(32694)
