#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import myro
import random


class ScribBot:

    def __init__(self, com, offset, name):
        self.coordOffset = offset
        self.robot = myro.makeRobot('Scribbler', com)
        self.name = name
        self.communicator = # r3ci.com.Client(SERVER, PORT, NAME)
        self.uniqueID = # self.communicator.send("reg", {"ocvid":name})
        self.check = lambda retVal: assert retVal != False


    # Function: 	turn()
    # Description:	Turns the robot to a given direction.
    # Parameters: 	direction -- Direction to turn robot to. Can be 'LEFT', 'RIGHT' or a int 0-360 representing an angle in degrees.
    # Returns: 		'2' if parameter direction was 'LEFT', '0' if parameter direction was 'RIGHT', None if parameter was angle 0-360. Anything else returns false.
    def turn(self, direction):
    	retVal = False

    	if type(direction) is str:
    		direction = direction.upper()

	        if direction == 'LEFT':
	            self.robot.turnBy(270) 
	            retVal = 2
	        if direction == 'RIGHT':
	            self.robot.turnBy(90)
	            retVal = 0

        if type(direction) is int:
        	direction = abs(direction)

        	if direction <= 360:
        		self.robot.turnBy(direction)
        	if direction > 360:
        		print("Direction integer out of bounds. 0-360 only.")

    	check(retVal)
        return retVal


    # Uses the Fluke's camera to snap a picture. 
    # Parameter 'size' defines the resolution of the photo. Defaults to 'small', 'large' is also an option.
    def takePic(self, size="small"):
    	retVal = False

    	self.robot.setPicSize(size)
    	retVal = self.robot.takePicture("jpeg-fast")

    	check(retVal)
    	return retVal



    def getAvgObstacle(self):
        count = 0
        obstacleVals = []  # Index 0 holds left, 1 holds center, 2 holds right
        while count <= 2:
            obstacleSum = 0

            # Checks sensor 4 times and gets average.

            for i in range(0, 4):
                obstacleSum += self.robot.getObstacle(count)
            obstacleVals.append(obstacleSum / 4)
            count += 1




			