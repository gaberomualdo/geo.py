def distance(x,y):
	return ((abs(x[0] - y[0]) ** 2) + (abs(x[1] - y[1]) ** 2)) ** 0.5

def midpoint(x,y):
	return [(x[0] + y[0]) / 2, (x[1] + y[1]) / 2]

def pythagorean_theorem(leg1, leg2):
	return ((leg1 ** 2) + (leg2 ** 2)) ** 0.5

def verify_righttriangle(point1, point2, point3):
	side1 = distance(point1, point2)
	side2 = distance(point1, point3)
	side3 = distance(point2, point3)

	leg1 = 0
	leg2 = 0
	for side in [side1, side2, side3]:
		if(side > leg1):
			leg2 = leg1
			leg1 = side
		elif(side > leg2):
			leg2 = side
	for side in [side1, side2, side3]:
		if(leg1 != side and leg2 != side):
			print side
			return pythagorean_theorem(leg1, leg2) == side