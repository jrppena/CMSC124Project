import re

class Data_Type ():

    def __init__(self, tab) -> None:
        self.tab = tab
        

    def numbr(self):
        
        return int (re.search("^-?[0-9]+", self.tab.capture).group())
    
    def numbar(self):
        
        return float (re.search("^-?[0-9]+(\.[0-9]+)?", self.tab.capture).group())
    
    def yarn(self):

        pass

    def troof(self): 
        pass
