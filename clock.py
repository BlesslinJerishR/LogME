import time
from datetime import datetime
import winsound
import string
import threading

keyboard = []
for key in string.ascii_letters:
    keyboard.append(key)
for num in range(10):
    keyboard.append(num)


def clock_banner():
    print("""
                                       ,--.-----.--.
                                       |--|-----|--|
                                       |--|     |--|
                                       |  |-----|  |
                                     __|--|     |--|__
                                    /  |  |-----|  |  \\
                                   /   \__|-----|__/   \\
                                  /   ______---______   \/\\
                                 /   /  11  1 2 / 1  \   \/
                                {   /10    ROLEX     2\   }
                                |  {     ,_.    /  ,_. }  |-,
                                |  |9  {   }  O--{- } 3|  | |
                                |  {   `-'  /    `-'   }  |-'
                                {   \8   7 /     5   4/   }
                                 \   `------_6_------'   /\\
                                  \     __|-----|__     /\/
                                   \   /  |-----|  \   /
                                    \  |--|     |--|  /
                                     --|  |-----|  |--
                                       |--|     |--|
                                       |--|-----|--|
                                       `--'-----`--'    
    """)


sec = 0
tok = True


def clock():
    global tok
    while tok:
        now = datetime.now()
        print(now.strftime("                                     %H  :  %M  :  %S"), end="\r", flush=True)


def clock_menu():
    clock_banner()
    global sec
    print(" ")
    print(f"""
    1. Five Mins
    2. Forty Mins
    3. One Hour
    4. Two Hour
    5. Custom
    """)
    print('>> ')
    option = int(input(''))
    if option == 1:
        sec = 300
        print('Break for 5 mins')
        time.sleep(300)
        print('Times Up, Get back on Track')
        alarm()
    elif option == 2:
        sec = 2400
        print('Concentrate for 40 mins')
        time.sleep(1800)
        print('Enjoy for 10 mins')
        alarm()
    elif option == 3:
        sec = 3600
        print('Concentrate for 1 hour')
        time.sleep(3600)
        print('Enjoy for 15 mins')
        alarm()
    elif option == 4:
        sec = 7200
        print('Concentrate for 2 hour')
        time.sleep(7200)
        print('Enjoy for 20 mins')
        alarm()
    elif option == 5:
        mins = int(input('Enter mins : '))
        secs = mins * 60
        time.sleep(secs)
        alarm()
    elif option == 0:
        # Test case
        # Secret option unlocked
        sec = 15
        time.sleep(10)
        alarm()


def dynamic_clock():
    c2 = threading.Thread(target=clock_menu)
    c2.start()
    time.sleep(5)
    c1 = threading.Thread(target=clock)
    c1.start()


# Alarm beep
def alarm():
    t1 = threading.Thread(target=alarm_start)
    t1.start()
    t2 = threading.Thread(target=alarm_stop)
    t2.start()


# Global Beep
beep = True


# Alarm Sound
def alarm_start():
    secs = 0
    global sec
    global beep
    while beep:
        winsound.Beep(940, 500)
        time.sleep(.5)
        secs += 1
        if secs == sec:
            beep = False


# Alarm stop
def alarm_stop():
    global beep
    global tok
    tok = False
    print("Stop the damn Clock !")
    stop = input('>> ')
    if stop in keyboard:
        print("Yo Snooze, Yo Loose")
        beep = False
        clock_menu()
