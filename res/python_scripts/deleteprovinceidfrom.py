x = raw_input("Province ID's seperated by spaces: ")
#Seperation char
data = x.split(' ')
for id in data:
  #Source file, assumes that script lies next to source file
  #Deletes given ID's from source file
  with open("1-World.txt", 'U') as f:
	#Assumes Province ID's are present in the ' 1234 5678 91011 ' format (every ID has a space in front and behind of itself)
    newText = f.read().replace(' ' + id + ' ', ' ')
  with open('1-World.txt', "w") as f:
    f.write(newText)
input("Press enter to exit the script.")