
class Output():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars
        

    def main(self):
        self.__concat("^\+ ")
        self.tab.terminal += self.concat
        print("terminal:", self.tab.terminal)

    def concatination(self):
        self.__concat()
        self.tab.variables["IT"] = self.concat

    def __concat(self, delimiter= "^AN "):

        # <output> ::= VISIBLE <literal> <concat>
        # <concat> ::= <linebreak> | + <literal> <concat> 
        self.concat = ""
        self.concat += str(self.pars.get_lexemes(["boolean", "concatination", "infinite", "expression", "comparison", "literal"]))
        print("concat:", str(self.concat))

        while True:
            if self.pars.get_rid("^! ?","delimeter"):
                self.pars.get_rid_new_line()
                break
            if self.pars.get_rid_new_line(error = False):
                self.concat+= "\n"
                break
        
            self.pars.get_rid(delimiter, "delimiter", f"There should be {delimiter} to concatinate")
            self.concat += str(self.pars.get_lexemes(["boolean", "concatination",  "infinite", "expression", "comparison",  "literal"]))
 
