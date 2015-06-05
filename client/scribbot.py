# -*- encoding:utf-8 -*-
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

import Myro, Graphics, r3controller, random, time, threading

class ScribBot:

	def __init__(self, name, com, offset, sim=False):
		if not sim:
			self._robot = Myro.makeRobot("Scribbler", com)
		else:
			self._sim = Myro.Simulation("Simulation", 600, 600, Graphics.Color("lightgrey"))
			# Add lights first:
			self._sim.addLight((200, 200), 25, Graphics.Color("orange"))
			# Add walls and other objects:
			self._sim.addWall((10, 10), (20, 20), Graphics.Color("black"))
			self._sim.addWall((100, 100), (120, 120))
			# Is movable:
			circle = Graphics.Circle((100, 200), 20)
			self._sim.setup()
			self._robot = Myro.makeRobot("SimScribbler", self._sim)

		self._controller = r3controller.R3Controller(name, "192.168.1.119")
		self._robot.setPosition(offset[0], offset[1])
		self.name = name
		self._robot.setName(name)

		self._robot.setIRPower(120)
		t = threading.Thread(target=self.checkStall, args=())
		t.daemon = True
		t.start()


	def forward(self, distance):
		angle = self._robot.getAngle()
		(x, y) = self._controller.getForwardCoords(angle, distance)
		print(x,y)
		Myro.doTogether([self._robot.moveBy, x, y], [self._controller.setCoords, self.getPosition()])


	def backward(self, distance):
		angle = self._robot.getAngle()
		(x, y) = self._controller.getForwardCoords(angle, distance)
		Myro.doTogether([self._robot.moveBy, 0-x, 0-y], [self._controller.setCoords, self.getPosition()])


	def turnToFace(self, UID):
		curAngle = self._robot.getAngle()
		turnAngle = self._controller.getAngleToRobot(UID)
		self.turn(turnAngle)

	def turn(self, degree):
		self._robot.turnBy(degree)
		curAngle = self._robot.getAngle()
		self._controller.setAngle(curAngle)

	def turnLeft(self):
		self.turn(270)

	def turnRight(self):
		self.turn(90)

	def speak(self, words):
		self._robot.speak(words)

	def beep(time, frequency):
		self._robot.beep(time, frequency)

	def getPosition(self):
		retVal = self._robot.getPosition()
		return(retVal)

	def checkStall(self):
		while True:
			stalled = self._robot.getStall()
			dist = self._robot.getDistance()
		try:
    			if stalled or dist[1] < 15:
    				self._robot.stop()
    				self.backward(100)
    		except:
			pass
				
	def roam(self):
		turnVal = random.randint(1,360)
		moveVal = random.randint(50, 300)
		self.forward(moveVal)
		self.turn(turnVal)
        identify = self.r3controller._requestFront()
        return(identify)
