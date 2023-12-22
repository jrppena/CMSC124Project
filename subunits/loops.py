
class Loops():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        print(f""" 
            capture: {self.tab.capture}
            capture group: {self.tab.capture_group}
            line: {self.tab.line}
            row: {self.tab.row}
        """)

        self.pars.get_rid("([a-zA-Z][a-zA-Z0-9_]*) ?", "label", "there should be a valid label")
        label = self.tab.capture
        print("label: ",label)

        self.pars.get_rid("(UPPIN|NERFIN) ?", "label", "there should be a valid label")
        operation = self.tab.capture
        print("operation: ",operation)

        self.pars.get_rid("YR ?", "delimeter", "there should be a YR delimeter")
        self.pars.get_rid("([a-zA-Z][a-zA-Z0-9_]*) ?", "label", "there should be a valid label")
        variable = self.tab.capture

        self.pars.get_rid("(TIL|WILE) ?", "condition")
        condition = self.tab.capture

        print("condition: ", condition)
        print(self.tab.line)
        # self.tab.semantic_error("here")
        var = self.pars.get_lexemes(["comparison"])
