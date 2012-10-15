#!/usr/bin/env python 
# -*- coding: iso-8859-15 -*-

import sys
import BaseHTTPServer

PORT = int(sys.argv[1])

Handler = BaseHTTPServer.BaseHTTPRequestHandler

def ok(self):
    self.send_response(200)
    self.send_header("Content-type", "text/plain")
    return None

Handler.do_GET = ok
Handler.do_POST = ok

server_address = ('', PORT)
BaseHTTPServer.HTTPServer(server_address, Handler).serve_forever()
