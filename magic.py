import stdiomask
import time
import random
from irc.vpn import vpn, irc_menu
from hello import hellos
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from clock import dynamic_clock
from times import date, hour, mins, days_alive, year, month, day
from encrypt import encrypt, decrypt, write_key, load_key
from Quotes.quotes_1 import quotes_1
from Quotes.quotes_2 import quotes_2
from Quotes.quotes_3 import quotes_3
from Quotes.quotes_4 import quotes_4
from Quotes.quotes_5 import quotes_5
from Quotes.quotes_6 import quotes_6
from Quotes.quotes_7 import quotes_7
from Quotes.quotes_8 import quotes_8
from Quotes.quotes_9 import quotes_9
from Quotes.quotes_10 import quotes_10

# Mask

rules_file = f'Clogs/{year}/commandments.txt'
fiction_file = f'Clogs/{year}/fiction.txt'
thoughts_file = f'Clogs/{year}/thoughts.txt'
positive_file = f'Clogs/{year}/positive.txt'
negative_file = f'Clogs/{year}/negative.txt'
goals_file = f'Clogs/{year}/goals.txt'
bucket_file = f'Clogs/{year}/bucket.txt'
task_file = f'Clogs/{year}/tasker.txt'
irc_file = f'Clogs/{year}/irc.txt'

# files to flash
flash_files = {

    'rules_file': [f'Clogs/{year}/commandments.txt', 'commandments.txt', rules_file],
    'fiction_file': [f'Clogs/{year}/fiction.txt', 'fiction.txt', fiction_file],
    'thoughts_file': [f'Clogs/{year}/thoughts.txt', 'thoughts.txt', thoughts_file],
    'positive_file': [f'Clogs/{year}/positive.txt', 'positive.txt', positive_file],
    'negative_file': [f'Clogs/{year}/negative.txt', 'negative.txt', negative_file],
    'goals_file': [f'Clogs/{year}/goals.txt', 'goals.txt', goals_file],
    'bucket_file': [f'Clogs/{year}/bucket.txt', 'bucket.txt', bucket_file],
    'task_file': [f'Clogs/{year}/tasker.txt', 'tasker.txt', task_file],
    'irc_file': [f'Clogs/{year}/irc.txt', 'irc.txt', irc_file],
}

# Quotes Generator
quotes = [
    quotes_1,
    quotes_2,
    quotes_3,
    quotes_4,
    quotes_5,
    quotes_6,
    quotes_7,
    quotes_8,
    quotes_9,
    quotes_10,
]


def quotes_generator():
    random.shuffle(quotes)
    quotes_choice = random.choice(quotes)
    quote, author = random.choice(list(quotes_choice.items()))
    print(f"""
{quote}
by {author}
""")


# Tick Symbol
def tick():
    symbol = '\u2713'
    return symbol


# Hello Friend
def hello_friend():
    print("""
           _   _          _   _                 _____          _                      _     
          | | | |   ___  | | | |   ___         |  ___|  _ __  (_)   ___   _ __     __| |    
          | |_| |  / _ \ | | | |  / _ \        | |_    | '__| | |  / _ \ | '_ \   / _` |    
          |  _  | |  __/ | | | | | (_) |  _    |  _|   | |    | | |  __/ | | | | | (_| |  _ 
          |_| |_|  \___| |_| |_|  \___/  ( )   |_|     |_|    |_|  \___| |_| |_|  \__,_| (_)
                                         |/                                                 
                """)


# Root logo
def root_banner():
    print("""
                        :::..:..:::::::..:::::..:::.......::::.......::::::..:::::    
                        :::'##'##::::::'########:::'#######:::'#######::'########:
                        ::: ## ##:::::: ##.... ##:'##.... ##:'##.... ##:... ##..::
                        :'#########:::: ##:::: ##: ##:::: ##: ##:::: ##:::: ##::::
                        :.. ## ##.::::: ########:: ##:::: ##: ##:::: ##:::: ##::::
                        :'#########:::: ##.. ##::: ##:::: ##: ##:::: ##:::: ##::::
                        :.. ## ##.::::: ##::. ##:: ##:::: ##: ##:::: ##:::: ##::::
                        ::: ## ##:::::: ##:::. ##:. #######::. #######::::: ##::::
                        :::..:..:::::::..:::::..:::.......::::.......::::::..:::::
    """)


