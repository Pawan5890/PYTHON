#Recursion- A function calling itself until a condition stops it is called recursion.
 #Two cases
  #base case- the condition given to stop the recursion function
  #Recursive case- It is the condition where function calling itself

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
