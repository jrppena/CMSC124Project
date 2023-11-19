
class Output():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars
        self.concat = ""

    def main(self):
        self.concatination("^\+ ")

    def concatination(self, delimiter= "^AN "):
        # <output>::= VISIBLE <literal> <concat>
        # <concat> ::= <linebreak> | + <literal> <concat> 
        self.tab.terminal += str(self.pars.get_lexemes(["literal"]))

        while True:
            if self.pars.get_rid("^! ?","delimeter"):
                self.pars.get_rid_new_line()
                break
            if self.pars.get_rid_new_line(error = False):
                self.tab.terminal+= "\n"
                break

            self.pars.get_rid(delimiter,"delimeter", "There should be '+' to concatinate")
            self.tab.terminal += str(self.pars.get_lexemes(["literal"])) 




            
        



 
