# 2/11/20
# Evan Dobson
# Project: Alien crash
# Module: choose_path_6

import time
import random
import variables as var

def choose_path6():
    path6 = " "
    while path6 != "1" and path6 != "2":
        print("\nDo you go and check out the noise? Or do you forget it and get back to your ship as soon as possible? (1 or 2)")
        path6 = input()
    return(path6)
    
def check_path6(path6):
    if path6 == str(1):
        print("\nYou start walking around the pile of scrap, nervous. Hopefully no people are over there.")
        time.sleep(3.5)
        print("\nYou hear the whimper again, closer. Whatever it is could be hurt.")
        time.sleep(3.5)
        print("\nThe source of the sound comes into view. It's a dog.")
        time.sleep(3.5)
        print("\nAs you get closer you notice its sleeping; it must be dreaming. You also notice the chain around its neck tying in to the wall.")
        time.sleep(3.5)
        print("\nYou accidentally step on a can, which makes a loud noise.")
        time.sleep(3.5)
        print("\nThe dog instantly is awake; barking ferociously and straining against the chain.")
        time.sleep(3.5)
        print("\nYou panic, looking around for someone to hear and come investigating.")
        time.sleep(3.5)
        print("\nSure enough, a man comes drunkenly staggering out of a little shed you didn't even notice before.")
        time.sleep(3.5)
        print("\nHe starts yelling at the dog to be quiet but stops in his tracks when he notices you...")
        time.sleep(3.5)
        print("\n\nYou were discovered! You got taken away by the government, never to be seen again...")
        var.end = True
        
    elif path6 == str(2):
        print("\nYou take a step towards the sound but then come to your senses.")
        time.sleep(3.5)
        print("\nWhatever it is, it's not worth your time. There could be people over there. You can live without that part too.")
        time.sleep(3.5)
        print("\nTurning away from the whimpering, you start out back to your ship, materials in tow.")
        time.sleep(3.5)
        print("\nThis time you go around the town, just to be safe...")
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
            print("Just as you are about to reach the door and be safe, the people come running and catch you right as you were about to board...")
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