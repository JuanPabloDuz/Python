# GIT STEPS
To download this just hit "<> Code" green button, and it will show the "Download ZIP" option.
 
**Creating a new repository**
Go into the directory containing the project.
```bash
git init
git add .
git commit -m "readme"
```
Go to  www.github.com and loggin
Right upper corner and hit create a new repository, then:
```bash
git branch -M main
git remote add origin git@github.com:your_user/your_repo_name.git
git push -u origin main
```
# 2
## INSTALLING PYTHON

## INSTALL pyenv for version control
pyenv - is a simple Python version manager tool, which allows you easily switch between multiple versions of Python. You can set local or global system-wide Python versions via the tool.
1- Install dependencies
```bash
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
2- Download and run installation script
```bash
curl https://pyenv.run | bash
```
3- AAd the following entries into your ~/.bashrc
```bash
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

```
4- Restart your shell and validate
```bash
exec $SHELL
pyenv --version
```
5- Install Python and check versions
```bash
pyenv install 3.7.6
pyenv versions
```
6- To change Python version and check effects
```bash
python shell 3.7.6
python --version
```

# 3
## REPL
Great place to test things
Access:
```bash
python3.7
```

## PYTHON FILES 

```bash
touch hello.py
echo '#!/usr/bin/env python3.7' >> hello.py
echo 'print("Hello, World!")' >> hello.py
chmod u+x hello.py
./hello.py 

```
# 4
## PYTHON COMMENTS and MULTILINE STRINGS

```bash
# this is a comment in python
"""
This is no a comment
This is a multiline string, and uses memory
"""
```

## VARIABLES

Lower case is used for variables, Python Keywords are forbiden as variables names.
```bash
my_string =  "This is a simple string" 
print(my_string)
my_string += " with" #you can add strings
my_string = my_string + " addings" 
print(my_string)
my_string = 1 #a variable has no fixed format
print(my_string)

```

## QUOTING

```bash
'single quoted strings' #String literal

"double quoted strings" #String literal resulting the same 'single quoted strings' 

'''
this is a triple quoted
multi-line string
'''
'\nthis is a triple quoted\nmulti-line string\n' # back slash n (\n) indicates a new line

"'Single' in Double" # "'Single' in Double"
'"Double" in Single' # '"Double" in Single'
"\"Double\" in Double" # '"Double" in Double' by escaping with \
```

## OPERATORS

Adding strings
```bash
"pass" + "word" # 'password'
```
Multiplying strings
```bash
"pass" * 4 # = 'passpasspasspass'
```


## OBJECTS IN PYTHON

States and methods "state.behavior"
```bash
"my_string".find('t') # finds letter t and indicates possition = 4
``` 
Low-case 
```bash
"TesTinG".lower() # output a lower-case of the string
``` 

## ESCAPING

```bash
print("Tab\tDelimited") # Tab     Delimited
print("New\nLine")  # New
                    # Line
print("New\\nLine") # New\nLine
```
## BOOLEANS AND NUMBERS

BOOLEANS can only be TRUE or FALSE, everything in Python is represented at some point as a boolean.

NUMBERS

```bash
2 + 2   # INT = integer
4       #

2.0 + 2.0   # FLOAT = 
4.0         # 

