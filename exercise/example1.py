# Example 1: Simple Version
# Create a few empty .py file.

# for i in range(1, 6):  # creates exercise1.py to exercise5.py
#     filename = f"exercise{i}.py"
#     with open(filename, "w") as f:
#         pass  # just create the file (empty)
#     print(f"Created: {filename}")

# ✅ Output example:

#     Created: exercise1.py
#     Created: exercise2.py
#     Created: exercise3.py
#     Created: exercise4.py
#     Created: exercise5.py

# =========================================================

# Example 2: Let User Choose How Many Files

# n = int(input("How many Python files do you want to create? : "))

# for i in range(1, n + 1):
#     filename = f"exercise{i}.py"
#     with open(filename, "w") as f:
#         f.write(f"# This is exercise {i}\n")
#     print("Created:", filename)

# ✅ Flexible — user decides the count.
# Output:
#     How many Python files do you want to create? : 2
#     exercise1.py
#     exercise2.py

# ===============================================================

# Optional Bonus: Create Files in a Folder

import os

folder = "exercises"
os.makedirs(folder, exist_ok=True)

for i in range(1, 6):
    filepath = os.path.join(folder, f"exercise{i}.py")
    with open(filepath, "w") as f:
        f.write(f"# Exercise {i}\n")
    print("Created:", filepath)

✅ Automatically makes a folder called exercises/ and puts all files there.