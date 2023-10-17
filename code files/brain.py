import random
import math

class brain:
    def __init__(self, size):
        self.directions = [PVector(0, 0) for x in range(size)]
        self.steps = 0
        self.randomize()
    
    def randomize(self):
        random.seed()
        for i in range(len(self.directions)):
            randomAngle = random.uniform(0,2*math.pi)
            self.directions[i] = PVector.fromAngle(randomAngle);

    def mutate(self,b=0,cvp=0,bst = False):
        mutation_rate = 0.4
        if cvp < 7:
            cvp = 7
        if bst == True:
            for i in range(0,len(self.directions)):
                if i < cvp-7:
                    self.directions[i] = b.brain.directions[i]
                else:
                    random.seed()
                    randomAngle = random.uniform(0,2*math.pi)
                    self.directions[i] = PVector.fromAngle(randomAngle)
        else:
            if self.steps == 0 or self.steps == 1:
                self.steps = 2
            for i in range(self.step-2, len(self.directions)):
                random.seed()
                rand = random.uniform(0.1, 1)
                if rand < mutation_rate:
                    randomAngle = random.uniform(0,2*math.pi)
                    self.directions[i] = PVector.fromAngle(randomAngle)
