from brain import *

class bot:
    def __init__(self, area, start, goal, rad=10):
        self.radius = rad
        self.start = PVector(start[0],start[1])
        self.pos = PVector(start[0],start[1])
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.dead = False
        self.fitness = -1
        self.brain = brain(500)
        self.area = area
        self.goal = goal
        self.win = False
        
    def reset(self):
        self.pos = PVector(self.start[0],self.start[1])
        self.dead = False
        self.brain.steps = 0
        self.vel = PVector(0,0)
        self.acc = PVector(0,0)
        
    def show(self,isbest = False):
        if isbest:
            fill(0,255,0)
            ellipse(self.pos.x, self.pos.y, self.radius, self.radius)
        elif self.dead:
            fill(0,0,0)
            ellipse(self.pos.x, self.pos.y, self.radius, self.radius)
        else:
            fill(200,100,150)
            ellipse(self.pos.x, self.pos.y, self.radius, self.radius)
    
    def circle_inside_polygon2(self, point, radius, polygon):
        n = len(polygon)
        inside = False
        p1x, p1y = polygon[0]
        for i in range(n + 1):
            p2x, p2y = polygon[i % n]
            if point[1] > min(p1y, p2y):
                if point[1] <= max(p1y, p2y):
                    if point[0] <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (point[1] - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                            if p1x == p2x or point[0] <= xinters:
                                inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def circle_inside_polygon(self):
        p1 = self.circle_inside_polygon2([self.pos[0],self.pos[1]+self.radius-2],self.radius,self.area)
        p2 = self.circle_inside_polygon2([self.pos[0]+self.radius,self.pos[1]],self.radius,self.area)
        p3 = self.circle_inside_polygon2([self.pos[0]-self.radius+2,self.pos[1]],self.radius,self.area)
        p4 = self.circle_inside_polygon2([self.pos[0],self.pos[1]-self.radius+2],self.radius,self.area)
        if p1 == p2 == p3 == p4:
            return True
        return False
    
    def move(self):
        if self.brain.steps < len(self.brain.directions):
            self.acc = self.brain.directions[self.brain.steps]
            self.brain.steps += 1
        else:
           # print("brain dead")
            self.dead = True

        self.vel.add(self.acc)
        self.vel.limit(5)
        if self.circle_inside_polygon() == True:
            self.pos.add(self.vel)
        else:
            #print("died by coliding with wall")
            self.dead = True
    
    def update(self, obs):
        for pos in obs:
            if dist(self.pos[0],self.pos[1],pos[0],pos[1]) < pos[2]-5: 
                self.dead = True
                #print("collided with balls")
                
        if self.dead == False:
            self.move()
            
        if self.pos[1] >= self.goal[1]:
            print("win")
            if self.win == False:
                self.win = True
                with open("best.txt", 'w') as file:
                    for x in self.brain.directions:
                        st = str(x[0])+" "
                        st += str(x[1])
                        file.write(st+'\n')
                file.close()
            self.dead = True
        
        if self.dead == True:
            self.calculate_fitness()
    
    def calculate_fitness(self):
        dist_to_goal = int(math.sqrt((self.pos[0] - self.goal[0])**2 + (self.pos[1] - self.goal[1])**2))
        self.fitness = int(dist_to_goal)
    
    def crossover(self, parent, bot2 = 0, swap=0, cvp=0):
        cvp-=10
        if cvp < 0:
            cvp = 0
        if swap == 0:
            crossover_point = self.brain.steps-1
            for i in range(crossover_point, len(self.brain.directions)):
                temp = self.brain.directions[i]
                self.brain.directions[i] = parent.brain.directions[i]
                parent.brain.directions[i] = temp
        
        else:
            for i in range(0, cvp):
                self.brain.directions[i] = parent.brain.directions[i]
                
            for i in range(cvp, len(self.brain.directions)):
                self.brain.directions[i] = bot2.brain.directions[i]
