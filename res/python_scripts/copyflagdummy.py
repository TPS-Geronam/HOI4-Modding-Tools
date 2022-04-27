import os
import shutil

def main():
	x = raw_input("TAG's seperated by spaces: ")
	#Seperation char
	data = x.split(' ')
	#Name of dummy flag file
	srcfile = os.getcwd() + "\dummy.tga"
	for tag in data:
		desfile = f"{os.getcwd()}\\{tag}.tga"
		shutil.copy(srcfile, desfile

if __name__ == "__main__":
	main()
