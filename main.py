# 2/7/20
# Evan Dobson
# Project: Alien crash
# Module: main

# There's 96 different ways to play!
import time

import choose_path_1 as cp1 # imports the choose_path_1 file
import choose_path_2 as cp2 # imports the choose_path_2 file
import choose_path_3 as cp3 # imports the choose_path_3 file
import choose_path_5 as cp5 # imports the choose_path_3 file
import choose_path_6 as cp6 # imports the choose_path_3 file
import variables as var # imports the variables file

def display_intro(): # defines a function to display the intro 
    print("""
                   *     *     * Welcome to Alien crash! *     *     *
                   ---------------------------------------------------                   
    Oh no! Your spaceship crashed, now you're stranded on Earth with no way to contact
your people. To get back to your home world, you must venture out to find the materials to fix 
        your ship and come back. But be careful; if you are discovered by humans, 
                    you will be taken away and locked up for good.\n\n""")



while var.play_again == "yes": # creates a while loop that will run this code unless the player answers no
    
    var.continue_var1 = False # resets the variables to their original values (false)
    var.end = False

    display_intro() # Calls display function
    
    path_number_1 = cp1.choose_path1() # Go in house, sneak around, or ignore
    cp1.check_path1(path_number_1) 
    if var.end == True: # after the player chooses a path, it checks to see if the player was discovered
        var.play_again = " "
        while var.play_again != "yes" and var.play_again != "no": 
            time.sleep(4)
            print("\nDo you want to play again? (yes or no)")
            var.play_again = input()
        continue

    path_number_2 = cp2.choose_path2() # If there's a helecopter, run to or away from it
    cp2.check_path2(path_number_2)
    if var.end == True: # after the player chooses a path, it checks to see if the player was discovered
        var.play_again = " "
        while var.play_again != "yes" and var.play_again != "no":
            time.sleep(4)
            print("\nDo you want to play again? (yes or no)")
            var.play_again = input()
        continue

    if var.continue_var1 == True:
        path_number_5 = cp5.choose_path5() # Go around or through town 
        cp5.check_path5(path_number_5)
        if var.end == True: # after the player chooses a path, it checks to see if the player was discovered
            var.play_again = " "
            while var.play_again != "yes" and var.play_again != "no":
                time.sleep(4)
                print("\nDo you want to play again? (yes or no)")
                var.play_again = input()
            continue
   
    else:
        path_number_3 = cp3.choose_path3() # Leave or help the other alien (only if theres a helecopter and the player decides to run from it)
        cp3.check_path3(path_number_3)
        if var.end == True: # after the player chooses a path, it checks to see if the player was discovered
            var.play_again = " "
            while var.play_again != "yes" and var.play_again != "no":
                time.sleep(4)
                print("\nDo you want to play again? (yes or no)")
                var.play_again = input()
            continue
            
        path_number_4 = cp3.choose_path4() # Go with alien or get his materials (only if the player reaches 3)
        cp3.check_path4(path_number_4)
        if var.end == True: # after the player chooses a path, it checks to see if the player was discovered
            var.play_again = " "
            while var.play_again != "yes" and var.play_again != "no":
                time.sleep(4)
                print("\nDo you want to play again? (yes or no)")
                var.play_again = input()
            continue
            
    path_number_6 = cp6.choose_path6() # Investigate noise or leave
    cp6.check_path6(path_number_6)
    if var.end == True: # after the player chooses a path, it checks to see if the player was discovered
        var.play_again = " "
        while var.play_again != "yes" and var.play_again != "no":
            time.sleep(4)
            print("\nDo you want to play again? (yes or no)")
            var.play_again = input()
        continue

