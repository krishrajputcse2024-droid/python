
# Write a program using functions to find greatest of three numbers.

'''def greatest(a , b , c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
print(greatest(a , b , c))'''
    
    
    
    
    
    # Write a python program using function to convert Celsius to Fahrenheit.
'''def conver_to_celsius(cel):
   return (cel*9/5) + 32
cel = int(input("enter a temperature: "))
print(conver_to_celsius(cel))'''




# How do you prevent a python print() function to print a new line at the end.
'''print("hello" ,end=" ")
print("world")'''


# . Write a recursive function to calculate the sum of first n natural numbers
'''def num(n):
    if(n==0):
        return 0
    return num(n-1) + n
n = int(input("Enter a Number:"))
print(num(n))'''





# . Write a python function to print first n lines of the following pattern.
# ***
# **
# *
# - for n = 3
# #


'''def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)'''



# Write a python function which converts inches to cms

'''def inch_to_cms(inch):
    return inch*2.54
n = int(input("enter a number : "))
print(inch_to_cms(n))'''




# Write a python function to print multiplication table of a given number.
'''def multiplication(n):
    for i in range(1 , 11):
        print(n ,"x" ,i ,"=",n*i)
        n= int(input("Enter a Number:"))
        multiplication(n)'''
        