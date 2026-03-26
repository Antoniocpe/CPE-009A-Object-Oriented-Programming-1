import math

def quad_eq(a,b,c):
    d = b**2 - 4*a*c

    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    return root1, root2

    
        
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
    
answer1, answer2 = quad_eq(a, b, c)
print(f"root 1: {answer1}")
print(f"root 2: {answer2}")

    