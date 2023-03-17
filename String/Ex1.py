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