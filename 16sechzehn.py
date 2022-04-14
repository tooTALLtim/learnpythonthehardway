from sys import argv

script, filename = argv

print(f"Now, instead of erasing data from {filename} let's simply add to it using append!")
# must put the '+' after the 'a' otherwise it won't read the file!
target = open(filename, "a+")

print("What would you like to be recorded in the annals of time?")
line1 = input(">>> ")
line2 = input(">>> ")
line3 = input(">>> ")

print(f"Cool cool, that's some good stuff! I'll write {line1}, {line2}, and {line3} into {filename} at the end.")
print("Gimme a second...\n\ndone!\n\n")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n\n")

print(f"I'm just going to check if {filename} is readable. Hey computer, is this True?")
print(target.readable())
print("Ah, that's good.")
input("Are you ready to open the file? Hit RETURN when you're ready or Ctrl-C if you want to end.")

# use seek() to go to the beginning of the file using '0' or it will just return blank
# since it's at the end of the file!
target.seek(0)
print("\nGood, So what's in the file now?")
print(target.read())

print(f"Ok, and let's not forget to close {filename}!\n")
target.close()
print(".....>>>>>closed<<<<<.....")



# # take the argument variable from the command line
# from sys import argv

# # define the argument variable using the name of the script we're running an the input after that
# script, filename = argv

# print(f"We're going to erase filename {filename}.")
# print("If you don't want that to happen hit Ctrl-C (^C).")
# print("If you want to proceed, hit RETURN.")

# input("????????")

# print("Opening that file...")
# # defining the variable 'target' to use the function 'open' on 'filename'
# # the 'w' is crucial or python won't be able to edit 'filename'
# target = open(filename, "w")

# print("Truncating the file, seeya data!")
# # the 'truncate' command erases the data in the file
# target.truncate()

# print("Now let's put some data back in there. Let's add three lines")

# line1 = input("line one shall be: ")
# line2 = input("and now for line two: ")
# line3 = input("finally, line drei: ")

# print(f"I'll go ahead and write these lines into {filename} for you.")

# # this is the orignal way the lesson teaches, now Zed commands optimization!
# # target.write(line1)
# # target.write("\n")
# # target.write(line2)
# # target.write("\n")
# # target.write(line3)
# # target.write("\n")

# # >>>optimization<<<
# # this will only work with '+' between, as ',' between them are passed as multiple arguments and
# # the 'write()' function will only accept one argument! The '+' tells the 'write()' command
# # to view this as one argument that has multiple...parts?
# target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# print(f"And let's do the right thing and close {filename}.")
# target.close()