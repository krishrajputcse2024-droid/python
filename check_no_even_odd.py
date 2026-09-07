n = int(input("Enter a number :"))
if(n%2==0):
    print("Even number")
else:
    print("Odd number")
    
    #2nd method

def check_even_odd(n):
    if(n%2==0):
        return "Even number"
    else:
        return "Odd number"
n= int(input("enter a number:"))
s = check_even_odd(n)
print(s)