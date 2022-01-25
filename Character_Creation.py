import random
import time

#time between random rolls
Roll_Timer = .75

#time between input requests
input_timer = .75

#time between sections
Section_Timer = 2

def stat_roll() :
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

#Input promp is "Do you want to {text}? Yes or No: ""
def y_n_prompt(text):
 valid_input = False
 
 while valid_input == False:
   prompt = input(f"Do you want to {text}? Yes or No: ")
   prompt = prompt.lower()

   if prompt == "yes" or prompt == "y" :
     y_n_answer = True
     valid_input = True
     return y_n_answer
  
   elif prompt ==  "no" or prompt == "n" :
     y_n_answer = False
     valid_input = True
     return y_n_answer
   else:
     print("Please enter Yes or No: ")

stats_prompt = y_n_prompt("roll for your stats")

#Auto Rolled
if stats_prompt == True: 
  print("Ok let's see what you get...")
  time.sleep(2)
  agility = stat_roll()
  print(f"  Your agility is {agility}.")
 
  time.sleep(Roll_Timer)
  charisma = stat_roll()
  print(f"  Your charisma is {charisma}.")
  
  time.sleep(Roll_Timer)
  intellect = stat_roll()
  print(f"  Your intellect is {intellect}.")
  
  time.sleep(Roll_Timer)
  perception = stat_roll()
  print(f"  Your perception is {perception}.")
  
  time.sleep(Roll_Timer)
  strength = stat_roll()
  print(f"  Your strength is {strength}.")

#Manually Entered
elif stats_prompt == False:
  print("Ok let's get started. All stats must be from 3 to 18.")
  
  time.sleep(input_timer)
  #agility =int(input("Enter your Agility stat: "))
  
  agility = get_and_validate_stat("agility")

  time.sleep(input_timer)
  #charisma =int(input("Enter your Charisma stat: "))
  
  charisma = get_and_validate_stat("charisma")

  time.sleep(input_timer)
  #intellect =int(input("Enter your Intellect stat: "))

  intellect = get_and_validate_stat("intellect")
 
  time.sleep(input_timer)
  #perception =int(input("Enter your Perception stat: "))

  perception = get_and_validate_stat("perception")
 
  time.sleep(input_timer)
  #strength =int(input("Enter your Strength stat: "))
  strength = get_and_validate_stat("strength")

else:
  print("Please enter Yes or No.")

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

time.sleep(Section_Timer) 

#Kin selection Roll 1d12: 1-9 human, 10 halfling, 11 dwarf, 12 elf.

kin_prompt = y_n_prompt("roll for you kin")

if kin_prompt == True:
  print("Great let's see what you are...")
  time.sleep(Roll_Timer)
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
  proper_kin = False
  while proper_kin == False:
    kin = input("Are you a huamn, halfling, dwarf, or elf?: ")
    if kin == "huamn":
      proper_kin = True
    elif kin == "halfling":
      proper_kin = True
    elif kin == "dwarf":
      proper_kin = True
    elif kin == "elf":
      proper_kin = True
    else:
      print("That is not a recognized kin.")      
time.sleep(Section_Timer)

background_prompt = y_n_prompt('roll for your backgrounds')

#Human
#halfling
#dwarf
#elf

time.sleep(Section_Timer)

description_prompt = y_n_prompt('roll for your descriptors')

#Attitude
#hair
#face
#eyes
#body
#quirk

time.sleep(Section_Timer)

money_prompt = y_n_prompt('roll for your starting coins')

if money_prompt == True:
  starting_coins = (random.randint(1,6)+random.randint(1,6)+random.randint(1,6))*10
  print(f"You have {starting_coins} coins for your journey.")
else:
    starting_coins_check = False
    while starting_coins_check == False:
      starting_coins = int(input("Enter number of coins between 30 and 180: "))
      if starting_coins < 30:
        print("You aren't that poor.")
      elif starting_coins > 180:
        print("No one that rich is going adventuring.")
      else:
        starting_coins_check = True

time.sleep(Section_Timer)

max_hp = stat_rating_calc(strength) + 10

def heavy(str):
  if stat_rating_calc(strength) >= 0:
    max_heavy = stat_rating_calc(strength) + 1
  else:
    max_heavy = 1

  return max_heavy

max_heavy = heavy(stat_rating_calc(strength))

name_prompt = y_n_prompt('roll for a random name')

time.sleep(Section_Timer)

print("""
Ok let's get this all together...
""")

print(f"""
Your stats are the following:
  Agility:    {agility} | {stat_rating_calc(agility)}
  Charisma:   {charisma} | {stat_rating_calc(charisma)}
  Intellect:  {intellect} | {stat_rating_calc(intellect)}
  Perception: {perception} | {stat_rating_calc(perception)}
  Strength:   {strength} | {stat_rating_calc(strength)}

Your maximum HP is {max_hp}.

You can carry at most {max_heavy} heavy item(s) unaided.

You hail from the {kin} lands and left with {starting_coins} coins in your pocket.

""")

print(f"Good Hunting {kin}!")