import os
#Goes through all the files in current directory, assumes script lies next to files
dir = os.listdir(os.getcwd())

inp = ""
while (inp == ""):
	inp = str(raw_input("Enter characters to search for: ")).replace("\n", "")

#Create output file
with open('__output.txt', 'w') as o:
	for filename in dir:
		#Check whether current file is not self, not output file and not a directory
		if not os.path.isdir(filename) and filename != "find_files_with_unequal_counts.py" and filename != "__output.txt":
			with open(filename, 'U') as f:
				content = f.read()
				count = content.count(inp[0])
				for c in inp:
					if count != content.count(c):
						print("unequal count in " + filename)
						o.write(filename + '\n')
		#File is self
		else:
			print "Encountered self, skipping."
raw_input("Press enter to exit the script.")