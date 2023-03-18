#1.  Write a Python script to merge two Python dictionaries. 

dict_1 = {'a': 100, 'b':200}
dict_2 = {'c': 300, 'd':400}
result= dict_1.copy()
result.update(dict_2)
print(result)



#2.  Write a Python program to iterate over dictionaries using for loops.

a_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
for k,v in a_dict.items():
    print(k, v)



#3. Write a Python program to sum all the items in a dictionary.

b_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
print(sum(b_dict.values()))



#4. Write a Python program to remove a key from a dictionary.
c_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
c_dict.pop('a')
print(c_dict)                   #{'b': 200, 'c': 300, 'd': 400}



#5. Write a Python program to map two lists into a dictionary.

list1=['a', 'b', 'c', 'd']
list2 =[1,2,3,4]
print(dict(zip(list1, list2)))          # {'a': 1, 'b': 2, 'c': 3, 'd': 4}