import initial_vals

class Comparison():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars
        self.operation = ""
        self.literal1 = None
        self.literal2 = None
        self.literal3
        self.result = None

    def main(self):
        # <comparison> ::= <both_saem> | <diffrint> 
        self.literal1 = self.pars.get_lexemes(["comparison", "literal"])
        self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")
        self.literal2 = self.pars.get_lexemes(["comparison", "literal"])

    def both_saem(self):
        # <comparison> ::= BOTH SAEM <x> AN <y>
        self.main()
        if self.literal1 == self.literal2:
            self.result = True
        else:
            self.result = False
        return self.result

    def diffrint(self):
        # <comparison> ::= DIFFRINT <x> AN <y>
        self.main()
        if self.literal1 != self.literal2:
            self.result = True
        else:
            self.result = False
        return self.result

    def biggr_of(self):
        # <biggr_of> ::= BIGGR OF <x> AN <y>
        self.main()
        if self.literal1 > self.literal2:
            self.result = True
        else:
            self.result = False
        return self.result
    
    def smallr_of(self):
        # <smallr_of> ::= SMALLR OF <x> AN <y>
        self.main()
        if self.literal1 < self.literal2:
            self.result = True
        else:
            self.result = False
        return self.result
