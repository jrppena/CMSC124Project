import subunits as s

class Input():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "variable name")
        var = self.tab.capture_group[0]
        get_var = True if var in self.tab.variables.keys() else False

        # if the variable is initialize,
        if get_var:
            self.tab.variables[var]  = input()
            self.pars.get_rid_new_line()
            return  self.tab.variables[var]
        
        self.tab.semantic_error(f"\'{var}\' variable is not initialized")
