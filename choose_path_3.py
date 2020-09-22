# 2/10/20
# Evan Dobson
# Project: Alien crash
# Module: choose_path_3

import time
import random
import variables as var

    
def choose_path3(): # defines a function to allow the player to choose a path    
    path3 = " "
    while path3 != "1" and path3 != "2":
        print("\nWill you help him? Or will you leave him? (1 or 2)")
        path3 = input()
    return(path3)
    
def check_path3(path3): # defines a function to check which path the player took
    if path3 == str(1): # checks if the path the player entered equals 1
        print("\nHe is ecstatic when you tell him that you'll help him. You learn that he needs help rebuilding a part of his ship")
        time.sleep(3.5)
        print("\nHe doesn't have the mechanical knowledge to fix it, but you do.")
        time.sleep(3.5)
        print("\nAfter a hard few hours of work, the ship is up and ready to go. As his thanks, he offers you the reward.")
        time.sleep(3.5)
        
        def choose_path4():
            path4 = " "
            while path4 != "1" and path4 != "2":
                print("\nYou can go with him on his ship, but that means leaving all your hard earned treasures on your ship.")
                time.sleep(3.5)
                print("\nOr he can give you the rest of his materials so you can fix your ship and keep your treasures.")
                time.sleep(3.5)
                print("\nWhat will you do? (1 or 2)")
                path4 = input()
            return(path4)
            
        def check_path4(path4): # defines a function to check which path the player took
            if path4 == str(1): # checks if the path the player entered equals 1
                print("\nYou tell him that you would like to accompany him on his voyage home.")
                time.sleep(3.5)
                print("\nYou feel a deep regret for leaving your ship and its valuables here on Earth, but maybe one day you'll come back to get it.")
                time.sleep(3.5)
                print("\n\nCongradulations! You left Earth without being discovered by the humans!")
                var.end = True
                
            elif path4 == str(2):
                print("\nYou tell him that his offer is generous, but your ship is too precious to leave behind. He nods in understanding.")
                time.sleep(3.5)
                print("\nHe gives you the rest of his materials; its more than enough to finish the repairs on your ship.")
                time.sleep(3.5)
                print("\nAfter thanking him profusely, you leave the house and set off back towards your ship.")
                time.sleep(3.5)
                print("\nIt's night now, which gives you the benefit of darkness, but it also means a lot of time has passed. You quicken your stride.")
                time.sleep(3.5)
                
                people_at_crash = random.randint(1,4)
                if people_at_crash == 1:
                    print("\nAs you approach where your ship crashed, you notice a set of lights bobbing around. Looks like your ship has been found.")
                    time.sleep(3.5)
                    print("\nYou reach the top of the hill and lay down to avoid being seen while trying to figure out the best way to do this.")
                    time.sleep(3.5)
                    print("\nAfter a little bit of thinking, you decide to run to your ship while the people are out of view.")
                    time.sleep(3.5)
                    print("\nThe lights dissappear behind the ship. Ok. Time to run.")
                    time.sleep(3.5)
                    print("\nGetting up, you sprint down the hill with your materials in tow. They are making a lot of noise.")
                    time.sleep(3.5)
                    print("\nJust as you are about to reach the door and be safe, the people come running and catch you right as you were about to board...")
                    time.sleep(3.5)
                    print("\n\nYou were discovered! You got taken away by the government, never to be seen again...")
                    var.end = True
                    
                else:
                    print("\nIts eerily quiet as you reach where your ship crashed. You expected lots of people, but it doesn't seem like anyone's around.")
                    time.sleep(3.5)
                    print("\nYou reach the top of the hill and lay down to make sure there's no one here.")
                    time.sleep(3.5)
                    print("\nAfter inspecting the area around the ship, you are satisfied that no one is here.")
                    time.sleep(3.5)
                    print("\nAll the same, as you get up, you run down the hill, constantly looking left and right.")
                    time.sleep(3.5)
                    print("\nYou make it to the door without incident.")
                    time.sleep(3.5)
                    print("\nAfter another hard couple of hours hammering away, your ship is repaired.")
                    time.sleep(3.5)
                    print("\nYou engage the warp drive and jump into hyperspace, on your way home.")
                    time.sleep(3.5)
                    print("\n\nCongradulations! You repaired your ship and left Earth without being discovered by the humans!")
                    var.end = True
        
    elif path3 == str(2):
        print("\nHe frowns, and abruptly walks out of the room. Slightly troubled, you exit the house and continue on your way.")
        time.sleep(3.5)
        print("\nAfter a while, you are walking across a giant open field. It's very serene.")
        time.sleep(3.5)
        print("\nTo your surprise, you see the helecopter coming straight for you, again.")
        time.sleep(3.5)
        print("\nYou frantically look side to side, searching for a place to hide.")
        time.sleep(3.5)
        print("\nUnfortunatly, this time there's no where to hide.")
        time.sleep(2.5)
        print("\nThe helecopter is over you in no time, blinding you with its spotlight.")
        time.sleep(3.5)
        print("\nPeople are thudding to the ground all around you, dropping from the helecopter on ropes...")
        time.sleep(3.5)
        print("\n\nYou were discovered! You got taken away by the government, never to be seen again...")
        var.end = True