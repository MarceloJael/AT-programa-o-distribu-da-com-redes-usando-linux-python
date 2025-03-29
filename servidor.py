from http.server import BaseHTTPRequestHandler, HTTPServer

class MeuServidor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        mensagem = "<h1>Servidor Web em Python está funcionando!</h1>"
        self.wfile.write(mensagem.encode())

# Configurações do servidor
host = "0.0.0.0"
porta = 8080
servidor = HTTPServer((host, porta), MeuServidor)
print(f"Servidor ativo em http://{host}:{porta}")
servidor.serve_forever()

