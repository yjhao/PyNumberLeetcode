from random import randint

class pyNumber(object):

    def __init__ (self):
        self.list = set()
        self.lower = 0
        self.higher = 330
        self.readFromFile()

    def readFromFile(self):
        f = open('number.txt', 'r')
        lines = f.read().split(',')
        f.close()
        for item in lines:
            self.addToSet(item)

    def saveToFile(self):
        with open("number.txt", "w") as myfile:
            for item in self.list:
                myfile.write(str(item))
                myfile.write(",")

    def appendToFile(self,val):
        with open("number.txt", "a") as myfile:
            myfile.write(",")
            myfile.write(str(val))

    def addToSet(self, val):
        if val not in self.list:
            self.list.add(val)

    def removeFromSet(self, val):
        if val in self.list:
            self.list.remove(val)
        self.saveToFile()

    def printList(self):
        print "Answered questions are: "
        for item in self.list:
            print item

    def randomNumber(self):
        val = (randint(self.lower,self.higher))
        return val

    def getNextNumber(self):
        nextNumber = self.randomNumber()
        while(nextNumber in self.list):
            nextNumber = self.randomNumber()
        return nextNumber


### main Function

def __main__():
    py = pyNumber()
    py.readFromFile()

    nextNumber = py.getNextNumber()

    print "\nNext question is:", nextNumber

    nb = raw_input('Do you accept it?  Y(yes) or N(no)\n')

    while nb!="y":
        nextNumber = py.getNextNumber()
        print "\nTry one more time. Next question is:", nextNumber
        nb = raw_input('Do you accept it?  Y(yes) or N(no)\n')

    print "You accept the question ", nextNumber, "!\n\n"
    py.addToSet(nextNumber)
    py.appendToFile(nextNumber)



__main__()




