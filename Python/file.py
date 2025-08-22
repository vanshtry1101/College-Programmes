file1 = open( "file1.txt", "w")
file1.write("Hello, World!\n")
file1.write("This is a file.\n")
file1.write("Hello Bugga \n")
file1.close()

file1 = open("file1.txt", "r")
data = file1.read()
file1.close()

file2 = open("file2.txt", "w")
file2.write(data)
file2.close()