R3CI - Robot Communication, Coordination, Collision and Identification
-----------------------------------------------------------------------

R3CI is an attempt at developing a system for Parallax Scribbler 2 robots to
communicate, perform complex coordination as a group, accurately identify
other robots, and differentiate collisions between robots, along with avoiding
other obstacles such as walls.

scribbot.py serves as the interface for R3CI. Those who wish to use R3CI as is should
refer to the documentation within that file after reading the rest of this readme. 

When setting up the robots, you must measure their distance in centimeters from a given 
origin point (a point that you can call 0,0), and pass that into ScribBot as the offset.
You must measure this distance in terms of x and y values, as you would on a coordinate grid.

You must also decide what will be considered the 'front' of the room (direction that you would
consider to increase position on the Y axis). You must then measure the angle of the robot 
relative to that direction. If they were facing that direction, they would have an angle of
360 or 0. If they were facing opposite of that direction, they would have angle of 180.
You must then pass that angle into ScribBot. 

Because R3CI relies so heavily on mathematics to keep track of the the robots, you must
be as precise as possible when taking this measurements. For simplicity, it is recommended
you do this on floor with 1 sqaure foot tiles.

You will also need to have a central computer to serve as the medium for robot 
communication. You will need to run server.py on that computer. The IP of that computer 
will later be passed as a parameter when initializing the ScribBot class.


*R3CI requires IPRE's Calico to run.*

**There is a known issue where Calico must be restarted after each attempt to connect to the robot.**
**If you are receiving a bluetooth error, restart Calico.**
