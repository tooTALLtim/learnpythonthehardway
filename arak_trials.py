artifact_dict = {
    'goblet' : '''It is a strange fate that we should suffer so much fear 
    and doubt over so small a thing … such a little thing.''',
    'horn' : 'The wise speak only of what they know.',
    'necklace' : """Into his heart, the thought will not enter that any will
    refuse it — that having the Ring we may seek to destroy it. 
    If we seek this, we shall put him out of reckoning.""",
    'scroll': 'Gandalf, my old friend this will be a night to remember.'
    }


usr_list = []

the_answer = ['speak', 'friend', 'and', 'enter']

inscriptions_found = artifact_dict.values()
print(inscriptions_found)

for words in inscriptions_found:
    print("works?")
    usr_list.extend(words.split(" ")) # The split function makes a list!
    print(usr_list)

print("user words:", usr_list)
print("the answer list:", the_answer)
have_correct_words = any(ele in usr_list for ele in the_answer)
print("Does user have some correct words?", have_correct_words)

if have_correct_words == True:
    print("""Eagle: \"You do have part of the code!
    The following words are indeed part of the code:\"
    """)
    res = [i for i in usr_list if i in the_answer]
    print(res)
    print("Eagle: \"Now it's up to you to find the rest... and the correct order!\"")
else:
    print("Eagle: \"Hmmm, none of those words are in the code, keep looking!")




# This works!!!!!

# the_answer = ['speak', 'friend', 'and', 'enter']

# print("""
# Eagle: \"Ok, what words have you found so far?
# Make sure you put a space between the words.\"
# """)

# words_found = input(">>>>> ")

# usr_list = words_found.split(" ") # The split function makes a list!

# print("user words:", usr_list)
# print("the answer list:", the_answer)
# have_correct_words = any(ele in usr_list for ele in the_answer)
# print("Does user have some correct words?", have_correct_words)

# if have_correct_words == True:
#     print("""Eagle: \"You do have part of the code!
#     The following words are indeed part of the code:\"
#     """)
#     res = [i for i in usr_list if i in the_answer]
#     print(res)
#     print("Eagle: \"Now it's up to you to find the rest... and the correct order!\"")
# else:
#     print("Eagle: \"Hmmm, none of those words are in the code, keep looking!")