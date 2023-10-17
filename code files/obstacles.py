import math

class obstacles:
    def __init__(self, obs):
        self.obs = obs
        self.velocity = []
        for x in self.obs:
            if x[0][1] == x[1][1]:
                self.velocity.append(PVector(7,0))
            elif x[0][0] == x[1][0]: 
                self.velocity.append(PVector(0,3.5))
            else:
                self.velocity.append(PVector(2,1))
                
        self.radius = [x[len(x)-2] for x in self.obs]
        self.pos = [PVector(x[0][0],x[0][1]) for x in self.obs]
    
    def move_obs(self):
        pos = [[x[0],x[1],r] for x,r in zip(self.pos,self.radius)]
        #return pos
        for index, x in enumerate(self.obs):
            if x[len(x)-1] == 'xyline':
                start_cord = [x[0][0],x[0][1]]
                end_cord = [x[1][0], x[1][1]]
                
                self.pos[index].add(self.velocity[index])
                e = end_cord[0]
                s = start_cord[0]
                y1 = start_cord[1]
                y2 = end_cord[1]
                
                if e < s:
                    s = e
                    e = start_cord[0]
                
                if y2 < y1:
                    y1 = y2
                    y2 = start_cord[1]
                    
                if self.pos[index][0] > e or self.pos[index][0] < s and s!=e:
                    self.velocity[index][0] *= -1
                
                if self.pos[index][1] > y2 or self.pos[index][1] < y1:
                    self.velocity[index][1] *= -1
                
                stroke(0)
                fill(255,0,0)
                ellipse(self.pos[index][0], self.pos[index][1], self.radius[index], self.radius[index])
        return pos
