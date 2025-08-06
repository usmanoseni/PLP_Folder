# declaration and initialization of a list
# This code initializes a list with four integer elements.
my_list = []
my_list.append(10)  # Appends 10 to the list
my_list.append(20)  # Appends 20 to the list
my_list.append(30)  # Appends 30 to the list
my_list.append(40)  # Appends 40 to the list
print("The initial list is: ", my_list)

# code to insert an element at a specific index
my_list.insert(1, 25)  # Iinserts 15 to second position
print("The list after inserting 25 at index 1 is: ", my_list)

# code to extend the list with another list
my_list.extend([50, 60, 70])
print("The list after extending with [50, 60, 70] is: ", my_list)

# code to remove an element from the list
my_list.pop()  # Removes the last element in the list
print("The list after popping the last element is: ", my_list)

# code to sort the list in ascending order
my_list.sort()
print("The list after sorting in ascending order is: ", my_list)

# code to iterate through the list and check for a specific value
# This code iterates through the list and checks if the value 30 is present.
for k in my_list:
    if k == 30:
        print("The value 30 is present in the list at index: ", k)
        break
    else:
        continue
