import math, myro, random

class ScribBot:
	uniqueID = ""
	coordOffset = [0,0]
	robot = None

	# Generates random ASCII string to be used as unique identifier.
	def __init__(self, offset, com):
		self.uniqueID = __genUniqueID()
		self.coordOffset = offset
		self.robot = myro.makeRobot("Scribbler", com)

	def turn(self, direction):
		retVal = False

		if direction.upper() == "LEFT" or direction.upper() == "0":
			robot.turnBy(270)
			retVal = 2
		if direction.upper() == "RIGHT" or direction.upper() = "2":
			robot.turnBy(90)
			retVal = 0
		if type(direction) is int and direction <= 360:
			robot.turnBy(direction)
			retVal = True

		return(retVal)

	# move can be passed as false to return x and y without moving the robot
	def forward(self, distance, move=True):
		retVal = False

		x = distance * math.cos(bot1angle * (math.pi / 180))
		y = distance * math.sin(bot1angle * (math.pi / 180))

		if move:
			robot.moveBy(x,y)

		retVal = [x,y]
		return(retVal)

	def turnToFace(self, uniqueID):
		bot1x, bot1y = getPosition()
		bot1angle = getAngle()
		bot2x, bot2y = None # TODO

		x2 = bot2x - bot1x
		y2 = bot2y - bot1y
		r = math.sqrt(x2**2 + y2**2)
		x1, y1 = forward(r, move=False)

		turnAngle = math.atan((y))
		robot.turnBy(turnAngle)
	
	def getAvgObstacle(self):
		count = 0
		obstacleVals = [] # Index 0 holds left, 1 holds center, 2 holds right
		while count <= 2:
			obstacleSum = 0
			# Checks sensor 4 times and gets average.
			for i in range(0,4):
				obstacleSum += robot.getObstacle(count)
			obstacleVals.append(obstacleSum / 4)
			count += 1

		return(obstacleVals)

	def avoidObstacles(self):
		retVal = False
		threshold = 3000 	# If greater than 3000 assume obstacle in front of robot. Value might need tinkering.
		obstacleVals = getAvgObstacle()

		if obstacleVals[1] > threshold:
			retVal, avoiding = True
			obstacleDir = None # Holds the number value of the sensor that is facing the obstacle after a turn.

			if obstacleVals[0] < obstacleVals[2]:
				obstacleDir = robot.turnLeft()

			elif obstacleVals[2] < obstacleVals[0]:
				obstacleDir = robot.turnRight()

			else:
				x = random.randint(0,1)
				if x == 1:
					obstacleDir = robot.turnRight()
				else:
					obstacleDir = robot.turnLeft()

			turnCount = 0
			displacement = 0

			while avoiding:
				self.forward(50)

				if turnCount == 0:
					displacement += 50

				obstacleVals = getAvgObstacle()
				if obstacleVals[obstacleDir] < threshold:
					self.turn(str(obstacleDir))
					turnCount += 1
				
				if turnCount == 3:
					self.forward(displacement)
					if obstacleDir == 2:
						self.turn("0")
					else:
						self.turn("2")
					avoiding = False




