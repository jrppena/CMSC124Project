


class IfElse():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):

        if self.tab.variables["IT"]:
            self.pars.run_lines("^NO WAI")
            self.pars.run_lines("^OIC", skip=True)
        else:
            self.pars.run_lines("^NO WAI", skip=True)
            self.pars.run_lines("^OIC")

        