# Fiction Banner
def fiction_banner():
    print("""
         _  _  _  _  _              _                                       _                      _                                                    
        (_)(_)(_)(_)(_)            (_)                                     (_)                    (_)                                                   
        (_)                      _  _                 _  _  _            _ (_) _  _             _  _                 _  _  _            _  _  _  _      
        (_) _  _                (_)(_)              _(_)(_)(_)          (_)(_)(_)(_)           (_)(_)             _ (_)(_)(_) _        (_)(_)(_)(_)_    
        (_)(_)(_)                  (_)             (_)                     (_)                    (_)            (_)         (_)       (_)        (_)   
        (_)                        (_)             (_)                     (_)     _              (_)            (_)         (_)       (_)        (_)   
        (_)                      _ (_) _           (_)_  _  _              (_)_  _(_)           _ (_) _          (_) _  _  _ (_)       (_)        (_)   
        (_)                     (_)(_)(_)            (_)(_)(_)               (_)(_)            (_)(_)(_)            (_)(_)(_)          (_)        (_)   
                                                                                                                                                                                                                                                                                                          
    """)


def commandments_banner():
    print(f"""
             _______  _______  _______  _______  _______  _        ______   _______  _______  _       _________ _______     _    
            (  ____ \(  ___  )(       )(       )(  ___  )( (    /|(  __  \ (       )(  ____ \( (    /|\__   __/(  ____ \   ( )   
            | (    \/| (   ) || () () || () () || (   ) ||  \  ( || (  \  )| () () || (    \/|  \  ( |   ) (   | (    \/   | |   
            | |      | |   | || || || || || || || (___) ||   \ | || |   ) || || || || (__    |   \ | |   | |   | (_____  __| |__ 
            | |      | |   | || |(_)| || |(_)| ||  ___  || (\ \) || |   | || |(_)| ||  __)   | (\ \) |   | |   (_____  )(__   __)
            | |      | |   | || |   | || |   | || (   ) || | \   || |   ) || |   | || (      | | \   |   | |         ) |   | |   
            | (____/\| (___) || )   ( || )   ( || )   ( || )  \  || (__/  )| )   ( || (____/\| )  \  |   | |   /\____) |   | |   
            (_______/(_______)|/     \||/     \||/     \||/    )_)(______/ |/     \|(_______/|/    )_)   )_(   \_______)   (_)   

""")


def thoughts_banner():
    print(f"""
                     _____  _                           _      _        
                    |_   _|| |                         | |    | |       
                      | |  | |__    ___   _   _   __ _ | |__  | |_  ___ 
                      | |  | '_ \  / _ \ | | | | / _` || '_ \ | __|/ __|
                      | |  | | | || (_) || |_| || (_| || | | || |_ \__ \\
                      \\_/  |_| |_| \___/  \__,_| \__, ||_| |_| \__||___/
                                                  __/ |                 
                                                 |___/                      """)


def positive_banner():
    print("""
                        +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+   +-+ +-+
                        |P| |o| |s| |i| |t| |i| |v| |e|   |+| |+|
                        +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+   +-+ +-+    
    """)


def negative_banner():
    print("""
                        +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+
                        |N| |e| |g| |a| |t| |i| |v| |e| |-| |-|
                        +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+    
    """)


def goals_banner():
    print("""                                                                                                        
                        //   ) )                                         
                       //            ___        ___       //      ___    
                      //  ____     //   ) )   //   ) )   //     ((   ) ) 
                     //    / /    //   / /   //   / /   //       \ \     
                    ((____/ /    ((___/ /   ((___( (   //     //   ) )       
    """)


