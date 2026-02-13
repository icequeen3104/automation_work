""" Nested Dictionary "Flattener"
The Challenge: Write a recursive function that takes a deeply nested dictionary and flattens it
into a single-level dictionary where keys are concatenated with dots.
Example Input: {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
Example Output: {"a": 1, "b.c": 2, "b.d.e": 3}
The Goal: Handle edge cases like empty dictionaries or lists within the values
"""

data = {"a": 1, "b": {"c": 2, "d": {"e": 3}}}

flat = {}
stack = [("", data)]  # (parent_key, current_dictionary)

while stack:
    parent, current = stack.pop() # in the third loop "b" will be the "parent" and "current" will have "{"c":2, "d": {"e":3}}}"

    for key, value in current.items(): #"b"(key): {"c": 2, "d": {"e": 3}}(value)
        new_key = parent + "." + key if parent else key #a #b

        if isinstance(value, dict) and value: #false so go to the else part #isinstance compares the type of the val with the val
            stack.append((new_key, value))
        else:
            flat[new_key] = value #"a" : 1 #'b.c':2

print(flat)
