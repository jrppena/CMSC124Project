

# here you can call you functions 

from subunits import *

reg = Regex()
pars = Parser_Function()
tab = Tables_Values()

f = open('testcases\sample1.lol',  'r')

reg.code = f.readlines()

# Lexical analyzer
reg.get_lexemes()

reg.print_val()
