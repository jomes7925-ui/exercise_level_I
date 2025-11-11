# Method 1: Basic Formula with input()

# from math import pi

# r = float(input("Enter the radius of the circle: "))
# area = pi * r ** 2
# print("Area = ", area)

# Note: Simple and clear — directly uses the formula πr².

# ========================================

# Method 2: Using a Function
# If you want reusable code:

# from math import pi

# def circle_area(radius):
#     return pi * radius ** 2

# r = float(input("Enter radus: "))
# print("Area = ", circle_area(r))

# ✅ Better for larger programs — you can call circle_area() many times.

# ==============================

# Method 3: Using math.pow()
# Another way to calculate power:

# import math

# r = float(input("Enter radius: "))
# area = math.pi * math.pow(r, 2)
# print("Area = ", area)

# ✅ Uses math.pow() instead of **.

# ===================================

