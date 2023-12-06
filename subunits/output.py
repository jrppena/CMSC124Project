
class Output():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars
        

    def main(self):
        self.concatination("^\+ ")
        self.tab.terminal += self.tab.variables["IT"]

    def concatination(self, delimiter= "^AN "):

        # <output>::= VISIBLE <literal> <concat>
        # <concat> ::= <linebreak> | + <literal> <concat> 
        self.concat = ""
        self.concat += str(self.pars.get_lexemes(["boolean", "infinite","expression", "literal"]))


        while True:
            if self.pars.get_rid("^! ?","delimeter"):
                self.pars.get_rid_new_line()
                break
            if self.pars.get_rid_new_line(error = False):
                self.tab.terminal+= "\n"
                break

            self.pars.get_rid(delimiter,"delimeter", "There should be '+' to concatinate")
            self.concat += str(self.pars.get_lexemes(["boolean", "infinite","expression", "literal"]))


        self.tab.variables["IT"] = self.concat




            
        



 
