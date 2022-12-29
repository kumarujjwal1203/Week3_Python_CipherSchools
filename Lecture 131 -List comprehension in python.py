#List Comprehension **IMPORTANT**
# create a list of squares from 1 to 10
l = []
for i in range(1,11):
    l.append(i**2)
print(l)



# by list comprehension
l2 = [i**2 for i in range(1,11)]


l3=[]
for i in range(1,11):
    l3.append(-i)
print(l3)


#by list comprehension
l3l=[-i for i in range(1,11)]
print(l3)

names = ['Sandarbh' , 'Mohit' , 'Rohit']
#new_list = ['S','M','R']
new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)

#list comprehension use krkr
new_list2 = [name[0] for name in names]
print(new_list2)