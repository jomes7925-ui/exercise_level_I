for i in range(15, 151):  # creates exercise1.py to exercise5.py
    filename = f"exercise{i}.py"
    with open(filename, "w") as f:
        pass  # just create the file (empty)
    print(f"Created: {filename}")
