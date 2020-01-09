#! /usr/bin/env python3

# 1)Write a function that returns a float corresponding to the volume of a cone:
def get_cone_volume(radius, height):
    return (height/3)*3.14159265*(radius**2)

# 2) Write a function that calculates and returns an integer corresponding to the factorial of an integer:
# 2a) using recursivity
def recursive_factorial(n):
    if (n == 0 or n == 1):
        return 1
    return n*recursive_factorial(n-1)

# 2b) without recursivity
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    result = 1
    while (n > 1):
        result = result*n
        n = n -1
    return result


#3) Write a function for counting down numbers from n to 0, showing the count down in the screen. If parameter odd is set to True, prints only odd numbers:
def count_down(n, odd=False):
    while (n >= 0):
        if(n%2 == 1):
            print(n)
        # Si odd es falso y es par se imprime
        elif(not odd and n%2 == 0):
            print(n)
        n -= 1

#4) Find and solve the bugs in the following function:
def get_final_price(price, discount_percentage=10):
    """Return the final price after applying the discount percentage"""
    return price - (price * discount_percentage / 100)

print("Cone Volume: r=2, h=6")
print(get_cone_volume(2, 6))
print("Factorial of 10")
print("Recursive:")
print(recursive_factorial(10))
print("Iterative:")
print(factorial(10))
print("Countdown from 10, full")
count_down(10)
print("Countdown from 10, only odd")
count_down(10, True)
print("Price after discount (price=10, discount 10%):")
print(get_final_price(10, 10))
