import re
from subunits import *



def get_data(regex_index, res, line):
    # this means that it is not included in the lexemes 

    return line[res.span()[1]:]
        






reg = Regex()
txt = "I HAS A var1 BTW YEEES!\n"


remaining = txt




while remaining:
    for regex_index, regex in enumerate(reg.lexemes):

        # search if the lexemes exis and adding it to the lexemes list[]
        res = re.search(regex, remaining)
        print(res,regex )
        if res:
            
            remaining= get_data(regex_index, res, remaining)
            print(remaining)
            break

    
