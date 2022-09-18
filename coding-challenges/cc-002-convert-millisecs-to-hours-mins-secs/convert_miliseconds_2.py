while True:
    milis = input("Enter time in milliseconds, type 'exit' to end the program: ")
    if milis != "exit":
        try:
            milis = int(milis)
            if milis >= 1000:
                milis = int(milis)
                seconds=(milis/1000)%60
                seconds=int(seconds)
                minutes=(milis/(1000*60))%60
                minutes=int(minutes)
                hours=(milis/(1000*60*60))%24
                days=(milis/(1000*60*60*24))%30
                print("%d:%d:%d:%d" % (days,hours, minutes, seconds))
            elif milis >=1 and milis<1000:
                print(milis,"ms")
            else:
                print("invalid value it must be bigger than 0")
        except:
            print("invalid value, please enter an intiger and it must be bigger than 0")
    else:
        print("Exiting the program... Good Bye")
        break