import os
#Goes through all the files in current directory, assumes script lies next to files
dir = os.listdir(os.getcwd())
for filename in dir:
	#Check whether current file is not self
	if filename != "replacestatetype.py":
		with open(filename, 'U') as f:
			newText = f.read()
			#Find all '}' characters
			k = newText.rfind("}")
			#Replace last '}' with "\tstate_category = rural\n}"; "\t" equals a tab, "\n" equals a new line
			new_string = newText[:k] + "\tstate_category = rural\n}" + newText[k+1:]
		with open(filename, "w") as f:
			f.write(new_string)
	#File is self
	else:
		print "Encountered self, skipping."
input("Press enter to exit the script.")