4.5e9 == 4.5 * (10 ** 9)    # Scientific notation
TRUE                        #
```

## NUMERIC OPERATORS
SUM
```bash
2.0 + 2 #
4.0     # if at list one FLOAT, the result will be FLOAT
```
MULTIPLICATION
```bash
3 * 9
27
```
DIVISION
```bash
6 / 3
3.0
```
FLOOR DIVISION
How many times it is evenly divided
```bash
5 // 3
1
6 // 3
2
```
REMINDER
Ohter portion of the floor division. Can identify simply way whether a number divides cleanly by other (when is zero)
```bash
5 % 3
2   # Whole nomber reminder
12 % 2
0   # Divides cleanly by 3
```
EXPONENT
```bash
2 ** 3
8
```
# 5
## NUMBER SYSTEMS

**Binary**

Prefix 0b (0b101)

**Octal**

Prefix 0o (0o724)

**Hexadecimal**

Prefix 0x (0xFF012)

**Converting to binary**

15 / 2 = 7 with remainder of 1   # MOST SIGNIFICANT

7 / 2 = 3 with remainder of 1       
                                        
3 / 2 = 1 with remainder of 1       

1 / 2 = 0 with remainder of 1    # LESS SIGNIFICANT

**Converting to decimal**

(1\*2³) + (1\*2²) + (1\*2¹) + (1\*2⁰)

**FLOAT numbers accuracy**

Flotaing-Point numbers are stored as binary fractions in memory.

Not all decimals can be represented by binary fractions.

0.1 can conly be approximated by 0.100000000000000000005555111123125782...

Most of the time this is not a problem, but in other, like when working with money it is, and for that money is preffered to be expressed in cents.

# 6
## OPERATORS AND BINDINGS

### Bitwise operators
Two's compliment 
```bash
a = 0b010   # a = 2
bin(a)      # '0b10'
~a          # -1*a - 1 = -3
bin(~a)     # 0b10
```
### AND OR XOR NOT
**OR = a | b**
```bash
a=0b1001
b=0b1101
bin(a|b)    #0b1101
```
**AND = a & b**
```bash
a=0b1001
b=0b1101
bin(a&b)    #0b1000
```
**XOR = a ^ b**
```bash
a=0b1001
b=0b1101
bin(a^b)    #0b0101
```

### SHIFTING OPERATORS
**Right shift**

a >> x removes rightest x digits
```bash
a=0b1001
bin(a>>2)    #0b10
```
**Left shift**

a << x add zeros to the right side
```bash
a=0b1001
bin(a<<2)    #0b100100
```
## BOOLEAN OPERATORS

NOT
```bash
not True    # False
```
OR
```bash
True or True    # True
False or True   # True
False or False  # False
True or False   # True
```
AND
```bash
True and True   # True
False and True  # False
False and False # False
True and False  # False
```
## COMPARSION OPERATORS

```bash
1<2    # True
2<1    # False
1<=1   # True
2.0<=3      # False
2.0<=2      # True
'a'<'b'     # True
'a'>'b'     # False
ord('a')    # 97
ord('b')    # 98
'bb'>'ba'   # True
1 == 1      # True
1.0 == 2    # False
'a' ==  2   # False
1 != 1      # False
2 != 1      # True
1 is 1      # True
1.0 is 1    # False
'a' is not 'a'  # False
id('a')     # 140347512797424
id('a')==id('a')    # True 
[] is []    # False (lists are not inmutable)
```
### OPERATOR PRIORITY
(binding)
https://docs.python.org/3/reference/expressions.html#operator-precedence

For whatever reason, the Python documentation shows the least binding operators first, but we'll talk about them from most binding to least. We'll leave the ones that we won't cover in this course out of the list though:

Parenthesis and List/Dictionary/Set literals

Accessing attributes (subscription, slicing, function/method call, attribute reference)

Exponentiation (**)

Positive, Negative, and bitwise complement

Multiplication *, Division /, Floor Division //, Modulo %

Addition +, Subtraction -

Bitwise Shifts << & >>

Bitwise AND &

Bitwise XOR ^

Bitwise OR |

Comparison operators (in, not in, is, is not, <, >, <=, >=, ==, !=)

Boolean NOT not

Boolean AND and

Boolean OR or

Conditions if

examples:
```bash
14 & 3 * 2 + 4      # 10
14 & 3 * (2 + 4)    # 2
(14 & 3) * 2 + 4    # 8
14 & (3 * 2) + 4    # 10
```
# 7
## TYPECASTING
changing types

```bash
float(1)    # 1.0
int(1.3)    # 1
int(1.6)    # 1
str(1.0)    # '1.0'
float('1.2')  # 1.2
int('1.2')  # error
bool(1)     # true
bool(2.4)   # true
bool('tada')    # true
# mostly everything will be true
bool(0)     # false
bool(0.0)     # false
bool('')     # false
# and
1 and 0     # true and false = false = 0
0 and 'this'   # 0
'this' and 0   # 0
'this' and 'that'   # 'that'
'this' and 0 and 'that'   # 0 (returns first false value)
# or
1 or 0   # 1
0 or 1   # 1
0 or ""   # ''
0 or 1 or 'this'   # 1 (returns first true value)
# not
not ""  # true
not 1   # false
```
## INPUT and PRINT

See:
/code/bio.py
/code/to-celsius.py

# 8
## INMUTABILITY

Most of the types are inmutable.

```bash
my_string = 'test'  #
id(my_string)          #
my_str.capitalize() #'Testing'
otrher = 'test'
id(other) == id(my_string) # True

