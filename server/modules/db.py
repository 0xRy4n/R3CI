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

import uuid

BaseTemplate = {
	"angle":0,
	"loc":[0,0],
	"classifier":""
}

class Database():
	def __init__(self, template=BaseTemplate):
		self.template = template
		self.database = self._new_db()

	def newe(self):
		UID = self._new_id()
		return UID

	def dele(self, ID):
		self._delete(ID)

	def sete(self, ID, key, value):
		self._set_key(ID, key, value)

	def gete(self, ID, key):
		rv = None
		rv = self._get_key(ID, key)
		return rv
	
	def setm(self, ID, keyvals):
		for key in keyvals:
			self.sete(ID, key, keyvals[key])

	def getm(self, ID, keys):
		rv = {}
		for key in keys:
			rv[key] = self.gete(ID, key)

		return rv

	def _new_db(self):
		return {}

	def _new_id(self):
		new = self.template
		uuid_str = str( uuid.uuid1() )
		self.database[uuid_str] = new
		return uuid_str

	def _key_exists(self, ID, key):
		rv = False
		if key in self.database[ID]:
			rv = True
		return rv

	def _get_key(self, ID, key):
		return self.database[ID][key]

	def _set_key(self, ID, key, value):
		self.database[ID][key] = value
		return self.database[ID][key]
	
	def _delete(self, ID):
		del self.database[ID]

def init(server, logger, sender, req):

	rv = server.db.newe()
	logger.info("{} registered as {}".format(sender, rv))
	return rv

def delete(server, logger, sender):
	server.db.dele(sender)
	logger.info(sender + " removed")

"""
''' Requires "set" or "get" or both:
''' {
''' "<uid of robot>": {
'''     "set": {
'''         "<key>":"<value>"
'''            },
'''
'''     "get": [
'''         "<key>"
'''            ]
''' }
'''
''' Returns what is fetched if "get"::
''' {
'''     "<uid of robot>": {
'''         "<key>" : "<value>"
'''     }
''' }
"""
def handle(sender, req, database, logger):
	rv = {}
	for UID in req:
		if "set" in req[UID]:
			database.setm(UID, req[UID]["set"])
		if "get" in req[UID]:
			rv[UID] = database.getm(UID, req[UID]["get"])

	return rv

