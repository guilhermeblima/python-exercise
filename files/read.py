# opens the file for reading - r - read - w - write - a -append
file = open("example.txt", "r")
# reads the full content, all lines at once and saves as a string
content = file.read();
print(content)
#return the reading pointer to the beginning of the file
file.seek(0)
# reads the line and stores as a list
content = file.readlines()
print(content)
#Get rid of the "\n" in each item of the list
content = [i.rstrip("\n") for i in content]
print(content)
#Closes the file, otherwise the file wont be accessible
file.close()
