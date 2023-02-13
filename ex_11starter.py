#!/usr/bin/python

belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# 1. Print a line of hyphens the same length as the Belgium string:
print(['-' for i in belgium])

# 2. Print with commas replaced with colons:
print(belgium.replace(',',':'))

# 3. Print population of Belgium plus pop. of Brussels:
#Split string to make a list using ',' to separate list items
belgium_list = belgium.split(',')
belgium_pop = int(belgium_list[1])
brussels_pop = int(belgium_list[3])
print(belgium_pop + brussels_pop)
