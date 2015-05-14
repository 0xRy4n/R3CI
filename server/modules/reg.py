
def handle(req, database):
	rv = {}
	rv["UID"] = database.newe(req["ID"])
	return rv
