### FILE HADLING #############
## File OPen
""""
Use open() to manipulate files. Open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
===================================================================
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""
#### apending reading
f = open('learn.txt', 'a')
f.write('material: Some learning material here\n')
f.close()
#### reading as text
f = open('learn.txt', 'rt')
#print(f.read())
""" read() method can take an int to specify how many chars to read e.g."""
#print(f.read(10))
#### reading as binary
f = open('learn.txt', 'rb')
#print(f.read())
### Reading single line
""" use readline() to return a single line from the file """
f = open('learn.txt', 'rt')
print(f.readline())
print(f.readline())
print(f.readline())

print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

####  print by looping
f = open('learn.txt', 'rt')
for material in f:
    print(material)
f.close()

print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
##### Deleting Files
""" import OS module to delete files """
import os
f = open('demo.txt', 'x')
f.close()
os.remove("demo.txt")
print ('file deleted')
print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
#### Check if file exisits
if os.path.exists('learn.txt') :
    print ('file exists')
else:
    print ('file not found ')

##### Deleting folders
"""" use os.rmdir("myfolder") to delete folders """


