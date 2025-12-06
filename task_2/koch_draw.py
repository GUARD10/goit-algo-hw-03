import turtle

from koch_algo import koch


def draw_snowflake(level: int) -> None:
    screen = turtle.Screen()
    root = screen._root
    root.attributes("-topmost", True)
    screen.title("Snowflake")

    turtle.tracer(0, 0)

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 100)
    t.pendown()

    for _ in range(3):
        koch(t, 300, level)
        t.right(120)

    turtle.update()
    print("Drawing complete. Close the window to exit.")
    turtle.done()