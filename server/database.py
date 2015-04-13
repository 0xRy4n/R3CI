import MySQLdb as db

class SQL:
	conn, cur, usernm, passwd, host = None
	connected = False

	# Connects to MySQL
	def connect(self):
		self.conn = db.connect(username=self.usernm, passwd=self.passwd, host=self.host)
		self.cur = self.conn.cursor()
		self.connected = True

	# Disconnects MySQL
	def disconnect(self):
		self.cur.close()
		self.connected = False

	# Executes SQL Commands
	def execute(self, command):
		if !connected:
			self.connect()
		else:
			self.cur.execute(command)

	# Creates a database called 'name'
	def createDB(self, name):
		command = "CREATE DATABASE {};".format(name)
		self.execute(command)

	# Creates a table in 'database' called 'name'.
	def createTable(self, name, database):
		command = "USE {};".format(database)
		command1 = "CREATE TABLE {};".format(name)
		self.execute(command)
		self.execute(command1)

	# Creates a column under 'table' in 'database' called 'name'.
	# Optional parameters:
	#	 'length' to specify how many values to store if required (as varchar does for example).
	#	 'after' to insert column after another column.
	def createColumn(self, name, table, database, coltype="varchar", length=60, after=None):
		types = ["char, varchar, text, bool, int, float"]

		match = 0
		for i in range(0, len(types) - 1):
			if types[i].upper() == coltype.upper():
				match = 1
				if <= 1:
					coltype = "{}({})".format(coltype, length)

		if match:
			command = "USE {};".format(database)
			command1 = "ALTER TABLE {} ADD {} {};".format(table, name, coltype)

	def __init__(self, username, password, hostnm="127.0.0.1"):
		self.usernm = username
		self.passwd = password
		self.host = hostnm

		# Test settings
		print("Testing configuration.")
		try:
			self.connect()
		except Exception as e:
			print("Configuration failed. Caught: {}".format(Exception))
		else:
			self.disconnect()
			print("Configuration Successful.")

