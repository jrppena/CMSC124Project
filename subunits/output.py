
class Output():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars
        self.concat = ""

    def main(self):
        self.concatination("+ ")

    def concatination(self, delimiter= "AN "):
        values = self.tab.line.split(delimiter)
        print(self.tab.variables)


        for val in values: 
            self.tab.line = val
            self.tab.capture = val
            self.concat += str(self.pars.get_lexemes(["literal"]))

            if self.pars.get_rid_new_line(error=False):
                break

        print(self.concat)
