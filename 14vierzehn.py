from sys import argv

script, user_name = argv
prompt = "Type your anwer here please >>> "

print(f"Hi {user_name}, I'm the {script} script.")
print("I am programmed to ask you a few questions.")
print(f"What do you think about me {user_name}?")
likes_us = input(prompt)

print(f"Where are you currently located {user_name}?")
print("(Don't worry, we won't send the nukes.)")
location = input(prompt)

print(f"Finally, {user_name} what is your favourite type of activity?")
print("It could be", " climbing " * 10)
activity = input(prompt)

print(f"""
Alright, so you you said you think {likes_us} about me.
You're currently located in {location}. I'll let you know next time I'm in {location}.
And you really like to go {activity}, that's cool! I thought it would be {activity}.
""")