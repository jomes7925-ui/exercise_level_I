# Method 1: Basic and clear Way

# values = input("Enter comma-spearated numbers: ")
# list_values = values.split(",")
# tuple_values = tuple(list_values)

# print("List: ", list_values)
# print("Tuple: ", tuple_values)

# ✅ Simple and works perfectly

# ===================================================

# Method 2: Clean Extra Space

# values = input("Enter comma-separated number: ")
# list_values = [x.strip() for x in values.split(",")]
# tuple_values = tuple(list_values)

# print("List: ", list_values)
# print("Tuple: ", tuple_values)

# To remove spaces after commas (like ' 5' → '5'):

# =====================================================

# Method 3: Using a Function

# If you want to reuse it late:

# def generate_list_and_tuple():
#     data = input("Enter comma-separated numbers: ")
#     data_list = [x.strip() for x in data.split(",")]
#     data_tuple = tuple(data_list)
#     return data_list, data_tuple

# lst, tpl = generate_list_and_tuple()
# print("List :", lst)
# print("Tuple :", tpl)

# ✅ Great for larger programs.

# ======================================================

# 🧮 Optional - Convert to Numbers

# If you want actual integers instead of strings:

# values = input("Enter comma-separated numbers: ")
# list_values = [int(x.strip()) for x in values.split(",")]
# tuple_values = tuple(list_values)

# print("List :", list_values)
# print("Tuple :", tuple_values)