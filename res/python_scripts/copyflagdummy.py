import os
import shutil

def main():
	tags = input("TAGs separated by spaces: ")
	#Separation char
	data = tags.split(" ")
	#Name of dummy flag file
	srcfile = "./dummy.tga"
	for tag in data:
		desfile = f"./{tag}.tga"
		shutil.copy(srcfile, desfile)

if __name__ == "__main__":
	main()
	