def bucket_banner():
    print("""                                                                                                                                                                                                                      
        //   ) )                                                            / /                                
       //___/ /                 ___       / ___      ___     __  ___       / /        ( )      ___     __  ___ 
      / __  (      //   / /   //   ) )   //\ \     //___) )   / /         / /        / /     ((   ) )   / /    
     //    ) )    //   / /   //         //  \ \   //         / /         / /        / /       \ \      / /     
    //____/ /    ((___( (   ((____     //    \ \ ((____     / /         / /____/ / / /     //   ) )   / /          
    """)


def logs_banner():
    print(f"""
        ___    _______                         ______  ___       _________      
        __ |  / /___(_)_____ ___      __       ___   |/  /______ ______  /_____ 
        __ | / / __  / _  _ \__ | /| / /       __  /|_/ / _  __ \_  __  / _  _ \\
        __ |/ /  _  /  /  __/__ |/ |/ /        _  /  / /  / /_/ // /_/ /  /  __/
        _____/   /_/   \___/ ____/|__/         /_/  /_/   \____/ \__,_/   \___/                                                                        
    """)


def mastermind_banner():
    print("""
            &&&&&&&&&&&&&&&%%%%%%%%%%#****#,*,(/,,,,,,,,,(#,,*/&&&#/&&&&&&&&&&&&&&&&&&&&&&&&
            &&&&&&&&&&&&&&&%%%%%%%%%%#,,,,,,,,,.,,,,,,,,,,...,,#%#**%%&&&&&&&&&&&&&&&&&&&&&&
            ,#&&&&&&&&&&&%%%%%%%#(%###,,,,,,,,,.,,,.,,,,,,...,,**,,*(%%&&%%&&&&&&&&&&&&&&&&&
            ..,#&&&&&&&&&&&&&&%%%/*(#(,,,,,,.,,.,,...,,,,,..,,,,,,,,/%%%#*#%&%%&&&&&&&&&&%,.
            ...,,#&&&&&&&&&&&&&%%#**,/..,,,,..,,,,...,,,,,.,,,,,,,,,(****%%&&&&&&&&&&&&%,...
            ......,/%&&&&&%&&%%%&%,,,,...,,,,...,.....,.,,,,,,,,,,,,,,,*%%%&&&&%&%%%%#,.....
            .........,*%&%&&&&&&&%*,,,,...,,,..........,,,,,,,,,,,,,,,,*%%&%&%&%&%%*......  
                .........,(%&&%(&&/.,,,,,.,,,(#........,,,((,,,,,,,,,,,#&&&&&%%%#,......    
                    ........,,#%,,%....,,,/##%%#*,.....,,#%%%##,,,,,,,*&&&#(&%,.....        
                         ...............,*#%%%#%##/,,,*##%%%%###,,,,,,#,,(%,..... .         
                          .          ...,#%%%#%%%%%#,###%%%%%%##,,,,,.,.......              
                           ... .     ...,(#%%%%%%%%%%##/######%#**,,..          .           
                                     ..(/%%%%#%%#####****((##%%###,..                       
                             . ,((....../###(////,*/***(##(#((###*....*...                  
                           .,###/#*/#,,/.,,///*..,,,,,,,,..*//,..././*(###(,                
                          ,*####/#**,*/#*,/*,,//..,,,,,,.,//**/,,#(**,//####(..             
                        /#########//*(/###,,,,,,*##(**/(/,,,,,,*##(*###(######/*.           
                      ,*,*(#######(**,/(##########/,((,(/########((*,(########(.            
                        ./#######/**/##(((,*,*(##/(####/(####**,*((/,###########(.          
                        *(#######/**####//,**###############(**/(*#*//##########/.          
                          *((#####*#####(#(/,,......,....,....,(*(,(*(/########(,           
                         ..,(######/#####(#(/,.****//,**/*,..,#/,,*/,(#########(*           
                           .,,(#####(/##(**(((*,,..........,(((,,,,,,,/######((,            
                             .(*,,******,,,,*(((((((#(((#((((*,,,,,,,(((((/((*..*           
                .              *//(/*,,,,,,,,,/#((#(##((((((,,,,,,,*(((((((/.               
             ./%*....         .,.*(((((((((,,,,,(((((((((((,,,,/(((((/,,/*.                 
            .#%%./%%,,.            ,(((/(((((,,,,/(((((((/,/((((((((((/  ..              .#/
            ###/*%%%(,,.             .*,/((((*/((//*///((((((((((,/*.,                  .###
            ###*#%%%%#/,.            .,    .,..*(,/((((((((((((*.,                   ..(,%%%
            ###(##%%%#%#,,                 .        .,,,*////* .                    .#%%/&&%
            ######%%%%%%(,,.                          ..                           ,%&&&%&&&
            %%%%%%%%%%%%%%,,,..                                                   .%%%%&&&&&    
    """)


