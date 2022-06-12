artifact_dict = {
    'goblet' : 'It is a strange fate that we should suffer so much fear and doubt over so small a thing … such a little thing.',
    'horn' : 'The wise speak only of what they know.',
    'necklace' : """Into his heart, the thought will not enter that any will refuse it — that having the Ring we may 
    seek to destroy it. If we seek this, we shall put him out of reckoning.""",
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






# # Not the correct order
# print("Eagle: \"which words are correct?\"")
# if (words_found & str(the_answer)):
#     print(words_found & the_answer)
# else:
#     print("that's not in there")

# def compare(this, that):
#     this_set = set(this)
#     that_set = set(that)

#     if (this_set & that_set):
#         print(this_set & that_set)
#     else:
#         print("that isn't in there")

# compare(the_answer, usr_list)














# for have_correct_words in the_answer:
#     try:
#         if 'speak' in usr_list:
#             print("speak")
#         elif 'friend' in usr_list:
#             print('friend')
#         elif 'and' in usr_list:
#             print('and')
#         elif 'enter' in usr_list:
#             print('enter')
#         else:
#             print("that word isn\'t in the answer")
#     except:
#         ValueError




# doesn't work, but getting warmer
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

# print("Eagle: \"which words are correct?\"")
# if have_correct_words == True:
#     print("""
#     Eagle: \"Looks like you do have some of the code!
#     Let me help you put the words that you have in order.\"
#     """)
#     for ele in the_answer:
#         ele in usr_list
#         print(f"{ele} is correct!")
#     else:
#         print(f" {ele} is not part of the code")
# else:
#     print("no correct words")




# for ele in y in the_answer:
#     print(ele in the_answer)



# x = input('what words do you have?\n>>>>> ')
# y = x.split(" ")
# empty_list = []
# empty_list.append(y)
# print(empty_list)

# contains!!!!

# for thing in the_answer:
#     print(the_answer)