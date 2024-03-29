import os
import re
#SCRIPT IS OPTIMIZED FOR MAPGEN STATES, CHANGE SYNTAX IF STATES WERE NOT GENERATED BY MAPGEN
#Used file name syntax: "1234-State_1234"
#Used state name syntax: "STATE_1234"
#1234 = ID
#Goes through all the files in current directory, assumes script lies next to files
dir = os.listdir(os.getcwd())
x = raw_input("State ID to delete: ")
for filename in dir:
	#Check whether current file is not self
	if filename != "deletestate.py":
		file = open(filename)
		for item in file.read().split("\n"):
			if "id=" in item:
				#ID of state
				id = int(re.search(r'\d+', item).group())
				#ID of state - 1
				id_new = id - 1
				#Found ID of to be deleted state
				if id == x:
					file.close()
					os.remove(file.name)
				#Found ID smaller than desired ID, new ID needed
				elif id > x:
					print item
					file.close()
					#Reading and replacing of state ID and name, watch out for the syntax if in need of change
					newText = open(filename, 'U').read().replace('id=' + str(id), 'id=' + str(id_new)).replace('name="STATE_' + str(id), 'name="STATE_' + str(id_new))
					open(filename, "w").write(newText)
					#Renaming of state file, watch out for the syntax if in need of change
					os.rename(filename, str(id_new) + "-State_" + str(id_new) + ".txt")
				else:
					print "ID not equals or smaller. File " + filename + " not deleted or changed."
			else:
				print "Line is not ID line."
	#File is self
	else:
		print "Encountered self, skipping."
raw_input("Press enter to exit the script.")