def check_in_banner():
    print("""
                   ____   _                     _        _                       __
                  / ___| | |__     ___    ___  | | __   (_)  _ __               / /
                 | |     | '_ \   / _ \  / __| | |/ /   | | | '_ \      _      / / 
                 | |___  | | | | |  __/ | (__  |   <    | | | | | |     \ \   / /  
                  \____| |_| |_|  \___|  \___| |_|\_\   |_| |_| |_|      \_\ /_/   
                                                                   
    """)


def check_out_banner():
    print("""
                   ____   _                     _                        _      __  __
                  / ___| | |__     ___    ___  | | __     ___    _   _  | |_    \ \/ /
                 | |     | '_ \   / _ \  / __| | |/ /    / _ \  | | | | | __|    \  / 
                 | |___  | | | | |  __/ | (__  |   <    | (_) | | |_| | | |_     /  \ 
                  \____| |_| |_|  \___|  \___| |_|\_\    \___/   \__,_|  \__|   /_/\_\\
                                                                                                                                                             
    """)


def task_me_banner():
    print("""
                        #    # _______ #       #      # _     # _______ # _______ #
                     _  # _  #(_______)#       #      #| |    #(_______)#(_______)#
                    ( \ #( \ #    _    # _____ #  ___ #| |  _ # _  _  _ # _____   #
                     ) )# ) )#   | |   #(____ |# /___)#| |_/ )#| ||_|| |#|  ___)  #
                    (_/ #(_/ #   | |   #/ ___ |#|___ |#|  _ ( #| |   | |#| |_____ #
                        #    #   |_|   #\_____|#(___/ #|_| \_)#|_|   |_|#|_______)#
                        ##    ##         ##       ##      ##       ##         ##         ##    
    """)


def irc():
    print("""
          _______. ____     ______ .______       ____   .___________.     ______  __    __       ___      .___________.
        /       ||___ \   /      ||   _  \     |___ \  |           |    /      ||  |  |  |     /   \     |           |
       |   (----`  __) | |  ,----'|  |_)  |      __) | `---|  |----`   |  ,----'|  |__|  |    /  ^  \    `---|  |----`
        \   \     |__ <  |  |     |      /      |__ <      |  |        |  |     |   __   |   /  /_\  \       |  |     
    .----)   |    ___) | |  `----.|  |\  \----. ___) |     |  |        |  `----.|  |  |  |  /  _____  \      |  |     
    |_______/    |____/   \______|| _| `._____||____/      |__|         \______||__|  |__| /__/     \__\     |__|     
    
    1. VPN
    2. IRC Chat
    """)
    key = int(input(">> "))
    if key == 1:
        vpn()
    elif key == 2:
        irc_menu()
    else:
        print("Yo have eyes nigga ?")


def rules_list():
    with open(rules_file, 'r') as rf:
        rules = rf.readlines()
        num = 1
        for rule in rules[12:]:
            print(f"""    {num}. {rule}""")
            num += 1
        print("""    
    """)
        # 'a' > ++ | 'r' > -- | 'h' > #
        rf.close()


