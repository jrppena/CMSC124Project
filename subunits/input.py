import subunits as s

class Input():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        # grammar for variable
        self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "variable name", "there should be a variable")

        # get variable with error handling
        var = s.Variable(self.tab, self.pars).get_var()

        # put the current data in the front end
        self.tab.show_data()

        # wait for the users' input
        self.tab.root_front.wait_variable(self.tab.buffer)

        # format the user's input
        self.tab.variables[var]  = self.tab.buffer.get().strip()

        # grammar: new line
        self.pars.get_rid_new_line()
        return  self.tab.variables[var]

