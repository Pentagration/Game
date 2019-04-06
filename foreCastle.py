def foreCastle():
  #remove the options that are NOT valid for your room
  valid = ['r','l','b']
  
  #Add the story about your room
  print "You are in the Forecastle where the Baker, Tanner,"
  print "and Sail Maker work."
  
  print "(R)IGHT: The Baker"
  print "(L)EFT: The Tanner "
  print "(B)ACK: The Deck"
  
  #see what they decided to do
  result = choice(valid)
  
  #based on the choice return where does the player move to?
  #CALL LOCATION FROM SETUP
  if result == 'r':
    print "This is our area. Go back to the deck."
    return name
  elif result == 'l':
    print "This is our area. Go back to the deck."
    return name
  elif result == 'b':
    name = "deck"
    location(turtle,name)
    return name
#end room                                                                     