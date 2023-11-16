

# here you can call you functions 
from initial_vals import *
from subunits import *

tab = Tables_Values()
pars = Parser_Function(tab)

file = 'testcases\sample1.lol'
f = open( file,  'r')

tab.file = file
tab.code = f.readlines()

tab.row = 0
tab.line = tab.code[tab.row]

"""
Instructions in getting the classes up and running

1. Build your class in .\subunits folder
2. make sure that import your class in .\subunits\__init__.py
3. add the abtractions and regex in .\init_vals\parser_function.py 
    in self.cfg variable
4. to test if it is working you can execute it below this file

"""

# You can call you newly created lexemes here !!!
print(pars.get_lexemes(["expression"]))
print(pars.get_rid_new_line())
print()
print(pars.get_lexemes(["expression"]))
print()




    
