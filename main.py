

# here you can call you functions 
from initial_vals import *
from subunits import *

tab = Tables_Values()
pars = Parser_Function(tab)

f = open('testcases\sample1.lol',  'r')

tab.code = f.readlines()

# print(tab.code)


for i , line in enumerate(tab.code):
    tab.row = i
    tab.line = line

    print(pars.get_lexemes(["expression"]))
    print()

    tab.column = 0


    
