import initial_vals

class Comparison():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars
        self.literal1 = None
        self.literal2 = None
        self.literal3 = None
        self.result = None

    def main(self):
        # <comparison> ::= <both_saem> | <diffrint> 
        checker1 = self.tab.capture_group[0]
        self.literal1 = self.pars.get_lexemes(["expression", "number"])
        self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")

        if self.pars.get_rid("^(BIGGR OF|SMALLR OF) ", "delimiter"):
            checker2 = self.tab.capture_group[0]
            self.literal2 = self.pars.get_lexemes(["expression", "number"])
            if self.literal1 != self.literal2:
                self.tab.semantic_error(f"The two values {self.literal1} and {self.literal2} should be the same")
            self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")
            self.literal3 = self.pars.get_lexemes(["expression", "number"])
            self.checkRelOp(checker1, checker2)
            self.tab.variables["IT"] = self.result
            print(self.result)
            return self.result
            
        self.literal3 = self.pars.get_lexemes(["expression", "number"])
        if checker1 == "BOTH SAEM":
            self.result = self.literal1 == self.literal3
        elif checker1 == "DIFFRINT":
            self.result = self.literal1 != self.literal3
        self.tab.variables["IT"] = self.result
        print(self.result)
        return self.result

    def checkRelOp(self, checker1, checker2):
        if checker1 == "BOTH SAEM" and checker2 == "BIGGR OF":
            self.result = self.literal2 >= self.literal3
        elif checker1 == "BOTH SAEM" and checker2 == "SMALLR OF":
            self.result = self.literal2 <= self.literal3
        elif checker1 == "DIFFRINT" and checker2 == "BIGGR OF":
            self.result = self.literal2 < self.literal3
        elif checker1 == "DIFFRINT" and checker2 == "SMALLR OF":
            self.result = self.literal2 > self.literal3
        