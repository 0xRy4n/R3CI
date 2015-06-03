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

import math

class Coordinator:

	# Function:		calcForwardCoords
	# Description:	calculates change in X and Y coordinates needed to move by in order to move a robot forward by a given distance at its current angle
	# Parameters: 	distance - type int ; desired foward distance
	#				curAngle - type float ; angle to move forward from
	# Returns:		two index integer list containing the needed change in x and y to move forward given distance.
	def calcForwardCoords(self, distance, curAngle):
		retVal = False

		if type(distance) is int and type(curAngle) is float:
			angle = curAngle * (math.pi / 180)

			displacementX = distance * math.cos(angle)
			displacementY = distance * math.sin(angle)

			retVal = [displacementX, displacementY]
		else:
			raise TypeError("Invalid parameter types. Requires and an int and a float.")

		return(retVal)
		

	# Function:		calcAngleToCoords
	# Description:	calculates the angle needed to turn a robot in curPosition to face the coordinates of targPosition
	# Parameters:	curPosition - type list ; a list with 2 indexes- the current x and y coordinates of the robot whom is turning
	#				targPosition - type list; a list wit.h 2 indexes- the x and y coordinates of the target position to turn to
	# Returns:		float containing the needed turn angle
	def calcAngleToCoords(self, curAngle, curPosition, targPosition):
		retVal = False

		if type(curPosition) is list and type(targPosition) is list:
			x_1, y_1 = curPosition
			x_2, y_2 = targPosition
			# Sets origin coordinate to zero
			x_2 = x_2 - x_1
			y_2 = y_2 - y_1

			radius = math.sqrt(y_2 ** 2 + x_2 ** 2) # Pythagorean Thereom, a^2 + b^2 = c^2 | Radius = c, y_2 = a, x_2 = b
			angle = curAngle * (math.pi / 180)

			x_1 = radius * math.cos(angle)
			y_1 = radius * math.sin(angle)

			turnArc = math.atan( (y_1 - y_2) / (x_2 - x_1) ) * (180 / math.pi)

			retVal = turnArc
			# TODO: Check to see if the angle is always clockwise.
		else:
			raise TypeError("Invalid parameter types. Requires two lists.")

		return(retVal)



