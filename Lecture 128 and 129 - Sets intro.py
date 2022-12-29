s = {1,2,3}#unordered collection of unique items
print(s)#indexing is not allowed
l=[1,2,3,4,5,5,5,6,7,7,8]
#if u want to remove the duplicate numbers from this list
s2 = list(set(l))
print(s2)
# if u want to add an item to your set
s.add(4)
s.add(5)
print(s)
#to remove something from set
s.remove(3)
print(s)
#key error will come if u try to remove something which is not present in set
s.discard(3)
print(s)
#isme key error nahi aayega even if the element is not present in the set
s.clear()
print(s)
s1=s.copy()
print(s1)
s={1,1.0,2.3,"string"}#list and dictionary cannot be stored in a set
print(s)# 1 and 1.0 is same for a set