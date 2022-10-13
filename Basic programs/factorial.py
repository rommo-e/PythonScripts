# First of all we define the factorial function for any number n

def factorial(n):
    result = 1 
    for i in range(1,n+1):
         result = i *result
    return result
print(factorial(1000))

