# Method 1: Basic Input and print
# first = input("Enter your first name: ")
# last = input("Enter your last name: ")

# print(first, last)

# ✅ Simple and clear — just prints the names in reverse order with a space.

# ===========================================

# Method 2: Use String Formatting (f-String)

# first = input("Enter your first name: ")
# last = input("Enter your last name: ")

# print(f"{last} {first}")

# ✅ Easier to read and format — works well for all cases.

# =============================================

# Method 3: Combine Input in One Line

# full_name = input("Enter your first and last name: ")
# first, last = full_name.split()
# print(last, first)

# ✅ Good practice for reusable code and functions.