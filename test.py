from errorCatcherForStatements import FindLines
#from averageCalc import averageCalc

def main():
    choice = -1

    while choice != 0:
        choice = int(input("Enter 1 to search a keyword, \nEnter 0 to Exit: "))
        if choice == 1:
            keyword = input("Enter a keyword to search statements: ")
            sl = FindLines(keyword)
            sl.searchKeyWord()
            sl.averageIncomePerMonth()
            #sl.searchKeyWord()
            #print(search.searchKeyWord())
        else:
            exit(0)

main()
