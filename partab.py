import math
def Newton_method(count):
    n=0
    x=0.1
    while n<count:
         f_x = math.e**(2*math.sin(x)) - 2*x - 1
         f_prime_x = (math.e**(2*math.sin(x))) * 2*math.cos(x) - 2
         x=x-(f_x/f_prime_x)
         n+=1
    return x

print(f"Newton_method: {Newton_method(9)}")

def Newton_modified_method(count):
    n=0
    x=0.1
    while n<count:
         f_x = math.e**(2*math.sin(x)) - 2*x - 1
         f_prime_x = (math.e**(2*math.sin(x)))* 2*math.cos(x) - 2
         x=x-2*(f_x/f_prime_x)
         n+=1
    return x

print(f"Newton_modified_method: {Newton_modified_method(9)}")