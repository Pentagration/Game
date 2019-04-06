##################################################
#SETUP SECTION OF THE GAME  
##################################################
def setup():
#this function draws our boat and places
#the turtle at the start position
  boat = makeWorld(500,500)
  turtle = makeTurtle(boat)
  drawBoat(turtle,boat)
  turnRight(turtle)
  location(turtle,"quay")
  help()
  intro()
  return turtle
#end setup

def square(turtle,x,y):
#Function to draw a square, called by drawBoat
  penUp(turtle)
  moveTo(turtle,x,y)
  penDown(turtle)
    
  for x in range(0,4):
    forward(turtle,50)
    turnLeft(turtle)
#end square

def drawBoat(turtle,boat):
#Function to draw the representation of our boat
  #Make sure the pen is down
  penDown(turtle)
  
  #starting square  
  square0 = square(turtle,140,275)       
  
  #50x50 squares, spaced 10 apart, 5x3 grid  
  for x in range(200,500,60):
    for y in range(215,395,60):
      square(turtle,x,y)
#end drawBoat

def location(turtle,name):
#Function to move the turtle to a location
  #move the turtle witout drawing a line
  penUp(turtle)                  
  
  #List of locations on the boat 
  #moves the turtle to the center of the square
  if name == "quay":
    moveTo(turtle,115,250)
  elif name == "deck":
    moveTo(turtle,175,250)
  elif name == "foreCastle":
    moveTo(turtle,175,190)
  elif name == "aftCastle":
    moveTo(turtle,175,310)
  elif name == "gunDeck":
    moveTo(turtle,235,250)
  elif name == "crew":
    moveTo(turtle,235,190)
  elif name == "gunPowder":
    moveTo(turtle,235,310)
  elif name == "tweenDeck":
    moveTo(turtle,295,250)
  elif name == "bunk":
    moveTo(turtle,295,190)
  elif name == "passengers":
    moveTo(turtle,295,310)
  elif name == "hold":
    moveTo(turtle,355,250)
  elif name == "food":
    moveTo(turtle,355,190)
  elif name == "livestock":
    moveTo(turtle,355,310)
  elif name == "ballast":
    moveTo(turtle,415,250)
  elif name == "rum":
    moveTo(turtle,415,190)
  elif name == "gold":
    moveTo(turtle,415,310)       
#end location

def help():  
  print "At each point in the game you will be told which directions"
  print "you can go.  You MAY be able to go:"
  print "(R)ight,(L)eft,(U)p,(D)own,(B)ack,(E)xit,or ask for (H)elp. \n"

def intro():  
  print "Let us pretend this is the year 1630, and that we have" 
  print "purchased a passage on the Talbot, one of the English galleons"
  print "sailing from Southampton Harbour this spring with John Winthrop???s" 
  print "fleet of eleven ships. We feel confident about this vessel because" 
  print "she transported another group of Puritan planters to New England" 
  print "last year in 1629. The Massachusetts Bay Company rented her for" 
  print "the expedition.\n"
##################################################
#END --- SETUP SECTION OF THE GAME  
##################################################



def choice(valid): 
#Evaluate the players entry for validity
  #Add the exit and help choices to the list
  valid.append('e')
  valid.append('h')
  
  #Prompt and take the first letter of the input   
  choice = requestString("What choice do you make?: ")
  choice = choice[0]
  choice = choice.lower()
  
  #Evaluate that the choice is a valid choice 
  while choice != True: 
    if choice.isalpha() != True:
      choice = requestString("INVALID LETTER OR WORD: \n What choice do you make?: ")     
    elif choice == 'e':
      print "You have left the game."
      break
    elif choice == 'h':
      help()
      choice = requestString("SEE THE HELP MESSAGE: \n What choice do you make?: ")
    elif choice not in valid:
      choice = requestString("THAT WAS NOT A VALID CHOICE: \n What choice do you make?: ")
    else:
      return choice
#end choice

def quay(turtle):
  #remove the options that are NOT valid for your room
  valid = ['u']
  
  #Add the story about your room
  print "You are standing on the quay at the base on the"
  print "gangplank ready to board the talbot along with 120"
  print "passengers and 30 crew.  150 people in all.\n"
  print "Are they all as pure as their puritan credentials?\n"
  
  print "(U)P: You're only at the beginning"
  print "your only choice is to board the Talbot."
  print "(E)xit: or you can quit.\n"

  #see what they decided to do
  result = choice(valid)
  result
  
  #based on the choice return where does the player move to?
  #CALL LOCATION FROM SETUP
  if result == 'u':
    name = "deck"
    location(turtle,name)
    return name
#end quay              

def deck(turtle):
  #remove the options that are NOT valid for your room
  valid = ['d','r','l']
  
  #Add the story about your room
  print "You are on the main deck of the Talbot."
  print "Welcome aboard!!!\n"
  
  print "(R)IGHT: Aft castle"
  print "(L)EFT: Forecastle"
  print "(D)OWN: Gun Deck"
  
  #see what they decided to do
  result = choice(valid)
  
  #based on the choice return where does the player move to?
  #CALL LOCATION FROM SETUP
  if result == 'r':
    name = "aftCastle"
    location(turtle,name)
    return name
  elif result == 'l':
    name = "foreCastle"
    location(turtle,name)
    return name
  elif result == 'd':
    name = "gunDeck"
    location(turtle,name)
    return name
#end room 
   
def playGame():
#Our game about the Galleon Talbot
  #Show the welcome messages and put the turtle
  #at the start position on the quay
  turtle = setup()    
  name = quay(turtle)
  
  #Depending on the user's choice display the 
  #message for the next room/location
  if name == "quay":
    name = quay(turtle)
  elif name == "deck":
    name = deck(turtle)
  elif name == "foreCastle":
    name = foreCastle(turtle)
  elif name == "aftCastle":
    name = aftCastle(turtle)
  elif name == "gunDeck":
    name = gunDeck(turtle)
  elif name == "crew":
    name = crew(turtle)
  elif name == "gunPowder":
    name = gunPowder(turtle)
  elif name == "tweenDeck":
    name = tweenDeck(turtle)
  elif name == "bunk":
    name = bunk(turtle)
  elif name == "passengers":
    name = passengers(turtle)
  elif name == "hold":
    name = hold(turtle)
  elif name == "food":
    name = food(turtle)
  elif name == "livestock":
    name = livestock(turtle)
  elif name == "ballast":
    name = ballast(turtle)
  elif name == "rum":
    name = rum(turtle)
  elif name == "gold":
    name = gold(turtle) 
  