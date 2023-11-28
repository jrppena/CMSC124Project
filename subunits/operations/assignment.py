import initial_vals
import subunits as s


class Assignment():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars
        self.var = " "
        

    def main(self):
        print(f""" 
            capture: {self.tab.capture}
            capture group: {self.tab.capture_group}
            line: {self.tab.line}
            row: {self.tab.row}
        """)

        # self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "variable", "there should be a variable")
        # var = self.tab.capture_group[0]
        # value = s.Variable(self.tab, self).get_var()
        # val = self.pars.get_rid("^(IS NOW A|R) ?", "operation assignment", "there should be either IS NOW A or R").group()

    def assign(self):
        val1 = self.pars.get_lexemes(["literal" ,"expression","statement"])

    def recasting(self):
        var = self.tab.capture_group[0]
        value = s.Variable(self.tab, self).get_var()
        new_val = s.Typecasting(self.tab, self).typecast(value)
        self.tab.variables[var] = new_val
        print("Successfully typecasted!")










    # def logic_op(self):
    #     # <logic_op> ::= (BOTH OF | EITHER OF | WON OF) <literal> AN <literal>
    #     self.literal1 = self.pars.get_lexemes(["boolean", "literal"])
    #     self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")
    #     self.literal2 = self.pars.get_lexemes(["boolean", "literal"])

    # def both_of(self):
    #     self.logic_op()
    #     print(self.literal1,"and",self.literal2)
    #     self.result = self.literal1 and self.literal2
    #     print(self.result)
    #     return self.result

    # def either_of(self):
    #     self.logic_op()
    #     print(self.literal1,"or",self.literal2)
    #     self.result = self.literal1 or self.literal2
    #     print(self.result)
    #     return self.result

    # def won_of(self):
    #     # <won_of> ::= WON OF <literal> AN <literal>
    #     self.logic_op()
    #     print(self.literal1,"xor",self.literal2)
    #     self.result = (self.literal1 or self.literal2) and not (self.literal1 and self.literal2)
    #     print("xor:",self.result)
    #     return self.result

    # def not_operation(self):
    #     # <not_operation> ::= NOT <boolean> | NOT <literal>
    #     self.literal1 = self.pars.get_lexemes(["boolean", "literal"])
    #     self.result = not self.literal1
    #     print("not:", self.result)
    #     return self.result

    # def all_of(self):
    #     # <all_of> ::= ALL OF <boolean> | <literal> AN <boolean> | <literal> <loop> | MKAY
    #     self.literal1 = self.pars.get_lexemes(["boolean", "literal"])
    #     self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")
    #     self.literal2 = self.pars.get_lexemes(["boolean", "literal"])
    #     self.result = self.literal1 and self.literal2

    #     while True:
    #         if self.pars.get_rid("^MKAY ?", "delimiter"):
    #             break
    #         self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")
    #         self.literal1 = self.pars.get_lexemes(["boolean", "literal"])
    #         self.result = self.result and self.literal1

    #     print("all of:", self.result)


    # def any_of(self):
    #     # <any_of> ::= ANY OF <boolean> | <literal> AN <boolean> | <literal> <loop> | MKAY
    #     self.literal1 = self.pars.get_lexemes(["boolean", "literal"])
    #     self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")
    #     self.literal2 = self.pars.get_lexemes(["boolean", "literal"])
    #     self.result = self.literal1 or self.literal2

    #     while True:
    #         if self.pars.get_rid("^MKAY ?", "delimiter"):
    #             break
    #         self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")
    #         self.literal1 = self.pars.get_lexemes(["boolean", "literal"])
    #         self.result = self.result or self.literal1

    #     print("all of:", self.result)