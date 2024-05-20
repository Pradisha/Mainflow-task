#mainflow
# Create a list, dictionary, and set
my_list = [1, 2, 3]
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_set = {1, 2, 3}

# List operations
print("Original list:", my_list)

# Adding elements
my_list.append(4)
print("List after adding an element:", my_list)

# Removing elements
my_list.remove(2)
print("List after removing an element:", my_list)

# Modifying elements
my_list[1] = 5
print("List after modifying an element:", my_list)

# Dictionary operations
print("\nOriginal dictionary:", my_dict)

# Adding elements
my_dict['d'] = 4
print("Dictionary after adding an element:", my_dict)

# Removing elements
del my_dict['b']
print("Dictionary after removing an element:", my_dict)

# Modifying elements
my_dict['a'] = 10
print("Dictionary after modifying an element:", my_dict)

# Set operations
print("\nOriginal set:", my_set)

# Adding elements
my_set.add(4)
print("Set after adding an element:", my_set)

# Removing elements
my_set.remove(2)
print("Set after removing an element:", my_set)

# Sets do not have indexing, so elements cannot be modified directly
# Instead, we can remove an element and add a new one
my_set.remove(3)
my_set.add(5)
print("Set after modifying elements:", my_set)
