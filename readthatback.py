from sys import argv

script, filename = argv
txt = open(filename)

print("Here's what I found in your file {}:".format(filename))
print(f"\n\t>>>>>>{filename}<<<<<<\n")
print(txt.read())
print("\n\nDon't forget to close the file!")
print("." * 20, ">>>closed<<<", "." * 20, "\n\n")
txt.close()