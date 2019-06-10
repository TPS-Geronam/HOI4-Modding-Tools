import os

#Goes through all the files in current directory, assumes script lies next to files
dir = os.listdir(os.getcwd())
for filename in dir:
	#Declare string, to be used later
	finalstring = filename[:3] + " = {\n\t"
	#Check whether current file is not self
	if filename != "religionscrapper.py":
		with open(filename, 'r') as f:
			#Check content of file line by line
			for line in f:
				#Check if line contains religion idea
				if "religion_" in line:
					rline = line.replace('	', '').replace(' ', '')[:-1]
					#Check for the special case of catholic->catholicism
					if "catholic" in rline:
						rline = rline.replace('catholic', 'catholicism')
					#Construct final string for the current file
					finalstring = finalstring + "add_to_array = { national_religion_array = global." + rline + " }\n}"
		#Create output file if it doesn't exist and append current final string as a new line(s)
		with open('__output.txt', 'a') as f:
			f.write(finalstring + "\n")
	#File is self
	else:
		print "Encountered self, skipping."
input("Press enter to exit the script.")
