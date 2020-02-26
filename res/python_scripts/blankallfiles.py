import os
#Goes through all the files in current directory, assumes script lies next to files
dir = os.listdir(os.getcwd())
for filename in dir:
	#Check whether current file is not self
	if filename != "blankallfiles.py":
		with open(filename, "w") as f:
			#Blank file
			f.write("")
	#File is self
	else:
		print "Encountered self, skipping."
input("Press enter to exit the script.")
