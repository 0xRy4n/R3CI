import math
import myro

class ScribBot:
	uniqueID = ""
	coordOffset = [0,0]
	robot = None

	# Generates random ASCII string to be used as unique identifier.
	def __init__(self, offset, com):
		self.uniqueID = __genUniqueID()
		self.coordOffset = offset
		self.robot = myro.makeRobot("Scribbler", com)

	def turnLeft(self):
		robot.turnBy(270)
	def turnRight(self):
		robot.turnBy(90)
	def turnBy(deg):
		robot.turnBy(deg)
	def turnToFace(uniqueID):
		bot1x, bot1y = getPosition()
		bot1angle = getAngle()
		bot2x, bot2y = # TODO

		x2 = bot2x - bot1x
		y2 = bot2y - bot1y
		r = math.sqrt(x2**2 + y2**2)
		x1 = r * math.cos(bot1angle * (math.pi / 180))
		y1 = r * math.sin(bot1angle * (math.pi / 180))

		turnAngle = math.atan((y))
		robot.turnBy(turnAngle)
		
	
	def avoidObstacle(self):
		retVal = False

		count = 0
		obstacleVals = [] # Index 0 holds left, 1 holds center, 2 holds right
		while count <= 2:
			obstacleSum = 0
			# Checks sensor 4 times and gets average.
			for i in range(0,4):
				obstacleSum += getObstacle(count)
			obstacleVals.append(obstacleSum / 4)

		# If greater than 3000 assume obstacle in front of robot. Value might need tinkering.
		if obstacleVals[1] > 3000:
			retVal = True
			if obstacleVals[0] < obstacleVals[2]:
				robot.turnBy(270)
			else:
				robot.turnBy(90)
		
		return(retVal)

	def checkCollision(self):
		if targeting:
			## TODO
		else:
			# Assume collision with obstacle.
			robot.




