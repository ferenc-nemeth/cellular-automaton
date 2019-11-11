##
# @file     cellular_automaton.py
# @author   Ferenc Nemeth
# @date     3 Nov 2019
# @brief    This script generates every generation of a cellular automaton based on the input criteria.
#
#           Copyright (c) 2019 Ferenc Nemeth - https://github.com/ferenc-nemeth/
#

import numpy as np
from PIL import Image
import scipy.signal
import sys

# Create the next generation based on the original generation, born and survival conditions.
def ca_next_generation(original, condition_born, condition_survive):
    # Count the neighbors with convolve2d.
    count = scipy.signal.convolve2d(original, np.ones((3,3)), mode="same", boundary="wrap") - original

    # Check (and return), if the counted neighbors contain the born values, then repeat with the survival ones.
    return (np.isin(count, condition_born) | ((1 == original) & np.isin(count, condition_survive)))

# Save the input array into a given filename.
def ca_save(array_to_save, filename, factor):
    # Turn the bool array, into an uint8 one, then convert the values into black and white one.
    # 8-bit image: 0 == black; 255 == white.
    im = Image.fromarray(np.array(array_to_save, dtype="uint8")*255, "L")
    # Make it "factor" times bigger, so it is more visible.
    im = im.resize((im.size[0]*factor, im.size[1]*factor))
    im.save(filename)

# Create the space and the initial generation (random values).
def ca_init(full_height, full_width, initial_height, initial_width):
    # The total (or full) area is filled with zeros.
    full = np.zeros((full_height, full_width), dtype="bool")
    # Some random noise for the original generation.
    initial_random = np.random.randint(0, 2,(initial_height, initial_width))
    # Place the random stuff into the center of the area.
    full[(full_height//2)-(initial_height//2):(full_height//2)+(initial_height//2), (full_width//2)-(initial_width//2):(full_width//2+initial_width//2)] = np.copy(initial_random)
    
    return full

# Main function.
def main():
    # Get the input parameters.
    if (8 == len(sys.argv)):
        full_width = int(sys.argv[1])
        full_height = int(sys.argv[2])
        initial_width = int(sys.argv[3])
        initial_height = int(sys.argv[4]) 
        generations = int(sys.argv[5])
        # The elements of the array are separated with ","
        # To get a numpy array, it needs to be turned into a map, then into a list and then into an actual numpy array. Huhh...
        condition_born = np.array(list(map(int ,sys.argv[6].split(","))))
        condition_survive = np.array(list(map(int, sys.argv[7].split(","))))

        # Create the generation zero and save it.
        ca = ca_init(full_height, full_width, initial_height ,initial_width)
        # Into the output folder with the name "0.png" and make it five times bigger.
        ca_save(ca, "output/0.png", 5)
        # Create all the other generations and save them.
        for i in range(1, generations+1):
            ca = ca_next_generation(ca, condition_born, condition_survive)
            ca_save(ca, "output/{:d}.png".format(i), 5)
    # Wrong input parameters.
    else:
        print("The following parameters are needed: full_width, full_height, initial_width, initial_height, generations, condition_born(array) and condition_survive(array)")
        print("For example, to generate Day&Night: python3 cellular_automaton.py 100 200 10 20 500 3,6,7,8 3,4,6,7,8")
        
# Starting point of the script.
if ("__main__" == __name__):
    main()

