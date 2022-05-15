from turtle import Turtle, Screen         # import Turtle and Screen Functions from turtle module
t = Turtle()
screen = Screen()


def move_forward():
    t.forward(20)          # move forward by distance of 20
def move_left():
    t.left(20)
def move_right():
    t.right(20)
def move_backwards():
    t.back(20)
def clear_window():        # Create function that will clear whatever u draw and return back to starting point
    t.home()                    # Move turtle to origin (0,0) and set heading to start orientation
    t.clear()                   # delete turtle drawing from screen

screen.listen()            # see what user press: Example of event listeners
screen.onkey(move_forward, "w")       # pass in function with no argument, key as a string: example of higher order functions, where i pass in function to another function
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(move_backwards, "s")
screen.onkey(clear_window, "c")              # pressing c will clear turtle drawing


screen.exitonclick()             # window won't disappear until i click

