
class IfElse():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        self.pars.get_rid_new_line()
        self.pars.get_rid_spacing()
        self.pars.get_rid("^YA RLY", "if statement", "There should be a 'YA RLY' if-statement")
        self.pars.get_rid_new_line()
        
        delimiter = "^(NO WAI|MEBBE|OIC) ?"
        has_run = False
        captured_delm = "YA RLY"
        while True:
            if ((self.tab.variables["IT"] and not has_run) or (captured_delm == "NO WAI" and not has_run)): # YA RLY and MEBBE, and NO WAI
                self.pars.run_lines(delimiter)
                has_run = True
            else: # skip
                self.pars.run_lines(delimiter, skip=True)

            captured_delm = self.tab.capture_group[0] # capture delimiter
            
            if captured_delm == "OIC": 
                self.pars.get_rid_new_line()
                break 
            elif captured_delm == "NO WAI":
                self.pars.get_rid_new_line()
                delimiter = "^(OIC) ?"
                continue
            else: # MEBBE
                self.pars.get_lexemes(["comparison"])
                continue

    def skip(self):
        self.pars.run_lines("^OIC *", skip=True)
