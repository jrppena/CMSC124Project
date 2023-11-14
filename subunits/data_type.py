import re

class Data_Type ():

    def __init__(self, tab) -> None:
        self.tab = tab
        

    def numbr(self):
        
        return int (self.tab.capture.strip())
    
    def numbar(self):
        
        return float (self.tab.capture.strip())
    
    def yarn(self):

        pass

    def troof(self): 
        pass
