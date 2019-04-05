def room():
  #remove the options that are NOT valid for your room
  valid = ['u','d','r','l']
  
  #Add the story about your room
  print "Your room's story"
  
  #see what they decided to do
  result = choice(valid)
  print result

###########################
#CHOICE NEEDS WORK                          
def choice(valid):   
  choice = requestString("What choice do you make?: ")
  choice = choice[0]
  choice = choice.lower()
  
  #Add the exit and help choices to the list
  valid.append('e')
  valid.append('h')
  
  print valid
    
  while choice.isalpha() != True:
    choice = requestString("THAT WAS NOT A LETTER: \n What choice do you make?: ")
    choice = choice[0]
    choice = choice.lower() 
     
  if choice == 'e':
    print "You have left the game."
    return 0
    
  elif choice == 'h':
  #This calls to the help function in setup.py
  #  help()
  
  elif choice not in valid:
    choice = requestString("THAT WAS NOT A VALID CHOICE: \n What choice do you make?: ")
  
  else:
    return choice
