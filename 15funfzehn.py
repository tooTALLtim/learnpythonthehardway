#this line pulls my argument variable (argv) from the command line input from the user
from sys import argv

#here is where I define the argument variable with the name of the script I'm running
#and defining that argument variable from the command line as 'filename'
script, filename = argv

#I'm making the variable 'txt' equal to using the command 'open()' to act on the variable 'filename'
#open is a command that takes a parameter and returns the value, in this case 'filename'
txt = open(filename)

#Now I make a format string that returns the filename that is being opened
print(f"Here are the contents of your file {filename}:")
#And this line uses the command 'read()' to open and display the contents of txt which was determined earlier
#Hey 'txt' do the 'read' command with no parameters!
print(txt.read())
txt.close()

#taking input from the user in the script I've written
#we could open any file this way
print("Type the filename again if you would: ")
file_again = input("\t>>>> ")

#defining the variable 'txt_again' to open the 'file_again' from the user input
txt_again = open(file_again)

#boom! telling 'txt' to do the 'read' command again with no parameters
print("Ok, here is the text in your file again!")
print(txt_again.read())
txt_again.close()

#just a little extra for funzies
happiness = input("Are you satisified with our progress? \n\t>>> ")
print("We truely hope that '{}' is what you were going for!".format(happiness))