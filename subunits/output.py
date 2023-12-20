
class Output():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars
        

    def main(self):
        self.__concat("^\+ ")
        self.tab.terminal += self.concat

    def concatination(self):
        self.__concat()
        self.tab.variables["IT"] = self.concat

    def __concat(self, delimiter= "^AN "):

        # <output>::= VISIBLE <literal> <concat>
        # <concat> ::= <linebreak> | + <literal> <concat> 
        self.concat = ""
        self.concat += str(self.pars.get_lexemes(["boolean", "infinite","expression", "literal"]))


        while True:
            if self.pars.get_rid("^! ?","delimeter"):
                self.pars.get_rid_new_line()
                break
            if self.pars.get_rid_new_line(error = False):
                self.concat+= "\n"
                break

            self.pars.get_rid(delimiter,"delimeter", "There should be '+' to concatinate")
            self.concat += str(self.pars.get_lexemes(["boolean", "infinite","expression", "literal"]))






            
        



 