```

## LEN function
Length, number of characters
```bash
len('hello') # 5
```

## INDEXING & SLICING

```bash
my_string = 'testing'
my_string[0]    # 't' - square brakets are for indexing
my_string{-2]   # 'n' - negative indexing
my_string[3:5]  # 'ti' - slicing from index 3 through 4 (>5)
my_string[3:len(my_tring)]  # 'ting' - slicing from index 0 through before the end
my_string[3:]  # 'ting' - slicing from index 0 through the end
my_string[0:7:2]  # 'tsig' - slicing from index 0 through 6 with step of 2
my_string[:7:2]  # 'tsig' - slicing from index 0 through 6 with step of 2
my_string[::2]  # 'tsig' - slicing from index 0 through the end with step of 2
my_string[::-1]  # 'gnitset' - clever way to reverse strings
```
see /code/strings.py

# 9
## LISTS
Collection of other items. 
```bash
list_1 = [1, 2, 3, 4, 5]    
List_2 = ['a', 1, 1.0, False]
List_1[0]   # 1 - Indexing
List_1[0:2] # [1, 2] - Slicing a List results a List
List_1[0::2] # [1, 3, 5] - Steping also works
```
Lists are mutable.

```bash
list_1[0] = 'a'
list_1              # ['a', 2, 3, 4, 5]
List_1 + [7, 8, 9]  # contactenate list
list_1              # ['a', 2, 3, 4, 5, 7, 8, 9]
List_1 += [7, 8, 9]  # Creates a new list and reasigns it
list_1              # ['a', 2, 3, 4, 5, 7, 8, 9]
list_1[1:3] = ['b', 'c']
list_1              # ['a', 'b', 'c', 4, 5, 7, 8, 9]
```
Delete items
```bash
list_1[3:] = []     # Slice a part and reasign it to keep it
list_1              # ['a', 'b', 'c']
del list_1[0]       # deletes an item or entire list
list_1              # ['b', 'c']
```

## LIST FUNCTIONS AND METHODS

```bash
list_1.append(4)        # appends at the end
list_1                  # ['b', 'c', 4]
list_1.insert(0, 'a')   # inserts an item in specific possition
list_1                  # ['a', 'b', 'c', 4]
list_1.index(2)         # 'c'
'd' in list_1           # False - checks if an item is in a list
'd' not in list_1       # True
list_1 = [9, 2, 1, 4, 5] 
sorted(list_1)          # [1, 2, 4, 5, 9]
list(reversed(list_1))  # [5, 4, 1, 2, 9]
```
## NESTED LISTS: MATRIX AND CUBES

```bash
matrix_1 = [[1, 2, 3], 
            [4, 5, 6]]
row_count = len(matrix_1)
row_count                   # 2
column_count = len(matrix_1[0])
column_count                # 3
matrix_1[0][0]              # 1
matrix_1[1][0]              # 4
```
A cube is a matrix with same number of columns and rows

Check lists.py

# 10
## TUPLES
Inmutable type list of items
```bash
tuple_1=(2.0, 4.0)
tuple_1[0] = 1  # err
tuple_1= tuple_1 + (6.0)    # (2.0, 4.0, 6.0)
x, y, z= tuple_1            # X=2.0, y=4.0, z=6.0
print("My name is %s %s" % ("Juan", "Pablo"))    # unpacking tuple
                                                 # My name is Juan Pablo
```
Lists and Tuples
```bash
list_1 = [1, 2, 3]
tuple_2 = (list_1, 1)
tuple_2     # ([1, 2, 3], 1)
list_2 = [1, 2, tuple_2]
list_2      # [1, 2, ([1, 2, 3], 1)]
list_2.append(4)
tuple_2     # ([1, 2, 3, 4], 1)
```
Even do tuples are inmutable, lists contained in tuples can change.

# 11
## Dictionaries
Dictionaries are mutable, if the key exists the value can be changed, if not exist can be added.

```bash
ages = {'juan': 43, 'nadia': 56, 'kevin': 19}
ages            # {'juan': 43, 'nadia': 56, 'kevin': 19}
ages['juan']    # 43
ages['caro'] = 33  
ages             # {'juan': 43, 'nadia': 56, 'kevin': 19, 'caro': 33}
ages['juan'] = 44   
ages             # {'juan': 44, 'nadia': 56, 'kevin': 19, 'caro': 33}
del ages['nadia']
ages             # {'juan': 43, 'kevin': 19, 'caro': 33}
nadia in ages   # True
juan in ages    # False
ages_2 = dict(juan=43, nadia=56, kevin=19) # dict function
ages_2          # {'juan': 43, 'nadia': 56, 'kevin': 19}
ages_3 = dict([('juan',43), ('nadia',56), ('kevin', 19)]) # from tuples
ages_2          # {'juan': 43, 'nadia': 56, 'kevin': 19}
```
**Methods to give access to dictionaries**
```bash
ages = {'juan': 43, 'nadia': 56, 'kevin': 19}
ages.keys()         # dict_keys(['juan', 'nadia', 'kevin'])
list(ages.keys())   # ['juan', 'nadia', 'kevin']
ages.values()         # dict_values([43, 56, 19])
list(ages.keys())   # [43, 56, 19]
ages.items()         # dict_items([('juan',43), ('nadia',56), ('kevin', 19)])
list(ages.items())   # [('juan',43), ('nadia',56), ('kevin', 19)]
```
See /code/dictionaries.py

# 12
## STRINGS
Multiple ways to encode strings
Default Unicode UTF-8. Each string has a code, there are over a millon codes.
Unicode Transformation Format.
ASCII - 256 codes (128 valid on UTF-8)
```bash
ord('a')        # 97
ord('™')        # 8482
U+2122          # 8482 - hexa format
ord('\u2122')   # 8482
'\u2122'        # '™'
chr(8482)       # '™'
```



