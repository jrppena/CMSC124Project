import subunits as s

class Typecasting():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars

    def str_to_num(self) -> int: 
        self.tab.capture = self.tab.capture_group[0]
        try:
            res = s.Data_Type(self.tab).numbr()
        except: 
            res = s.Data_Type(self.tab).numbar() 
        return res