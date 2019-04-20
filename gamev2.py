#STUDENTS: Adam Houser, Colin Reed, Marcus Gonzalez, Sergio Quiroz, Jason Pettit
#Team 5 - Pentagration
#CST205-40_SP19 Lab 12

import random

##################################################
#win/lose conditions
##################################################
#a simplified version of Clue!  Find the "killer"
#based on the clues in the rooms
#
#win by guessing the right "killer"
#lose by guessing wrong


##################################################
#SETUP SECTION OF THE GAME
##################################################
def collage():
#makes a 3 x 3 collage for the game board
  setMediaPath()
  study = makePicture("1_study.jpg")
  hallway = makePicture("2_hallway.jpg")
  lounge = makePicture("3_lounge.jpg")
  library = makePicture("4_library.jpg")
  billiard = makePicture("5_billiard.jpg")
  dining = makePicture("6_dining.jpg")
  conservatory = makePicture("7_conservatory.jpg")
  ballroom = makePicture("8_ballroom.jpg")
  kitchen = makePicture("9_kitchen.jpg")

  sourceFiles = [study,hallway,lounge,library,billiard,dining,conservatory,ballroom,kitchen]
  targetY = [0,0,0,200,200,200,400,400,400]
  targetX = [0,200,400,0,200,400,0,200,400]

  new_pic = makeEmptyPicture(600,600)

  for img in range(9):
    for x in range(0,getWidth(sourceFiles[img])):
      for y in range(0,getHeight(sourceFiles[img])):
        p = getPixel(sourceFiles[img],x,y)
        rgb_color = getColor(p)
        setColor(getPixel(new_pic,x+targetX[img],y+targetY[img]),rgb_color)

  return new_pic
#collage

def drawText(pic):
  new_pic = pic
  myStyle = makeStyle(sansSerif,bold,20)

  rooms = ["Study",
  "Hallway",
  "Lounge",
  "Library",
  "Billiard Room",
  "Dining Room",
  "Conservatory",
  "Ball Room",
  "Kitchen"]

  x = 30
  for room in rooms[:3]:
    y = 170
    addTextWithStyle(pic,int(x),int(y),room,myStyle,yellow)
    x += 200

  x = 30
  for room in rooms[3:6]:
    y = 370
    addTextWithStyle(pic,int(x),int(y),room,myStyle,yellow)
    x += 200

  x = 30
  for room in rooms[6:9]:
    y = 570
    addTextWithStyle(pic,int(x),int(y),room,myStyle,yellow)
    x += 200

  return new_pic

def drawLines(pic):
#draws the lines on the game board and creates
#the turtle world.
  pic = pic
  board = makeWorld(600,600)
  turtle = makeTurtle(board)

  #add background to board
  penUp(turtle)
  moveTo(turtle,0,0)
  drop(turtle,pic)

  #divide up the board into 9 rooms
  moveTo(turtle,0,200)
  penDown(turtle)
  turnRight(turtle)
  forward(turtle,600)

  penUp(turtle)
  moveTo(turtle,0,400)
  penDown(turtle)
  forward(turtle,600)

  penUp(turtle)
  moveTo(turtle,200,0)
  penDown(turtle)
  turnRight(turtle)
  forward(turtle,600)

  penUp(turtle)
  moveTo(turtle,400,0)
  penDown(turtle)
  forward(turtle,600)

  penUp(turtle)
  moveTo(turtle,300,300)
  turnToFace(turtle,300,0)

  return turtle
#end drawLines

def moveTurtle(turtle,room):
#move the turtle to the middle of the room
  room = room

  if room == "study":
    moveTo(turtle,100,100)
  elif room == "hallway":
    moveTo(turtle,300,100)
  elif room == "lounge":
    moveTo(turtle,500,100)
  elif room == "library":
    moveTo(turtle,100,300)
  elif room == "billiard":
    moveTo(turtle,300,300)
  elif room == "dining":
    moveTo(turtle,500,300)
  elif room == "conservatory":
    moveTo(turtle,100,500)
  elif room == "ballroom":
    moveTo(turtle,300,500)
  elif room == "kitchen":
    moveTo(turtle,500,500)
#moveTurtle

