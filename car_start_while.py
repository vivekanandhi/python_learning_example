command =""
started = False
while True:
    command = input('>').lower()
    if command == 'start':
        if started:
            print('car is already started!')
        else:
            started = True
            print('car started...Ready to go!')
    elif command == 'stop':
        if not started:
            print('car is already stopped!')
        else:
            started = False
            print('car stopped')
    elif command == 'help':
        print("""Start - to start the car
Stop - to stop the car
Quit - to exit""")
    elif command == 'quit':
        break
    else:
        print("I don't understand that..")


