
print("ayusin nlng hehe")

class Switch():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        self.pars.get_rid_new_line()
        self.pars.get_rid("^ *", "spacing")
        self.pars.get_rid("^WTF\?", "switch statement", "There should be a 'WTF?' switch-statement")
        self.pars.get_rid_new_line()
        
        delimiter = "^(OMG|OMGWTF) ?"
        has_run = False
        captured_delm = "WTF?"
        while True:
            if ((self.tab.variables["IT"] and not has_run) or (captured_delm == "OMGWTF" and not has_run)):
                self.pars.run_lines(delimiter)
                has_run = True
            else: # skip
                self.pars.run_lines(delimiter, skip=True)
        
    def skip(self):
        self.pars.run_lines("^OIC *", skip=True)