#Function with parameter without return
def function_name(parameter1,parameter2):
    print("Hello",parameter1,"your age is",parameter2)

function_name("Pawan",19)

#Function with parameter with return

def add(parameter1,parameter2):
    print("1st number",parameter1,"2nd number",parameter2)
    return parameter1+parameter2
print(add(2,4))

#using value returned by function
c=add(3,2)
print(c)