def update_rules():
    print('The Commandment++')
    com = input('>> ')
    if com == 'h':
        home()
    with open(rules_file, 'a') as wf:
        wf.write(f'\n{com}')
        print(f'Commandment added successfully {tick()}\n')
    pass


def rules_remover():
    print('The Commandment--')
    com = input('>> ')
    if com == 'h':
        home()
    with open(rules_file, 'r') as rf:
        lines = rf.readlines()
        com = int(com) - 1
        del lines[12 + com]
        rf.close()
        with open(rules_file, 'w') as wf:
            for line in lines:
                wf.write(f'{line}')
            wf.close()
    pass


def home():
    return menu()


def come_home():
    c = input('>> ')
    if c == 'a':
        update_rules()
        rules_list()
        come_home()
    if c == 'r':
        rules_remover()
        rules_list()
        come_home()
    if c == 'h':
        home()
    pass


def write_append(file):
    with open(file, 'a') as fa:
        fa.write('\n')
        fa.write(f'\nDate : {date}')
        fa.write(f'\nDay : {date.strftime("%A")}')
        fa.write(f'\nTime  : {str(hour)} hr {str(mins)} min')


def fictioner():
    fiction_banner()
    write_append(fiction_file)
    print('Fiction')
    fiction = input('>> ')
    if fiction == 'h':
        home()
    else:
        print("FikMe")
        fick = input('>> ')
        if fick == 'h':
            home()
        else:
            with open(fiction_file, 'a') as fa:
                fa.write(f'\nFiction : {fiction}')
                fa.write(f'\nFiks : {fick}\n')
                fa.close()
                print('Thank you for ficking me')
                home()


def thoughts():
    thoughts_banner()
    write_append(thoughts_file)
    print('Thought')
    thought = input('>> ')
    if thought == 'h':
        home()
    else:
        print("ThoughtMe")
        thoughts = input('>> ')
        if thoughts == 'h':
            home()
        else:
            with open(thoughts_file, 'a') as ta:
                ta.write(f'\nThought : {thought}')
                ta.write(f'\nThoughts : {thoughts}\n')
                ta.close()
                print('Thank you for thinking me')
                home()


def positive():
    positive_banner()
    write_append(positive_file)
    print('Positive++')
    positive = input('>> ')
    if positive == 'h':
        home()
    else:
        print("ChargeMe")
        charges = input('>> ')
        if charges == 'h':
            home()
        else:
            with open(positive_file, 'a') as pa:
                pa.write(f'\nPositive: {positive}')
                pa.write(f'\nCharges : {charges}\n')
                pa.close()
                print('Thank you for charging me')
                home()


def negative():
    negative_banner()
    write_append(negative_file)
    print('Negative--')
    negative = input('>> ')
    if negative == 'h':
        home()
    else:
        print("DrainMe")
        drains = input('>> ')
        if drains == 'h':
            home()
        else:
            with open(negative_file, 'a') as na:
                na.write(f'\nNegative : {negative}')
                na.write(f'\nCharges : {drains}\n')
                na.close()
                print('Thank you for charging me')
                home()


def goals():
    goals_banner()
    write_append(goals_file)
    print('Goals')
    goal = input('>> ')
    if goal == 'h':
        home()
    else:
        print("GoalMe")
        goals = input('>> ')
        if goals == 'h':
            home()
        else:
            with open(goals_file, 'a') as ga:
                ga.write(f'\nGoal: {goal}')
                ga.write(f'\nDescription : {goals}\n')
                ga.close()
                print('Great, Helicopter Shot')
                home()


def bucket():
    bucket_banner()
    write_append(bucket_file)
    print('Bucket List')
    bucket = input('>> ')
    if bucket == 'h':
        home()
    else:
        print("BucketMe")
        list = input('>> ')
        if list == 'h':
            home()
        else:
            with open(bucket_file, 'a') as ba:
                ba.write(f'\nGoal: {bucket}')
                ba.write(f'\nDescription : {list}\n')
                ba.close()
                print('Great, Helicopter Shot')
                home()


