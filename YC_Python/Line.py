import Saved

class Line:

    tricks = []

    def __init__(self, trick1, trick2=None, trick3=None):
        self.trick1 = trick1
        self.tricks.append(self.trick1)
        if(trick2 != None):
            self.trick2 = trick2
            self.tricks.append(self.trick2)
        if(trick3 != None):
            self.trick3 = trick3
            self.tricks.append(self.trick3)


    def performLine(self):
        s = ""

        for i in range(len(self.tricks)):
            s = s + str(self.tricks[i]) + ".\n"

        return s