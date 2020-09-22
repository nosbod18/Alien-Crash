# 2/11/20
# Evan Dobson
# Project: Alien crash
# Module: choose_path_5

import time
import random
import variables as var


def choose_path5():
    path5 = " "
    while path5 != "1" and path5 != "2":
        print("\nYou can go through the town, or around the town, which is much safer but much slower. Which do you do? (1 or 2)")
        path5 = input()
    return(path5)
    
def check_path5(path5):
    if path5 == str(1):
        print("\nThe day is already growing late, and you decide it would be best to cut through the town. You will just have to be extra careful.")
        time.sleep(3.5)
        print("\nAs you run through the town, you try to stick to the alleyways and shadows as much as possible, only crossing big roads when absolutely necessary.")
        time.sleep(3.5)
        print("\nYou hear voices right up ahead. They sound like kids.")
        time.sleep(2.5)
        print("\nYou duck behind a box in the alley and try your best to make yourself as small as possible.")
        time.sleep(3.5)
        print("\nThey pass you, a group of small children, but luckily they don't look your way.")
        time.sleep(3.5)
        print("\nYou let out a shaky breath. Maybe you should've gone around.")
        time.sleep(3.5)
        print("\nYou come up to the main road; it's going east to west, which is a shame because you're going north.")
        time.sleep(3.5)
        print("\nYou will have to cross it.")
        time.sleep(2)
        print("\nYou take a deep breath, check both ways multiple times, and when there's no one in sight you dash across...")
        time.sleep(3.5)
        print("\nYou made it! You stop in the alley between two shops to catch your breath.")
        time.sleep(3.5)
        
        is_discovered = random.randint(1,10)
        if is_discovered > 3:
            print("\nOnce your ready to continue, you come out of the alley and run down the sidewalk and turn the corner...")
            time.sleep(3.5)
            print("\nand run right into someone!...")
            time.sleep(3.5)
            print("\n\nYou were discovered! You got taken away by the government, never to be seen again...")
            var.end = True
            
        else:
            print("\nOnce you could breathe normally again, you continue down the alley you ran into. It looks like its a straight shot to the scrapyard.")
            time.sleep(3.5)
            print("\nYou burst out of the alley, right into the scrapyard. There are materials galore here.")
            time.sleep(3.5)
            print("\nAfter a time of gathering up the materials you need to repair your ship, you are ready to leave.")
            time.sleep(3.5)
            print("\nUnfortunately, you were unable to find a special piece you need for the warpdrive to operate at maximum thrust, but it can work without it.")
            time.sleep(3.5)
            print("\nJust as you were about to leave, you hear a small noise, almost like a whimper, coming from behind a big pile of scrap.")
            time.sleep(3.5)
            print("\nYou freeze, heart pounding, and strain to listen...")
            time.sleep(3.5)
            print("\nThere it is again! It's definately a whimper.")
            time.sleep(3.5)
            print("\nYou want to check out the noise, and a little more searching couldn't hurt. Maybe the special piece is over there.")
            time.sleep(3.5)
            
    elif path5 == str(2):
        print("\nYou decide the risk of the town is to great, it looks a lot of people could be in there.")
        time.sleep(3.5)
        print("\nGoing around the town will take longer, but you can just walk faster to make up for that.")
        time.sleep(3.5)
        print("\nHalfway around the town, you realize it's bigger than you thought. Maybe you should've gone through.")
        time.sleep(3.5)
        print("\nOnce you finally make it to the scrapyard, you forget all about the time that you spent getting there.")
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
            print("\nAs you round the pile of scrap metal where the noise came from, you see nothing obvious that could have made such a sound.")
            time.sleep(3.5)
            print("\nAfter a little more investigating, the wind blows past you making the same whirring noise you heard earlier.")
            time.sleep(3.5)
            print("\nThe wind knocks off a piece of metal from the top of the stack, which then falls and makes the same huge crash.")
            time.sleep(3.5)
            print("\nBreathing a sigh of relief that it wasn't a man made sound, you leave the scrapyard with your materials in tow.")
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
                print("\n\Congratulations! You repaired your ship and left Earth without being discovered by the humans!")
                var.end = True
