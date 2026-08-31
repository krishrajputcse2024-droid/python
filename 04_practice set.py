# WAP to input 8 numbers from a user and display all unique number 
"""""s = set()
n = input("enter a number : ")
s.add(int (n))
n = input("enter a number : ")
n = input("enter a number : ")
n = input("enter a number : ")
n = input("enter a number : ")
n = input("enter a number : ")
n = input("enter a number : ")
print(s)"""


#what is length od these
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))



#create an empty dict allow 4 friends to enter thier fav language as value and use kets as thier name 
d ={}
name = input("enter a name :  ")
movie = input("enter a movie")
d.update({name: movie})
name = input("enter a name :  ")
movie = input("enter a movie")
d.update({name: movie})
name = input("enter a name :  ")
movie = input("enter a movie")
d.update({name: movie})
name = input("enter a name :  ")
movie = input("enter a movie")
d.update({name: movie})
name = input("enter a name :  ")
movie = input("enter a movie")
d.update({name: movie})
print(d)