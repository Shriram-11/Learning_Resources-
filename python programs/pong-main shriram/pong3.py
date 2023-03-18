# Import required libraray 
import turtle; import time

#--------------------------------------------
#program variables
xdir=440
x_collision=412
collision_lrpad=230
gamestate='active' #active or passive
savestate='active' #active or passive

#these functions become passive on certain conditions
blueup_function='active'
bluedown_function='active'
redup_function='active'
reddown_function='active'
#or passive
#--------------------------------------------




#screen attributes
screen= turtle.Screen() 
screen.title("Pong") 
screen.bgcolor("#f0f0f0")
screen.setup(width=1000, height=600)


#net attributes
net=turtle.Turtle()
net.pensize(8)
net.goto(0,600)
net.color('black')
net.goto(0,-600)


if gamestate=='active':
  # Left paddle 
  lpad = turtle.Turtle() 
  lpad.speed(0) 
  lpad.shape("square") 
  lpad.color("blue") 
  lpad.shapesize(stretch_wid=6, stretch_len=1) 
  lpad.penup() 
  lpad.goto(-xdir, 0)

  #right paddle
  rpad = turtle.Turtle() 
  rpad.speed(0) 
  rpad.shape("square") 
  rpad.color("red") 
  rpad.shapesize(stretch_wid=6, stretch_len=1) 
  rpad.penup() 
  rpad.goto(xdir, 0)


elif gamestate=='passive':
  pass


# Ball of circle shape 
ball = turtle.Turtle() 
ball.speed(100) 
ball.shape("circle") 
ball.color("green") 
ball.penup() 
ball.goto(0, 0) 
ball.dx = 5
ball.dy = -5


# Initialize the score 
left_player = 0
right_player = 0


# Displays the score 
score = turtle.Turtle() 
score.speed(0) 
score.color("blue") 
score.penup() 
score.hideturtle() 
score.goto(0, 260) 
score.write("Left_player : 0    Right_player: 0",align="center", font=("Courier", 24, "normal")) 


#--------------------------------------------
# Functions to move paddle vertically 
def BlueUp():
  global gamestate

  if gamestate=='active':

    global blueup_function ;global bluedown_function

    if blueup_function=='active':

      y = lpad.ycor() 
      y += 20
      lpad.sety(y) 

    elif blueup_function=='passive':
      pass

    bluedown_function='active'

  elif gamestate=='passive':
    pass


def BlueDown():
  global gamestate

  if gamestate=='active':

    global blueup_function ;global bluedown_function

    if bluedown_function=='active':

      yblue_cor=lpad.ycor() 
      yblue_cor-= 20
      lpad.sety(yblue_cor)

    elif bluedown_function=='passive':
      pass

    blueup_function='active'

  elif gamestate=='passive':
    pass


def RedUp():
  global gamestate

  if gamestate=='active':

    global redup_function ;global reddown_function

    if redup_function=='active':

      yred_cor= rpad.ycor() 
      yred_cor+= 20
      rpad.sety(yred_cor)

    elif redup_function=='passive':
      pass

    reddown_function='active'

  elif gamestate=='passive':
    pass


def RedDown():
  global gamestate

  if gamestate=='active':

    global redup_function ;global reddown_function

    if reddown_function=='active':

      yred_cor=rpad.ycor() 
      yred_cor-= 20
      rpad.sety(yred_cor)

    elif reddown_function=='passive':
      pass

    redup_function='active'

  elif gamestate=='passive':
    pass





def Save():

  global gamestate; global savestate
  global redup_function; global reddown_function; global blueup_function; global bluedown_function

  if savestate=='active':

    global left_player ;global right_player

    hour=str(time.strftime('%I'))
    minute=str(time.strftime('%M'))
    second=str(time.strftime('%S'))
    am_pm=str(time.strftime('%p'))

    date=str(time.strftime('%d'))
    month=str(time.strftime('%m'))
    year=str(time.strftime('%Y'))
    day=str(time.strftime('%a'))


    curtime=hour+':'+minute+':'+second+' '+am_pm
    curdate=date+'/'+month+'/'+year+' - '+day


    if left_player==0 and right_player==0:
      status='Start'

    elif left_player==right_player:
      status='Tie'

    elif left_player>right_player:
      status='Blue wins'

    elif left_player<right_player:
      status='Red wins'



    serial=open('serial.txt', 'r')

    if serial.read()=='':
    	serial=open('serial.txt', 'w')
    	serial.write('1')
    	serial.close()

    else:
    	serial=open('serial.txt', 'r')
    	var1=serial.read()
    	var1=int(var1)
    	var1+=1
    	var1=str(var1)
    	serial=open('serial.txt', 'w')
    	serial.write(var1)
    	serial.close()


    data=open('data.txt', 'a')
    data.write('\n\nGame number: '+var1+'\n')
    data.write('Blue score: '+str(left_player)+'\n')
    data.write('Red score: '+str(right_player)+'\n')
    data.write('Status: '+status+'\n')
    data.write('Recorded at: '+curtime+'\n')
    data.write('At date: '+curdate+'\n-------------------------------------')

  elif savestate=='passive':
    pass

  gamestate='passive'; savestate='passive'





#-----------------------------------------
#key bindings
screen.listen() 
screen.onkeypress(BlueUp, "w") 
screen.onkeypress(BlueDown, "s") 
screen.onkeypress(RedUp, "Up") 
screen.onkeypress(RedDown, "Down")
screen.onkeypress(Save, 'q')



while True:
  screen.update()

  if gamestate=='active':
      
    if lpad.ycor()<=-(collision_lrpad):
      bluedown_function='passive'

    if lpad.ycor()>=(collision_lrpad):
      blueup_function='passive'

    if rpad.ycor()<=-(collision_lrpad):
      reddown_function='passive'

    if rpad.ycor()>=(collision_lrpad):
      redup_function='passive'

    



    ball.setx(ball.xcor()+ball.dx) 
    ball.sety(ball.ycor()+ball.dy) 

    # Checking borders 
    if ball.ycor() > 280: 
      ball.sety(280) 
      ball.dy *= -1

    if ball.ycor() < -280: 
      ball.sety(-280) 
      ball.dy *= -1
    #for bouncing off the y axis border

    if ball.xcor() > 500: 
      ball.goto(0, 0) 
      ball.dy *= -1
      left_player += 1
      score.clear() 
      score.write("Left_player : {}    Right_player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal")) 

    if ball.xcor() < -500: 
      ball.goto(0, 0) 
      ball.dy *= -1
      right_player += 1
      score.clear() 
      score.write("Left_player : {}    Right_player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal")) 
      #for bouncing off the x axis border

      # Paddle and ball collision 
    if ball.xcor() > x_collision and ball.xcor() < x_collision+10 and ball.ycor() < rpad.ycor()+40 and ball.ycor() > rpad.ycor()-40: 
      ball.setx(x_collision) 
      ball.dx*=-1

    if ball.xcor()<-x_collision and ball.xcor()>-(x_collision+10) and ball.ycor()<lpad.ycor()+40 and ball.ycor()>lpad.ycor()-40: 
      ball.setx(-x_collision) 
      ball.dx*=-1


  elif gamestate=='passive':
    screen.bgpic('gameover.png')
    net.clear()
    lpad.clear()
    rpad.clear()
    ball.clear()
    score.clear()

