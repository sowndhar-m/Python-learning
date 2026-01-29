Python Basic: 
              Python is popular programming language, can be used on a sever to create the applications, software development, mathematics, system scripting. 
#prototyping: Code can be executed as soon as.
Python Indentation:
                Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.
Python variables:
                Variables are containers for storing data values.
                Variables do not need to be declared with any particular data type, and can even change type after they have been set. (If you want a specify data type is can be done by casting) x = str (7), 
 y = float (7), then (if you want a data type of the variable type () will be helpful). Print(type(y))
*Variables are case-sensitive (Below two variables are defined but “A” is not over write “a”)
e.g : a=7 
          A = “Sowndharraj”
Variable names: 
1.Variables must be Start alphabet or Underscore and it’s Contains alpha – numeric, underscore (A -z, 0-9, _), very important cannot start with a number.
2. case – sensitive and variable names cannot be any of the python keywords (and, if, for, while)
Multi Words Variable Names: 
Camel Case: myVariableName = "John" 
Pascal Case: MyVariableName = "John"
Snake case: my_variable_name = “John”
Many Values to Multiple Variables:
Python allows you to assign values to multiple variables in one line: 
x, y, z = "Orange", "Banana", "Cherry" (Make sure the number of variables matches the number of values, or else you will get an error.)
One Value to Multiple Variables:
you can assign the same value to multiple variables in one line:
x, y, z = “apple”

Unpack a Collection:
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
Python Data Types:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

Python Numbers: 
                 Int (Integers), float (decimal values), complex numbers (Real part + imaginary part)
Random number (Python does not have a random () function to make a random number, but Python has a built-in module called random that can be used to make random numbers)
import random
print (random.randrange(1, 10))
