import re
import datetime
class FindLines:
    def __init__(self, checkKeyWord):
        self.checkKeyWord = checkKeyWord


    def searchKeyWord(self):
        checkKeyWord = self.checkKeyWord
        statments = open("Estatements/checker.txt")
        statments1 = statments.readlines()
        total = 0
        count = 0
        timeStart = datetime.datetime.now()

        for x in statments1:
            if str(checkKeyWord).lower() in x.lower(): #searches for user key word and converts it to a string
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
        print(timeDifstr.format(timeDif) , "milliseconds to complete \n")
        #print(timeStart)
        #print(timeStop)asdfasdf






#errorCatcherForStatements(checkKeyWord = "FRAME")