from itertools import islice

def main(r):
	try:
		points = []
		current = frame = most = 0

		while True:
			line = raw_input()
			
			if line == "" or line == "\n":
				frame += 1

				with open(str(frame) + ".txt", "w") as file:
					for point in islice(points, current):
						file.write(point + "\n")

				current = 0

			else:
				if current >= most:
					points.append(line)
					most += 1

				else:
					points[current] = line
				
				current += 1

	except EOFError:
		return

if __name__ == "__main__":
	from sys import argv
		
	if len(argv) == 2:
		main(float(argv[1]) / 2)

	else:
		print("usage: " + argv[0] + " sphere_diameter")
