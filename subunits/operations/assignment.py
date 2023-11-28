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

        # self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "variable", "there should be a variable")
        # var = self.tab.capture_group[0]
        # value = s.Variable(self.tab, self).get_var()
        # val = self.pars.get_rid("^(IS NOW A|R) ?", "operation assignment", "there should be either IS NOW A or R").group()

    def assign(self):
        val1 = self.pars.get_lexemes(["literal" ,"expression","statement"])

    def recasting(self):
        var = self.tab.capture_group[0]
        value = s.Variable(self.tab, self).get_var()
        new_val = s.Typecasting(self.tab, self).typecast(value)
        self.tab.variables[var] = new_val
        print("Successfully typecasted!")
