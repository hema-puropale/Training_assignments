# Reading
file=open("example.txt","r")
content=file.read()
print(content)
file.close()

# Writing
file=open("example.txt","w")
file.write("Hello world \n")  # replacing the existing text with new text
file.close()

# Appending
file=open("example.txt",'a')
file.write("Nice to see you all")  # It will add text additional to existing text
file.close()

# checking (file exists or not)
import os
if os.path.exists("example.txt"):
    print('FILE EXISTS')
else:
    print('FILE DOES NOT EXISTS')