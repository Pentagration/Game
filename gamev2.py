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
  room=setRoom("quay")
  penUp(turtle)
  moveTo(turtle,room['x'],room['y'])
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


def help():
  print "At each point in the game you will be told which directions"
  print "you can go.  You MAY be able to go:"
  print "(R)ight,(L)eft,(U)p,(D)own,(E)xit, or ask for (H)elp. \n"

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
  choice = requestString("What choice do you make?: ")

  #Evaluate that the choice is a valid choice
  while True:
    if choice in valid and choice!='x' and choice!='y':
      return valid[choice]                                      #returns a room name
    elif choice == 'e':
      return choice
    elif choice == 'h':
      help()
      choice = requestString("SEE THE HELP MESSAGE: \n What choice do you make?: ")
    else:
      choice = requestString("What choice do you make?: ")
#end choice
#######################################################################
#############              ROOMS                  #####################
#######################################################################
def quay():
  print "You are standing on the quay at the base on the"
  print "gangplank ready to board the talbot along with 120"
  print "passengers and 30 crew.  150 people in all.\n"
  print "Are they all as pure as their puritan credentials?\n"

  print "(U)P: You're only at the beginning"
  print "your only choice is to board the Talbot."
  print "(E)xit: or you can quit.\n"
#end quay

def deck():
  print "You are on the main deck of the Talbot."
  print "Welcome aboard!!!\n"

  print "(R)IGHT: Aft castle"
  print "(L)EFT: Forecastle"
  print "(D)OWN: Gun Deck"
#end deck

def aftCastle():
  print "You are in the Aft Castle where the"
  print "Captain and important passsengers stay."
  print "You are not important.\n"
  
  print "(D)OWN: The gunPowder"
  print "(L)EFT: The Deck"
#end aftCastle

def foreCastle():
  print "You are in the Forecastle where the Baker, Tanner,"
  print "and Sail Maker work.\n"
  
  print "(D)OWN: The Crew"
  print "(R)IGHT: The Deck\n"
#end foreCastle

def gunDeck():
  print "You are on the Gun deck, where the Talbot's cannons are secured.\n"
  
  print "(D)OWN: The Tween Deck"
  print "(U)P: Deck"
  print "(L)eft: The Crew"
  print "(R)ight: The Gun Powder\n"
#end gunDeck
  
def crew():
  print "You are in the crew area.  What are you doing here? Passengers aren't"
  print "supposed to be on the Gun Deck.\n"
  
  print "(D)OWN: Your bunk"
  print "(U)P: Fore Castle"
  print "(R)IGHT: Gun Deck\n"
#end crew

def gunPowder():
  print "DANGER. You are in the gun powder area, it's very unstable."
  print "Even the slightest spark could blow up the Talbot.\n"
  
  print "(D)OWN: Passengers"
  print "(U)P: Aft Castle"
  print "(L)EFT: Gun Deck\n"
#end gunPowder

def tweenDeck():
  print "The Tween Deck is the passenger area. This is where your"
  print "fellow passengers and you bunk are.\n"
  
  print "(D)OWN: Hold"
  print "(U)P: Gun Deck"
  print "(L)EFT: Bunk"
  print "(R)IGHT: Passengers\n"
#end tweenDeck

def bunk():
  print "Bunk\n"
  
  print "(D)OWN: Food"
  print "(U)P: Crew"
  print "(R)IGHT: Tween Deck\n"
#end bunk
    
def passengers():
  print "Passengers\n"
  
  print "(D)OWN: Livestock"
  print "(U)P: Gun Powder"
  print "(L)EFT: Tween Deck\n"
#end passengers

def hold():
  print "Hold\n"
  
  print "(D)OWN: Ballast"
  print "(U)P: Tween Deck"
  print "(L)EFT: Rum"
  print "(R)RIGHT Gold\n"
#end hold

def food():
  print "Food\n"
  
  print "(D)OWN: Rum"
  print "(U)P: Bunk"
  print "(R)IGHT: Hold\n"
