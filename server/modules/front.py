import math

def translate(coords, angle):
	x = (math.cos(angle) * coords[0]) + (math.sin(angle) * coords[1])
	y =(-math.sin(angle) * coords[0]) + (math.cos(angle) * coords[1])
	return (x,y)


def handle(sender, req, database, logger):
	# Translate coordinates
	# x =  cos(a)x + sin(a)y
	# y = -sin(a)x + cos(a)y

	# if y > x^2 -> robot in sight

	robots = []

	for ID, robot in database.database:
		x, y = translate(robot["loc"], robot["angle"])
		if y > x**2:
			robots.append(ID)

	return robots
