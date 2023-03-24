# 1. Read a given string, change the character at a given index and then print the modified string.

def mutate_string(input_str, index, character):
    new_str = input_str[:index] + character + input_str[index+1:]
    return new_str

print(mutate_string('abracadabra', 2, 'c'))


#2. The user enters a string and a substring. You have to print the number of times that the substring occurs
#  in the given string. String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    count=0
    for i in range(len(string)-1):
        if string[i:i+len(sub_string)] == sub_string:
            count +=1
    return count
print(count_substring("ABCDCDC", "CDC"))

'''
3. You are given a string .Your task is to find out if the string  contains: 
alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

'''
def check_string(string):
    print(any(i.isalnum() for i in string))
    print(any(i.isalpha() for i in string))
    print(any(i.isdigit() for i in string))
    print(any(i.islower() for i in string))
    print(any(i.isupper() for i in string))
check_string("Hello123")


'''
4.  You are given a string  and width .Your task is to wrap the string into a paragraph of width .
'''
import textwrap
def wraptext(string, max_width):
    new_str = textwrap.fill(string, max_width)
    return new_str
print(wraptext("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ


'''
5.  
'''