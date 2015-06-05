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


""" Class: ScribBot
    
Description:		ScribBot is intended to be the object that serves as the front-end of R3CI. It contains 
		code with high-level functionality, such as moving the robot forward, or making it turn. It is the object
		closest to the end-user, and should be used as a replacement to simply importing Myro. Movement in ScribBot
		is done on a simulated coordinate grid, allowing the server to map the position of the robot in a way
		that cooresponds with the its physical position. Whenever a function that involves movement is called, 
		the server is alerted of this change and updates its knowledge of the robots position and orientation 
		in a database.
		
Parameters:	'name' - a string that represents the name of the robot, ex; "bob"
		'com' - a string cointaining the com port of the bluetooth connection the scribbler
		'offset' - a list containing two INTEGERS, x and y, specifying the robots initial distance from the origin.
		'sim' - a condition defaulted to False that if True initializes a scribbler simulation instead of a robot.

To Do:			- Get coordinate movement to work with Fluke forward. The IR sensors are much better and avoiding 
		obstacles is critical to correctly mapping a robots position. Failure to avoid an obstacle could lead to 
		things such as the robot telling the server that it just moved 10 feet when in reality its been stuck at 
		a wall
			- Check if com port is open before attempting to connect, and close it if it is. Probably
		could do this with PySerial, but not sure if admin privileges would be needed or how python handles
		that. This would fix bluetooth connection issues where Calico must be restarted before reconnecting.
		
Ryan J Gordon, 2015 """
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
		Myro.speak(words)
    def beep(time, frequency):
		self._robot.beep(time, frequency)

    def getPosition(self):
		retVal = self._robot.getPosition()
		return(retVal)

    def checkStall(self):
		while True:
		    stalled = self._robot.getStall()
		    dist = self._robot.getDistance()
		    print(dist)
		    try:
				if stalled or (dist[0] + dist[1]) < 22 or dist[0] is 0 or dist[1] is 0:
				    self._robot.stop()
				    self.backward(100)
		    except:
				pass
		
    def roam(self):
		turnVal = random.randint(1,360)
		moveVal = random.randint(50, 300)
		self.forward(moveVal)
		self.turn(turnVal)
		identify = self._controller._requestFront()
		return(identify)
