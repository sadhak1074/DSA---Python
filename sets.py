# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(Set)

print("\nElements of set: ")

for i in Set:
    print(i, end=" ")
    
#frozen sets
frozen_set = frozenset([1, 2, 3, 4, 5])
print("\nFrozen Set is: ", frozen_set)
