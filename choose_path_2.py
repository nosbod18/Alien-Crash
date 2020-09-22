# 2/10/20
# Evan Dobson
# Project: Alien crash
# Module: choose_path_2

import time
import random
import variables as var

def choose_path2(): # defines a function to allow the player to choose a path
    is_helecopter = random.randint(1,2) # sets a random number (1 or 2) to is_helecopter 
    if is_helecopter == 1: # checks if is_helecopter equals 1
        print("\n\nAfter you walk some more, you start to hear the unmistakable sound of a helecopter.")
        time.sleep(3.5)
        print("\nThis didn't sound like an ordinary helecopter, this one was big. Proabably military.")
        time.sleep(3.5)
        print("\nYou briefly laugh at the chances of you meeting a helecopter out here, but right now your only focus is to evade the helecopter,")
        print("which you can now see, heading straight towards you")
        time.sleep(4.5)
        print("\nThere's a grove of trees far ahead that would provide you with a good hiding spot, but theres a good chance the helecopter will see you before you get there.")
        time.sleep(3.5)
        print("\nOr you could go back to that run down house you passed a while ago, but you would lose a lot of time, which only increases the chance of your ship being found.")
        time.sleep(3.5)
        
        path2 = " "
        while path2 != "1" and path2 != "2": # defines a while loop that will display the code below until the player enters 1 or 2
            print("\nWill you run towards the helecopter, or will you play it safe and run back? (1 or 2)")
            path2 = input()
        return(path2)
        
    else:
        print("\nAs you walk, you start to see buildings on the horizon. Looks like a town is ahead, but it's still a long way off.")
        time.sleep(3.5)
        print("\nYou start worrying about all the things that could go wrong, like your ship being found, or someone spotting you out here in the open.")
        time.sleep(3.5)
        print("\nYou quicken your stride.")
        time.sleep(3)
        print("\nFinally you reach the edge of the town. On the other side of it is a big scrapyard where there is sure to be enough materials for you.")
        time.sleep(3.5)
        var.continue_var1 = True

        
def check_path2(path2): # defines a function to check which path the player took
    if path2 == str(1): # checks if the path the player entered equals 1
        print("\nYou start sprinting towards that small patch of trees way up ahead.")
        time.sleep(3.5)
        print("\nAs you run, you notice the trees don't seem to be getting any closer. They're a lot farther away than you thought.")
        time.sleep(3.5)
        print("\nThe helecopter's even closer now.")
        time.sleep(3)
        print("\nJust as you're about to enter the trees, the helecopter is right above you. A spotlight bursts on,")
        time.sleep(3.5)
        
        is_discovered = random.randint(1,10) # sets a random number (1 or 2) to is_discovered 
        if is_discovered > 3: # checks to see if is_discovered equals the path the player chose
            print("\nilluminating everything around you! A feeling of dread creeps in you as you know you have been spotted.")
            time.sleep(3.5)
            print("\nYou dive behind a fallen tree and try your best to hide, but to no avail.")
            time.sleep(3.5)
            print("\nYou hear feet hitting the ground as people are lowered from the helecopter, which has been hovering over the patch of trees.")
            time.sleep(3.5)
            print("\nPeople rush into the woods and in no time you are found...")
            time.sleep(3.5)
            print("\n\nYou were discovered! You got taken away by the government, never to be seen again...")
            var.end = True
                    
        else:
            print("\nbut you are already in the woods. You dive behind a fallen tree and wait, terrified that you were spotted.")
            time.sleep(3.5)
            print("\nThe helecopter hovers over the woods, its spotlight sweeping from side to side.")
            time.sleep(3.5)
            print("\nLuckily, the leaves are dense enough that only a little of the light penetrates into the woods.")
            time.sleep(3.5)
            print("\nAfter what seems like forever, the helecopter flys off and you breathe a huge sigh of relief.")
            time.sleep(3.5)
            print("\nThat was close. Again. You need to be more careful.")
            time.sleep(3)
            print("\nYou start walking, and soon see a town on the horizon. There's a scrapyard on the outskirts.")
            time.sleep(3.5)
            print("\nHopefully it's big enough materials for you to find everything you need.")
            time.sleep(3.5)
            print("\nOnce your reach the scrapyard, all doubts are flung from your mind.")
            time.sleep(3.5)
            print("\nPiles and piles of materials are scattered all around. You will definately be able to find all the materials you need.")
            time.sleep(3.5)
            print("\nAs you are searching for the last few pieces, you hear a strange whirring noise followed by a tremendous crash")
            print("which scares you so bad you drop all of your materials.")
            time.sleep(4.5)
            print("\nGrumbling as you pick them up, you go and investigate the noise.")
            time.sleep(3.5)
            
            is_person = random.randint(1,10)
            if is_person == 1:
                print("\nAs you round a pile of scrap metal where the noise came from, you see a person operating a huge crane. He spots you immediatly and you know it...")
                time.sleep(3.5)
                print("\n\nYou were discovered! You got taken away by the government, never to be seen again...")
                var.end = True
                
            else:
                print("\nAs you round the pile of scrap metal where the noise came from, you see nothing obvious that could have made such a noise.")
                time.sleep(3.5)
                print("\nAfter a little more investigating, the wind blows past you making the same whirring noise you heard earlier.")
                time.sleep(3.5)
                print("\nThe wind knocks off a piece of metal from the top of the stack, which then falls and makes the same huge crash.")
                time.sleep(3.5)
                print("\nBreathing a sigh of relief that it wasn't a human made sound, you leave the scrapyard with your materials in tow.")
                time.sleep(3.5)
                        
                people_at_crash = random.randint(1,10)
                if people_at_crash > 3:
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
                    time.sleep(3)
                    print("\nAfter another hard couple of hours hammering away, your ship is repaired.")
                    time.sleep(3.5)
                    print("\nYou engage the warp drive and jump into hyperspace, on your way home.")
                    time.sleep(3.5)
                    print("\n\nCongradulations! You repaired your ship and left Earth without being discovered by the humans!")
                    var.end = True
            
    elif path2 == str(2):
        print("\nYou look at the trees ahead, but decide to play it safe. Turning around, you sprint back to the house.")
        time.sleep(3.5)
        print("\nYou make it into the house with plenty of time before the helecopter flys over. Turning around, you take in the inside of the house.")
        time.sleep(3.5)
        print("\nAs you look around, the sight of a body on the ground startles you hard enough to knock over some jars on the table. Is it dead?")
        time.sleep(3.5)
        print("\nThe body jumps to his feet, just as startled as you are. Oh. Not dead, just asleep. Wait...")
        time.sleep(3.5)
        print("\nHe's another alien... just like you.")
        time.sleep(3.5)
        print("\nAfter getting to know him a little, you learn that he desperatly needs your help. If you help him, he is sure to reward you.")
        time.sleep(3.5)
        print("\nHowever, helping him will cost a lot of time.")
        time.sleep(3.5)


