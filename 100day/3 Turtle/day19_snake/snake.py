from turtle import Screen, Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
PACE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

            
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
            
    def reset_snake(self):
        for segment in self.segments:
            segment.goto(5000,5000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
            
    def snake_on(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(PACE)
        
    def move(self, dir):
        if(dir == "up" and self.head.heading()!= 270):
            self.head.setheading(90)
            
        elif (dir == "down" and self.head.heading()!= 90):
            self.head.setheading(270)
            
        if(dir == "left" and self.head.heading()!= 0):
            self.head.setheading(180)
            
        elif (dir == "right" and self.head.heading()!= 180):
            self.head.setheading(0)
        print(self.head)
        
    def add_segment(self, pos):
            part = Turtle("square")
            part.penup()
            part.color("white")
            part.goto(pos)
            self.segments.append(part)
            
    def grow(self):
        self.add_segment(self.segments[-1].position())
        
    def self_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False