class Coordination:

	def __init__(self, robot, communicator, UID):
		self.robot = robot
		self.communicator = communicator
		self.UID = UID

	def updateCoords(self):

		x, y = self.robot.getPosition() 
		communicator.send(self.communicator.send("db", "UID": { {"set": {"x":x, "y":y} } }) # Requests to set the x and y vals associated to UID in the database.


	# Moves the object self.robot forward while keeping track of its position on the coordinate map.
	# Parameter 'distance' is the distance  in you want to move.
	# Optionally, you can pass in 'move = False' if you simply want to simulate where the new coordinate position of the robot would be, without actually moving.
	# Units are in millimeters.
    def moveForward(self, distance, move = True):
    	retVal = False

	    bot1angle = self.robot.getAngle()
	    x = distance * math.cos(bot1angle * (math.pi / 180))
	    y = distance * math.sin(bot1angle * (math.pi / 180))

	    if move:
	        self.robot.moveBy(x, y)

	    retVal = [x, y]
    	return retVal


    # Turns robot to face another robot (specified by their uniqueID).
    # bot1 refers to robot doing the turning, bot2 refers to robot to turn towards.
    # Units are in degrees.
    def turnToFace(self, uniqueID):

        (bot1x, bot1y) = self.robot.getPosition() # Current x and y coordinates of bot1
        bot1angle = self.robot.getAngle() # Current angle of bot1
        (bot2x, bot2y) = None  # TODO

        x2 = bot2x - bot1x # Change in X
        y2 = bot2y - bot1y # Change in Y
        r = math.sqrt(x2 ** 2 + y2 ** 2) # Radius of turn arc
        (x1, y1) = self.forward(r, move=False) 

        turnAngle = math.atan(y1)
        self.robot.turnBy(turnAngle)