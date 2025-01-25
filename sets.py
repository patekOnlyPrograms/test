set_of_evens = {0,2,4,6,8,10}
set_of_evens.add(12)
print(set_of_evens)

null_set = {}
print(type(null_set))
null_set = set()
print(type(null_set))

print('0 in evens: ', 0 in set_of_evens)
print('1 in evens: ', 1 in set_of_evens)

#two sets
evens = {0, 2, 4, 6, 8}
odds = {1, 3, 5, 7, 9}

#Union
#The union of two sets A and B is the set containing all the elements of A and B
print(evens | odds)

#Intersection
#The intersection of two sets A and B is the set containing elements present in both A and B
print(evens & odds) #returns nothing

#Difference & relative complement
#Difference of two sets A and B denoted A - B is the set that contains all elements present in A but not in B
print(evens - odds)
