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


import coordination, communication

class R3Controller:

	def __init__(self, name, server="localhost"):
		self.coordinator = coordination.Coordinator()
		self.communicator = communication.Client(name, server)
		self.uid = self.communicator.uid
		self.communicator.send("db", {self.uid: {"set":{"name":name}}})

	# Private Functions #
	def _requestCoord(self, uid):
		retVal = False
		# Format for a coordinate request of robot with uid
		request = {}
		request[uid] = {
			"get" : ["loc"]
		}

		response = self.communicator.send("db", request)

		if type(response) is dict:
			# TODO: Properly get x y values in a list from dict
			retVal = response[uid]
		else:
			# Following assumes server will return a string containing a message if an error occurs.
			print("Request failed. Server returned the following string:\n\n{}".format(response))
			# TODO: Add error handling here
		
		return(retVal)

	def _requestAngle(self, uid):
		retVal = False

		request = {}
		request[uid] = {
			"get" : ["angle"]
		}

		response = self.communicator.send("db", request)

		if type(response) is dict:
			# TODO: Properly get angle from dict
			angle = response[uid]["angle"]
			retVal = angle
		else: 
			print("Request failed. Server returned the following string:\n\n{}".format(response))

		return(retVal)
	
	def _requestFront(self):
		response = self.communicator.send("front", {})
		name = ""
		if response != {"":""}:
			name, uid = response.popitem()

		return name

	# Public Functions #

	def setAngle(self, angle):
		request = {}
		request[self.uid] = {
			"set" : {"angle" : angle}
		}

		response = self.communicator.send("db", request)

	def setCoords(self, coords):
		request = {}
		request[self.uid] = {
			"set" : {"loc" : coords}
		}

		response = self.communicator.send("db", request)

	def getAngleToRobot(self, curAngle, targetuid):
		retVal = False

		curCoords = self._requestCoord(self.uid)
		targCoords = self._requestCoord(targetuid)

		angleToTarget = self.coordinator.getAngleToCoords(curAngle, curCoords, targCoords)

		if angleToTarget != False:
			retVal = angleToTarget

		return(retVal)

	# Gets new coordinates of robot if moved forward by given distance
	def getForwardCoords(self, curAngle, distance):
		retVal = False

		forwardCoords = self.coordinator.calcForwardCoords(int(distance), float(curAngle))

		if forwardCoords != False:
			retVal = forwardCoords

		return(retVal)


