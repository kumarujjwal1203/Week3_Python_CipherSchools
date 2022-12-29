l=['abc','tuv','xyz']
l2 = [(l[0][::-1],l[1][::-1],l[2][::-1]) for i in l]
print(l2)