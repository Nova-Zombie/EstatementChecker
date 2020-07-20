from errorCatcherForStatements import errorCatcherForStatements

def main():
    choice = -1

    while choice != 0:
        choice = int(input("Enter 1 to search a keyword, \nEnter 0 to Exit: "))
        if choice == 1:
            keyword = input("Enter a keyword to search statements: ")
            errorCatcherForStatements(keyword)
        else:
            exit(0)

main()