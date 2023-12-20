import initial_vals
import subunits as s


class Assignment():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars
        self.var = " "
        
    def main(self):
        print(f""" 
            capture: {self.tab.capture}
            capture group: {self.tab.capture_group}
            line: {self.tab.line}
            row: {self.tab.row}
        """)

    def assign(self):
        var_name = self.tab.capture_group[0]
        value = s.Variable(self.tab, self.pars).get_var()        
        if(self.pars.get_rid("^MAEK ?", "typecasting")):
            
            self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "variable", "there should be a variable")
            self.pars.get_rid("^A ", "delimeter", "there should be an A delimeter")

            other_var = self.tab.capture
            other_val = s.Variable(self.tab, self.pars).get_var()
            new_val = s.Typecasting(self.tab, self.pars).typecast(other_val)
            self.tab.variables[var_name] = new_val
            print("Successfully typecasted!")
        else:
            assigned_value = self.pars.get_lexemes(["literal","variable","expression"])
            self.tab.variables[var_name] = assigned_value
            print("Succesfully assigned")
            
    def recasting(self):
        var = self.tab.capture_group[0]
        value = s.Variable(self.tab, self.pars).get_var()
        new_val = s.Typecasting(self.tab, self.pars).typecast(value)
        self.tab.variables[var] = new_val
        print("Successfully typecasted!")

