
### Chapter 2 Notes
#### Running the IPython Shell
- Python is a pretty-printed, meaning it is formatted to be more readable. 
- IPython also helps with executing small blocks of code as well as whole Python scripts.

#### Running the Jupyter Notebook
- Open command prompt and run the following command:`$ jupyter notebook`
- The Jupyter notebook will open in a default browser. 
- Jupyter notebooks will save with .ipynb extension that saves all input and output content. 

#### Tab Completion
- Tab key will search the namespace for any variables. 
- Period can also complete methods and attributes on any object. 
- Period can be use for modules and tab can be used with file paths as well. 

#### Introspection
- Using a question mark before or after a variable will display metadata about the obejct
- Use question mark(s) to display the docstring and the source code.
- Use wildcard (*) to display all functions matching the wildcard expression. 

#### %run Command
- Run files using the %run command.
- All variables defined in the file will be available in IPython shell. 
- In Jupyter notebook, `%load` has the same functionality as `%run` in IPython shell.
- Ctrl-C will cause all Python programs to stop running

#### Executing Code from the Clipboard
- Use `%paste` or `cpaste` to paste any code into IPython shell. 
- `%paste` pastes the whole code and executes it. 
- `%cpaste` give users the option to view and determine how much of the code they want to paste before it is executed. 

#### Magic Commands
- Magic commands are not built into Python
- Magic commands are prefixed by the `%` symbol 
- Command-line programs to be run within the IPython system
- Automagic - Magic functions can be assigned to a variable as long as no other variable is defined with the same name.

#### Matplotlib Integration
- `%matplotlib` configures integration with IPython shell
- `%matplotlib inline` configures integration with Jupyter notebook

#### Python Language Semantics
- Indentation - Python uses whitespace (tabs or spaces) to structure code
- Colon denotes the start of an indented code block
- All of the code must be indented same amount until the end of code block
- Semi-colons are used to seperate multiple statements on a single line
  - Discourage from writing multiple statement on a single line
- Object model - everything is a Python object.
  - Every object has an associated type and internal data
- `#` can be used to comment 
- Methods - attached functions to objects
- Functions can take both positional and keyword arguments
- Creating a variable means creating a reference to the object

#### Dynamic references, strong type
- Object refrences in Python does not have type associated with them
  - Variables are names for object within a particular namespace
  - Types are stored within the object itself
- Python is astrongly typed language
  - Every object has a specific type (or class) and implicit conversions will occur only in certain obvious circumstances
- `isinstance` function is used to check the object is an instance of a particular type

#### Attributes and methods
- Attributes - other Python objects stored "inside" the object
- methods - functions associated with an object that can have access to the object's internal data

#### Duck Typing
- Checking to see if the object has certain methods or behavior

#### Imports
- module - a file with .py extension containing Python code.
- import Example
```
# file = some_module.py
PI = 3.14159

def f(x):
    return x + 2

def g(a, b):
    return a + b
----
import some_module # imports the whole file
----
from some_module import f, g, PI # users are able to select specifics variables and functions defined in the file
----
import some_module as sm
from some_module import PI as pi, g as gf # rename the variables
```

#### Binary Operators and Comparisons
- Use `is` and `is not` to check the validity of the statements 
- `list` creates a copy, new Python list
- `is` is not same as `==` operator
- There can only be one instance of `None`

#### Mutable and Immutable Objects
- Mutable - object or values can be modified
  - lists, dicts, NumPy arrays, most user-defined types are mutable
- Immutable - object or values cannot be modified
  - strings and tuples are immutable
  
#### Scalar Types
- Scalar types = single value types
  - Examples: None, str, bytes, float, bool, and int
- int - can store arbitrarily large numbers
- float - double-precision (64-bit) value; can also be expressed with scientific notation
  - integar division not resultsing in whole number will be yield a floating point number
  - `//` - floor operator - drops the fractional part if the result is not a whole number
- str - can use single or double quotes; multiline strings with line breaks use triple single or double quotes
  - strings can be sliced 
  - `\` is an escape character - used to specify special characters
  - `r` = raw - characters should be interpreted as is
  - `format` method 
    - In [74]: template = '{0:.2f} {1:s} are worth US${2:d}
    - {0:.2f} means to format the first argument as a floating-point number with two decimal places.
    - {1:s} means to format the second argument as a string.
    - {2:d} means to format the third argument as an exact integer.

#### Bytes and Unicode
- UTF-8 is preferred for any encoding
- `b` - define your own byte literals by prefixing a string with `b`

#### Booleans
- Boolean values are combined with `and` and `or` keywords

#### Type Casting
- str, bool, int and float can be used to cast values to those types 

#### None
- `None` - Python null value type

#### Dates and Times
- `datetime` is a built-in Python module
  - Provides `datetime`, `date`, and `time` types
- `strtime` used to format datetime as a string
- 'strptime` used to parse strings into datetime objects
- datetime.datetime is an immutable type

#### if, elif, and else
- `if` - checks the condition and if `True` evaluates the code in the block that follows
- `elif` - additional conditions
- `else` - catch-all conditions if false 

### for loops
- `for` loops are for iterating over a list or tuple or an iterator 
``` 
for value in collection:
   # do something with value
```
- `continue` - advances to the next iteration, skipping the remainder of the block
```
sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None: # skips the None values
        continue
    total += value
```
- `break` - exits the `for` loop
```
sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in sequence:
   of value == 5: # code sums elements until a 5 is reached
      break
    total_until_5 += value
```
   - `break` only terminates the innermost loop, the outer loops will continue to run
   
#### while loops
- `while` loop specifies a condition and a block of code that is to be executed until the condition evaluates to `False` or the loop is explicitly ended with break

#### pass
- `pass` = "no-op" statement - no action is to be taken

#### range
- `range` returns iterator that yields a sequence of evenly spaced integers
- can provide start, end, step - Step is the increment

#### Ternary Expressions
- Ternary expressions allows users to combine `if-else` block that produces a value into a single line or expression
``` 
value = true-expr if condition else false-expr
```
same as 
``` 
if condition: 
   value = true-expr
else: 
   value = false-expr
```
- Using ternary expressions might decrease readability of the code if the true and false expressions are complex. 
