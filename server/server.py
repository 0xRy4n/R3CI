"""
    This file is part of R3CI.

    Copyright (C) R3CI Team :: All Rights Reserved

    R3CI is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    R3CI is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with R3CI.  If not, see <http://www.gnu.org/licenses/>.
"""

import SocketServer, logging, threading, json, modules
from optparse import OptionParser
from time import sleep

class R3CIServer(SocketServer.TCPServer):
	def __init__(self, server_address, RequestHandlerClass, database, EnableCV=False):
		self.logger = logging.getLogger("R3CIServer")
		self.db = database
		self.cv = EnableCV
		SocketServer.TCPServer.__init__(
			self, server_address, RequestHandlerClass, bind_and_activate=True
		)
	def server_activate(self):
		self.logger.debug("server_activate")
		SocketServer.TCPServer.server_activate(self)
		return

	def serve_forever(self):
		self.logger.debug("waiting for request")
		self.logger.info("Handling requests, press <Ctrl-C> to quit")
		while True:
			self.handle_request()
		return

	def handle_request(self):
		self.logger.debug("handle_request")
		return SocketServer.TCPServer.handle_request(self)

	def verify_request(self, request, client_address):
		self.logger.debug("verify_request(%s, %s)", request, client_address)
		return SocketServer.TCPServer.verify_request(self, request, client_address)

	def process_request(self, request, client_address):
		self.logger.debug("process_request(%s, %s)", request, client_address)
		return SocketServer.TCPServer.process_request(self, request, client_address)

	def server_close(self):
		self.logger.debug("server_close")
		return SocketServer.TCPServer.server_close(self)

	def finish_request(self, request, client_address):
		self.logger.debug("finish_request(%s, %s)", request, client_address)
		return SocketServer.TCPServer.finish_request(self, request, client_address)

	def close_request(self, request_address):
		self.logger.debug("close_request(%s)", request_address)
		return SocketServer.TCPServer.close_request(self, request_address)


class R3CIRequestHandler(SocketServer.BaseRequestHandler):
	def __init__(self, request, address, server, CV=False):
		self.logger = logging.getLogger("R3CIRequestHandler")
		self.logger.debug("__init__")
		self.req_data = ""
		self.res_data = ""
		self.req      = {}
		self.res      = {}
		SocketServer.BaseRequestHandler.__init__(self, request, address, server)
	
	def setup(self):
		self.logger.debug("setup")
		return SocketServer.BaseRequestHandler.setup(self)

	def handle(self):
		self.logger.debug("handle")
		self.req_data = self.request.recv(1024)
		self.logger.debug("request(%s)", self.req_data)
		self.req = json.loads(self.req_data)

		if self.req["ID"] == "":
			response = modules.reg.handle(
				self.client_address, self.req["bod"], self.server.db, self.logger
			)
			if self.server.cv and self.req["bod"]["classifier"]:
				if not modules.ocv.init(response["UID"], self.req["bod"]["classifier"]):
					response = "Can't find CV Classifier"
		else:
			response = getattr(
				modules, self.req["req"]
			).handle(
				self.req["ID"], self.req["bod"], self.server.db, self.logger
			)

		if type(response) is dict:
			self.res["success"] = True
			self.res["bod"]     = response
		else:
			self.res["success"] = False
			self.res["bod"]     = response
		
		self.res_data = json.dumps(self.res)
		self.logger.debug("response(%s)", self.res_data)
		self.request.send(self.res_data)
		return
	
	def finish(self):
		self.logger.debug("finish")
		return SocketServer.BaseRequestHandler.finish(self)

def parsearg():
	parser = OptionParser()

	parser.add_option("-p", "--port", dest="port", default="9998",
	                  help="Set the port", metavar="PORT")
	parser.add_option("-o", action="store_true", default=False,
	                  help="Enable opencv")
	parser.add_option("-v", action="store_true", default=False,
	                  help="Verbose logging (debug)")

	return parser.parse_args()

def main():
	options, args = parsearg()

	OCV = False
	LOGLVL = logging.INFO

	if options.o:
		OCV = True
	
	if options.v:
		LOGLVL = logging.DEBUG

	logging.basicConfig(level=LOGLVL,
                    format="%(name)s: %(message)s",
                    )

	db = modules.db.Database()
	host, port = "localhost", int(options.port)

	server = R3CIServer((host,port), R3CIRequestHandler, db, EnableCV=OCV)
	rhost, rport = server.server_address

	t = threading.Thread(target=server.serve_forever)
	t.setDaemon(True)
	t.start()

	logger = logging.getLogger("main")
	logger.info("Server on %s:%s", rhost, rport)

	try:
		while 1: sleep(1000)
	except:
		print("\nGoodbye.\n")

if __name__ == "__main__":
	main()
