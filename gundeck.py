def gunDeck(turtle):
  #remove the options that are NOT valid for your room
  valid = ['u','d']
  
  #Add the story about your room
  print "You decended a ladder to the Gun Deck."
  print "Passengers aren't allowed here.\n"
  
  print "(U)P: Go back to the deck."
  print "(D)OWN: Go down a ladder to the tween deck.\n"
  
  #see what they decided to do
  result = choice(valid)
  
  #based on the choice return where does the player move to?
  #CALL LOCATION FROM SETUP
  elif result == 'u':
    name = "deck"
    location(turtle,name)
    return name
  elif result == 'd':
    name = "tweenDeck"
    location(turtle,name)
    return name
#end gunDeck                                                                    