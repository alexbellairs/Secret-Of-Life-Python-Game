from code import interact
from gettext import find
import random
import re
import sys
import time
from time import sleep
from tkinter.messagebox import YES


from playsound import playsound

def print_slow(str):
    for char in str:
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

def prRed(skk): print_slow("\033[91m {}\033[00m" .format(skk))
def prYellow(skk): print_slow("\033[93m{} \033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prPurple(skk): print_slow("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

riddles = [
    "You’ll put big things on top of me, and small stuff inside, I’m a good place for pencils and paper to hide.\n", #(Desk)
    "Look at me and you’ll see a familiar sight, you can’t beat my movements, try as you might.\n", #(Mirror)
    "My hands move slow but I’m quick to give you my numbers, like when you should go to bed, or when to arise out of slumber.\n", #(Grandfather Clock)
    "I have seas without water, coast without sand, towns without people, mountains without land. You'll need me to continue\n", #(Map)
    "Pirates were sneaky, you could say they were crooks. To find the next clue, go to a room that has books?\n" #(Library)
]

riddle = "You’ll put big things on top of me, and small stuff inside, I’m a good place for pencils and paper to hide.\nLook at me and you’ll see a familiar sight, you can’t beat my movements, try as you might.\nMy hands move slow but I’m quick to give you my numbers, like when you should go to bed, or when to arise out of slumber.\nI have seas without water, coast without sand, towns without people, mountains without land. You'll need me to continue\nPirates were sneaky, you could say they were crooks. To find the next clue, go to a room that has books\n"[::-1]

hero = [
    "a diary", "a map" ,
]

def inventory_check():
    hero.sort()
    print(str(hero) + "\n")
    time.sleep(0.7)
    print_slow("\n\nGot ITTT!\n")
    print_slow("\n")
    kitchen()

def credits():
    time.sleep(2)
    prPurple("\nThankyou for playing our game \nCreated By \nAND \nWritten By \nAlex Bellairs \nJack West \nJohn Bridges \nAND \nPeter Nwabuokei")
    print_slow("\nWould you like to play again? \n1.Yes \n2.No")
    restart = (input("\n: "))
    if restart == "Yes" or restart == "yes" or restart == "YES" or restart == "y" or restart == "Y" or restart == 1:
        print_slow("\nLet's Go!")
        intro()
    else:
        print("\nGOODBYE!")

def diary():
    prRed("\nClue 1...\n\nYou put big things on top of me, small things inside, I'm a good place for pens and paper to hide.\n")
    prRed("\nClue 2...\n\nLook at me and you'll see a familiar sight, you can't beat my movements try as you might.\n")
    prRed("\nClue 3...\n\nMy hands move slow but I'm quick to give you my numbers, like when you need to go to bed or arise out of slumber.\n")
    prRed("\nClue 4...\n\nI have seas without water, coast without sand, towns without people, mountains without land.\n")
    prRed("\nClue 5...\n\nPirates were sneaky, you could say they were crooks. To find the next clue, go to a room that has books.\n")

safe_code = 126
restart = YES

def attempt_3():
    print_slow("Please enter the safe code ")
    safe_code = int(input("\n: "))
    if safe_code == 126:
        playsound("C:\\Users\\AB\\Downloads\\ES_MetalDoorOpen.wav")
        prCyan("                                   .''.       ")
        prCyan("       .''.      .        *''*    :_\/_:     . ")
        prCyan("      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.")
        prCyan("  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-")
        prCyan(" :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'")
        prCyan(" : /\ : :::::     *_\/_*     -= o =-  /)\    '  *")
        prCyan("  '..'  ':::'     * /\ *     .'/.\'.   '")
        prCyan("      *            *..*         :")
        prCyan("        *")
        prCyan("        *")
        playsound("C:\\Users\\AB\\Downloads\\Fireworks.wav")
        print_slow("CONGRATULATIONS YOU HAVE WON OUR GAME \n THE SECRET TO LIFE IS THE MEMORIES YOU MAKE ALONG THE WAY!!!!\n\nBut that's not all .......\n\n")
        playsound("C:\\Users\\AB\\Downloads\\Phone_Ring.wav")
        prRed("Phone Rings...\n")
        time.sleep(2)
        print_slow("Hello...???\n")
        time.sleep(1)
        prRed("Hey kid, I see you unlocked the safe \n")
        time.sleep(1)
        print_slow("Grandfather???\n")
        time.sleep(1)
        prRed("Yeah kid, you're not done \nMeet me in Grenada and I'll make you rich beyond your wildest dreams....")
        time.sleep(2)
        credits()
    else:
        print_slow("Sorry wrong code!!\n")
        print_slow("You failed to unlock the safe and complete the game!!!\n")
        print_slow("Would you like to play again?")
        restart = input("\n: ")
        if restart == "Yes" or restart == "yes" or restart == "YES" or restart == "y" or restart == "Y":
            print_slow("\nLet's Go!")
            time.sleep(1)
            intro()
        else:
            print("\nGOODBYE!")
            time.sleep(2)
            credits()

def attempt_2():
    print_slow("Please enter the safe code ")
    safe_code = int(input("\n: "))
    if safe_code == 126:
        playsound("C:\\Users\\AB\\Downloads\\ES_MetalDoorOpen.wav")
        prCyan("                                   .''.       ")
        prCyan("       .''.      .        *''*    :_\/_:     . ")
        prCyan("      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.")
        prCyan("  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-")
        prCyan(" :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'")
        prCyan(" : /\ : :::::     *_\/_*     -= o =-  /)\    '  *")
        prCyan("  '..'  ':::'     * /\ *     .'/.\'.   '")
        prCyan("      *            *..*         :")
        prCyan("        *")
        prCyan("        *")
        playsound("C:\\Users\\AB\\Downloads\\Fireworks.wav")
        print_slow("CONGRATULATIONS YOU HAVE WON OUR GAME \n THE SECRET TO LIFE IS THE MEMORIES YOU MAKE ALONG THE WAY!!!!\n\nBut that's not all .......\n\n")
        playsound("C:\\Users\\AB\\Downloads\\Phone_Ring.wav")
        prRed("Phone Rings...\n")
        time.sleep(2)
        print_slow("Hello...???\n")
        time.sleep(1)
        prRed("Hey kid, I see you unlocked the safe \n")
        time.sleep(1)
        print_slow("Grandfather???\n")
        time.sleep(1)
        prRed("Yeah kid, you're not done \nMeet me in Grenada and I'll make you rich beyond your wildest dreams....")
        time.sleep(2)
        credits()
    else:
        print_slow("\nSorry wrong code please try again, \nYou have 1 attempt remaining!\n ")
        attempt_3()

def attempt_1():
    print_slow("Please enter the safe code ")
    safe_code = int(input("\n: "))
    if safe_code == 126:
        playsound("C:\\Users\\AB\\Downloads\\ES_MetalDoorOpen.wav")
        prCyan("                                   .''.       ")
        prCyan("       .''.      .        *''*    :_\/_:     . ")
        prCyan("      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.")
        prCyan("  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-")
        prCyan(" :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'")
        prCyan(" : /\ : :::::     *_\/_*     -= o =-  /)\    '  *")
        prCyan("  '..'  ':::'     * /\ *     .'/.\'.   '")
        prCyan("      *            *..*         :")
        prCyan("        *")
        prCyan("        *")
        playsound("C:\\Users\\AB\\Downloads\\Fireworks.wav")
        print_slow("CONGRATULATIONS YOU HAVE WON OUR GAME \n THE SECRET TO LIFE IS THE MEMORIES YOU MAKE ALONG THE WAY!!!!\n\nBut that's not all .......\n\n")
        playsound("C:\\Users\\AB\\Downloads\\Phone_Ring.wav")
        prRed("Phone Rings...\n")
        time.sleep(2)
        print_slow("Hello...???\n")
        time.sleep(1)
        prRed("Hey kid, I see you unlocked the safe \n")
        time.sleep(1)
        print_slow("Grandfather???\n")
        time.sleep(1)
        prRed("Yeah kid, you're not done \nMeet me in Grenada and I'll make you rich beyond your wildest dreams....")
        time.sleep(2)
        credits()
    else:
        print_slow("Sorry wrong code please try again, \nYou have 2 attempts remaining\n")
        attempt_2()

def library():
    global hero
    print_slow("You enter the library and have a quick look around. You can see \n 1.A Book on a Table, \n 2.A Safe, \n 3.A pile of old newspapers \n 4.And a Telescope \n 5.Check Diary \n 6.Check Inventory \n 7.Leave Room")
    print_slow("\nWhat would you like to look at? ")
    interact = int(input ("\n: "))
    if interact == 2 :
        time.sleep(1)
        print_slow("You walk over and examine the safe.\n")
        time.sleep(1)
        print_slow("It has a keypad to unlock it and is requesting a 3 digit number.\n")
        time.sleep(1)
        print_slow("Would you like to enter code now? Or continue looking for clues?")
        print_slow("\n1.Enter Code\n2.Continue Looking\n\n\n")
        prRed("WARNING ONCE YOU CHOOSE TO PUT IN THE CODE YOU CAN'T GO BACK SO MAKE SURE YOU HAVE ALL THE CLUES!!\n")
        code = int(input("\n: "))
        if code == 1:
            attempt_1()
        else:
            library()
    elif interact == 1 :
        time.sleep(1)
        print_slow("You look around the library and there is one book seemingly out of place just sat on its own\n")
        time.sleep(1)
        print_slow("You go over and examine it\n")
        time.sleep(1)
        print_slow("The book is called \n")
        prRed("'Everyting Adds Up'\n")
        print_slow("You can't help but wonder if that is important\n")
        library()
    elif interact == 3 :
        time.sleep(1)
        print_slow("There are a bunch of old newspapers piled in ther corner you have a rumage around them but find nothing of interest\n")
        time.sleep(1)
        library()
    elif interact == 4 :
        time.sleep(1)
        print_slow("The telescope is marvelous, made of wood and gold, you bend over to look out of it.\n\n")
        prLightGray("                                 ____                                         ")
        prLightGray("                              .-\"    `-.      ,                               ")
        prLightGray("                            .'          '.   /j\                              ")
        prLightGray("                           /              \,/:/#\                /\           ")
        prLightGray("                          ;              ,//' '/#\              //#\          ")
        prLightGray("                           \       /'\ -._:__    '/#\        ;      /#, \"\"\"---")
        prLightGray("                            `-.   / ;#\ ]\" ; \"\"\"--./#J       ':____...!       ")
        prLightGray("                               `-/   /#\  J  [;[;[;Y]         |      ;        ")
        prLightGray("""""""---....             __.--\"/    '/#\ ;   \" \"  |     !    |   #! |        ")
        prLightGray("             \"\"--.. _.--\"\"     /      ,/#\ -..____.;_,   |    |   '  |        ")
        prLightGray("                   \"-.        :_....___,/#} \"####\" | '_.-\",   | #['  |        ")
        prLightGray("                      '-._      |[;[;[;[;|         |.;'  /;\  |      |        ")
        prLightGray("                      ,   `-.   |        :     _   .;'    /;\ |   #\" |        ")
        prLightGray("                      !      `._:      _  ;   ##' .;'      /;\|  _,  |        ")
        prLightGray("                     .#\"\"\"---..._    ';, |      .;{___     /;\  ]#' |__....--")
        prLightGray("          .--.      ;'/#\         \    ]! |       \"| , \"\"\"--./_J    /         ")
        prLightGray("         /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__      ")
        prLightGray("        i__..'%] _:_   ;##J         \      :\"#...._!   '  \"  \"|__  |    `--.._")
        prLightGray("         | .--\"\"\" !|\"\"\"  |\"\"\"----...J     | '##\"\" `-._       |  \"\"\"---.._    ")
        prLightGray("     ____: |      #|      |         #|     |          \"]      ;   ___...-\"T,  ")
        prLightGray("    /   :  :      !|      |   _______!_    |           |__..--;\"\"\"     ,;MM;  ")
        prLightGray("   :____| :    .-.#|      |  /\      /#\   |          /'               ''MM;  ")
        prLightGray("    |\"\"\": |   /   \|   .----+  ;      /#\  :___..--\"\";                  ,'MM; ")
        prLightGray("   _Y--:  |  ;     ;.-'      ;  \______/#: /         ;                  ''MM; ")
        prLightGray("  /    |  | ;_______;     ____!  |\"##\"\"\"MM!         ;                    ,'MM;")
        prLightGray(" !_____|  |  |\"#\"#\"|____.'\"\"##\"  |       :         ;                     ''MM  ")
        prLightGray("  | \"\"\"\"--!._|     |##\"\"         !       !         :____.....-------\"\"\"\"\"\" |'")
        prLightGray("  |          :     |______                        ___!_ \"#\"#\"\"#\"\"\"#\"\"\"#\"\"\"|  ")
        prLightGray("__|          ;     |MM\"MM\"\"\"\"\"---..._______...--\"\"MM\"MM]                   |   ")
        prLightGray("  \"\-.      :      |#                                  :                   |  ")
        prLightGray("    /#'.    |      /##,                                !                   |  ")
        prLightGray("   .',/'\   |       #:#,                                ;       .==.       |  ")
        prLightGray("  /\"\'#\"\',.|       ##;#,                               !     ,'||||',     |  ")
        prLightGray("        /;/`:       ######,          ____             _ :     M||||||M     |  ")
        prLightGray("       ###          /;\"\.__\"-._   \"\"\"                   |===..M!!!!!!M_____|  ")
        prLightGray("                           `--..`--.._____             _!_                    ")
        prLightGray("                                          `--...____,=\"_.'`-.____        ")
        print_slow("\n\nIt shows you a beautiful view of the local castle on the hill, but nothing else helpful.\n")
        time.sleep(5)
        library()
    elif interact == 5:
        time.sleep(1)
        diary()
        time.sleep(2)
        library()
    elif interact == 6:
        print(hero)
        library()
    else:
        time.sleep(1)
        print_slow("You leave the room\n")
        upstairs()

def bathroom():
    global hero
    print_slow("\nYou enter the bathroom and have a quick look around. You can see a \n 1. Bathtub \n 2. Mirror \n 3. Shower \n 4. Toilet \n 5. Cupboard \n 6. Read Diary \n 7. Check Inventory \n 8. Leave Room ")
    print_slow("\nWhat do you want to interact with? ")
    interact = int(input("\n: "))
    if interact == 2:
        time.sleep(1)
        print_slow("\nI'm sure something in my Grandfather's diary made me think of a mirror.")
        time.sleep(1)
        prYellow(riddles[1])
        time.sleep(2)
        print_slow("\nYou take a closer look at the mirror, you see an image that reminds you of your Grandfather stirring right back at you. \nTo your suprise the mirror begins to shake and wobble for a moment, then turns foggy and you see the number ")
        res = [random.randrange(1, 100, 1) for i in range(1)]
        for i in res:
            print(i)
        bathroom() 
    elif interact == 1:
        time.sleep(1)
        print_slow("\nYou begin to run the hotwater on the tub to check the temperature of the running water.")
        time.sleep(2)
        bathroom()
    elif interact == 3:
        time.sleep(1)
        print_slow("\nYou already had a shower this morning.")
        time.sleep(2)
        bathroom()
    elif interact == 4:
        time.sleep(1)
        print_slow("\nYou flush the toilet to check if it is working properly.")
        time.sleep(2)
        bathroom()
    elif interact == 5:
        time.sleep(1)
        print_slow("\nYou open the cupboard to find some medicines and sleeping pills.")
        hero.append("sleeping pills")
        time.sleep(2)
        bathroom()
    elif interact == 6:
        time.sleep(1)
        diary()
        time.sleep(2)
        bathroom()
    elif interact == 7:
        time.sleep(1)
        print(hero)
        time.sleep(1)
        bathroom()
    else:
        time.sleep(1)
        print_slow("\nYou leave the room... ")
        upstairs()

def bedroom():
    global hero
    print_slow("\nYou enter the bedroom and have a quick look around. You can see a \n 1. Mirror \n 2. Bed \n 3. Wardrobe \n 4. Drawers \n 5. Box of chocolate \n 6. Diary \n 7. Check Inventory \n 8. Leave Room ") 
    print_slow("\nWhat do you want to interact with? ")
    interact = int(input("\n: "))
    if interact == 1:
        time.sleep(1)
        print_slow("\nI'm sure something in my Grandfather's diary made me think of a mirror.\n")
        time.sleep(1)
        prYellow(riddles[1])
        time.sleep(1)
        print_slow("\nYou take a closer look at the mirror, you see a reflection of yourself and as you investigate the mirrior closer you see a very small scratched on the top right corner that looks like a number 33.")
        hero.append("33")
        bedroom()
    elif interact == 2:
        time.sleep(1)
        print_slow("\nYou sit on the bed and gather your thoughts for a moment...")
        time.sleep(1)
        bedroom()
    elif interact == 3:
        time.sleep(1)
        print_slow("\nYou open the wardrobe and you see an old leather jacket and a pair of Granfather's favourite jeans.")
        time.sleep(1)
        bedroom()
    elif interact == 4:
        time.sleep(1)
        print_slow("\nYou open the draws to find neatly folded hankerchiefs and a pair of purple socks.")
        time.sleep(1)
        bedroom()
    elif interact == 5:
        time.sleep(1)
        print_slow("\nHmmm..Grandpa never really liked chocolates.")
        hero.append("box of chocolates")
        time.sleep(1)
        bedroom()
    elif interact == 6:
        time.sleep(1)
        diary()
        time.sleep(2)
        bedroom()
    elif interact == 7:
        time.sleep(1)
        print(hero)
        time.sleep(1)
        bedroom()
    else:
        time.sleep(1)
        print_slow("\nYou haven't selected any item, you leave the room... ")
        upstairs()
def rummage():
    global hero
    print_slow("uarghmmmm....let me take a quick look through the \n 1. Cupboards \n 2. breadbasket \n 3. spice rack \n 4. daydream \n 5. I dont have time for this tbf \n\n")
    time.sleep(0.4)
    look_around = str(input("\n: "))
    if look_around == "1":
        print_slow("\nugh throw, move! grrrk")
        time.sleep(0.3)
        print_slow("\n*bump crash*")
        time.sleep(0.5)
        time.sleep(0.1)
        print_slow("\nnothing in here")
        time.sleep(0.2)
        if hero == "psypower":
            time.sleep(0.3)
            print("SPArKkKK")
            time.sleep(0.2)
            print_slow("\n*sheewwsssssshhhhhHHH*")
            print_slow("\nI'm a good place for pencils and paper to hide....")
            time.sleep(2)
            print_slow("\nBut not the best...")
            time.sleep(0.5)
            print_slow("\nbetter do your STUDIES and prepare for any tests.")
            rummage()
        rummage()
    elif look_around == "2":
        print_slow("\nsand??? whats all this doing in here")
        time.sleep(2)
        print_slow("\n*sand begins to poouuuurrrrr from the crevices of the breadbasket all over the counter top table and floor...surrounding his feet the sand begins to take the shape of miniature city \n\n\n")
        prLightGray("                                                          |>>>")
        prLightGray("                   _                      _                |")
        prLightGray("    ____________ .' '.    _____/----/-\\ .' './========\\   / \\ ")
        prLightGray("   //// ////// /V_.-._\  |.-.-.|===| _ |-----| u    u |  /___\\")
        prLightGray("  // /// // ///==\\ u |.  || | ||===||||| |T| |   ||   | .| u |_ _ _ _ _ _")
        prLightGray(" ///////-\\////====\\==|:::::::::::::::::::::::::::::::::::|u u| U U U U U")
        prLightGray(" |----/\\u |--|++++|..|'''''''''''::::::::::::::''''''''''|+++|+-+-+-+-+-+")
        prLightGray(" |u u|u | |u ||||||..|              '::::::::'           |===|>=== _ _ ==")
        prLightGray(" |===|  |u|==|++++|==|              .::::::::.           | T |....| V |..")
        prLightGray(" |u u|u | |u ||HH||         \|/    .::::::::::.")
        prLightGray(" |===|_.|u|_.|+HH+|_              .::::::::::::.              _")
        prLightGray("                __(_)___         .::::::::::::::.         ___(_)__")
        prLightGray("---------------/  / \\  /|       .:::::;;;:::;;:::.       |\\  / \\  \-------")
        prLightGray("______________/_______/ |      .::::::;;:::::;;:::.      | \\_______\\________")
        prLightGray("|       |     [===  =] /|     .:::::;;;::::::;;;:::.     |\\ [==  = ]   |")
        prLightGray("|_______|_____[ = == ]/ |    .:::::;;;:::::::;;;::::.    | \\[ ===  ]___|____")
        prLightGray("     |       |[  === ] /|   .:::::;;;::::::::;;;:::::.   |\\ [=  ===] |")
        prLightGray("_____|_______|[== = =]/ |  .:::::;;;::::14::::;;;:::::.  | \\[ ==  =]_|______")
        prLightGray(" |       |    [ == = ] /| .::::::;;:::::::::::;;;::::::. |\\ [== == ]      |")
        prLightGray("_|_______|____[=  == ]/ |.::::::;;:::::::::::::;;;::::::.| \\[  === ]______|_")
        prLightGray("   |       |  [ === =] /.::::::;;::::::::::::::;;;:::::::.\\ [===  =]   |")
        prLightGray("___|_______|__[ == ==]/.::::::;;;:::::::::::::::;;;:::::::.\\[=  == ]___|_____")
        time.sleep(3)
        print_slow("\nBefore our hero gets a chance to react, swarms of tiny creatures begin flowing towards the garden door\n\n")
        print_slow("\nYUUUUUCKKKK")
        hero.append("14")
        time.sleep(0.2)
        print("GeTt\n")
        time.sleep(0.3)
        print("OUTTTTTTTT\n\n")
        time.sleep(0.8)
        print_slow("NOOWWWWWWWWWWWWWWWW\n")
        print_slow("Do I:\n 1. Follow the creatures \n 2. Run as farrrr the other way as possible?!! \n")
        decide_2 = int(input("\n: "))
        if decide_2 == 1:
            garden()
        elif decide_2 == 2:
            downstairs()
        else:
            print("\n*our hero was swallowed by indecisionnnnnn, modernity huh!*")
            time.sleep(0.3)
            credits()
    elif look_around == "3":
        print_slow("How old is this thing!!\n\n")
        print_slow("smells like some old pirate ship \n")
        hero.append("Old Spice")
        time.sleep(2)
        print_slow("now what?\n")
        time.sleep(2)
        rummage()
    elif look_around == "3" or look_around == 3: #or hero["psypower"] == True:
        print_slow("\nHow old is this thing!!")
        print_slow("smells like some old pirate ship \n")
        time.sleep(2)
        print("\n*TicKTocKTiCKTOCktiCKTOck* \n *TicKTocKTiCKTOCktiCKTOck* \n\n *TicKTocKTiCKTOCktiCKTOck*\n")
        #hero.append("14")
        print_slow("now what?\n")
        time.sleep(2)
        rummage()
    elif look_around == "4" or look_around == 4:
        print(hero)
        rummage()
def kitchen():  
    global hero
    print_slow("\n\nThe Kitchen?..\n" )
    time.sleep(0.8)
    print_slow("this where THAT HOUSEKEEPER cooked up the plan huh??\n\n\n")
    time.sleep(0.6)
    print_slow("I don't even know where to start! \n 1. Check another room \n 2. Check diary \n 3. Use Psychic powers \n 4. Rummage \n 5. Wonder \n")
    interact = str(input("\n: "))
    time.sleep(0.7)
    if interact == "1" or interact == 1:
        time.sleep(0.7)
        print_slow("\nYe theres no chance I'm finding anything in here...")
        time.sleep(0.5)
        #hero.append("14")
        print_slow("\nyeeee this is longgg..\n\n")
        time.sleep(0.4)
        print_slow("\n*leaves*")
        downstairs()
    elif interact == "1" and hero["psypower"] == True: ## this needs
        print("\nYOULL FIND IT IF YOU RISK IT, MY FATHERS FATHER STILL STANDS TALL!\n ")
        #hero.append("14")
        diary(-1)
        time.sleep(0.5)
        print("\n*shudders*")
        time.sleep(0.8)
        downstairs()
    elif interact == "1" and hero["Old Spice"] == True: #Need to sort out how to check if something is
        time.sleep(1.5)
        print_slow("\n*GHosTlY VoiCe*\n\nYou smell mate...please go and freshen up i dont care where!")
        time.sleep(2)
        print_slow("\nactually you can go to the \n 1. Bathroom \n 2. Garden \n BUT GO NOW!!")
        decision = input("\n: ")
        if decision == 1:
            bathroom()
        elif decision == 2:
            garden()
        else:
            print_slow("\nyou really are trying to die arent you?!")
            kitchen()
    elif interact == "2" or interact == 2:
        time.sleep(0.7)
        print_slow("\nI'm sure theres something in this book about the kitchen...")
        time.sleep(0.7)
        #hero.append("14")
        print_slow("*reads diary* \n\n")
        diary()
        time.sleep(2)
        print_slow("hmmmmm \n")
        time.sleep(0.5)
        print_slow("now what?")
        time.sleep(0.8)
        kitchen()
    elif interact == "3" or interact == 3:
        time.sleep(0.7)
        print_slow("\nI know its dangerous but I dont have time to waste..*clenches fists*")
        time.sleep(0.3)
        hero.append("psychicpower")
        #hero.append("psypower")
        #hero.append("insight")
        print_slow("\nrumbles rumbles\n")
        #hero.append("Old Spice")
        time.sleep(0.4)
        print_slow("*shake rumble*")
        time.sleep(0.7)
        print_slow ("\n BOOK falls to floor..\n")
        time.sleep(1)
        print_slow("ehhhhhhhh whats in this then?\n")
        time.sleep(0.4)
        print_slow("*picks up diary*\n")
        time.sleep(1)
        prYellow(riddle)
        time.sleep(2)
        print_slow("i see \n")
        time.sleep(0.5)
        print_slow("now what?\n")
        time.sleep(0.7)
        kitchen()
    elif interact == "4" or interact == 4:
        time.sleep(0.7)
        print_slow("\nso much junk")
        time.sleep(0.2)
        print("\nguhhhh")
        time.sleep(0.3)
        rummage()
    elif interact == 5 or interact == "5":
        print_slow("FOCUS \n\n")
        time.sleep(2)
        time.sleep(0.3)
        inventory_check()
    elif interact != 1 or interact != 2 or interact != 3 or interact != 4:
        time.sleep(0.7)
        print_slow("\nnot the best time for this Brain stop distracting me!!")
        kitchen()
    else:
        time.sleep(0.7)
        print_slow("\nYe theres no chance I'm finding anything in here...")
        time.sleep(1)
        print_slow("\nyeeee this is longgg..")
        time.sleep(0.4)
        print_slow("\n*leaves*")
        downstairs()

def lounge():
    global hero
    print_slow("\nYou enter the lounge and have a quick look around. You can see \n 1.A sofa, \n 2.A fire place, \n 3.A coffee table \n 4.And a grandfather clock \n 5.Check Inventory \n 6.Check Diary \n7.Leave Room")
    print_slow("\nWhat would you like to look at? ")
    interact = int(input ("\n: "))
    if interact == 4 :
        time.sleep(1)
        print_slow("\nI'm sure something in my Grandfathers diary made me think of a grandfather clock\n")
        time.sleep(1)
        prYellow(riddles[2])
        time.sleep(1)
        print_slow("\nYou take a closer look at the grandfather clock, it isn't running but the time is stuck at 12 dead")
        hero.append("12")
        time.sleep(1)
        downstairs()
    elif interact == 1 :
        time.sleep(1)
        print_slow("\nYou look over the sofa it's quite grand, brown leather, wooden legs but looks like it hasn't been sat on in a long time\n")
        time.sleep(1)
        lounge()
    elif interact == 3 :
        time.sleep(1)
        print_slow("\nThe coffee table is really quite beautiful, you guess it is an antique but it doesn't offer anything useful\n")
        time.sleep(1)
        lounge()
    elif interact == 2 :
        time.sleep(1)
        print_slow("\nThe fire place is dirty and well used, you have a closer look but nothing else stands out\n")
        time.sleep(1)
        lounge()
    elif interact == 5:
        time.sleep(1)
        print(hero)
        time.sleep(1)
        lounge()
    elif interact == 6:
        time.sleep(1)
        diary()
        time.sleep(1)
        lounge()
    else:
        time.sleep(1)
        print_slow("\nYou leave the room")
        downstairs()

def study():
    global hero
    print_slow("\nYou enter the study and have a quick look around. You can see \n1.A desk \n2.A small bin \n3.An old laptop \n4.A computer chair \n5.Check Diary \n6.Check Inventory\n7.Leave Room\n")
    print_slow("\nWhat would you like to look at? ")
    interact = int(input("\n: "))
    if interact == 1:
        time.sleep(1)
        print_slow("\nI'm sure something in my Grandfathers diary made me think of a desk\n")
        time.sleep(1)
        prYellow(riddles[0])
        time.sleep(1)
        print_slow("\nYou take a closer look at the desk, wipe off some of the dust and spot a stain in the corner that looks like the number 52\n")
        hero.append("52")
        study()
    elif interact == 2:
        time.sleep(1)
        print_slow("\nYou have a rumage around the bin but there is nothing interesting in there\n")
        time.sleep(1)
        study()
    elif interact == 3:
        time.sleep(1)
        print_slow("\nThe laptop looks ancient, and you can't find a power lead making it useless to you\n")
        time.sleep(1)
        study()
    elif interact == 4:
        time.sleep(1)
        print_slow("\nThe chair looks suprsingly nice, you sit down and it is extremely comfortable\n")
        time.sleep(1)
        study()
    elif interact == 5:
        time.sleep(1)
        diary()
        time.sleep(2)
        study()
    elif interact == 6:
        time.sleep(1)
        print(hero)
        time.sleep(1)
        study()
    else:
        time.sleep(1)
        print_slow("\nYou leave the room\n")
        time.sleep(1)
        downstairs()

def upstairs():
    global hero
    print_slow("\nYou go upstairs and have a quick look around. You can see \n 1.A Bathroom, \n 2.A Bedroom, \n 3.A Library \n 4.Check Diary \n 5.Check Inventory \n 6.Leave Room")
    print_slow("\nWhat room would you like to look at? ")
    interact = int(input ("\n: "))
    if interact == 1:
        time.sleep(1)
        print_slow("\nLet's check out the bathroom\n")
        playsound("C:\\Users\\AB\\Downloads\\ES_Footsteps.wav")
        time.sleep(1)
        bathroom()
    elif interact == 2:
        time.sleep(1)
        print_slow("\nLet's check out the bedroom\n")
        playsound("C:\\Users\\AB\\Downloads\\ES_Footsteps.wav")
        time.sleep(1)
        bedroom()
    elif interact == 3:
        time.sleep(1)
        print_slow("\nI'm sure one of the riddles in Grandfathers diary made me think of a Library\n")
        playsound("C:\\Users\\AB\\Downloads\\ES_Footsteps.wav")
        time.sleep(1)
        prYellow(riddles[4])
        time.sleep(1)
        print_slow("\nLet's check it out\n")
        library()
    elif interact == 4:
        time.sleep(1)
        diary()
        time.sleep(2)
        upstairs()
    elif interact == 5:
        time.sleep(1)
        print(hero)
        time.sleep(1)
        upstairs()
    else:
        time.sleep(1)
        print_slow("\nYou leave the room\n")
        time.sleep(1)
        downstairs()


def garden():
    global hero
    print_slow("\nYou are in the garden, you see some items laying around the garden.\n\n")
    print_slow("What would you like to do?\n\n1. Enter the kitchen.\n2. Enter the front door.\n3. Interact with the gnomes.\n4. Interact with the bbq.\n5. Interact with the map.\n6. Interact with the diary.\n7. Check Inventory\n")
    i = int(input("\n: "))
    if i==1:
        time.sleep(1)
        kitchen()
    elif i==2:
        time.sleep(1)
        downstairs()
    elif i==3:
        playsound("C:\\Users\\AB\\Downloads\\ES_Trumpet_Muted.wav")
        print_slow("\nThis can't be right.\n")
        time.sleep(1)
        garden()
    elif i==4:
        print_slow("\nThis isn't it.\n")
        time.sleep(1)
        garden()
    elif i==5:
        print_slow("\nAha! of course, a map!\n")
        prYellow(riddles[3])
        print_slow("\nYou look around the map and notice the number 15 written in the corner!\n")
        hero.append("15")
        time.sleep(1)
        garden()
    elif i==6:
        time.sleep(1)
        diary()
        time.sleep(1)
        garden()
    elif i==7:
        time.sleep(1)
        print(hero)
        time.sleep(1)
        garden()
    else:
        garden()


def downstairs():
    global hero
    i=" "
    print_slow("\nYou are in the hallway.\n")
    print_slow("What would you like to do?\n\n1. Go upstairs\n2. Enter the study\n3. Enter the kitchen\n4. Enter the lounge\n5. Go to the garden\n6. Interact with the diary.\n7. Check Inventory\n")
    i=int(input("\n: "))
    if i==2:
        playsound("C:\\Users\\AB\\Downloads\\ES_Footsteps.wav")
        study()
    elif i==1:
        playsound("C:\\Users\\AB\\Downloads\\ES_Footsteps.wav")
        upstairs()
    elif i==3:
        playsound("C:\\Users\\AB\\Downloads\\ES_Footsteps.wav")
        kitchen()
    elif i==4:
        playsound("C:\\Users\\AB\\Downloads\\ES_Footsteps.wav")
        lounge()
    elif i==5:
        playsound("C:\\Users\\AB\\Downloads\\ES_Footsteps.wav")
        garden()
    elif i==6:
        time.sleep(1)
        diary()
        time.sleep(1)
        downstairs()
    elif i==7:
        time.sleep(1)
        print(hero)
        time.sleep(1)
        downstairs()
    else:
        print_slow("\nPlease select one of the available options.\n")
        time.sleep(1)
        downstairs()


def outside():
    global hero
    print_slow("You approach your Grandfather's house.\n\n")
    print_slow("What would you like to do?\n1. Look around.\n2. Enter the house.\n3. Search the garden.\n4. Interact with the diary.\n5. Check Inventory\n")
    i = int(input("\n: "))
    if i==2:
        playsound("C:\\Users\\AB\\Downloads\\ES_Footsteps.wav")
        downstairs()
    elif i==3:
        playsound("C:\\Users\\AB\\Downloads\\ES_Footsteps.wav")
        garden()
    elif i==1:
        time.sleep(3)
        print("You waste some time...\n")
        outside()
    elif i==4:
        time.sleep(1)
        diary()
        time.sleep(1)
        outside()
    elif i==5:
        time.sleep(1)
        print(hero)
        time.sleep(1)
        outside()
    else:
        print("Please select '1', '2', '3', '4' or '5'.\n")
        time.sleep(1)
        outside()

def intro():
    print_slow("\nYou get home from work one day to the news that your beloved Grandfather has tragically died of food poisoning.\n")
    print_slow("The following morning you contact his lawyer, who presents you with his will.\n")
    print_slow("You discover that your Grandfather has left you his fortune!\n")
    print_slow("Unfortunately, he does not trust his traitorous housekeeper to not take the fortune for herself.\n")
    print_slow("He leaves you a key to his cottage along with his diary which you notice has clues inside.\n")
    print_slow("This must lead to his treasure!\n\n")
    print_slow("You realise you must go to his cottage in order to solve his set of clues...\n\n")
    time.sleep(3)
    outside()

intro()