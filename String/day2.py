# 1. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
#  If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def check_substr(input_string):
    i_not = input_string.find("not")
    i_poor = input_string.find("poor")
    if i_not<i_poor and i_not >0 and i_poor>0:
        new_str = input_string.replace(input_string[i_not:(i_poor+4)], 'good')
        return new_str
    else:
        return input_string

print(check_substr('The lyrics is not that poor!' 'The lyrics is poor!'))


# 2. Write a Python function that takes a list of words and return the longest word and
#  the length of the longest one.

def check_longest(word_list):
    len_words={}
    for item in word_list:
        len_words[len(item)]=item
    len_list = len_words.keys()
    return max(len_list),len_words[max(len_list)] 
print(check_longest(['apple','ball','cat']))

def check_long(word_list):
    len_words = []
    for item in word_list:
        len_words.append((len(item), item))
    len_words.sort(key=lambda x:x[0])
    return len_words[-1][0], len_words[-1][1]

print(check_long(['apple','ball','cat']))


#3. Write a Python program to remove the nth index character from a nonempty string

def remove_nth(input_str, r_index):
    new_str = input_str[:r_index] + input_str[r_index+1:]
    return new_str

print(remove_nth("apple", 2))

# 4. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

def change_str(string_in):
    return string_in[-1]+string_in[1:-1]+string_in[0]
print(change_str('python'))


#5. Write a Python program to remove characters that have odd index values in a given string.

def remove_chr(input_str):
    result_str =''
    for i in range(len(input_str)):
        if i%2==0:
            result_str = result_str + input_str[i]
    return result_str
print(remove_chr('python'))

