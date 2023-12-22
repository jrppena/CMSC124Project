HAI
    WAZZUP
        I HAS A choice ITZ 2
        I HAS A input ITZ 2002
    BUHBYE

    BTW if w/o MEBBE, 1 only, everything else is invalid
    VISIBLE "1. Compute age"
    VISIBLE "2. Compute tip"
    VISIBLE "3. Compute square area"
    VISIBLE "0. Exit"

    VISIBLE "Choice: "

    BOTH SAEM choice AN 1
    O RLY?
        YA RLY
            VISIBLE "Enter birth year: "
            VISIBLE DIFF OF 2022 AN input
OBTW
    BTW uncomment this portion if you have MEBBE
    BTW else, this portion should be ignored
        MEBBE BOTH SAEM choice AN 2
            VISIBLE "Enter bill cost: "
            VISIBLE "Tip: " PRODUKT OF input AN 0.1
        MEBBE BOTH SAEM choice AN 3
            VISIBLE "Enter width: "
            VISIBLE "Square Area: " PRODUKT OF input AN input
        MEBBE BOTH SAEM choice AN 0
            VISIBLE "Goodbye"
TLDR
        NO WAI
            VISIBLE "Invalid Input"
    OIC

    DIFFRINT BIGGR OF 3 AN choice AN 2
    O RLY?
        YA RLY
            VISIBLE "Invalid input is > 3."
            DIFFRINT BIGGR OF 3 AN choice AN 3
            O RLY?
                YA RLY 
                    VISIBLE "Pumasok ulit sa IT."
                NO WAI
                    VISIBLE "Pumasok sa NO WAI."
                OIC
    OIC

KTHXBYE