f = open("demofile1.txt", "w+")
f.write("My Name is Liam")
f.close()

#open and read the file after the appending:
f = open("demofile1.txt", "r")
print(f.read())