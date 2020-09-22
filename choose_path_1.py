# 2/8/20
# Evan Dobson
# Project: Alien crash
# Module: choose_path_1

import time
import random
import variables as var


def choose_path1(): # defines a function to allow the player to choose a path
    time.sleep(7)
    print("After walking for a while, you come across a lone farm house. Smoke is coming out of the chimney, so you know people are there.")
    time.sleep(3.5)
    print("\nHowever, if you get discovered it's game over, but you need those materials.")
    time.sleep(3.5)
    
    path1 = " " # assigns an empty string to path and waits for the player to make a decision
    while path1 != "1" and path1 != "2" and path1 != "3": # defines a while loop that will display the code below until the player enters 1, 2, or 3
        print("\nWill you go into the house, sneak around to see if they have any materials, or avoid the house entirely? (1, 2, 3)")
        path1 = input()
    return(path1) # Gives the player input to the program for it to check it
    
    
def check_path1(path1): # checks what number the player input
    if path1 == str(1):
        print("\nYou nervously walk up to the house, waiting to be spotted. You test the door handle to see if it's unlocked, which it is. Strange...")
        time.sleep(3.5)
        print("\nYou wince as the door creaks loudly, but you manage to slip inside and close the door behind you.")
        time.sleep(3.5)
        print("\nAs you tiptoe through the house, trying to be as quiet as possible, a voice seems to be getting closer to you from down the hallway.")
        time.sleep(3.5)
        print("\nSo, in a panic, you run back the way you came...")
        time.sleep(3.5)
        
        is_discovered = random.randint(1,4) # sets a random number (1 to 4) to is_discovered 
        if is_discovered == 1: # checks to see if is_discovered equals 1
            print("\nand make it back outside. There's an old tractor that you hide behind, and as soon as you get behind it you hear someone step out onto the porch.")
            time.sleep(3.5)
            print("They go back inside, and you breathe a sigh of relief. You continue walking.")
            time.sleep(3.5)
            
        else:
            print("\nOnly to run directly into the father of the family!")
            time.sleep(3.5)
            print("\n\nYou were discovered! You got taken away by the government, never to be seen again...")
            var.end = True
        
    elif path1 == str(2):
        print("\nYou sneak up to investigate the barn that's a little ways away from the house. There could be some materials you need inside.")
        time.sleep(3.5)
        print("\nInside, there are tools and haybales on one side and animals on the other. You see the animals and instantly grow nervous.")
        time.sleep(3.5)
        print("\nKeeping an eye on the animals, you start checking for materials over by the toolbench.")
        time.sleep(3.5)
        print("\nSuddenly, one of the horses neighs loudly, which causes all the other animals to start making noise. Panicking, you hide in a stack of hay.")
        time.sleep(4)
        print("\nThe door to the barn is yanked open and someone comes in, shouting at the animals to be quiet. He eventually gets them to calm down, but that only makes it easier")
        print("for your gasping breaths to be heard.")
        time.sleep(4.5)
        print("\nYou hear feet shuffling in your direction, and you try your hardest to quiet your breathing.")
        time.sleep(3.5)
            
        is_discovered = random.randint(1,3) # sets a random number (1 to 3) to is_discovered
        if is_discovered == 1: # checks to see if is_discovered equals 1
            print("\nSuddely, a hand yanks you out of the hay! You come face to face with the father of the family....")
            time.sleep(3.5)
            print("\n\nYou were discovered! You got taken away by the government, never to be seen again...")
            var.end = True
            
        else:
            print("\nAfter a few tense moments, the person leaves the barn and closes the door. That was close.")
            time.sleep(3.5)
            print("\nYou get up out of the hay and brush off your clothes. After a little more searching...")
            time.sleep(3.5)
            
            found_materials = random.randint(1,4) # sets a random number (1 to 4) to found_materials
            if found_materials == 1: # checks to see if found_materials equals 1
                print("\nyou find the materials you need! You gather up as much of them as you can and exit the barn, glaring at the animals as you go.")
                time.sleep(3.5)
                print("\nStill wary of being discovered, you take the long way back, out of sight of the house.")
                time.sleep(3.5)
                
                people_at_crash = random.randint(1,3) # sets a random number (1 to 3) to people_at_crash
                if people_at_crash == 1: # checks to see if people_at_crash equals 1
                    print("\n\nAs you make your way back to your ship, you notice footprints and tire tracks in the ground that weren't there before. This worries you, because if your ship")
                    print("is found, there's no way to repare it without being seen.")
                    time.sleep(4.5)
                    print("\nYou crest the hill and to your horror, there are swarms of people surrounding your ship. Many of them look like farmers,")
                    print("and with all the pickup trucks around, you guess that these are all the locals.")
                    time.sleep(4.5)
                    print("\nYou flinch as someone comes up from behind you and grabs you by the arms, forcing you to drop your materials....")
                    time.sleep(3.5)
                    print("\n\nYou got discovered! You were taken away by the government, never to be seen again...")
                    var.end = True
                    
                else:
                    print("\nAs you approach your ship, you breathe a sigh of relief that no one has found it yet. That would've been be very bad for you.")
                    time.sleep(3.5)
                    print("\nYou run across the open field, materials still in your arms.")
                    time.sleep(3.5)
                    print("\nYour ship opens its door for you and you walk up into it, undiscovered. After a few hours of hammering and fixing, your ship is good to go.")
                    time.sleep(3.5)
                    print("\nYou fire up your newly repaired warp drive and shoot off into hyperspace.")
                    time.sleep(3.5)
                    print("\n\nCongradulations! You repaired your ship and left Earth without being discovered!")
                    var.end = True         
                            
            else:
                print("\nyou don't find any materials. Disappointed, you leave the barn, glaring at the animals as you go.")
                time.sleep(3.5)
                print("\nStill wary of being discovered, you take the long way, out of sight of the house.")
            
    elif path1 == str(3):
        print("\nYou look at the house, but decide the risk of discovery is too great. There are smarter ways to get the materials you need.")
        time.sleep(3.5)
        print("\nYou start walking.")
