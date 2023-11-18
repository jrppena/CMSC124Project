import subunits as s

class Input():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?")
        var = self.tab.capture_group[0]
        get_var = True if var in self.tab.variables.keys() else False

        if get_var:
            self.tab.variables[var]  = input()
            print(self.tab.variables)
            self.pars.get_rid_new_line()
            return  self.tab.variables[var]
        
        print("Semantic error!!")
        print(f"{var} is not initialized\n")