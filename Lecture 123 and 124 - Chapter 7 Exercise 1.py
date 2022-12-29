def cubefinder(n):
    cube = {}
    for i in range(1,n+1):
        cube[i]= i**3
    return cube

print(cubefinder(10))