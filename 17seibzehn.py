#modifying the base lesson 
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")
original = (open(from_file)).read()

print(f"The input file is {len(original)} bytes long.")
print(f"Does the output file exist? {exists(to_file)}")
print("Hit RETURN to continue or Ctrl-C to abort.")
input("???")

open(to_file, 'w').write(original)

print("Alright, all done!")

# Zed says these are already closed by Python
# original.close()
# to_file.close()



# original lesson
# from sys import argv
# from os.path import exists

# script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}.")
# in_file = open(from_file)
# indata = in_file.read()

# print(f"The input file is {len(indata)} bytes long.")
# print(f"Does the output file exist? {exists(to_file)}")
# print("Hit RETURN to continue or Ctrl-C to abort.")
# input("???")

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print("Alright, all done!")

# out_file.close()
# in_file.close()