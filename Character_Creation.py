```

import random
import time

def roll() :
  return random.randint(1,6)+random.randint(1,6) + random.randint(1,6)


def get_and_validate_stat(stat):
  valid_stat = False

  while valid_stat == False:
    stat_value =int(input(f"  Enter your {stat} stat: "))
    if stat_value < 3:
      print("  That is too low. Please enter a number between 3 and 18.")
    elif stat_value > 18:
      print("  That is too high. Please enter a number between 3 and 18.")
    else:
      valid_stat = True
   
  return stat_value

#Input promp is "Do you want to {text}? 1 for yes 2 for no: ""
def y_n_prompt(text):
 valid_input = False
 
 while valid_input == False:
   prompt = int(input(f"Do you want to {text}? 1 for yes 2 for no: "))
  
   if prompt == 1 :
     y_n_answer = True
     valid_input = True
     return y_n_answer
  
   elif prompt ==  2 :
     y_n_answer = False
     valid_input = True
     return y_n_answer
   else:
     print("Please enter 1 for yes 2 for no: ")

stats_prompt = y_n_prompt("roll for your stats")

#Some type of validation to confirm they put yet or no is needed here to prevent an error. - SA 1/21/22

#Auto Rolled
if stats_prompt == True: 
  print("Ok let's see what you get...")
  time.sleep(2)
  agility = roll()
  print(f"  Your agility is {agility}.")
 
  time.sleep(1)
  charisma = roll()
  print(f"  Your charisma is {charisma}.")
  
  time.sleep(1)
  intellect = roll()
  print(f"  Your intellect is {intellect}.")
  
  time.sleep(1)
  perception = roll()
  print(f"  Your perception is {perception}.")
  
  time.sleep(1)
  strength = roll()
  print(f"  Your strength is {strength}.")

#Manually Entered
elif stats_prompt == False:
  print("Ok let's get started. All stats must be from 3 to 18.")
  
  time.sleep(.5)
  #agility =int(input("Enter your Agility stat: "))
  
  agility = get_and_validate_stat("agility")


  time.sleep(.5)
  #charisma =int(input("Enter your Charisma stat: "))
  
  charisma = get_and_validate_stat("charisma")


  time.sleep(.51)
  #intellect =int(input("Enter your Intellect stat: "))

  intellect = get_and_validate_stat("intellect")
 
  time.sleep(.5)
  #perception =int(input("Enter your Perception stat: "))

  perception = get_and_validate_stat("perception")
 
  time.sleep(.5)
  #strength =int(input("Enter your Strength stat: "))
  strength = get_and_validate_stat("strength")
  print("Calculating values now....")

else:
  print("Please enter 1 or 2.")
  

def stat_rating_calc(stat):
  #This should be some type of formula instead of a dict I think. Didn't feel like doing the math at the time - SA 1/21/22  
  stat_rating = {
  3: -3,
  4: -3,
  5: -3,
  6: -2,
  7: -2,
  8: -1,
  9: -1,
  10: 0,
  11: 0,
  12: 0,
  13: 1,
  14: 1,
  15: 1,
  16: 2,
  17: 2,
  18: 3
  }

  return stat_rating[stat]

time.sleep(2) 

#Kin selection Roll 1d12: 1-9 human, 10 halfling, 11 dwarf, 12 elf.

kin_prompt = y_n_prompt("roll for you kin")

if kin_prompt == True:
  print("Great let's see what you are...")
  time.sleep(1)
  kin_roll = random.randint(1,12)
  if kin_roll <=9:
    kin = "human"
    print(f"  You are a {kin}.")
  elif kin_roll == 10:
    kin = "halfling"
    print(f"  You are a {kin}.")
  elif kin_roll == 11:
    kin = "dwarf"
    print(f"  You are a {kin}.")
  elif kin_roll == 12:
    kin = "elf"
    print(f"  You are a {kin}.")    
if kin_prompt == False:
  kin = input("Are you a huamn, dwarf, or elf")

time.sleep(2)

#Determine Background

#Describe your character - Let's make this a madlib that sounds fun

#Determine HP and Max Heavy

#Determin starting gold


print(f"""
Your stats are the following:
  Agility:    {agility} | {stat_rating_calc(agility)}
  Charisma:   {charisma} | {stat_rating_calc(charisma)}
  Intellect:  {intellect} | {stat_rating_calc(intellect)}
  Perception: {perception} | {stat_rating_calc(perception)}
  Strength:   {strength} | {stat_rating_calc(strength)}

 You hail from the {kin} lands.

""")


print(f"Good Hunting {kin}!")

```