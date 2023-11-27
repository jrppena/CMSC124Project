
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
