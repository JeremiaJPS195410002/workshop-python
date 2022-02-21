#Using/manipulate String
'spam eggs'  # single quotes
'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

#print function
'"Isn\'t," they said.'
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output
print(s)  # with print(), \n produces a new line

#Using raw strings by adding an "r" before the first quote
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

#Span multiple lines
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#Strings can be concatenated (glued together) with the + operator
3 * 'un' + 'ium'
'Py' 'thon'

#Break long strings
text = ('Put several strings within parentheses '
'to have them joined together.')
text

prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal
('un' * 3) 'ium'
prefix + 'thon'

#Strings can be indexed (subscripted), with the first character having index 0
word = 'Python'
word[0]  # character in position 0
word[5]  # character in position 5

#Indices may also be negative numbers, to start counting from the right:
word[-1]  # last character
word[-2]  # second-last character
word[-6]

#Slicing
word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)
word[:2]   # character from the beginning to position 2 (excluded)
word[4:]   # characters from position 4 (included) to the end
word[-2:]  # characters from the second-last (included) to the end
word[:2] + word[2:]
word[:4] + word[4:]

#Attempting to use an index that is too large will result in an error:
word[42]  # the word only has 6 characters

#Handling out of range slice
word[4:42]
word[42:]

#Assigning to an indexed position in the string results in an error
word[0] = 'J'
word[2:] = 'py'

#Create a new one, if need a different string
'J' + word[1:]
word[:2] + 'py'

#The built-in function len() returns the length of a string
s = 'supercalifragilisticexpialidocious'
len(s)