def days_live():
    return days_alive.days


days_living = days_live()


def view_logs(file):
    with open(file, 'r') as fr:
        view = fr.read()
        print(view)


check_flag = True


def check_in():
    global check_ins
    print("TaskME ?")
    task = input('>> ')
    print('check in successful')
    start = time.time()
    shr = time.strftime("%H")
    sms = time.strftime("%M")
    ssec = time.strftime("%S")
    check_ins = [int(shr), int(sms), int(ssec)]
    print("press 'x' to check out")
    opt = input('>> ')
    if opt != 'x':
        print('Yo have eyes nigga ?')
        time.sleep(5)
    elif opt == 'x':
        check_out_banner()
        end = time.time()
        ehr = time.strftime("%H")
        ems = time.strftime("%M")
        esec = time.strftime("%S")
        check_outs = [int(ehr), int(ems), int(esec)]
        # check_in_time = f'Logged in time : {check_outs[0] - check_ins[0]}hrs : {check_outs[1] - check_ins[1]}mins : {check_outs[2] - check_ins[2]}secs'
        secs = end - start
        in_time = secs / 3600
        with open(task_file, 'a') as ea:
            ea.write('\n')
            ea.write(f'\nDate : {date}')
            ea.write(f'\nDay : {date.strftime("%A")}')
            ea.write(f"\nTask : {task}")
            ea.write(f"\n{in_time} hrs")
        print(f'Total Logged Time ---> {in_time} hrs')
        print('check out successful')
        time.sleep(5)
        check_in_banner()
        check_in()


def logs():
    logs_banner()
    print("""
    1. ComLogs
    2. FickLogs
    3. BrainLog
    4. PosLogs
    5. NegLogs
    6. GoaLogs
    7. BuckLogs
    8. TasKLogs
    
    0 - Log Out
    """)
    option = int(input('>> '))
    if option == 1:
        view_logs(rules_file)
        print()
        opt = input('>> ')
        if opt == 'h':
            logs()
    elif option == 2:
        view_logs(fiction_file)
        print()
        opt = input('>> ')
        if opt == 'h':
            logs()
    elif option == 3:
        view_logs(thoughts_file)
        print()
        opt = input('>> ')
        if opt == 'h':
            logs()
    elif option == 4:
        view_logs(positive_file)
        print()
        opt = input('>> ')
        if opt == 'h':
            logs()
    elif option == 5:
        view_logs(negative_file)
        print()
        opt = input('>> ')
        if opt == 'h':
            logs()
    elif option == 6:
        view_logs(goals_file)
        print()
        opt = input('>> ')
        if opt == 'h':
            logs()
    elif option == 7:
        view_logs(bucket_file)
        print()
        opt = input('>> ')
        if opt == 'h':
            logs()
    elif option == 8:
        view_logs(task_file)
        print()
        opt = input('>> ')
        if opt == 'h':
            logs()
    elif option == 0:
        login()
    elif option == 'h':
        menu()
    else:
        print('Yo have EYES nigga ?')
    pass


# Flash
gauth = GoogleAuth()
drive = GoogleDrive(gauth)


def flash(flash_files):
    for key, item in flash_files.items():
        # Read file and set it as the content of this instance.
        if item[0] == item[2]:
            # GDrive logs 2021
            # change this gdrive api every year of the folder
            gfile = drive.CreateFile({'parents': [
                {'id': '1fXqfhEZzK8MOh_7-4DCaCQlRKpwT5GZZ'}
            ],
                'title': f'{item[1]}',
            })
            gfile.SetContentFile(item[0])
            gfile.Upload()  # Upload the file.
            print(f'Flashing file {item[1]} {tick()}')
    print(f'Flash Completed {tick()}')


