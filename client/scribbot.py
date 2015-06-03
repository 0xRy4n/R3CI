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

class ScribBot:

	def __init__(name, com, offset):
		self._robot = myro.makeRobot(name, com)
		self._controller = R3Controller.R3Controller()
		self._robot.setPosition(offset[0], offset[1])

	def forward(self, distance):
		angle = self._robot.getAngle()
		self._controller.getForwardCoords(angle, distance)
		
	def turnToFace(self, UID):
		curAngle = self._robot.getAngle()
		turnAngle = self._controller.getAngleToRobot(UID)
		self._robot.turnBy(turnAngle)

	def turn(self, degree):
		self._robot.turnBy(degree)

	def getPosition(self):
		retVal = self._robot.getPosition()
		return(retVal)
