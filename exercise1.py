# =================step 1
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# print("Twinkle, twinkle, little star,")
# print("\tHow I wonder what you are!")
# print("\t\tUp above the world so high,")
# print("\t\tLike a diamond in the sky.")
# print("Twinkle, twinkle, little star,")
# print("\tHow I wonder what you are")

# ===== Using Multiline String ("""...""")

# Using triple quotes
# poem = """Twinkle, twinkle, little star,
# \tHow I wonder what you are!
# \t\tUp above the world so high,
# \t\tLike a diamond in the sky.
# Twinkle, twinkle, little star,
# \tHow I wonder what you are"""
# print(poem)

# ===== Using List + Loop
# lines = [
#     "Twinkle, twinkle, little star,",
#     "\tHow I wonder what you are!",
#     "\t\tUp above the world so high,",
#     "\t\tLike a dimond in the sky.",
#     "Twinkle, twinkle, little star,",
#     "\tHow I wonder what you are"
# ]
# for line in lines:
#     print(line)

# ===== Using Join()
poem_lines = [
    "Twinkle, twinkle, little star,",
    "\tHow I wonder what you are!",
    "\t\tUp above the world so high,",
    "\t\tLike a dimond in the sky.",
    "Twinkle, twinkle, little star,",
    "\tHow I wonder what you are"
]
print("\n".join(poem_lines))