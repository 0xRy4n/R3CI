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
			
			# TODO: Properly get x y values in a list from dict
			coords = response["get"]
			retVal = coords
		else:
			# Following assumes server will return a string containing a message if an error occurs.
			print("Request failed. Server returned the following string:\n\n{}".format(response))		
			# TODO: Add error handlign here
		
		return(retVal)
			
	def getAngleToRobot(self, curAngle, clientUID, targetUID):
		retVal = False

		curCoords = self._requestCoord(clientUID)
		targCoords = self._requestCoord(targetUID)

		angleToTarget = self.coordinator.getAngleToCoords(curAngle, curCoords, targCoords)

		



