

def Newton_method(count):
    n=0
    x=0.15

    while n<count:
        f_x=(8*(x**2))/(3*(x**2)+1)
        f_prime_x=(16*x)/((3*(x**2)+1)**2)
        x=x-f_x/f_prime_x
        n+=1
    return x

def Newton_modified_method(count):
    n=0
    x=0.15

    while n<count:
        f_x=(8*(x**2))/(3*(x**2)+1)
        f_prime_x=(16*x)/((3*(x**2)+1)**2)
        x=x-2*f_x/f_prime_x
        n+=1
    return x

print(f"Newton method: {Newton_method(9)}")
print(f"Newton modified method: {Newton_modified_method(9)}")