def gameBoard():
  new_pic = collage()
  new_pic = drawText(new_pic)
  turtle = drawLines(new_pic)
  #moveTurtle(turtle,room)

#end setup section


def help():
  showInformation("At each point in the game you will be told which directions\n\
  you can go.  You MAY be able to go:\
  (R)ight,(L)eft,(U)p,(D)own,(E)xit, or ask for (H)elp.")
  showInformation("In each room you can (I)nspect to look for clues.\n\
  Use the (C) key to review the (C)haracters.")
  showInformation("At any point you may (G)uess if you think you know the answer.")

def characters():
  print """
  The General:
      - often wears green
      - likes cats
      - has brown hair

  The Actress:
      - often wears black
      - likes cats
      - has blonde hair

  The Politician:
      - often wears black
      - likes dogs
      - has brown hair

  The Scientist:
      - often wears green
      - likes dogs
      - has blonde hair"""

def intro():
  sound=makeSound("scream.wav")
  play(sound)
  print """A classic game of 'Who Done It?' starts now!
  There has been a murder and only you can crack the case.
  You have 4 suspects, and know the following about them:\n"""

  # print characters
  characters()

  print """
  Search the rooms, find the clues, and discover the
  perpetrator before your turns run out!"""
##################################################
#END --- SETUP SECTION OF THE GAME
##################################################



def choice(valid):
#Evaluate the players entry for validity
  choice = requestString("What choice do you make?: ")
  choice = choice.lower()
  choice = choice[0]

  #Evaluate that the choice is a valid choice
  while True:
    if choice in valid and choice!='x' and choice!='y':
      return valid[choice]                                      #returns a room name
    elif choice == 'e':
      return choice
    elif choice == 'h':
      help()
      choice = requestString("SEE THE HELP MESSAGE: \n What choice do you make?: ")
    elif choice == 'c':
      characters()
      choice = requestString("Characters are: \n What choice do you make?: ")
    elif choice == 'g':
      return choice
    elif choice == 'i':
      return choice
    else:
      choice = requestString("What choice do you make?: ")
#end choice

#######################################################################
#############              ROOMS                  #####################
#######################################################################
def study():
  print """
  You move into a study and see an open journal.  The entry
  is from yesterday but the content is mundane - it does not
  help your case.\n"""
#end study

def hallway():
  print """
  The hallway between the study and the lounge is having some
  work done.  There are lots of stray pieces of debris from
  fabric and paint.  You'll have to look very close if you are
  to find any clues here.\n"""
#end hallway

def lounge():
  print """
  You find a scotch glass, partially finished, sitting on the
  side table.  Apart from that, the room seems to be in order.\n"""
#end lounge

def library():
  print """
  Books opened, as if in the middle of research, greet you in
  the library.  Could it be something turned up in the books
  caused the victims untimely death?\n"""
#end library

def billiard():
  print """
  The table is set for a game of 8-ball.  You pause, thinking
  about time spent in halls, with tables like this in your youth,
  wondering if you chose the wrong career...\n"""
#end billiard

def dining():
  print """
  While the dishes are not set for a party, the punchbowl out
  suggests one may have been planned, or recently had.  Could a
  guest from said party be the killer?  You note to look for any
  invites sent recently.\n"""
#end dining

def conservatory():
  print """
  A french press and setting for coffee and breakfast greet you.
  It seems the victim liked to start the day here, and you can
  understand with the nice view to the east.\n"""
#end conservatory

def ballroom():
  print """
  Floors that Rudy Valentino would be happy to grace show your
  reflection when you come in.  If anything happened here, it would
  have to have been by hand, there aren't any objects to do bodily
  harm that aren't secured to the walls or floors.\n"""
#end ballroom

def kitchen():
  print """
  Professional, large appliances and a myriad of cooking utensils
  line the walls.  You wonder how often this gets used to the its
  full capability.  A far cry from your fridge and microwave at home.\n"""
#end kitchen

#######################################################################
#############              END ROOMS              #####################
#######################################################################
#
#######################################################################
#############             CHARACTERS              #####################
#######################################################################
def pickCharacter():
  num = random.randint(0,3)
  chars = ["general", "actress", "politician", "scientist"]
  return chars[num]

