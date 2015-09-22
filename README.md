R3CI - Robot Communication, Coordination, Collision and Identification
-----------------------------------------------------------------------

R3CI is an attempt at developing a system for Parallax Scribbler 2 robots to
communicate, perform complex coordination as a group, accurately identify
other robots, and differentiate collisions between robots, along with avoiding
other obstacles such as walls.

scribbot.py serves as the interface for R3CI. Those who wish to use R3CI as is should
refer to the documentation within that file. 

You will also need to have a central computer to serve as the medium for robot 
communication. You will need to run server.py on that computer. The IP of that computer 
will later be passed as a parameter when initializing the ScribBot class.


*R3CI requires IPRE's Calico to run.*

**There is a known issue where Calico must be restarted after each attempt to connect to the robot.**
**If you are receiving a bluetooth error, restart Calico.**
