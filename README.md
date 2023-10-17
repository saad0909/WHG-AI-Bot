# World's Hardest Game AI Bot Trained Using Genetic Algorithm

![Untitled video - Made with Clipchamp (4)](https://user-images.githubusercontent.com/108808181/236902512-a25edf32-0f0c-4d59-8114-b7da1793086f.gif)

## Introduction

The World's Hardest Game is a notoriously difficult game that challenges players to navigate a small red square through a series of mazes filled with moving objects and deadly obstacles. To conquer this game, we trained an AI bot using Genetic Algorithm (GA) and Python programming language. 

The aim of the project was to create an AI bot that could successfully navigate through four levels of the game using GA. Each chromosome in the training represents an AI bot with a brain that has a capacity of 500 instructions, meaning it can take 500 steps before it dies. The bot dies when it touches a moving object or runs out of instructions, and if it collides with walls, it dies too. 

## The GA Process

The GA is an iterative process that involves generating a population of bots with randomly assigned brains and chromosomes. The fitness function is used to evaluate each bot's ability to survive and navigate through the game. The fitness function calculates the distance between the bot and the goal state, and the bot with the lowest distance is deemed the most fit. 

The next step is to select the most fit bot as the parent for the next generation. The crossover process is then applied to generate new bots. In crossover, the best bot's brain instructions are kept intact, and a random parent's instructions are used to replace the least fit bot's instructions. The crossover point is determined by the instruction that caused the bot to die. The parent is selected random to get crossover with high fitness chromosomes because we need to maintain diversity in our population so we cannot just discard the low fitness chromosomes

After seven generations, if the bot's fitness value of the best chromosome is not changing or no good performance is seen, we apply mutation instead of crossover. In mutation, all the instructions after the crossover point are replaced with randomly generated instructions. 

## Training the AI Bot

![Untitled video - Made with Clipchamp (3)](https://user-images.githubusercontent.com/108808181/236899632-deca25f6-a766-45d5-88a4-e3e86ea6d94f.gif)


To train the AI bot go to the main file and set allow = False this wil show training process and once trained, model is saved in best.txt and it can be manually copied to specific level.txt file to save the model.

![ezgif com-video-to-gif](https://github.com/saad090/WHG-AI-Bot/assets/108808181/e4551e07-0f79-489a-80dd-ed0c98ecdb71)

To see the already trained models playing the game move set the allow variable to True in main file. To select the level look for the specific level key in levels dictinory in levels.py.

![ezgif com-video-to-gif (2)](https://github.com/saad090/WHG-AI-Bot/assets/108808181/d19705b0-0740-4300-97c4-891708d8ef32)


To train the AI bot, we first created a Python program to simulate the game environment using Processing IDE. We then applied the GA process to train the bot to navigate through the game. Once the bot successfully reaches the goal state in each level, the best bot's brain instructions are saved in a text file representing the model and saved as level_n.txt where n is in range(0, 4) as many levels there are. In training the bot the complexity level of the the current level is not much of a issue as what impacts the efficiency of the algorithm the most is how much diversity is maintained in every genratetion as more diversity means more variety of instructions avaialble for the chromosomes to get as a result of crossover. In case all the bots are dying at same position then we will never converge to goal state using crossover and we need to perform mutation which will tkae a lot of time to converge.

## Analyzing the GA Performance

![newplot (2)](https://user-images.githubusercontent.com/108808181/236903903-d801a085-b1b0-4f62-b934-1d64c7f9765f.png)

![newplot (3)](https://user-images.githubusercontent.com/108808181/236904057-333e15e8-6d7e-4500-abad-7fbd5cfc9b11.png)


## Conclusion

In conclusion, we successfully trained an AI bot for the World's Hardest Game using Genetic Algorithm and Python programming language. The bot's performance improved with each generation, and the best bot's brain instructions were saved as models. With further improvements, this AI bot could potentially solve the World's Hardest Game efficiently by reducing the number of instructions used to reach the final goal. The project demonstrates the use of GA in AI bot training and showcases its potential for solving complex problems.


