# 1.  Write a Python script to sort (ascending and descending) a dictionary by value. 

def sort_dict(dict):
    asc_order=sorted(dict.items(), key=lambda x:x[1])
    desc_order=sorted(dict.items(), key=lambda x:x[1], reverse=True)

    print(asc_order, desc_order)

sort_dict({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})


# 2. Write a Python script to add a key to a dictionary. Go to the editor

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

def add_key(dict_1):
    dict_1[2]=30
    print(dict_1)

add_key({0: 10, 1: 20})


# 3. Write a Python script to concatenate the following dictionaries to create a new one. Go to the editor

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def concatenate_dict(dict1, dict2, dict3):
    dict4={}
    for d in(dict1,dict2,dict3):
        dict4.update(d)

    print(dict4)
concatenate_dict({1:10, 2:20},{3:30, 4:40}, {5:50,6:60} )


# 4. Write a Python script to check whether a given key already exists in a dictionary

def check_key(dict1, key):
    if key in dict1.keys():
        return True
    else:
        return False
print(check_key({1:10, 2:20}, 2))
    

# 5. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def create_dict(num):
    dict1={}
    for i in range(1,num+1):
        dict1[i]=i*i
    print(dict1)

create_dict(5)

