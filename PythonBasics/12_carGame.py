print("Hello to the car game! Type in 'help' to see all commands")
helpCommand = ("start - to start the car",
               "stop - to stop the car", "quit - to exit the game")
startCommand = "Car started...Ready to go!"
stopCommand = "Car stopped."
commands = ("help", "start", "stop", "quit")
commandLine = ""
started = False
stopped = False

while commandLine != "quit":
    commandLine  = input(">").lower()
    if commandLine == "help":
        for command in helpCommand:
            print(command)
    elif commandLine == "start":
        if started:
            print("DUDE, you've  already started the car!")
        else:
            started = True
            stopped = False
            print(startCommand)
    elif commandLine == "stop":
        if stopped:
            print("Are you serious? You've already stopped the car!")
        else:
            stopped = True
            started = False
            print(stopCommand)
    elif commandLine == "quit":
        exit()
    else:
        print("Sorry I don't understand you!")


