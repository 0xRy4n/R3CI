import MySQLdb as db

class SQL:
	conn, cur, usernm, passwd, host = None
	connected = False

	def connect(self):
		self.conn = db.connect(username=self.usernm, passwd=self.passwd, host=self.host)
		self.cur = self.conn.cursor()
		self.connected = True

	def disconnect(self):
		self.cur.close()
		self.connected = False

	# Executes SQL Commands
	def execute(self, command):
		if !connected:
			self.connect()
		else:
			self.cur.execute(command)
			
	def createDB(self, name):
		command = "CREATE DATABASE {};".format(name)
		self.execute(command)

	def createTable(self, name, database):
		command = "USE {};".format(database)
		command1 = "CREATE TABLE {};".format(name)
		self.execute(command)
		self.execute(command1)

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

