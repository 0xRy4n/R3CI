import coordination, communication, collision

class R3Controller:

	coordinator = coordination.Coordinator()
	communicator = communication.Communicator()
	collision = collision.Collider()

	def _requestCoord(UID):
		retVal = False

		# Format for a coordinate request of robot with UID
		request = { 
				UID : {
				"get" : ["x", "y"] 
					  }
				  }

		response = self.communicator.send("db", request)

		if type(response) is dict:

			


	def getAngleToRobot(self, clientUID, targUID):
		# Request format for x and y coordinates of robot with UID
		request = { 
				UID : {
				"get" : ["x", "y"] 
						}
				  

		targCoords = self.communicator.send("db", request)

		angleToRobot = self.coordinator.getAngleToCoords()
