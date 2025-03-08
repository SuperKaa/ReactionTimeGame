import keyboard
import random
import time

def writetxt(newdata):
    with open("pb.txt", "w") as txt:
        txt.write(newdata)

def readtxt():
    with open("pb.txt", "r") as txt:
        data = txt.read()
    return  data

def mainpart():

    print(f"your current personal best is {readtxt()}")

    keys = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

    chosen = random.choice(keys)

    print(5)
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print()

    time1 = time.time()

    print(chosen)

    while True:
        if keyboard.is_pressed(chosen):
            time2 = time.time()
            print("pressed")
            break

    timetaken = time2 - time1
    timetaken = round(timetaken, 2)

    print(f"{timetaken} seconds to press {chosen}")

    if timetaken < float(readtxt()):
        writetxt(str(timetaken))
        print("new personal best!")
    else:
        print("you didnt beat your personl best try again")

turn = 0

while True:
    
    if turn > 0:
        input("press enter to start reaction time game again")
    else:
        input("press enter to start reaction time game")
    turn += 1
    mainpart()
