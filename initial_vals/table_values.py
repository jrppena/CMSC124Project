

class Tables_Values:
    def __init__(self) -> None:
        self.file = " "
        self.capture = " "
        self.code = []
        self.row = 0
        self.column =0 
        self.line = " "
        self.variables = []
        self.function_names = []
        self.stack = []

    def new_line(self):
        self.row+=1
        self.line = self.code[self.row]