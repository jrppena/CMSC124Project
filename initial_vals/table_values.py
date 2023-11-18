

class Tables_Values:
    def __init__(self) -> None:

        self.capture = " "
        """Data type (str)
        This is where the lexemes are stored. 
        Note that it overwrites itself everytime it 
        encounters a lexeme
        """

        self.capture_group = " " 
        """Tuple[str]
        Tuple of captured in the regex
        """

        self.code = []
        """
        List if the code
        """

        self.line = " "
        """
            current line is assigned here
            this is the line we get the lexemes
        """

        self.variables = {'IT': None}
        """
        variables = {
            "var1": value
            "var2": value
        }
        
        """

        self.function = {}
        """
        function = {
            "func1": [code ..],
            "func2": [code ..],
        }
        
        """
        self.stack = []



        #  for error handling 
        self.file = " "
        self.row = 0        # current line index
        self.column =0      # current column

    def new_line(self):
        self.row+=1
        self.line = self.code[self.row]
        self.column =0