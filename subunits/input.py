import subunits as s

class Input():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "variable name", "there should be a variable")
        var = s.Variable(self.tab, self.pars).get_var()
        self.tab.show_data()
        self.tab.root_front.wait_variable(self.tab.buffer)
        self.tab.variables[var]  = self.tab.buffer.get().strip()
        self.pars.get_rid_new_line()
        return  self.tab.variables[var]

