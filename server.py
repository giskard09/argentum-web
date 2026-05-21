"""Servidor estático mínimo para argentum-web con SPA routing.

Sirve archivos estáticos normales. Para rutas bajo /dashboard/* que no
corresponden a un archivo real, sirve dashboard/index.html — el JS
lee el agent_id desde window.location.pathname.
"""
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = int(os.environ.get("PORT", 8018))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class SPAHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Quitar query string
        path = path.split("?", 1)[0].split("#", 1)[0]
        # Para /dashboard/* que no existen como archivo, servir dashboard/index.html
        if path.startswith("/dashboard/") or path == "/dashboard":
            full = os.path.join(BASE_DIR, "dashboard", "index.html")
            if os.path.exists(full):
                return full
        return super().translate_path(path)

    def log_message(self, fmt, *args):
        pass  # silenciar logs en producción


if __name__ == "__main__":
    os.chdir(BASE_DIR)
    server = HTTPServer(("0.0.0.0", PORT), SPAHandler)
    server.serve_forever()
