from map import *
from levels import *
from obstacles import *
from bot import *
from brain import *
import time
import math

allow = True
lvl = 'level1'
best_bot_model = lvl+'.txt'
population = 100
start = levels[lvl][2]
goal = levels[lvl][3]
mapp = map(levels[lvl][0], goal)
obs = obstacles(levels[lvl][1])
bots = [bot(levels[lvl][0], start, goal) for x in range(population)]

store = []
counter = 0
prev_max = 0
def setup():
    global store
    global bots
    print("starting game...")
    size(1000,500)
    smooth()
    if allow == True:
        bots = [bot(levels[lvl][0], start, goal)]
        with open(best_bot_model, 'r') as file:
            for index, x in enumerate(file):
                if len(x) > 3:
                    val1 = float(x.strip().split(' ')[0])
                    val2 = float(x.strip().split(' ')[1])
                    bots[0].brain.directions[index] = PVector(val1,val2)
                    store.append(PVector(val1, val2))
        file.close()
                
    
obs_curr_pos = [[] for x in range(population)]
most_fit = 0
mutation = False

def draw():
    random.seed()
    global obs_curr_pos
    global bots
    global most_fit
    global obs
    global counter
    global prev_max
    global mutation
    noStroke()
    fill(60)
    rect(0,0,width,height)
    mapp.draw_map()
    if allow == True:
        if bots[0].dead == True:
            obs = obstacles(levels[lvl][1])
            obs_curr_pos = obs.move_obs()
            bots[0] = bot(levels[lvl][0], start, goal)
            for i in range(len(bots[0].brain.directions)):
                bots[0].brain.directions[i] = store[i]
        else:
            obs_curr_pos = obs.move_obs()
            bots[0].show()
            bots[0].update(obs_curr_pos)
    else:
        obs_curr_pos = obs.move_obs()
        dead_count = 0
        for b in bots:
            if b.fitness == most_fit:
                b.show(True)
            else:
                b.show()
            b.update(obs_curr_pos)
            if b.dead == True:
                dead_count+=1
        mutation = False
        if dead_count == population:
            print("counter: ", counter)
            if counter >= 10:
                counter = 0
                mutation = True
            else: counter+=1      
            bots = list(sorted(bots, key=lambda x: x.fitness))
            cvp = bots[0].brain.steps-1
            most_fit = int(bots[0].fitness)
            diff = abs(prev_max-most_fit)
            if most_fit == prev_max or (1 <= diff <= 3):
                counter+=1
            else:
                counter = 0
                prev_max = most_fit
            for index, b in enumerate(bots):
                parent = index
                while parent == index:
                    parent = int(random.uniform(1,population))
                if index != population-1 and index != 0:
                    if mutation == True:
                        print("mutating rest")
                        bots[index].brain.mutate()
                    else:
                        bots[index].crossover(bots[parent])
                else:
                    if mutation == True:
                        print("mutating best")
                        bots[index].brain.mutate(bots[0],cvp,True)
                    else:
                        bots[index].crossover(bots[0],bots[parent],1,cvp)
                mutation = False
                b.reset()
            obs = obstacles(levels[lvl][1])
            print("all reseted")
            print("best fitness: ", most_fit)
