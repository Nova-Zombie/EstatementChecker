import re
import datetime

def errorCatcherForStatements():
    statments = open("Estatements/checker.txt")
    statments1 = statments.readlines()
    total = 0
    count = 0
    timeStart = datetime.datetime.now()

    for x in statments1:
        if "FRAME" in x: #searches for FRAME in statements

            val = re.search("[$]\d*[.]\d{2}", x)
            cutMoneySign = val.group().split('$') #returns an array of re.search - $ sign
            value = float(cutMoneySign[1]) #converts the reg exp to an int
            total += value
            count += 1
            print(x.strip())
            print(value, "paycheck number", count)
            stri = "${:.2f} total \n"
            print(stri.format(total))
    timeStop = datetime.datetime.now()
    timeDif = (float(timeStop.strftime("%f")) - float(timeStart.strftime("%f"))) *.000001
    timeDifstr = "{:.6f}"
    print()
    print(timeDifstr.format(timeDif) , "milliseconds to complete")
    #print(timeStart)
    #print(timeStop)




    return total

errorCatcherForStatements()