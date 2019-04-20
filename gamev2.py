#STUDENTS: Sergio Quiroz, Jason Pettit
#Team 5 - Pentagration
#CST205-40_SP19 Lab 13 Part 2

##################################################
#win/lose conditions
##################################################
#win condition involves picking up the items in the
#pickup rooms (crew, gold, rum) and stashing them
#in the secret room before turns run out
#
#lose condition is if the above is not met


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
  #room=setRoom("quay")
  penUp(turtle)
  moveTo(turtle,115,250)
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
  print "(R)ight,(L)eft,(U)p,(D)own,(E)xit, or ask for (H)elp. "
  print "Some rooms may have an object you can (P)ICK UP.\n"

def intro():
  showInformation(
  "Let us pretend this is the year 1630, and that we have"
  "purchased a passage on the Talbot, one of the English galleons"
  "sailing from Southampton Harbour this spring with John Winthrop's"
  "fleet of eleven ships. We feel confident about this vessel because"
  "she transported another group of Puritan planters to New England"
  "last year in 1629. The Massachusetts Bay Company rented her for"
  "the expedition.\n"

  "You've paid half your fare upfront, the other half due on arrival."
  "The problem is, you don't have it.  You need to find something to"
  "give to the crew they may want, and something with which to defend"
  "yourself in case things go awry.  All must be done befor you land"
  "(your turns run out).\n")
##################################################
#END --- SETUP SECTION OF THE GAME
##################################################



def choice(valid):
#Evaluate the players entry for validity
  choice = requestString("What choice do you make?: ")
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
    else:
      choice = requestString("What choice do you make?: ")
#end choice

def drawSecret(turtle):
  # draws the secret room when it is entered
  # not part of setup because we don't want it by default
  penUp(turtle)
  square(turtle,330,155)
  penUp(turtle)
#end drawSecret

#######################################################################
#############              ROOMS                  #####################
#######################################################################
def quay():
  print "You are standing on the quay at the base on the"
  print "gangplank ready to board the Talbot along with 120"
  print "passengers and 30 crew.  150 people in all.\n"
  print "Are they all as pure as their puritan credentials?\n"

  print "(U)P: You're only at the beginning"
  print "your only choice is to board the Talbot."
  print "(E)xit: or you can quit.\n"
#end quay

def deck():
  print """You are on the main deck of the Talbot."
   Welcome aboard!!!\n
   (R)IGHT: Aft castle
   (L)EFT: Forecastle
   (D)OWN: Gun Deck"""

#adam or colin can you let me know if you can see this
#testing if i am doing the pull and push right -  sergio
# btw triple quotes work here but not on my JES IDE try it out


  print "You are on the main deck of the Talbot."
  print "Welcome aboard!!!\n"

  print "(R)IGHT: Aft castle"
  print "(L)EFT: Forecastle"
  print "(D)OWN: Gun Deck\n"
#end deck

def aftCastle():
  print "You are in the Aft Castle where the"
  print "Captain and important passsengers stay."
  print "You are not important.\n"

  print "(D)OWN: The gunPowder"
  print "(L)EFT: The Deck\n"
#end aftCastle

def foreCastle():
  print "You are in the Forecastle where the Baker, Tanner,"
  print "and Sail Maker work.\n"

  print "(D)OWN: The Crew"
  print "(R)IGHT: The Deck\n"
#end foreCastle

def gunDeck():
  print "You are on the Gun deck, where the Talbot's cannons are secured"
  print "and the crew is housed.\n"

  print "(D)OWN: The Tween Deck"
  print "(U)P: Deck"
  print "(L)eft: The Crew"
  print "(R)ight: The Gun Powder\n"
#end gunDeck

def crew():
  print "You are in the crew area.  What are you doing here? Passengers aren't"
  print "supposed to be on the Gun Deck.  If you hang around too long one of"
  print "crew may come along, pick up a cutlass from the rack, and drive you off!\n"

  print "(D)OWN: Your bunk"
  print "(U)P: Fore Castle"
  print "(R)IGHT: Gun Deck\n"
#end crew

def crewPickup(items):
  print "You picked up a cutlass! It's an intimidating weapon indeed."
  print "(D)OWN: Your bunk"
  print "(U)P: Fore Castle"
  print "(R)IGHT: Gun Deck\n"

  items.append("cutlass")
#end crewPickup

def gunPowder():
  print "DANGER. You are in the gun powder area, it's very unstable."
  print "Even the slightest spark could blow up the Talbot.\n"

  print "(D)OWN: Passengers"
  print "(U)P: Aft Castle"
  print "(L)EFT: Gun Deck\n"
