import os
#Goes through all the files in current directory, assumes script lies next to files
dir = os.listdir(os.getcwd())
for filename in dir:
	#Check whether current file is not self
	if filename != "replacemanpower.py":
		with open(filename, 'U') as f:
			#Replacing 'manpower=0' with 'manpower=100000'; usage: replace('original string', 'replaced string')
			newText = f.read().replace('manpower=0', 'manpower=100000')
		with open(filename, "w") as f:
			f.write(newText)
	#File is self
	else:
		print "Encountered self, skipping."
input("Press enter to exit the script.")