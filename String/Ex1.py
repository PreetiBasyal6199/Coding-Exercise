# Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

giver_str = 'google.com'
dir1={}
for letter in giver_str:
    if letter not in dir1.keys():
        dir1[letter]=1
    else:
        dir1[letter]+=1
print(dir1)


#  Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'      Expected Result : 'w3ce'
# Sample String : 'w3'              Expected Result : 'w3w3'
# Sample String : ' w'              Expected Result : Empty String

input_str = input("Please enter the string.")
if len(input_str)<2:
    print("")
else:
    print(input_str[:2] + input_str[-2:])


# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. 
# Sample String : 'restart'             # Expected Result : 'resta$t'
input_str1= input("Enter the string.")
new_str = input_str1.replace(input_str1[0], '$')
print(input_str1[0]+new_str[1:])


# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
def change_str(str1, str2):
    changedstr1 = str2[:2]+ str1[2]
    changedstr2 = str1[:2] + str2[2]
    print(changedstr1 + ' ' + changedstr2) 
change_str('abc', 'xyz')

#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'           Expected Result : 'abcing'
# Sample String : 'string'          Expected Result : 'stringly'

def add_ing(str1):
    if len(str1)>=3:
        if str1[-3:]=="ing":
            str1+= 'ly'
        else:
            str1+='ing'
    return str1

print(add_ing("Diying"))


 