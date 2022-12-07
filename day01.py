'''
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
'''

# elves are seperated by blank line
# divide elve inventories into list where each item is an inventory
# for each item in the list (inventory)
# convert item string to list of floats
# sum up floats and add to new list
# exit for loop - new list will have sum of calories for each elf
# find greatest item in this list (how?)
# this is solution!

import fileinput

all_inventories = open('day01-input.txt').read()
sums = []

inventories_list = all_inventories.split('\n'*2)
for i in inventories_list:
  individual = i.split('\n')
  calories = [float(n) for n in individual] # now have list of calories for each individual elf
  sums.append(calories.sum())
  
print(sums.max())
  
    
