from itertools import imap, islice, izip
from visual import color, rate, scene, sphere, vector

scene.center = (0.1, 1, 0)
scene.forward = (-1, 0, -3)
scene.fullscreen = True
scene.scale = (0.5, 0.5, 0.5)
scene.title = "Space Carving"

def main(r):
	try:
		points = []
		spheres = []
		current = most = 0

		while True:
			if most > 0:
				rate(most * 25)

			line = raw_input()
			
			if line == "" or line == "\n":
				for i in xrange(current, most):
					spheres[i].visible = False

				for s, p in izip(islice(spheres, current), islice(points, current)):
					s.pos = vector(p)
					s.visible = True
					
				current = 0

			else:
				point = tuple( imap(float, line.split()) )

				if current >= most:
					spheres.append( sphere(radius = r, color = color.white, visible = False) )
					points.append(point)
					most += 1

				else:
					points[current] = point
				
				current += 1

	except EOFError:
		return

if __name__ == "__main__":
	from sys import argv
		
	if len(argv) == 2:
		main(float(argv[1]) / 2)

	else:
		print("usage: " + argv[0] + " sphere_diameter")