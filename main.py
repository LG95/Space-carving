from functools import reduce
from numpy import arange, mat
from PIL import Image

def main(d):	
	cameras = []

	for i in range(1, 9):
		filename = "calibration/Camera" + str(i) + ".Pmat.cal"
		camera = []

		try:
			with open(filename, "r") as file:
				for line in file:
					camera.append( map(float, line.split()) )

			cameras.append( [mat(camera), None] )

		except IOError:
			print(filename + " could not be read.")

	for k in range(175):
		points = []

		for i in range(8):
			imagename = "silhouettes/Silhouette" + str(i + 1)
			imagename += "_" + "{:04d}".format(k) + ".png"
				
			try:
				cameras[i][1] = Image.open(imagename).load()

			except IOError:
				print(imagename + " could not be read.")

		for x in arange(-1, 1, d):
			for y in arange(0, 2, d):
				for z in arange(-1, 1, d):
					camera = iter(cameras)
					hit = True

					try:
						while hit:
							pmatrix, image = next(camera)
							p = pmatrix * mat( (x, y, z, 1) ).transpose()
							u, v, w = p[0, 0], p[1, 0], p[2, 0]
							u, v = int(u / w), int(v / w)

							if 0 <= u < 1600 and 0 <= v < 1200:
								hit = image[u, v] > 0

					except StopIteration:
						points.append( (x, y, z) )

		for point in points:
			print( reduce(lambda p1, p2: str(p1) + " " + str(p2), point) )
		print("")

if __name__ == "__main__":
	from sys import argv
		
	if len(argv) == 2:
		main( float(argv[1]) )

	else:
		print("usage: " + argv[0] + " distance")