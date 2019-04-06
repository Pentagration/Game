def aftCastle(turtle):
  #remove the options that are NOT valid for your room
  valid = ['r','l','b']
  
  #Add the story about your room
  print "You are in the Aft Castle where the"
  print "Captain and important passsengers stay."
  print "You are not important.\n"
  
  print "(R)IGHT: First Mate"
  print "(L)EFT: A wall"
  print "(B)ACK: The Deck\n"
  
  #see what they decided to do
  result = choice(valid)
  
  #based on the choice return where does the player move to?
  #CALL LOCATION FROM SETUP
  if result == 'r':
    print "FIRST MATE: Says get below decks."
    print "He pushes you back out the door. \n"
    name = "deck"
    location(turtle,name)
    return name
  elif result == 'l':
    print "You're looking at a wall.  You decide to go back"
    print "to the deck."
    name = "deck"
    location(turtle,name)
    return name
  elif result == 'b':
    name = "deck"
    location(turtle,name)
    return name
#end room                                                                     