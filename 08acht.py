#this is a string with 
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I sure like to eat chocolate!",
    "I wonder how my twisted ankle will feel today",
    "I sure like kissing Jasmyn!!",
    "Coding, this is the way."
))

#let's try this again
#maybe easier to see how this works without a variable that is "formatter"
#ok, so I can reduce the number of {} in the string and it'll only pass that number
#of arguments. But if I have too many (five or more) then that breaks it
argylesocks = "{} {} {} {}"

#passes the following arguments into the {} of the string
print(argylesocks.format(1, 2, 3, 4))
print(argylesocks.format("eins", "zwei", "drei", "vier"))
print(argylesocks.format(True, False, False, True))

#so if no argument is passed to the string then it just treats the "" literally
print(argylesocks.format(argylesocks, argylesocks, argylesocks, argylesocks))

#typing it this way makes it cleaner, and allows it to be collapsable!
#turns out that the code doesn't care if it's on different lines, but 
#the commas tell it what's up!! spaces don't count
print(argylesocks.format(
    "Ich mochete das Gelt!",
    "Was ist das Wetter heute?",
    "Ich spreche ein bisschen Deutsch.",
    "Das Badezimmer ist hell, ich mag nicht!"
))