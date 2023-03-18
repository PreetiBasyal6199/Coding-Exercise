#1. Write a Python program to get a list, sorted in increasing order by the last element in each tuple
#  from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def sort_list(input_list):
    sorted_list = sorted(input_list, key=lambda x:x[1])
    return sorted_list
print(sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


#2. Write a Python program to remove duplicates from a list.

def remove_dublicate(input_list):
    new_list = list(set(input_list))
    return new_list
print(remove_dublicate([1,2,3,2,4,5,4]))

#3.  Write a Python program to clone or copy a list.

def create_copy(input_list):
    return input_list.copy()

print(create_copy([1,2,3,4]))

#4.  Write a Python function that takes two lists and returns True if they have at least one common member.

def check_list(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
print(check_list([1,2,4], [1,5,6]))


# 5.   Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def create_new_list(list1):
   new_list = [x for i,x in enumerate(list1) if i not in(0,4,5)]
   return new_list
print(create_new_list(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))