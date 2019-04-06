def foreCastle(turtle):
  #remove the options that are NOT valid for your room
  valid = ['r','l','b']
  
  #Add the story about your room
  print "You are in the Forecastle where the Baker, Tanner,"
  print "and Sail Maker work.\n"
  
  print "(R)IGHT: The Baker"
  print "(L)EFT: The Tanner "
  print "(B)ACK: The Deck\n"
  
  #see what they decided to do
  result = choice(valid)
  
  #based on the choice return where does the player move to?
  #CALL LOCATION FROM SETUP
  if result == 'r':
    print "BAKER SAYS: This is our area. Go back to the deck."
    print "He pushes you back out the door. \n"
    name = "deck"
    location(turtle,name)
    return name
  elif result == 'l':
    print "TANNER SAYS: This is our area. Go back to the deck."
    print "He pushes you back out the door. \n"
    name = "deck"
    location(turtle,name)
    return name
  elif result == 'b':
    name = "deck"
    location(turtle,name)
    return name
#end foreCastle   