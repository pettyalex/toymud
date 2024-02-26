import http.server
import asyncio
import multiprocessing as mp

from .server import run_ws_server

DIRECTORY=__path__[0] + '/web'

def start_http_server():
    """
    Uses the http module to start a server.
    Serves static web content from the web dir
    """
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)

    http_server = http.server.HTTPServer(("", 8000),Handler)
    http_server.serve_forever()

def main():
    http_process = mp.Process(target=start_http_server)
    http_process.start()
    asyncio.run(run_ws_server())
    http_process.join()
