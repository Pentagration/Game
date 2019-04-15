def collage():  
#makes a 3 x 3 collage for the game board
  setMediaPath()
  study = makePicture("1_study.jpg")
  hallway = makePicture("2_hallway.jpg")
  lounge = makePicture("3_lounge.jpg")
  library = makePicture("4_library.jpg")
  billard = makePicture("5_billard.jpg")
  dining = makePicture("6_dining.jpg")
  conservatory = makePicture("7_conservatory.jpg")
  ballroom = makePicture("8_ballroom.jpg")
  kitchen = makePicture("9_kitchen.jpg")
  
  sourceFiles = [study,hallway,lounge,library,billard,dining,conservatory,ballroom,kitchen]
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
  "Billard Room", 
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
  elif room == "billard":
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
  
  