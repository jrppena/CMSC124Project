
class IfElse():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        self.pars.get_rid_new_line()

        if self.tab.variables["IT"]:
            self.pars.run_lines("^NO WAI")
            self.pars.get_rid_new_line()
            self.pars.run_lines("^OIC", skip=True)
            self.pars.get_rid_new_line()
        else:
            self.pars.run_lines("^NO WAI", skip=True)
            self.pars.run_lines("^OIC")

    def skip(self):
        self.pars.get_rid_new_line()
        self.pars.run_lines("^OIC", skip=True)
        self.pars.get_rid_new_line()

