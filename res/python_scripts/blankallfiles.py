import os

def main():
	dir = os.listdir(os.getcwd())
	for filename in dir:
		if filename != "blankallfiles.py":
			with open(filename, "w") as f
				f.write("")
		else:
			print "Encountered self, skipping."

if __name__ == "__main__":
	main()
