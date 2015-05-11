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

    # Turns the robot.
    # Parameter 'direction' defines direction to turn in.
    # If 'direction' = 'LEFT', turns 270. If direction = 'RIGHT', turns 90. Else, if direction is an integer, turns by said integer. 
    # Units are in degrees.
    def turn(self, direction):
        retVal = False

        if direction.upper() == 'LEFT' or direction.upper() == '0':
            self.robot.turnBy(270)
            retVal = 2

        if direction.upper() == 'RIGHT' or direction.upper() == '2':
            self.robot.turnBy(90)
            retVal = 0

        if type(direction) is int and direction <= 360:
            self.robot.turnBy(direction)
            retVal = True

        return retVal

    # Uses the Fluke's camera to snap a picture. 
    # Parameter 'size' defines the resolution of the photo. Defaults to 'small', 'large' is also an option.
    def takePic(self, size="small"):
    	retVal = False

    	self.robot.setPicSize(size) # Defines large or small picture. Small is orders of magnitude faster.
    	try:
    		picture = takePicture("jpeg-fast") 
    		retVal = picture

    	except Exception as e:
    		print("Failed to take picture. Caught: {}".format(e))

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




			