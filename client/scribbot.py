import Myro as myro
import r3controller

class ScribBot:

	def __init__(self, name, com, server):
		self.name = name
		self.server = server
		self.robot = myro.makeRobot("Scribbler", com)
		self.controller = r3controller.R3Controller(self.name, self.server)

	def forward(self, distance):
		angle = self.robot.getAngle()
		self.controller.getForwardCoords(angle, distance)
		
	def turnToFace(self, UID):
		curAngle = self.robot.getAngle()
		turnAngle = self.controller.getAngleToRobot(UID)
		self.robot.turnBy(turnAngle)

