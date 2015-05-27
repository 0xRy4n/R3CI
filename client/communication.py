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

import socket,json
from time import sleep
class Sock():
	def __init__(self, server_address):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect(server_address)

	def send(self, data):
		self.sock.send(data)
		return self.sock.recv(1024)

	def __del__(self):
		self.sock.close()
"""
''' The Client() class handles communications between the server
''' along with implementing the R3CI communications protocol
"""
class Client():
	# Registers client on server and gives client a UID
	def __init__(self, name, host="localhost", port=9998):
		self.server_address = (host, port)
		self.uid = self.send("reg", {"ID":name})["bod"]["UID"]

	# Send packet to server -> returns response if succeeds, None if fail
	def send(self, typ, data):
		s = Sock(self.server_address)
		request  = self.form_packet(typ, data)
		response = s.send(request)
		del s

		rv = {}
		try:
			rv = json.loads(response)
		except:
			rv = None

		return rv
	# Takes a type and data, and forms a useable packet in the form of a string
	def form_packet(self, typ, data):
		new = {}
		new["req"] = typ
		new["bod"] = data
		return json.dumps(new)

# A quick test to see if the client/server are working nicely
if __name__ == "__main__":
	c = Client("potato")
	req = {}
	req[c.uid] = {"set":{"a":"b"}}
	res = c.send("db", req)
	if res == None: print("Fail")
	req = {}
	req[c.uid] = {"get":["a","ID"]}
	res = c.send("db", req)
	if res == None: print("Fail")
	print(res)
	
	del c

