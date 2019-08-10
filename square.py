import turtle

# Window Design
window=turtle.Screen()
window.bgcolor("black")
window.title("Ball Animation")

# Shape Design
shape=turtle.Turtle()
shape.shape("square")
shape.shapesize(4)
shape.color("white")
shape.penup()
shape.speed(0)
shape.goto(0,200)

# Animation
shape.y=2
down=0.2

while True:
    shape.y -= down
    shape.sety(shape.ycor() +shape.y)
    
    if shape.ycor()<-270:
        shape.y*=-1         

window.mainloop()

#Created By Hamzah
