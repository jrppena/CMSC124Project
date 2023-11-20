import initial_vals

class Arithmetic():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars
        self.val1 = 0
        self.val2 = 0

    def main(self):
        # Use main function for the context-free grammar
        # <expression> | <number> AN <expression> | <number> 
        self.val1 = self.pars.get_lexemes(["expression" ,"number"])
        self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimeter")
        self.val2 = self.pars.get_lexemes(["expression", "number" ])
        

    def add(self):
        self.main()
        print(self.val1 , "+", self.val2)

        return self.val1 + self.val2
    
    def minus(self):
        self.main()
        print(self.val1 , "-", self.val2)

        return self.val1 - self.val2
    
    def mul(self):
        self.main()
        print(self.val1 , "*", self.val2)

        return self.val1 * self.val2
    
    def div(self):
        self.main()
        print(self.val1 , "/", self.val2)
        return int (self.val1 / self.val2)
    
    def mod (self):
        self.main()
        print(self.val1 , "%", self.val2)
        return self.val1 % self.val2
    
    def biggr(self):
        self.main()
        print(self.val1 , "max", self.val2)
        return max(self.val1, self.val2 )
    
    def smallr(self):
        self.main()
        print(self.val1 , "min", self.val2)
        return min(self.val1, self.val2 )