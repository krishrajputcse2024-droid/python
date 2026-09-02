# muliplication of number usng for loop
# n = int(input("enter a number"))
# for i in range(1,11):
#     print( n," x",i, "=",n*i)




# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul","shubham"]
# for name in l:
#   if name.startswith("S"):
#     print("hello",name)




# n = int(input("enter a number: "))
# i=1
# while i<=10:
#     print(n ,"x",i ,"=", i*n)
#     i = i+1



# prime or not
# n = int(input("enter a number: "))
# for i in range(2,n):
#     if n%i==0:
#         print("not a prime no")
#         break
# else:
#         print("prime number")



# n = int(input("enter a number : "))
# fact = 1
# for i in range(1, n+1):
#     fact=fact*n
#     print("fact", fact)







# n = int(input("Enter number: "))

# i = 1
# total = 0

# while i <= n:
#     total += i
#     i += 1

# print("Sum =", total)





''' 
  *
 ***
*****
for n = 3
'''


'''n = int(input("enter a number: "))
for i in range(1,n+1):

  print(" "*(n-i),end ="")
  print("*" *(2*i-1) , end="")
  print("\n")
  '''
  
  
  
'''n = int(input("enter a number:"))
for i in range(1,n+1):
    print(""*(n-1),end="")
    print("*"*i, end="")
    print("\n")'''
    
    
n = 3

for i in range(1, n + 1):
    if i % 2 != 0:      # odd row
        print("* " * n)
    else:               # even row
        print("* " * (n - 1))