#end food

def livestock():
  print "Livestock\n"
  
  print "(D)OWN: Gold"
  print "(U)P: Passengers"
  print "(L)EFT: Hold\n"
#end livestock

def ballast():
  print "Ballast\n"
  
  print "(U)P: Hold"
  print "(L)EFT: Rum"
  print "(R)IGHT: Gold\n"
#end ballast

def rum():
  print "Rum\n"
  
  print "(U)P: Food"
  print "(R)IGHT: Ballast\n"
#end rum

def gold():
  print "Gold\n"
  
  print "(U)P: Livestock"
  print "(L)EFT: Ballast\n"


#######################################################################
#############              END ROOMS              #####################
#######################################################################

def setRoom(name):
  "'This function maps values to room information. Room name is mapped to room. x and y are mapped to coordinates.'"
  "'(u)p (d)own (l)eft (r)ight are mapped to other rooms'"
  if name=="quay":
    return {"room":"quay",'x':115,'y':250,'call':quay(),'u':"deck"}
  elif name=="deck":
    return {"room":"deck",'x':175,'y':250,'call':deck(),'d':"gunDeck",'r':"aftCastle",'l':"foreCastle"}
  elif name == "foreCastle":
    return {"room":"foreCastle",'x':175,'y':190,'call':foreCastle(),'d':"crew",'r':"deck"}
  elif name == "aftCastle":
    return {"room":"aftCastle",'x':175,'y':310,'call':aftCastle(),'d':"gunPowder",'l':"deck"}
  elif name == "gunDeck":
    return {"room":"gunDeck",'x':235,'y':250,'call':gunDeck(),'d':"tweenDeck",'u':"deck",'l':"crew",'r':"gunPowder"}
  elif name == "crew":
    return {"room":"crew",'x':235,'y':190,'call':crew(),'d':"bunk",'u':"foreCastle",'r':"gunDeck"}
  elif name == "gunPowder":
    return {"room":"gunPowder",'x':235,'y':310,'call':gunPowder(),'d':"passengers",'u':"aftCastle",'l':"gunDeck"}
  elif name == "tweenDeck":
    return {"room":"tweenDeck",'x':295,'y':250,'call':tweenDeck(),'d':"hold",'u':"gunDeck",'l':"bunk",'r':"passengers"}
  elif name == "bunk":
    return {"room":"bunk",'x':295,'y':190,'call':bunk(),'d':"food",'u':"crew",'r':"tweenDeck"}
  elif name == "passengers":
    return {"room":"passengers",'x':295,'y':310,'call':passengers(),'d':"livestock",'u':"gunPowder",'l':"tweenDeck"}
  elif name == "hold":
    return {"room":"hold",'x':355,'y':250,'call':hold(),'d':"ballast",'u':"tweenDeck",'l':"food",'r':"livestock"}
  elif name == "food":
    return {"room":"food",'x':355,'y':190,'call':food(),'d':"rum",'u':"bunk",'r':"hold"}
  elif name == "livestock":
    return {"room":"livestock",'x':355,'y':310,'call':livestock(),'d':"gold",'u':"passengers",'l':"hold"}
  elif name == "ballast":
    return {"room":"ballast",'x':415,'y':250,'call':ballast(),'u':"hold",'l':"rum",'r':"gold"}
  elif name == "rum":
    return {"room":"rum",'x':415,'y':190,'call':rum(),'r':"ballast",'u':"food"}
  elif name == "gold":
    return {"room":"gold",'x':415,'y':310,'call':gold(),'l':"ballast",'u':"livestock"}


def playGame():
  turtle = setup()
  room = setRoom("quay")
  result=''
  while result != 'e':
    room['call']                                #call room function
    result=choice(room)                         #stores a room name
    if result != 'e':
      room=setRoom(result)                      #set room to room in the direction that player chooses
      moveTo(turtle,room['x'],room['y'])

