# cellular-automaton
A Cellular automaton generator for Python

### Table of Contents
- [Introduction](#introduction)
- [How it works](#how-it-works)
- [How to use it](#how-to-use-it)
- [References](#references)

### Introduction

This script can generate different kind of Cellular automatons [[1]](#references) based on input parameters.

### How it works

***[Demonstration videos on youtube.](https://www.youtube.com/playlist?list=PLwIV1dqznwSeTUnED8rprp_eUtDq7WBZv)***

The script creates an emtpy space (based on the input size) and generates a random array (based on the input size) in the middle of the space. After that, it generates and saves every single generation until it reaches the limit given by the user.

The user can manually set what ruleset they want to use.

Some pre-made samples:

<img src="https://raw.githubusercontent.com/ferenc-nemeth/cellular-automaton/master/design/conway.gif" >

*Figure 1. Conway's Game of Life.*

<img src="https://raw.githubusercontent.com/ferenc-nemeth/cellular-automaton/master/design/maze.gif" >

*Figure 2. Maze.*

<img src="https://raw.githubusercontent.com/ferenc-nemeth/cellular-automaton/master/design/replicator.gif" >

*Figure 3. Replicator.*

The functions of the script:

| Function           | Description                                                                                                      |
| ------------------ |:----------------------------------------------------------------------------------------------------------------:|
| main               | The main function.                                                                                               |
| ca_init            | Creates the space as an empty numpy array. Generates the generation zero with random values.                     |
| ca_save            | Saves the input array as an image with a given name and path. Also it's possible to enlarge the pixels.          |
| ca_next_generation | Generates the next cellular automation generation. It is possible to adjust the borning and surviving conditions.|

### How to use it

To use it, you need the following Python modules:
```
numpy
scipy
PIL
```

And you can run it with the following command:
```
python3 cellular_automaton.py full_width full_height initial_width initial_height generations condition_born(array) condition_survive(array)
```

For example:
```
python3 cellular_automaton.py 500 500 20 20 250 3 1,2,3,4,5
```
This creates a 500x500 sized space with an initial 20x20 randomly generated generation zero. The cellular automation has 250 generations and the rulestring is B3/S12345.

The born and survival values can be anything, the values must be separated with a comma.

### References
[1] [Wikipedia - Cellular Automaton](https://en.wikipedia.org/wiki/Cellular_automaton)
