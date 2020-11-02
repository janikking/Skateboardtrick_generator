import socket
import Line
import Saved
import pickle
from util import b2s, s2b
import threading
import ServerOperations
from Trick import FlatTrick, GrindTrick, SlideTrick, ManualTrick, CombinationTrick


def saveReceivedLine(line):
    t1 = line[0]
    t2 = line[1]
    t3 = line[2]
    line[0] = CombinationTrick(t1[0], t1[1], t1[2])
    if(line[1] != None):
        line[1] = CombinationTrick(t2[0], t2[1], t2[2])
    if(line[2] != None):
        line[2] = CombinationTrick(t3[0], t3[1], t3[2])
    return line


def checkIfNone(check):
    if (check == None):
        return True

myaddress = ('localhost', 1337)
maxsize = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(myaddress)
server.listen(5)

klaar = False

print("Server is listening...\n")

while(not klaar):
    client, addr = server.accept()
    receiveOperation = b2s(client.recv(maxsize))

    if(receiveOperation == "1"):
        print("Waiting for trick..\n")
        receivedTrick = client.recv(maxsize)
        trick = pickle.loads(receivedTrick)
        trickname = trick[0].replace(" ", "")
        trickname = trickname.lower
        Saved.tricks[trickname] = FlatTrick(trick[0], trick[1], trick[2], trick[3])
        s = "Trick saved! \n" + Saved.tricks[trickname].trickDescription()
        client.sendall(s2b(s))
        print("Trick made.\n")

    elif(receiveOperation == "3"):
        a = ''
        print("Waiting for line..\n")
        receivedLine = client.recv(maxsize)
        line = pickle.loads(receivedLine)
        line = saveReceivedLine(line)

        Saved.lines[line[3]] = Line.Line(line[0], line[1], line[2])
        a = Saved.lines[line[3]].performLine()
        s = "Line saved! \n" + a
        client.sendall(s2b(s))
        print("Line made.\n")

    elif(receiveOperation == "5"):
        print("Im out.")
        server.close()
        klaar = True


