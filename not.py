# all checks a list, returns True if all elements are Truthy

list_eg = ["", "hello", 1]
if not all(list_eg): 
    print("Not all conditions are Truthy.")  # Will print
else:
    print("All conditions are Truthy.")

list_eg = ["1", "hello", 1]
if not all(list_eg): 
    print("Not all conditions are Truthy.")  
else:
    print("All conditions are Truthy.")   # Will print




