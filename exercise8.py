# List of colors
# color_list = ["Red", "Green", "White", "Black"]

# # Display first and list colors
# print("First the color: ", color_list[0])
# print("Last the color: ", color_list[-1])

# ==================================================

# Method 1: Using indexing (most common)
# color_list = ["Red", "Green", "White", "Black"]
# print(color_list[0], color_list[-1])


# Method 2: Using list.pop() without removing original list
# color_list = ["Red", "Green", "White", "Black"]
# first = color_list.copy().pop(0)
# last = color_list.pop()
# print(first, last)

# =========================================================
# Method 3: Using unpacking
# color_list = ["Red", "Green", "White", "Black"]
# first, *middle, last = color_list
# print(first, last)

# ==========================================================
# Method 4: Using a Function
# color_list = ["Red", "Green", "White", "Black"]
# def first_last(items):
#     return items[0], items[-1]
# print(first_last(color_list))

# =========================================================
# Method 5: Using next() and reversed()
# color_list = ["Red", "Green", "White", "Black"]
# first = next(iter(color_list))
# last = next(iter(reversed(color_list)))
# print(first, last)
