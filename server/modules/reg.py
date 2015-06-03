
def handle(sender, req, database, logger):
	rv = {}
	rv["UID"] = database.newe(req["classifier"])
	logger.info("{} registered as {}".format(sender, rv["UID"]))
	return rv
