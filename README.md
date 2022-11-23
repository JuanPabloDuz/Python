# GIT STEPS
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

# INSTALLING PYTHON

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

## OPERTORS

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
## BOOLEANS and NUMBERS

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

## NUMERIC OPERATOR
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

