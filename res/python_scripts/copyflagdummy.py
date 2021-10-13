import os
import shutil
x = raw_input("TAG's seperated by spaces: ")
#Seperation char
data = x.split(' ')
#Name of dummy flag file
srcfile = os.getcwd() + "\dummy.tga"
print srcfile
for tag in data:
	#Construction of the copied file's name
	desfile = os.getcwd() + "\\" + tag + ".tga"
	shutil.copy(srcfile, desfile)
raw_input("Press enter to exit the script.")