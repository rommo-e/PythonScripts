# We need to define a function that operates with a number and returns it square 
def square(n):
    return n*n

def sum_squares(x):
 sum = 0
 for n in range(x):
     sum += square(n)
 return sum

print(sum_squares(100)) 

