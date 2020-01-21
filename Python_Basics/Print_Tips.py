#To remove the newline character from a string in Python, use its.rstrip() method, likevthis:

>>> 'A line of text.\n'.rstrip()
'A line of text.'

#Nesting quotation marks
"My favorite book is "Python Tricks""  # Wrong!
'My favorite book is "Python Tricks"'
"My favorite book is 'Python Tricks'"
"My favorite book is \"Python Tricks\"" #\" \" Works as well

'C:\\Users\\jdoe' #Getting cluttered
r'C:\Users\jdoe'

#To remove indentation from a multi-line string, you might take advantage of the built-in textwrap module:

>>> import textwrap
>>> paragraph = '''
...     This is an example
...     of a multi-line string
...     in Python.
...     '''
...
>>> print(paragraph)

    #This is an example
    #of a multi-line string
    #in Python.

>>> print(textwrap.dedent(paragraph).strip())
#This is an example
# of a multi-line string
# in Python.

