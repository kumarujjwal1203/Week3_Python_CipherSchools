s = {'a','b','c'}
if 'a' in s:
    print("'Present")
else:
    print("Not Present")

#using for loop
for items in s:
    print(items)

l=[1,2,3,3]
s1 = list(set(l))
print(s1)

#set math
s1l = {1,2,3,4}
s2 = {3,4,5,6}
union_set = s1l | s2
print(union_set)
intersection_set = s1l & s2
print(intersection_set)