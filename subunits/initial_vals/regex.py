
import re
class Regex: 
    def __init__(self) -> None:
        self.code = []
        self.lexeme_anot = [] # lexemes and anotation
        self.result_lexemes = [] # only the lexemes

        self.lexemes= ['^I HAS A ','^BTW .*$','^[a-zA-Z][a-zA-Z0-9_]* ', '^-?[0-9]+$', '^-?[0-9]+(\.[0-9]+)?$', 
                '^\”.*\” $', '^(WIN|FAIL)$',  
                '^HAI$', '^KTHXBYE$', '^WAZZUP$', '^BUHBYE$',  '^OBTW .*\n$',
                '^TLDR$',  '^ITZ ', '^R ', '^SUM OF ', '^DIFF OF ',
                '^PRODUKT OF ', '^QUOSHUNT OF ', '^MOD OF ', '^BIGGR OF ', '^SMALLR OF ',
                '^BOTH OF ', '^EITHER OF ', '^WON OF ', '^NOT ', '^ANY OF ', '^ALL OF ',
                '^BOTH SAEM ', '^DIFFRINT ', '^SMOOSH ', '^MAEK ', '^A ', '^IS NOW A ', 
                '^VISIBLE ', '^GIMMEH ', '^O RLY\?$', '^YA RLY\?$', '^MEBBE ', '^NO WAI ', 
                '^OIC$', '^WTF\?$', '^OMG ', '^OMGWTF ', '^IM IN YR ', '^UPPIN ', '^NERFIN ', 
                '^YR ', '^TIL ', '^WILE ', '^IM OUTTA YR ', '^HOW IZ I ', '^IF U SAY SO$', 
                '^FOUND YR ', '^I IZ ', '^MKAY ']
        
    
    def get_lexemes(self):
        for line_number, line in enumerate(self.code):
            remaining_string = line

            # if there is a space in the start of the line
            res = re.search("^ *", remaining_string)
            if res:
                remaining_string=  self.get_data(-1, res, remaining_string)
    
            # finding the right regex for the current string 
            print(remaining_string)
            # while remaining_string:
            for regex_index, regex in enumerate(self.lexemes):

                # search if the lexemes exis and adding it to the lexemes list[]
                res = re.search(regex, remaining_string)
                if res:
                    
                    remaining_string=  self.get_data(regex_index, res, remaining_string)
                    print(remaining_string)
                    break

    
    def get_data(self, regex_index, res, line):
        # this means that it is not included in the lexemes 
        if regex_index == -1:
            return line[res.span()[1]:]
        
        # adding the lexemes and adding the values
        self.lexeme_anot.append((self.lexemes[regex_index], res.group()))
        self.lexemes.append(res.group())
        return line[res.span()[1]:]

    
    def print_val(self):
        print(f"""
        Code: 
        {self.code}

        Lexemes Annotated : 
        {self.lexeme_anot}

""")



