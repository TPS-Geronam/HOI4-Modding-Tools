# HOLY FUCK THIS SCRIPT IS UGLY

import os
import re
#Goes through all the files in current directory, assumes script lies next to files
dir = os.listdir(os.getcwd())
#Create output file
with open('__output.txt', 'w') as o:
	for filename in dir:
		#Check whether current file is not self, not output file and not a directory
		if not os.path.isdir(filename) and filename != "find_non_commented_events.py" and filename != "__output.txt":
			with open(filename, 'U') as f:
				lines = f.read().splitlines()
				
				# line index
				i = 0
				# used for determining how many lines we should skip, since country_event could also be an effect
				skip = 0
				for l in lines:
					if skip == 0 and re.match(r'\bcountry_event\b', l) != None:
						# country_event = { #Event Comment
						if "#" in l:
							pass
						# #Event Comment
						# country_event = {
						elif i - 1 >= 0 and "#" in lines[i - 1]:
							pass
						else:
							j = i
							ln = l
							# as long as line does not contain the id-line
							while re.match(r'\s*id\s*=', ln) == None:
								j += 1
								# reached end of file or next event means we found no id
								if j > len(lines) or re.match(r'\bcountry_event\b', lines[j]) != None or re.match(r'\bnews_event\b', lines[j]) != None:
									print("No event id for country event at line " + str(i) + " in " + filename + " found. Fix this first.")
									break
								ln = lines[j]
							# id = event.0 #Event Comment
							if not "#" in ln:
								ln = re.sub(r'id\s*=\s*', "", ln)
								ln = re.sub(r'\s*', "", ln)
								o.write(ln + '\n')
								print(ln + '\n')
					
					if skip == 0 and re.match(r'\bnews_event\b', l) != None:
						if "#" in l:
							pass
						elif i - 1 >= 0 and "#" in lines[i - 1]:
							pass
						else:
							j = i
							ln = l
							while re.match(r'\s*id\s*=', ln) == None:
								j += 1
								if j > len(lines) or re.match(r'\bcountry_event\b', lines[j]) != None or re.match(r'\bnews_event\b', lines[j]) != None:
									print("No event id for news event at line " + str(i) + " in " + filename + " found. Fix this first.")
									break
								ln = lines[j]
							if not "#" in ln:
								ln = re.sub(r'id\s*=\s*', "", ln)
								ln = re.sub(r'\s*', "", ln)
								o.write(ln + '\n')
								print(ln + '\n')
					
					skip += l.count("{")
					skip -= l.count("}")
					
					i += 1
		#File is self
		else:
			print "Encountered self, skipping."
input("Press enter to exit the script.")
	