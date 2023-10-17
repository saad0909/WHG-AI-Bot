class map:
    def __init__(self, cords, goal):
        self.cords = cords
        self.goal = goal
        
    def draw_map(self):
        fill(255, 255, 255)
        stroke(0, 0, 255)
        strokeWeight(2)
        beginShape()
        for c in self.cords:
            vertex(c[0],c[1])
        endShape(CLOSE) 
        strokeWeight(0)
        fill(255, 0, 0)
        ellipse(self.goal[0], self.goal[1], 15, 15)
