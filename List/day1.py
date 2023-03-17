# 1. Write a Python program to sum all the items in a list.
def get_sum(list):
    sum =0
    for item in list:
        sum+=item
    print(sum) 
get_sum([1,2,3,4])


# 2. Write a Python program to multiply all the items in a list.
from functools import reduce
result = reduce(lambda x,y:x*y, [1,2,3,4])
print(result)

# 3. Write a Python program to get the largest number from a list
def get_max(list_1):
    max =list_1[0]
    for item in list_1:
        if item>max:
            max=item
    return max
print(get_max([1,2,3,4]))


# 4. Write a Python program to get the smallest number from a list.
def get_min(list_1):
    min =list_1[0]
    for item in list_1:
        if item<min:
            min=item
    return min
print(get_min([1,2,3,4]))


# 5. Write a Python program to count the number of strings from a given list of strings.
#  The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def count_str(list_1):
    count = 0
    for item in list_1:
        if item[0]==item[-1] and len(item)>=2:
            count +=1
    return count
print(count_str(['abc', 'xyz', 'aba', '1221']))


