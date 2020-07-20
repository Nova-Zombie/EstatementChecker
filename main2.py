def main():
    statements = ["C:/Users/tommy/BalanceReader/venv/Estatements/EstatementJan.txt", "C:/Users/tommy/BalanceReader/venv/Estatements/EstatementFeb.txt", "C:/Users/tommy/BalanceReader/venv/Estatements/EstatementMar.txt", "C:/Users/tommy/BalanceReader/venv/Estatements/EstatementApr.txt", "C:/Users/tommy/BalanceReader/venv/Estatements/EstatementMay.txt", "C:/Users/tommy/BalanceReader/venv/Estatements/EstatementJune.txt"]
    total = 0

    for x in statements:
        documents = open(x, "r")
        documents1 = documents.readlines()
        for x in documents1:
            if "Deposit ACH FRAME" in x:
                transaction = x.split(" ")
                print(transaction[5])
                t = float(transaction[5])
                total += t
                print(x)
    print("The total = ", total)
main()