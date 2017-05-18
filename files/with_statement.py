#For quick reading or writing use with. It's not necessery to call the close() function.
with open("example.txt", "a+") as file:
    #Bringing the pointer to the starting point
    file.seek(0)
    #reading the content
    content = file.read()
    file.write("Line 4")
