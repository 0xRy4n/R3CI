import coordination, communication, collision

class R3Controller:

	# Object Instantiation #
	coordinator = coordination.Coordinator()
	communicator = communication.Communicator()
	collision = collision.Collider()

	def __init__(uniqueID):
		self.uniqueID = uniqueID

	# Private Functions #

	def _requestCoord(self, UID):
		retVal = False
		# Format for a coordinate request of robot with UID
		request = { 
				UID :	{
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
			# TODO: Add error handling here
		
		return(retVal)

	def _requestAngle(self, UID):
		retVal = False

		request = 	{
				UID : 	{
					"get" : ["angle"]
						}
					}
		response = self.communicator.send("db", request)

		if type(response) is dict:
			# TODO: Properly get angle from dict
			angle = response["get"]
			retVal = angle
		else: 
			print("Request failed. Server returned the following string:\n\n{}".format(response))

		return(retVal)


	# Public Functions #
	def getAngleToRobot(self, targetUID):
		retVal = False

		curCoords = self._requestCoord(self.uniqueID)
		targCoords = self._requestCoord(targetUID)

		angleToTarget = self.coordinator.getAngleToCoords(curAngle, curCoords, targCoords)

		if angleToTarget != False:
			retVal = angleToTarget

		return(retVal)


	def getForwardCoords(self, distance):
		retVal = False

		curAngle = self._requestAngle(self.uniqueID)
		forwardCoords = coordinator.calcForwardCoords(distance, curAngle)

		if forwardCoords != False:
			retVal = forwardCoords

		return(retVal)


