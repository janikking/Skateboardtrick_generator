import socket
import ServerOperations
import pickle
import Saved
import threading
from util import b2s, s2b

myaddress = ('localhost', 1337)
maxsize = 4096

klaar = False


while(not klaar):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(myaddress)


    userinput = str(input("What do you want to do?\n"
                      "(0) Exit\n"
                      "(1) Create Trick\n"
                      "(2) Do a trick\n"
                      "(3) Make a line\n"
                      "(4) See tricks\n"
                      "(5) Close server and exit\n"))

    client.sendall(s2b(userinput))

    if(userinput == "0"):
        klaar = True

    elif(userinput == "1"):
        trickinfo = ServerOperations.makeTrick()


        pickledtrick = pickle.dumps(trickinfo)
        client.sendall(pickledtrick)
        print(b2s(client.recv(maxsize)))
        print(trickinfo)
    elif(userinput == "2"):
        donetrick = ServerOperations.initTrick2()
        print(donetrick)
    elif(userinput == "3"):
        lineinfo = ServerOperations.makeline2()
        pickledline = pickle.dumps(lineinfo)
        client.sendall(pickledline)
        s = b2s(client.recv(maxsize))
        print(s)

        outputinput = str(input("Do you want to save the line to a text file?\n"
                                "(0) No\n"
                                "(1) Yes\n"))

        if(outputinput == "1"):
            filename = lineinfo[3] + ".txt"
            with open(filename, "w") as f:
                try:
                    f.write(s[12:])
                    print("%s saved!\n" %(filename))

                except Exception as e:
                    print(str(e))


        else:
            pass


    elif(userinput == "4"):
        thread = threading.Thread(target=ServerOperations.printAllTricks())
        thread.start()


    elif(userinput == "5"):
        print("Shutting down...\n")
        client.sendall(s2b("kys"))
        client.close()
        klaar = True

