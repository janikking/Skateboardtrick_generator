import Saved
from Obstacles import Flatground, Rail, Kicker, Manualpad, Box
from Trick import FlatTrick, GrindTrick, SlideTrick, ManualTrick, CombinationTrick
from Line import Line


def makeTrick():
    trick = input("Whats the trick called?")
    try:
        yr = int(input("How often does the board flip? (leftside < 0 < rightside)"))
        xr = int(input("How often does the board rotate halfway? (frontside < 0 < backside)"))
        br = int(input("How often does the boarder rotate halfway? (frontside < 0 < backside)"))

    except:
        print("Please input numbers only")
        makeTrick()

    trickdetails = [trick, yr, xr, br]
    return trickdetails
    #Saved.flattricks.append(FlatTrick(trick, yr, xr, br))

def checkIfHelp(string):
    if(string == "help"):
        printTricks()

def printTricks():

    loop = True
    while(loop):
        i = input("What list do you want to see?\n"
                          "(1) Flatground\n"
                          "(2) Slides/Grinds/Manuals\n")

        if(i == "1"):
            for trick in Saved.tricks:
                if(Saved.tricks[trick].type == "gaptrick"):
                    print(trick)
                    loop = False
        elif(i == "2"):
            for trick in Saved.tricks:
                if(Saved.tricks[trick].type != "gaptrick"):
                    print(trick)
                    loop = False



def printAllTricks():

    for trick in Saved.tricks:
        print(trick + ": " + Saved.tricks[trick].type)


def initTrick2():
    finalTrick = None
    finalObstacle = None
    finalIntotrick = None
    picked = False
    trickname = ""
    nextTrick = ""
    doTrick = ""

    print("You can type 'help' at any time to see the list of available tricks")

    while(not picked):
        try:
            trickname = str(input("Whats the name of the trick you want to do? (Any flatground trick)\n"))
            checkIfHelp(trickname)
            for trick in Saved.tricks:
                if(trickname == trick):
                    finalTrick = Saved.tricks[trick]
                    picked = True

        except Exception as e:
            print(str(e))

    picked = False


    while(not picked):
        doTrick = input("Do you want to %s into another trick ?(Any grind, slide or manual)\n"
                              "(0) No\n"
                              "(1) Yes\n"
                              %(trickname))
        checkIfHelp(doTrick)



        if(doTrick == "1"):
            while(not picked):
                nextTrick = str(input("What trick do you want to do %s into?\n" %(trickname)))
                checkIfHelp(nextTrick)

                for trick in Saved.tricks:

                    if(nextTrick == trick) & (Saved.tricks[trick].type != "gaptrick"):
                        finalIntotrick = Saved.tricks[trick]
                        picked = True

        elif(doTrick == "0"):
            finalIntotrick = None
            picked = True

    picked = False


    while(not picked):
        print("Available obstacles: ")
        if(finalIntotrick != None):
            for i in Saved.obstacles:
                if(Saved.obstacles[i].tricktypes.__contains__(finalIntotrick.type)):
                    print(i)

        else:
            for i in Saved.obstacles:
                if(Saved.obstacles[i].tricktypes.__contains__("gaptrick")):
                    print(i)

        obstacle = str(input("Which of these obstacles do you want to %s %s on?\n" %(trickname, nextTrick)))
        checkIfHelp(obstacle)

        for i in Saved.obstacles:
            if(i == obstacle):

                finalObstacle = Saved.obstacles[i]
                picked = True

    trickinfo = [finalTrick,  finalObstacle, finalIntotrick]
    return trickinfo

def makeline2():


    linename = str(input("What do you want to call the line?\n"))
    tricks = [None, None, None, linename]
    loop = True
    i = 0
    #tricks.append(None)
    while(loop):
        gettrick = initTrick2()
        tricks[i] = gettrick
        i += 1
        newTrick = int(input("Do you want to add another trick?\n(0) No\n(1) Yes\n"))

        if(newTrick == 1):
            if(i == 3):
                loop = False
        else:
            loop = False



    return tricks


