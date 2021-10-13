import os
import re
#Goes through all the files in current directory, assumes script lies next to files
dir = os.listdir(os.getcwd())
#Create output file
with open('__output.txt', 'w') as o:
	for filename in dir:
		#Check whether current file is not self, not output file and not a directory
		if not os.path.isdir(filename) and filename != "find_empty_used_loc_keys.py" and filename != "__output.txt":
			with open(filename, 'U') as f:
				lines = f.read().splitlines()
				reg = re.compile("(:(.) *\"( *)\")")
				for l in lines:
					if reg.findall(l) != []:
						o.write(l + '\n')
						print(l)
		#File is self
		else:
			print "Encountered self, skipping."
raw_input("Press enter to exit the script.")