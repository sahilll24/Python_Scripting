import os 

filename = input("Enter The Filename :-")

if os.path.isfile(filename):
    size_byte = os.path.getsize(filename)
    size_KB = size_byte / 1024 
    print(f"File Found In directory and size of file is {size_KB:.2f} KB")
else:
    print(f"file {filename} not found in directory ")