from Calculator import Calculator

cc = Calculator()

def printSign():
    print("""
            ░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗███████╗██████╗░
            ██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
            ██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░█████╗░░██████╔╝
            ██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
            ╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
            ░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝""")
    print("""
                                        ▄▀█ █▄░█ █▀▄
                                        █▀█ █░▀█ █▄▀
    """)
    print("""
            ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
            ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
            ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
            ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
            ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
            ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
    """)
    print("\t\tby Luis R. Cedillo")

def printMenu():
    print("")
    print("""
                █▀▄▀█ █▀▀ █▄░█ █░█
                █░▀░█ ██▄ █░▀█ █▄█
    """)
    print("")
    print("\t\tplease enter an action:")
    print("\t\t[A]: Convert Base N to Base 10","\t[B]: Convert Base 10 to Base N")
    print("\t\t[C]: Binary Addition","\t\t[D]: Binary Subtraction")
    print("\t\t[E]: Get 1's Complement","\t[F]: Get 2's Complement")
    print("\t\t[G]: Get Signed Magnitude")
    print("\t\t[*] Type exit to exit")
    print("")

def start():
    printSign()
    printMenu()
    start = True
    while start:
        print("")
        userAction = input("\t\tPlease select an action: ")
        if userAction == "A" or userAction == 'a': 
            print("\t\tAnswer: {}".format(cc.baseNtobase10()))
        if userAction == "B" or userAction == 'b': 
            print("\t\tAnswer: {}".format(cc.base10tobaseN()))
        if userAction == "C" or userAction == 'c': 
            print("\t\tAnswer: {}".format(cc.binarySimpleCalc(1)))
        if userAction == "D" or userAction == 'd': 
            print("\t\tAnswer: {}".format(cc.binarySimpleCalc(0)))
        if userAction == "E" or userAction == 'e': 
            print("\t\tAnswer: {}".format(cc.onescomplement()))
        if userAction == "F" or userAction == 'f': 
            print("\t\tAnser: {}".format(cc.twoscomplement()))
        if userAction == "G" or userAction == 'g': 
            print("\t\tAnswer: {}".format(cc.signedmagnitude()))
        if userAction == "exit": 
            print("\t\tThank You!")
            start = False
        
        if start: printMenu()

start()