# A list containing the justice league members
justice_league= ['Superman','batman','wonderwoman','Flash','Aquaman','Green Lantern']
#Get the size of the list 
league_size = len(justice_league)
print(league_size)
#add two members to the list
justice_league.extend(['batgirl', 'nightwing'])
print(justice_league)

#Wonder woman becomes the leader of the group, move her to the first position in the list
# First Find the index of 'wonderwoman'
index = justice_league.index('wonderwoman')

# Then Remove 'wonderwoman' from the list
wonderwoman = justice_league.pop(index)

# Finally, Insert 'wonderwoman' at the beginning of the list
justice_league.insert(0, wonderwoman)

print(justice_league)

# to Move green lantern between flash and aquaman, first Find the index of 'Green Lantern'
index = justice_league.index('Green Lantern')

# Remove 'Green Lantern' from the list
green_lantern = justice_league.pop(index)

# Insert 'Green Lantern' between 'Aquaman' and 'Flash'
justice_league.insert(4, green_lantern)

print(justice_league)

# Replace the old team with the new members
justice_league = ['cyborg', 'shazam', 'hawkgirl', 'martian manhunter', 'green arrow']
#sort the justice league alphabetically 
justice_league.sort()
#leader is the first member of the list= cyborg
print(justice_league)
