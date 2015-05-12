class Coordination:

	def __init__(self, robot, communicator, UID):
		self.robot = robot
		self.communicator = communicator
		self.UID = UID
	
	def updateCoords(self):
		x, y = self.robot.getPosition() 
		self.communicator.send(self.communicator.send("db", "UID": { {"set": {"x":x, "y":y} } }) # Requests to set the x and y vals associated to UID in the database.
			
	def moveForward(self, distance, move = True):
		retVal = False
		
		bot1Angle= self.robot.getAngle() * (math.pi / 180) # Current angle of bot 1 converted to degrees
		x = distance * math.cos(bot1Angle) # X coordinate of new position
		y = distance * math.sin(bot1Angle) # Y coordinate of new position
		
		if move:
			self.robot.moveBy(x, y)
		
		retVal = [x, y]
		return retVal

	def turnToFace(self, uniqueID):
		retVal = False
		
		(bot1x, bot1y) = self.robot.getPosition() # Current x and y coordinates of bot1
		bot1angle = self.robot.getAngle() # Current angle of bot1
		(bot2x, bot2y) = 
		
		x2 = bot2x - bot1x # Change in X
		y2 = bot2y - bot1y # Change in Y
		r = math.sqrt(x2 ** 2 + y2 ** 2) # Radius of turn arc
		(x1, y1) = self.forward(r, move=False) 
		
		turnAngle = retVal = math.atan(y1))
		self.robot.turnBy(turnAngle)
		
		return(retVal)
