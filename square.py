import turtle


def draw_sqr(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
    

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    alex = turtle.Turtle()
    draw_sqr(alex, 60)
    wn.exitonclick()


if __name__ == "__main__":
    main()    
    