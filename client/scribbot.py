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

	def __init__(name, com):
		self.robot = myro.makeRobot(name, com)
		self.controller = R3Controller.R3Controller()

	def forward(self, distance):
		angle = self.robot.getAngle()
		self.controller.getForwardCoords(angle, distance)
		
	def turnToFace(self, UID):
		curAngle = self.robot.getAngle()
		turnAngle = self.controller.getAngleToRobot(UID)
		self.robot.turnBy(turnAngle)
