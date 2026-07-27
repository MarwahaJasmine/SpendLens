import turtle

# Create a screen
screen = turtle.Screen()
screen.title("Turtle Screen")

# Create the turtle
t = turtle.Turtle()
t.speed(5)
t.color("blue")
t.shape("turtle")

# Keep the window open
screen.mainloop()

import turtle

turtle.goto(200, 100)    
turtle.goto(-100, -100)  
turtle.goto(0, 0)        

print(turtle.xcor())     
print(turtle.ycor())  
what is goi