def menu():
    hello_friend()
    hello = random.choice(hellos)
    print(f"""
    {hello}, {user} ! Days alive {days_living}
    What made you come here, Today {day} / {month} - {date.strftime("%A")} ?
    
    1. Commandments
    2. Fiction
    3. Thoughts
    4. Positive
    5. Negative
    6. Goals
    7. Bucket List
    
    0. Log Out
    """)
    option = int(input('>> '))
    if option == 1:
        commandments_banner()
        rules_list()
        come_home()
    elif option == 2:
        fictioner()
    elif option == 3:
        thoughts()
    elif option == 4:
        positive()
    elif option == 5:
        negative()
    elif option == 6:
        goals()
    elif option == 7:
        bucket()
    elif option == 0:
        login()
    else:
        print('Yo have EYES nigga ?')


def root_menu():
    hello_friend()
    hello = random.choice(hellos)
    print(f"""
    {hello}, root user {user} ! Days alive {days_living}
    What made you come here, Today  {day} / {month} - {date.strftime("%A")} ?
    
    1. Commandments
    2. Fiction
    3. Thoughts
    4. Positive
    5. Negative
    6. Goals
    7. Bucket List
    8. Flash
    9. Clogs
    0. Log Out
    """)
    option = int(input('>> '))
    if option == 1:
        commandments_banner()
        rules_list()
        come_home()
    elif option == 2:
        fictioner()
    elif option == 3:
        thoughts()
    elif option == 4:
        positive()
    elif option == 5:
        negative()
    elif option == 6:
        goals()
    elif option == 7:
        bucket()
    elif option == 8:
        flash(flash_files)
        root_menu()
    elif option == 9:
        logs()
    elif option == 0:
        login()
    else:
        print('Yo have EYES nigga ?')


def logme_banner():
    print(f"""
              o                                    o          o    o__ __o__/_ 
             <|>                                  <|\        /|>  <|    v      
             / \                                  / \\o    o// \  < >          
             \o/           o__ __o      o__ __o/  \o/ v\  /v \o/   |           
              |           /v     v\    /v     |    |   <\/>   |    o__/_       
             / \         />       <\  />     / \  / \        / \   |           
             \o/         \         /  \      \o/  \o/        \o/  <o>          
              |           o       o    o      |    |          |    |           
             / \ _\o__/_  <\__ __/>    <\__  < >  / \        / \  / \  _\o__/_ 
                                              |                                
                                      o__     o                                
                                      <\__ __/>                                
            
                            [ LogMe ]
                            [ Developer : Mastermindx33 ]
                            [ Version : 1.0 ]
            """)


data = 'profile.txt'
cods = 'code.txt'
key = load_key()


def encrypt_user():
    encrypt(data, key)


def encrypt_cod():
    data = cods
    encrypt(data, key)


# Encryption
# encrypt_user()
# gen key
# write_key()


def encrypted_user():
    return decrypt(data, key)


def encrypted_cod():
    data = cods
    return decrypt(data, key)


user = encrypted_user()
cod = encrypted_cod()


def login():
    logme_banner()
    quotes_generator()
    print(f"""
    1. Login ****
    2. Check In {tick()}
    3. Beep  ...   
    4. IRC chat #
    """)
    option = int(input('>> '))
    if option == 1:
        mastermind_banner()
        admin_username = input("Username : ")
        if admin_username == './':
            print('\nSuperUser Root Successful')
            root_banner()
            root_menu()
        # To mask the password with *
        admin_password = stdiomask.getpass("Password : ", '*')
        # admin_password = input("Password : ")
        if admin_username == f'{user}' and admin_password == f'{cod}':
            print('\nLogin Successful')
            menu()
        else:
            print('Leave me alone')
            print("Don't run me again")
            exit()
    elif option == 2:
        check_in_banner()
        check_in()
    elif option == 3:
        dynamic_clock()
    elif option == 4:
        irc()


# Execution Phase
login()