#end gunPowder

def tweenDeck():
  print "The Tween Deck is the passenger area. This is where you"
  print "and your fellow passengers will bunk and store your chests.\n"

  print "(D)OWN: Hold"
  print "(U)P: Gun Deck"
  print "(L)EFT: Bunk"
  print "(R)IGHT: Passengers\n"
#end tweenDeck

def bunk():
  print "The Bunk area is where you'll find your designated space."
  print "Passengers are allocated area marked off in chalk."
  print "You see outlines and numbers and look to find yours."
  print "This is where you can tie down your chest, making sure it"
  print "will not go flying in a storm.  No one wants to be hit with that.\n"

  print "(D)OWN: Food"
  print "(U)P: Crew"
  print "(R)IGHT: Tween Deck\n"
#end bunk

def passengers():
  print "In the Passengers area you see candles and hammocks"
  print "lining the walls and hanging from the ceiling.  They"
  print "are stacked 2, 3, or 4 high in some places.  You wonder"
  print "if you'll get much sleep with close quarters and the smell.\n"

  print "(D)OWN: Livestock"
  print "(U)P: Gun Powder"
  print "(L)EFT: Tween Deck\n"
#end passengers

def hold():
  print "The Hold is the level where food and livestock are kept."
  print "You'll also find extra sails and lines as well as plenty of wood."
  print "One of the most important parts in the Hold is the firebox."
  print "This is where the cook builds the fires to cook food in the galley.\n"

  print "(D)OWN: Ballast"
  print "(U)P: Tween Deck"
  print "(L)EFT: Rum"
  print "(R)RIGHT Gold\n"
#end hold

def food():
  print "The Food room is one that has all the water, wine, biscuts,"
  print "salted meat, etc that the crew and passegers will need for the trip."
  print "You see barrels and kegs stacked and labelled neatly."
  print "This area does appear to be a bit smaller that you'd expect."
  print "All the stacked crates, barrels, and kegs would make a great cover"
  print "for a hiding place...\n"

  print "(D)OWN: Rum"
  print "(U)P: Bunk"
  print "(R)IGHT: Hold\n"
#end food

def livestock():
  print "Livestock are important because they provide food for the trip and"
  print "transportation upon arriving.  You see stalls and cages for: cows,"
  print "chickens, horses, goats, pigs, and rabbits.  Next to the stalls you"
  print "see food, hay and water for the animals.\n"

  print "(D)OWN: Gold"
  print "(U)P: Passengers"
  print "(L)EFT: Hold\n"
#end livestock

def ballast():
  print "The Ballast is the lowest level of the Talbot.  Here you find"
  print "the very important crew motivators - rum and treasure!\n"

  print "(U)P: Hold"
  print "(L)EFT: Rum"
  print "(R)IGHT: Gold\n"
#end ballast

def rum():
  print "A famous pirate once said, 'Where has all the rum gone?'  You"
  print "can see the rum for this voyage is here.  It is partially held"
  print "in larger casks, and partially in smaller, personal portion"
  print "sizes that an industrius person might be able to make off with...\n"

  print "(U)P: Food"
  print "(R)IGHT: Ballast\n"
#end rum

def rumPickup(items):
  print "You picked up a cup of Rum! No man of the sea has ever turned down some rum."

  items.append("rumcup")
#end rumPickup

def gold():
  print "Gold.  Gold!  GOLD!!  This may or may not be the prime mission"
  print "of the Talbot, but the crew certainly doesn't mind a chance to"
  print "get some and turn it into buillon and coins.  Amazingly, there"
  print "are a few coins out and not in a locked chest.  This could"
  print "definitely help someone starting a new life in a new world.\n"

  print "(U)P: Livestock"
  print "(L)EFT: Ballast\n"
#end gold

def goldPickup(items):
  print "You picked up a gold coin. One item that everyone enjoys..."
  print "(U)P: Livestock"
  print "(L)EFT: Ballast\n"

  items.append("goldCoin")
#end goldPickup

def secret():
  print "You have found a secret hold behind some food storage!"
  print "This could be a great place to hide if needed, or to stow"
  print "anything you're not supposed to have."

  print "(R)IGHT: Food"
  print "(S)TASH: Hide your stolen goods.\n"
#end secret

def secretStash(items, stash):
  print "Your stolen goods are now stashed away from prying eyes."
  for x in items:
    stash.append(x)
  print "(R)IGHT: Food\n"
#end secretStash

