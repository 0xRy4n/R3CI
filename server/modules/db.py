import uuid

BaseTemplate = {
	"x":0,
	"y":0,
	"ID":""
}

class Database():
	def __init__(self, template=BaseTemplate):
		self.template = template
		self.database = self._new_db()

	def newe(self, ID):
		UID = self._new_id(ID)
		return UID
	
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

	def _new_id(self, ID):
		new = self.template
		new["ID"] = ID
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

"""
''' Handles requests from the server
'''
''' {
'''     "set": {
'''         "<key>":"<value>"
'''            }
'''     "get": [
'''         "<key>"
'''            ]
''' }
"""
def handle(req, database):
	rv = {}
	for UID in req:
		if "set" in req[UID]:
			print(req[UID]["set"])
			database.setm(UID, req[UID]["set"])
		if "get" in req[UID]:
			rv = database.getm(UID, req[UID]["get"])
	return rv

