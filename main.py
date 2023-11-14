

# here you can call you functions 
from initial_vals import *
from subunits import *

tab = Tables_Values()
pars = Parser_Function(tab)

file = 'testcases\sample1.lol'
f = open( file,  'r')

tab.file = file
tab.code = f.readlines()

for i , line in enumerate(tab.code):
    tab.row = i
    tab.line = line

    print(pars.get_lexemes(["expression"]))
    print()

    tab.column = 0


    
