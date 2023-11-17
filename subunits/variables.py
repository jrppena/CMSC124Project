

class Variable():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        # <init_variables> ::= WAZZUP <linebreak> <undec_variable>
        # <undec_variable> ::= (BUHBYE | I HAS A <variable> (<linebreak> | <dec_variable>))
        # <dec_variable> ::= ITZ (<expression> | <literal> | <variable>) <linebreak> <undec_variable>

        self.pars.get_rid("^WAZZUP ?")
        self.pars.get_rid_new_line()

        while True:

            self.pars.get_rid("^ *")

            if self.pars.get_rid("^BUHBYE ?", False):
                # self.pars.get_rid_new_line()
                return

            # I HAS A <variable>
            self.pars.get_rid("^I HAS A ")
            var_name = self.pars.get_lexemes(["variable"])

            # if uninitialized variable set to None, nexline
            if not self.pars.get_rid("^ITZ ", False):
                self.tab.variables[var_name] = None
                self.pars.get_rid_new_line()
                continue
            
            # if initialize, can pick between "expression", "literal", "variable" (variable here is inside literal)
            self.tab.variables[var_name] = self.pars.get_lexemes(["expression", "literal"])
            self.pars.get_rid_new_line()

            print(self.tab.variables)
        
    def put_var(self):
        # gets the 
        var_name = self.tab.capture_group[0]
        return var_name


    def get_var(self):
        # gets the variable and looking for it in the table of variable
        var_name = self.tab.capture_group[0]
        get_var = True if var_name in self.tab.variables.keys() else False

        if get_var:
            return var_name
