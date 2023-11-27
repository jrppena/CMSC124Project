import subunits as s
import inflect
import re

class Typecasting():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        print(f""" 
            capture: {self.tab.capture}
            capture group: {self.tab.capture_group}
            line: {self.tab.line}
            row: {self.tab.row}
        """)
        var = self.pars.get_lexemes(["variable"])
        get_var = True if var in self.tab.variables.keys() else False
        
        # if the variable is initialize,
        if get_var:
            type_of_cast = self.pars.get_lexemes(["literal"])
            value = self.tab.variables[var]
            variable_type = self.get_data_type(value)

        if variable_type == "NOOB":
            new_val = self.noob_to_type(value,type_of_cast)
        elif variable_type  == "TROOF":
            new_val = self.troof_totype(value,type_of_cast)

        elif variable_type  == "NUMBAR":
            new_val = self.numbar_to_type(value,type_of_cast)

        elif variable_type  == "NUMBR":
            new_val = self.numbr_to_type(value,type_of_cast)
            
        elif variable_type  == "YARN":
            new_val = self.yarn_to_type(value,type_of_cast)
        

        if new_val == None:
            print("Cannot typecast")
        else:
            self.tab.variables[var] = new_val
            print("Typecast succesful!: ", self.tab.variables[var])

    def get_data_type(self,data):
        if(type(data) == int):
            return "NUMBR"
        elif(type(data) == float):
            return "NUMBAR"
        elif(type(data) == str):
            if(data == "WIN" or data == "FAIL"):
                return "TROOF"
            else:
                return "YARN"
        
    def noob_to_type(self,value,type_of_cast,new_val=None):
        if type_of_cast == "TROOF":
            new_val = "FAIL"
        elif type_of_cast == "NUMBAR":
            new_val = 0.0
        elif type_of_cast == "NUMBR":
            new_val = 0
        elif type_of_cast == "YARN":
            new_val = ""

        return new_val

    def troof_to_type(self,value,type_of_cast,new_val=None):
        
        if type_of_cast == "NOOB":
            pass
        elif type_of_cast == "NUMBAR":
            if value == "WIN":
                new_val = 1.0
            else:
                new_val = 0.0
        elif type_of_cast == "NUMBR":
            if value == "FAIL":
                new_val = 1
            else:
                new_val = 0
        elif type_of_cast == "YARN":
            if(value == "FAIL"):
                new_val = ""
        return new_val

    def numbar_to_type(self,value,type_of_cast,new_val=None):
        if type_of_cast == "NOOB":
            pass
        elif type_of_cast == "TROOF":
            if(value == 0):
                new_val = "FAIL"
            else:
                new_val = "WIN"
        elif type_of_cast == "NUMBR":
            new_val = int(value)
        elif type_of_cast == "YARN":
            new_val =  str(round(value,2))

        return new_val
    
    def numbr_to_type(self,value,type_of_cast,new_val=None):
        p = inflect.engine()
        if type_of_cast == "NOOB":
            pass
        elif type_of_cast == "TROOF":
            if(value == 0.0):
                new_val = "FAIL"
            else:
                new_val = "WIN"
        elif type_of_cast == "NUMBAR":
            new_val = float(value)
        elif type_of_cast == "YARN":
            new_val =  p.number_to_words(value)
        return new_val
    
    def yarn_to_type(self,value,type_of_cast):

        if type_of_cast == "NOOB":
            pass
        elif type_of_cast == "TROOF":
            if(value == ""):
                new_val = "FAIL"
            else:
                new_val = "WIN"
        elif type_of_cast == "NUMBAR":
            if(value.isdigit()):
                new_val = float(value)
        elif type_of_cast == "NUMBR":
           if(value.isdigit()):
                new_val = int(value)

        return new_val

    def str_to_num(self) -> int: 
        self.tab.capture = self.tab.capture_group[0]
        try:
            res = s.Data_Type(self.tab).numbr()
        except: 
            res = s.Data_Type(self.tab).numbar() 
        return res

        