def setCharacter(name):
  if name=="general":
    return {"call":"general","color":"green","like":"cats","hair":"brown"}
  elif name=="actress":
    return {"call":"actress","color":"black","like":"cats","hair":"blonde"}
  elif name=="politician":
    return {"call":"politician","color":"black","like":"dogs","hair":"brown"}
  elif name=="scientist":
    return {"call":"scientist","color":"green","like":"dogs","hair":"blonde"}
#######################################################################
#############           END CHARACTERSS           #####################
#######################################################################

#######################################################################
#############              CLUES                  #####################
#######################################################################
def setClues():
    rooms = ["study", "hallway", "lounge", "library", "billiard", "dining", "conservatory", "ballroom", "kitchen"]
    clueRooms = []
    count = 0
    while count != 3:
        pick = rooms[random.randint(0,8)]
        if pick not in clueRooms:
            clueRooms.append(pick)
            count +=1
    return clueRooms

def checkRoom(room, cluerooms, color, likes, hair):
    if room == cluerooms[0]:
        print "You come across some " + color + " cloth fibers that don't look like the victim's clothes."
    elif room == cluerooms[1]:
        print "Some " + likes + " hair is stuck to your pants, and the victim doesn't have pets."
    elif room == cluerooms[2]:
        print "The victim was a redhead and you stoop to pickup some " + hair + " hair."

#######################################################################
#############              END CLUES              #####################
#######################################################################
#
def setRoom(name):
  #This function maps values to room information. Room name is mapped to room. x and y are mapped to coordinates.
  #(u)p (d)own (l)eft (r)ight are mapped to other rooms
  if name=="study":
    return {"room":study(),"call":"study",'r':"hallway", 'd':"library"}
  elif name=="hallway":
    return {"room":hallway(),"call":"hallway",'l':"study",'r':"lounge",'d':"billiard"}
  elif name == "lounge":
    return {"room":lounge(),"call":"lounge",'d':"dining",'l':"hallway"}
  elif name == "library":
    return {"room":library(),"call":"library",'u':"study",'d':"conservatory", 'r':"billiard"}
  elif name == "billiard":
    return {"room":billiard(),"call":"billiard",'d':"ballroom",'u':"hallway",'l':"library",'r':"dining"}
  elif name == "dining":
    return {"room":dining(),"call":"dining",'d':"kitchen",'u':"lounge",'l':"billiard"}
  elif name == "conservatory":
    return {"room":conservatory(),"call":"conservatory",'u':"library",'r':"ballroom"}
  elif name == "ballroom":
    return {"room":ballroom(),"call":"ballroom",'r':"kitchen",'u':"billiard",'l':"conservatory"}
  elif name == "kitchen":
    return {"room":kitchen(),"call":"kitchen",'u':"dining",'l':"ballroom"}


def guess(villian):
# guesses the killer for win/lose
    guess = requestString("Who do you think the murderer is?")
    guess = guess.lower()

    if guess == villian:
        showInformation("Great job, you won!")
    else:
        showInformation("You guessed " + guess + ".  The killer was the " + villian + "!")
        showInformation("You lose.  The killer got away!")

def main():
#THE FUNCTION TO INITIATE THE GAME
  turnCount = 30                               #number of turns for game
  villian = setCharacter(pickCharacter())
  color = villian['color']
  likes = villian['like']
  hair = villian['hair']
  cluerooms = setClues()
  print cluerooms
  new_pic = collage()
  new_pic = drawText(new_pic)
  turtle = drawLines(new_pic)
  #gameBoard()                            #display the welcome, opening story, and help
  help()
  intro()
  room = setRoom("billiard")                       #set the starting location
  result=''
  while (result != 'e') and turnCount != 0:
    turnCount -= 1
    room['room']                                #call room function
    result=choice(room)                         #stores a room name
    if result == 'g':
        break
    elif result != 'i':
        room=setRoom(result)                    #set room to room in the direction that player chooses
        moveTurtle(turtle,room['call'])
    elif result == 'i':
        checkRoom(room["call"], cluerooms, color, likes, hair)
        #result=choice(room)
  guess(villian["call"])
