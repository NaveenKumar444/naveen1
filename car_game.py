i = ""
started = False
while True:
    i = input('> ').lower()
    if i == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif i == "start":
        if started:
            print("car was already started!!!")
        else:
            started = True
            print("car is started,,ready to go!!!")
    elif i == "stop":
        if not started:
            print("car was already stopped!!!")
        else:
            started = False
            print("car was stoped!!!")
    elif i == "quit":
        break
    else :
        print("option error!!!")


