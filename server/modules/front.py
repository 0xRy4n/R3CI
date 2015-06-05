import math

def translate(coords, angle):
	x = (math.cos(angle) * coords[0]) + (math.sin(angle) * coords[1])
	y =(-math.sin(angle) * coords[0]) + (math.cos(angle) * coords[1])
	return (x,y)

def init(server, logger, sender, req):
	return {}

def delete(server, logger, sender):
	pass


"""
   Calculate what is in front of the robot.
   Uses sender info, does not need a body.

   Returns robots that are 'seen':
   [
      "<uid>", ...
   ]
"""

def handle(sender, req, database, logger):
	# Translate coordinates
	# x =  cos(a)x + sin(a)y
	# y = -sin(a)x + cos(a)y

	# if y > x^2 -> robot in sight

	closest = [None, None]
	UID = ""
	loc = database.gete(sender, "loc")

	for ID, robot in database.database:
		x, y = translate(robot["loc"], robot["angle"])
		if y > (x**2) + (loc[0]*x) + loc[1]:
			if (closest[0] > x or closest[0] == None) and \
			   (closest[1] > y or closest[1] == None):
				closest[0] = x
				closest[1] = y
				UID = ID

	return UID
