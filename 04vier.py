ropes = 20
space_in_a_backpack = 2
leaders = 4
noobs = 20
climbers_total = leaders + noobs
ropes_we_need = climbers_total / leaders

print("There are", leaders, "leaders with us today")
print("We have", noobs, "noobs that want to climb with us.")
print("Oh, and we only have", ropes, "ropes.")
print("So if we have a total of", climbers_total, "climbers total with us today.")
#not really true, unless this is a guided expedition! :P
print("Then we'll need", ropes_we_need, "ropes because we only have", leaders, "leaders today.")
