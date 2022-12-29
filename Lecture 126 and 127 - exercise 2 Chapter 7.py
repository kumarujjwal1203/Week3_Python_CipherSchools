user = {}
name  = input('What is your name: ')
age = input('What is your age: ')
favmovies = input("What is your fav movie: ")
favsongs = input('What is your favsong: ')
user['name'] = name
user['age'] = age
user['favmovie'] = favmovies
user['favsongs'] = favsongs
print(user)
#to print in diff line
for key ,  value in user.items():
    print(f'{key}:{value}')