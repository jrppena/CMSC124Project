import subunits as s
import re

class Parser_Function():

    def __init__(self, tab) -> None:
        self.tab = tab
        
    # add here if you have an 'or' in your grammar
        """
        Naming convention for the context-free grammar
        self.cfg = {
            'abstractions' : {
                'regex1' : function1
                'regex2' : function2
            }
        }
        """
        self.cfg = {
            "number":{
                "^-?[0-9]+(\.[0-9]+)? ?": s.Data_Type(self.tab).numbar,
                "^-?[0-9]+ ?": s.Data_Type(self.tab).numbr,
                "^\"(-?[0-9]+(\.[0-9]+)?)\" ?" : s.Typecasting(self.tab, self).str_to_num,
            },

            "expression":{
                '^SUM OF ' : s.Arithmetic(self.tab, self).add, 
                '^DIFF OF ': s.Arithmetic(self.tab, self).minus,
                '^PRODUKT OF ': s.Arithmetic(self.tab, self).mul, 
                '^QUOSHUNT OF ': s.Arithmetic(self.tab, self).div , 
                '^MOD OF ': s.Arithmetic(self.tab, self).mod,
                '^BIGGR OF ': s.Arithmetic(self.tab, self).biggr,
                '^SMALLR OF ': s.Arithmetic(self.tab, self).smallr,
            },
            "input":{
                "^GIMMEH ": s.Input(self.tab, self).main
            }
        }

    def get_lexemes(self, cfg) :
        """Get lexemes

        This is where you implement the 'or' in your cfg. It loops over the
        regex of the 'abstractions' in self.cfg, will also run if one matches.
        Also already has error handler

        Args: 
            cfg (list[str]): List of string which abstractions inculded in the list

        Returns: 
            return (Any| None): what ever the function in being executed

        Examples:
            // will return the resulting value from the function and assigning it

            self.val1 = self.pars.get_lexemes(["expression", "number"])

            // printing the resulting value from the expression function

            print(pars.get_lexemes(["expression"]))
        """

        for abtraction in cfg:
            for reg in self.cfg[abtraction]:
                if res:= self.__get_data(reg):

                    return self.cfg[abtraction][reg]()
        else:
            self.error_handler()
                
    def __get_data(self, reg):
        """Get data
        search if there is a match. If there is a match: 
            add the column (currently being analyzed for error handler);
            puts the captured string in the table of values;
            removed the captured string in the line

        Args:
            reg (str): the keyword being removed using regex 

        Returns:
            res (regex class| None):  returns if there is mathc or none
        
        """
        res = re.search(reg, self.tab.line)
    
        if res:
            # print(self.tab.line) # comment if you dont like it
            self.tab.capture_group = res.groups()
            self.tab.column += res.span()[1]
            self.tab.capture = res.group()
            self.tab.line = self.tab.line[res.span()[1]:]

        return res                
    
    def get_rid (self, reg):
        """Get rid
        For context-free grammar with a certain keyword such as 'AN'
        or 'ITZ', 'get_rid' get rid of this keywords. If the keyword is 
        not seen error will be shown

        Args:
            reg (str): the keyword being removed using regex 

        Returns:
            res (regex class| None):  returns if there is mathc or none

        Examples: 
            self.pars.get_rid("^AN ")
        """
        res = self.__get_data(reg)
    
        if not res:
            self.error_handler()

        return res
    
    def get_rid_new_line(self):
        """Get rid new line
        
        This is a strict new line checker. It will also detect if there is a comment
        if there is a comment or \n, automatically go to next line.
        else error

        Return: (bool) : True if new line is executed
        
        """
        if self.__get_data("^ *BTW") or self.__get_data("^ *\n"):
            self.tab.new_line()
            return True
        
        self.error_handler()


    def error_handler (self):
        print("\nSYNTAX ERROR !!")
        print(f"There is an error in line {self.tab.row+1}:{self.tab.column}")

        print("\nFile")
        print(f".\{self.tab.file} {self.tab.row+1}:{self.tab.column}")
        print(f"\t{self.tab.row+1}. | {self.tab.code[self.tab.row].strip()}")
        print("\t"+" "*len(str(self.tab.row+1))+" "*(self.tab.column+4)+"^")
        print()

        exit()
