import turtle

def draw_school_logo():
    turtle.bgcolor("white")
    turtle.title("Anna-Freud-Schule Logo")

    # Beispielzeichnung
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.circle(50)

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.write("Anna-Freud-Schule", align="center", font=("Arial", 12, "normal"))

    turtle.exitonclick()

# Hauptprogramm
draw_school_logo()
