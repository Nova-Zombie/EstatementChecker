import re
import datetime
class FindLines:
    def __init__(self, checkKeyWord):
        self.checkKeyWord = checkKeyWord
        self.path = "Estatements/checker.txt"
        self.total = 0
        self.totalPerMonth = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    def searchKeyWord(self):
        checkKeyWord = self.checkKeyWord
        statments = open(self.path, "r")
        total = 0
        count = 0
        timeStart = datetime.datetime.now()
        statments1 = statments.readlines()

        for x in statments1:
            if str(checkKeyWord).lower() in x.lower(): #searches for user key word and converts it to a string
                val = re.search('[$]\d*[,]*\d*[.]\d{2}', x)
                cutMoneySign = val.group().replace('$', '').replace(',', '') #returns an array of re.search - $ sign
                value = float(cutMoneySign) #converts the reg exp to an int
                total += value
                count += 1
                print(x.strip())
                print(value, "paycheck number", count)
                stri = "${:.2f} total \n"
                print(stri.format(total))
                self.total = total
        statments.close()
        timeStop = datetime.datetime.now()
        timeDif = (float(timeStop.strftime("%f")) - float(timeStart.strftime("%f"))) *.000001
        timeDifstr = "{:.6f}"
        print()
        print(timeDifstr.format(timeDif) , "milliseconds to complete \n")
        #print(timeStart)
        #print(timeStop)asdfasdf

    def averageIncomePerMonth(self):
        statments = open(self.path)
        statments1 = statments.readlines()
        total = self.total
        control = 0
        index = 0


        for x in statments1:
            if str(self.checkKeyWord).lower() in x.lower():
                transDate = re.search('\d{2}[/]\d{2}[/]\d{4}', x)
                getMonth = transDate.group().split('/')
                val = re.search('[$]\d*[,]*\d*[.]\d{2}', x)
                cutMoneySign = val.group().replace('$', '').replace(',', '')

                control += float(cutMoneySign)

                if(int(getMonth[0]) == 12):
                    self.totalPerMonth[11] += float(cutMoneySign)
                elif(int(getMonth[0]) == 11):
                    self.totalPerMonth[10] += float(cutMoneySign)
                elif(int(getMonth[0]) == 10):
                    self.totalPerMonth[9] += float(cutMoneySign)
                elif(int(getMonth[0]) == 9):
                    self.totalPerMonth[8] += float(cutMoneySign)
                elif(int(getMonth[0]) == 8):
                    self.totalPerMonth[7] += float(cutMoneySign)
                elif(int(getMonth[0]) == 7):
                    self.totalPerMonth[6] += float(cutMoneySign)

                elif(int(getMonth[0]) == 6):
                    self.totalPerMonth[5] += float(cutMoneySign)
                elif(int(getMonth[0]) == 5):
                    self.totalPerMonth[4] += float(cutMoneySign)
                elif(int(getMonth[0]) == 4):
                    self.totalPerMonth[3] += float(cutMoneySign)
                elif(int(getMonth[0]) == 3):
                    self.totalPerMonth[2] += float(cutMoneySign)
                elif(int(getMonth[0]) == 2):
                    self.totalPerMonth[1] += float(cutMoneySign)
                else:
                    self.totalPerMonth[0] += float(cutMoneySign)
        if(total == control):
            print("value are the same")
        else:
            print("value not same")
            print(self.total, " ",control)
        statments.close()

        for x in self.totalPerMonth:
            totalPerMonthStr = "${:.2f}"
            print("The total made for month  is ", index + 1 , totalPerMonthStr.format(self.totalPerMonth[index]) )
            index += 1






#errorCatcherForStatements(checkKeyWord = "FRAME")