#######################################################################
#############              END ROOMS              #####################
#######################################################################
#
def setRoom(name,items=None,stash=None):
  #This function maps values to room information. Room name is mapped to room. x and y are mapped to coordinates.
  #(u)p (d)own (l)eft (r)ight are mapped to other rooms
  if name=="quay":
    return {"room":quay(),'x':115,'y':250,'u':"deck"}
  elif name=="deck":
    return {"room":deck(),'x':175,'y':250,'d':"gunDeck",'r':"aftCastle",'l':"foreCastle"}
  elif name == "foreCastle":
    return {"room":foreCastle(),'x':175,'y':190,'d':"crew",'r':"deck"}
  elif name == "aftCastle":
    return {"room":aftCastle(),'x':175,'y':310,'d':"gunPowder",'l':"deck"}
  elif name == "gunDeck":
    return {"room":gunDeck(),'x':235,'y':250,'d':"tweenDeck",'u':"deck",'l':"crew",'r':"gunPowder"}
  elif name == "crew":
    return {"room":crew(),'x':235,'y':190,'d':"bunk",'u':"foreCastle",'r':"gunDeck",'p':"crewPickup"}
  elif name == "crewPickup":
    return {"room":crewPickup(items),'x':235,'y':190,'d':"bunk",'u':"foreCastle",'r':"gunDeck"}
  elif name == "gunPowder":
    return {"room":gunPowder(),'x':235,'y':310,'d':"passengers",'u':"aftCastle",'l':"gunDeck"}
  elif name == "tweenDeck":
    return {"room":tweenDeck(),'x':295,'y':250,'d':"hold",'u':"gunDeck",'l':"bunk",'r':"passengers"}
  elif name == "bunk":
    return {"room":bunk(),'x':295,'y':190,'d':"food",'u':"crew",'r':"tweenDeck"}
  elif name == "passengers":
    return {"room":passengers(),'x':295,'y':310,'d':"livestock",'u':"gunPowder",'l':"tweenDeck"}
  elif name == "hold":
    return {"room":hold(),'x':355,'y':250,'d':"ballast",'u':"tweenDeck",'l':"food",'r':"livestock"}
  elif name == "food":
    return {"room":food(),'x':355,'y':190,'d':"rum",'u':"bunk",'r':"hold", 'l':"secret"}
  elif name == "livestock":
    return {"room":livestock(),'x':355,'y':310,'d':"gold",'u':"passengers",'l':"hold"}
  elif name == "ballast":
    return {"room":ballast(),'x':415,'y':250,'u':"hold",'l':"rum",'r':"gold"}
  elif name == "rum":
    return {"room":rum(),'x':415,'y':190,'r':"ballast",'u':"food", 'p':"rumPickup"}
  elif name == "rumPickup":
    return {"room":rumPickup(items),'x':415,'y':190,'r':"ballast",'u':"food"}
  elif name == "gold":
    return {"room":gold(),'x':415,'y':310,'l':"ballast",'u':"livestock", 'p':"goldPickup"}
  elif name == "goldPickup":
    return {"room":goldPickup(items),'x':415,'y':310,'l':"ballast",'u':"livestock"}
  elif name == "secret":
    return {"room":secret(),'x':355,'y':130,'r':"food", 's':"secretStash"}
  elif name == "secretStash":
    return {"room":secretStash(items, stash),'x':295,'y':130,'r':"food"}

def checkGame(turnCount,stash,name):
# checks win/lose scenario based on turns and items picked up
    if "goldCoin" in stash and "rumcup" in stash and "cutlass" in stash and turnCount > 0:
      print "You win " + name
      return 2                                 #2 is win scenario
    if turnCount>0:
      return 1                                 #1 is continue scenaio
    else:
      print "You lose " + name
      return 3                                 # 3 is lose

def playGame():
#THE FUNCTION TO INITIATE THE GAME
  items=[]                                     #list of items picked up
  stash=[]                                     #list of items stashed
  pickupRooms=("crewPickup","rumPickup","goldPickup")
  turnCount = 30                               #number of turns for game
  turtle = setup()                             #display the welcome, opening story, and help
  room = setRoom("quay")                       #set the starting location
  result=''
  name = requestString("Please enter your name: ")
  while (result != 'e') and checkGame(turnCount,stash,name)==1:
    turnCount -= 1
    room['room']                                #call room function
    result=choice(room)                         #stores a room name
    if result != 'e':
      drawSecret(turtle) if result=="secret" else None  #draws secret room on entering
      if result in pickupRooms:
        room=setRoom(result,items)              #passes 2 args if in a room that has item to pickup
      elif result=="secretStash":
        setRoom(result,items,stash)             #passes 3 args to secret room
      else:
        room=setRoom(result)                    #set room to room in the direction that player chooses
      moveTo(turtle,room['x'],room['y'])
