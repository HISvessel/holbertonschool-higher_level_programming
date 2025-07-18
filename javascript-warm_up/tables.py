"""practice of data structures and complex data types"""
#Exercise one: retrieve the odd elements of a list into a new list

def number_at_index(list, idx):
    #helper function to find element at index
    return list[idx]

def odd_list(a_list):
    #returns a new list to print only the odd numbers in a list
    new_list = [] #create a new empty list to return
    for key, element in enumerate(a_list): #iterate through the list by enumerating the index(key) and values
        elem = number_at_index(a_list, key)
        new_list.append(elem) if elem % 2 != 0 else None
    return new_list #non sorted return to check randmized data entries

print("Creation of two lists")
first_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
second_unsorted_list = [0, 3, 1, 1, 4, 5, 6, 4, 7, 8, 10, 9]
print(first_list)
print(second_unsorted_list)
print("-" * 10)
print("Checking the functionality of helper function")
five = number_at_index(first_list, 4)
seven = number_at_index(first_list, 6)
print(five)
print(seven)
print("-" * 10)
print()
print("Retrieving our desired odd values with odd_list()")
new_list = odd_list(first_list) #prints 9 at operating the number 0
expected_second_list = [1, 1, 5, 7, 9]
second_new_list = odd_list(second_unsorted_list)
print(new_list)
print("-" * 10)
print(expected_second_list)
print(second_new_list)
