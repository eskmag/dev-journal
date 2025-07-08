import os

# loop throug files in a folder
for filename in os.listsdir("."):
  if os.path.isfile(filename):
    print(f"Found file {filename}")
    

# read and write to a file
with open("input.txt", "r") as f:
  content = f.read()
  
with open("output.txt", "w") as f:
  f.write("Hello World!")
 