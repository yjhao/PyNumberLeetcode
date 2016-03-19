from random import randint
import sys

class problemSet(object):

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
            if item != '':
                self.addToSet(int(item))

    def saveToFile(self):
        with open("number.txt", "w") as myfile:
            for item in sorted(self.list):
                myfile.write(str(item))
                myfile.write(",")

    def appendToFile(self,val):
        with open("number.txt", "a") as myfile:
            myfile.write(",")
            myfile.write(str(val))

    def addToSet(self, val):
        if val not in self.list:
            self.list.add(int(val))

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

    def ifExist(self, val):
        if val in self.list:
            return True
        return False


class pyNumber(object):

    def __init__(self):
        self.py = problemSet()
        self.py.readFromFile()

    def addOne(self):
        if (len(sys.argv)>1):
            first_arg = sys.argv[1]
            second_arg = sys.argv[2]
            addProblem = -1

            if (first_arg=="add"):
                addProblem = int(second_arg)
                if not self.py.ifExist(addProblem):
                    self.py.addToSet(addProblem)
                    self.py.saveToFile()
                    print "\n Successfully add question", addProblem, "to your list!\n"
                else:
                    print "\n", addProblem, "already exists! Please add a different one!\n"

                sys.exit(0)

    def removeOne(self):
        if (len(sys.argv)>1):
            first_arg = sys.argv[1]
            second_arg = sys.argv[2]
            removeProblem = -1

            if (first_arg=="remove"):
                removeProblem = int(second_arg)
                if self.py.ifExist(removeProblem):
                    self.py.removeFromSet(removeProblem)
                    print "\n Successfully remove question", removeProblem, "from your list!\n"
                else:
                    print "\n", removeProblem, "does not exist! Please choose a different one!\n"

                sys.exit(0)

    def check(self):
        if (len(sys.argv)>1):
            first_arg = sys.argv[1]
            second_arg = sys.argv[2]

            if (first_arg=="check"):
                checkProblem = int(second_arg)
                if self.py.ifExist(checkProblem):
                    print "\n Found question", checkProblem, "from your list!\n"
                else:
                    print "\n", checkProblem, "does not exist\n"

                sys.exit(0)




    def getNext(self):
        nextNumber = self.py.getNextNumber()

        print "\nNext question is:", nextNumber

        nb = raw_input('Do you accept it?  Y(yes) or N(no)\n')

        while nb!="y":
            nextNumber = self.py.getNextNumber()
            print "\nTry one more time. Next question is:", nextNumber
            nb = raw_input('Do you accept it?  Y(yes) or N(no)\n')

        print "You accept the question ", nextNumber, "!\n\n"
        self.py.addToSet(nextNumber)
        self.py.saveToFile()



def __main__():
    generator = pyNumber()
    generator.addOne()
    generator.removeOne()
    generator.check()
    generator.getNext()


__main__()



