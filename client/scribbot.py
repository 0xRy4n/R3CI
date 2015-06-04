"""
    This file is part of R3CI.
    
    Copyright (C) R3CI Team :: All Rights Reserved
    
    R3CI is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    R3CI is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with R3CI.  If not, see <http://www.gnu.org/licenses/>.
"""

import Myro, r3controller, random

class ScribBot:

	def __init__(name, com, offset):
		self._robot = Myro.makeRobot(name, com)
		self._controller = r3controller.R3Controller()
		self._robot.setPosition(offset[0], offset[1])

	def forward(self, distance):
		angle = self._robot.getAngle()
		(x, y) = self._controller.getForwardCoords(angle, distance)
		self._robot.doTogether(self._robot.moveBy(x,y), checkStall())

	def backward(self, distance):
		angle = self._robot.getAngle()
		(x, y) = self._controller.getForwardCoords(angle, distance)
		self._robot.doTogether(self._robot.moveBy(0-x, 0-y), checkStall())

	def turnToFace(self, UID):
		curAngle = self._robot.getAngle()
		turnAngle = self._controller.getAngleToRobot(UID)
		self._robot.turnBy(turnAngle)

	def turn(self, degree):
		self._robot.turnBy(degree)

	def turnLeft(self):
		self._robot.turnBy(270)

	def turnRight(self):
		self._robot.turnBy(90)

	def speak(self, words):
		self._robot.speak(words)

	def beep(time, frequency):
		self._robot.beep(time, frequency)

	def getPosition(self):
		retVal = self._robot.getPosition()
		return(retVal)

	def checkStall(self):
		stalled = self._robot.getStall()
		if stalled:
			self._robot.stop()
			self.backward(100)
			self.turn(180)	

	def roam(self):
		turnVal = random.randint(1,360)
		moveVal = random.randint(50, 300)
		self.forward(moveVal)
		self.turn(turnVal)
		# check for robots
		# return robot name if found
		# else return false




