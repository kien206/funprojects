import turtle
import winsound

# turtle giup tao background (nhu pygame)
screen = turtle.Screen()
screen.title('Ping Pong')
screen.bgcolor('Black')
screen.setup(width=800, height=700)
screen.tracer(0)  # basically stops the game from updating?? -> runs faster

# Score
player1_score = 0
player2_score = 0

# Paddle 1
paddle_a = turtle.Turtle()  # tao object
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('White')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-375, 0)

# Paddle 2
paddle_b = turtle.Turtle()  # tao object
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('Blue')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(375, 0)

# Ball
ball = turtle.Turtle()  # tao object
ball.speed(0)
ball.shape('circle')
ball.color('Red')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('White')
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write('Player 1: 0 | Player 2: 0', align='center', font=('Courier', 24, 'normal'))

# Movement function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)


# Keyboard binding
screen.listen()  # listen to keyboard input
screen.onkeypress(paddle_a_up, 'w')
screen.onkeypress(paddle_a_down, 's')
screen.onkeypress(paddle_b_up, 'Up')
screen.onkeypress(paddle_b_down, 'Down')
# Main game
while True:
    screen.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border change
    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1  # reverse direction
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player2_score += 1
        pen.clear()
        pen.write('Player 1: {} | Player2: {}'.format(player1_score, player2_score), align='center',
                  font=('Courier', 24, 'normal'))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player1_score += 1
        pen.clear()
        pen.write('Player 1: {} | Player2: {}'.format(player1_score, player2_score), align='center',
                  font=('Courier', 24, 'normal'))

    # Paddle and ball collision
    if ball.xcor() > 365 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.dx *= -1
        ball.setx(365)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    if ball.xcor() < -365 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.dx *= -1
        ball.setx(-365)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
