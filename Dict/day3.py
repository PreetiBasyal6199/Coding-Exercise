#1.   Write a Python program to sort a given dictionary by key
def sort_dict(input_dict):
    sorted_list = sorted(input_dict.items(), key=lambda x : x[0])
    return dict(sorted_list)
print(sort_dict({'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}))


#2.   Write a Python program to get the maximum and minimum values of a dictionary.

def get_min_max(input_dict):
    values_list = input_dict.values()
    max_val = max(values_list)
    min_val = min(values_list)
    return max_val, min_val
print(get_min_max({'a':1,'b':2,'c':3,'d':4}))



my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])



#3. Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

def combine_dict(dict1, dict2):
    for item in dict2.keys():
        if item not in dict1.keys():
            dict1[item] = dict2[item]
        else:
            dict1[item] +=dict2[item]

    return dict1

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print(combine_dict(d1,d2))


# 4.  Write a Python program to print all distinct values in a dictionary. Go to the editor
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
def distinct_value(list1):
    return set(item for dict in list1 for item in dict.values())
    # result_list = []
    # for item in list1:
    #     for x in item.values():
    #         result_list.append(x)
    # return set(result_list)
input_val = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print(distinct_value(input_val))


#5.  Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output: ac ad bc bd

def new_reslt(dict1):
    val_list = dict1.values()
    
    pass
print(new_reslt({'1':['a','b'], '2':['c','d']}))
