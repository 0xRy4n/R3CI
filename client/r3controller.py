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

import coordination, communication, collision

class R3Controller:

	# Object Instantiation #
	coordinator = coordination.Coordinator()
	communicator = communication.Client()
	collision = collision.Collider()

	def __init__():
		self.uniqueID = self.communicator.uid

	# Private Functions #

	def _requestCoord(self, UID):
		retVal = False
		# Format for a coordinate request of robot with UID
		request = {}
		request[UID] = {
			"get" : ["x", "y"]
		}

		response = self.communicator.send("db", request)

		if type(response) is dict:
			# TODO: Properly get x y values in a list from dict
			coords = response["get"][UID]
			retVal = coords
		else:
			# Following assumes server will return a string containing a message if an error occurs.
			print("Request failed. Server returned the following string:\n\n{}".format(response))
			# TODO: Add error handling here
		
		return(retVal)

	def _requestAngle(self, UID):
		retVal = False

		request = {}
		request[UID] = {
			"get" : ["angle"]
		}

		response = self.communicator.send("db", request)

		if type(response) is dict:
			# TODO: Properly get angle from dict
			angle = response["get"][UID]
			retVal = angle
		else: 
			print("Request failed. Server returned the following string:\n\n{}".format(response))

		return(retVal)

	# Public Functions #

	def getAngleToRobot(self, curAngle, targetUID):
		retVal = False

		curCoords = self._requestCoord(self.uniqueID)
		targCoords = self._requestCoord(targetUID)

		angleToTarget = self.coordinator.getAngleToCoords(curAngle, curCoords, targCoords)

		if angleToTarget != False:
			retVal = angleToTarget

		return(retVal)


	def getForwardCoords(self, curAngle, distance):
		retVal = False

		forwardCoords = coordinator.calcForwardCoorSds(distance, curAngle)

		if forwardCoords != False:
			retVal = forwardCoords

		return(retVal)

