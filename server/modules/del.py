
def handle(sender, req, database, logger):
	database.dele(sender)
	logger.info(sender + " leaves")
	return {}
