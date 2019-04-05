def choice(valid): 
#Evaluate the players entry for validity
  #Add the exit and help choices to the list
  valid = ['u','d','r','l']
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
########THIS NEEDS TO CALL HELP FROM SETUP, THIS IS TEST CODE
      print "help"
      break
    elif choice not in valid:
      choice = requestString("THAT WAS NOT A VALID CHOICE: \n What choice do you make?: ")
    else:
      return choice
#end choice