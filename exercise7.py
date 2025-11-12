# 🧩 Method 1: Using split()
# filename = input("Enter the filename: ")
# ext = filename.split(".")[-1]
# print("Extension:", ext)


# ✅ Easy and short
# Example:

# Enter the filename: abc.java
# Extension: java

# 🧠 Method 2: Using rsplit() (safer for filenames with multiple dots)
# filename = input("Enter the filename: ")
# ext = filename.rsplit(".", 1)[-1]
# print("Extension:", ext)


# ✅ Handles names like my.code.file.py → py

# 🧰 Method 3: Using os.path.splitext()
# import os

# filename = input("Enter the filename: ")
# ext = os.path.splitext(filename)[1]
# print("Extension:", ext[1:])  # remove the dot


# ✅ Most reliable — works even if filename has folders or multiple dots
# Example:

# Enter the filename: project/data/test.py
# Extension: py

# 🧮 Optional — With Message Formatting
# import os

# filename = input("Input the Filename: ")
# ext = os.path.splitext(filename)[1][1:]
# print(f"The extension of the file is: '{ext}'")


# Output:

# Input the Filename: abc.java
# The extension of the file is: 'java'