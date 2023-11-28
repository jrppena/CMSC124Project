import subunits as s
import inflect
import re

class Typecasting():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars
        self.type = {
            "str": "YARN",
            "int": "NUMBR",
            "float": "NUMBAR",
            "bool": "TROOF",
        }

    def main(self):
        print(f""" 
            capture: {self.tab.capture}
            capture group: {self.tab.capture_group}
            line: {self.tab.line}
            row: {self.tab.row}
        """)
        
        self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "variable", "there should be a variable")
        var = self.tab.capture_group[0]
        value = s.Variable(self.tab, self).get_var()
        type_of_cast = self.pars.get_rid("^(NUMBR|NUMBAR|YARN|TROOF) ?", "type literal", "there should be a type literal").group()
       
        variable_type = type(value).__qualname__

        variable_type = self.type[variable_type]

        operation_dict = {
            'NOOB': self.noob_to_type,
            'TROOF': self.troof_to_type,
            'NUMBAR': self.numbar_to_type,
            'NUMBR': self.numbr_to_type,
            'YARN': self.yarn_to_type   
        }

        new_val = operation_dict[variable_type](value,type_of_cast)
        
        if new_val == None:
            print("Cannot typecast")
        else:
            # self.tab.variables[var] = new_val
            print("Typecast succesful!: ", new_val)

        
    def noob_to_type(self,value,type_of_cast,new_val=None):
        
        conversion_rules = {
            "TROOF": False,
            "NUMBAR": 0.0,
            "NUMBR": 0,
            "YARN": ""
        }
        
        return conversion_rules[type_of_cast]
    
    def troof_to_type(self,value,type_of_cast,new_val=None):

        conversion_rules = {
            "NOOB": None,
            "NUMBAR": 1.0 if value == True else 0.0,
            "NUMBR": 1 if value == True else 0,
            "YARN": "" if value == False else None,  # Use value as the alternative
        }

        return conversion_rules[type_of_cast]

    def numbar_to_type(self,value,type_of_cast,new_val=None):
        
        conversion_rules = {
            "NOOB": None,
            "TROOF": False if value == 0 else True,
            "NUMBR": int(value),
            "YARN": str(round(value,2))
        }

        return conversion_rules[type_of_cast]
    
    def numbr_to_type(self,value,type_of_cast,new_val=None):

        p = inflect.engine()

        conversion_rules = {
            "NOOB": None,
            "TROOF": False if value == 0.0 else True,
            "NUMBAR": float(value),
            "YARN": p.number_to_words(value)
        }
        return conversion_rules[type_of_cast]

    
    def yarn_to_type(self, value, type_of_cast):
                
        conversion_rules = {
            "NOOB": None,
            "TROOF": False if value == "" else True,
            "NUMBAR": float(value) if value.isdigit() else None,
            "NUMBR": int(value) if value.isdigit() else None,
        }
        return conversion_rules[type_of_cast]

    def str_to_num(self) -> int: 
        self.tab.capture = self.tab.capture_group[0]
        try:
            res = s.Data_Type(self.tab).numbr()
        except: 
            res = s.Data_Type(self.tab).numbar() 
        return res

        
