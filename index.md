```{python}
import random
import time

#time between random rolls base .75
Roll_Timer = 0

#time between input requests base .75
input_timer = 0

#time between sections base 2
Section_Timer = 0

#time spent pondering base 2
Thought_Timer = 0


def stat_roll():
    return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)


def get_and_validate_stat(stat):
    valid_stat = False

    while valid_stat == False:
        stat_value = int(input(f"  Enter your {stat} stat: "))
        if stat_value < 3:
            print("  That is too low. Please enter a number between 3 and 18.")
        elif stat_value > 18:
            print(
                "  That is too high. Please enter a number between 3 and 18.")
        else:
            valid_stat = True

    return stat_value


#Input promp is "Do you want to {text}? Yes or No: ""
def y_n_prompt(text):
    valid_input = False

    while valid_input == False:
        prompt = input(f"Do you want to {text}? Yes or No: ")
        prompt = prompt.lower()

        if prompt == "yes" or prompt == "y":
            y_n_answer = True
            valid_input = True
            return y_n_answer

        elif prompt == "no" or prompt == "n":
            y_n_answer = False
            valid_input = True
            return y_n_answer
        else:
            print("Please enter Yes or No: ")


stats_prompt = y_n_prompt("roll for your stats")

#Auto Rolled
if stats_prompt == True:
    print("Ok let's see what you get...")
    time.sleep(Thought_Timer)
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
    kin_roll = random.randint(1, 12)
    if kin_roll <= 9:
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
else:
    proper_kin = False
    while proper_kin == False:
        kin = input("Are you a human, halfling, dwarf, or elf?: ")
        if kin == "human":
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

if background_prompt == True:

    if kin == "human":
        background_roll = random.randint(0, 99)
        from human_info import human_backgrounds_names
        from human_info import human_backgrounds
        background_name = human_backgrounds_names[background_roll]
        background_description = human_backgrounds[background_name]

    elif kin == "halfling":
        background_roll = random.randint(0, 7)
        from halfling_info import halfling_backgrounds
        from halfling_info import halfling_backgrounds_names
        background_name = halfling_backgrounds_names[background_roll]
        background_description = halfling_backgrounds[background_name]

    elif kin == "dwarf":
        background_roll = random.randint(0, 7)
        from dwarf_info import dwarf_backgrounds
        from dwarf_info import dwarf_backgrounds_names
        background_name = dwarf_backgrounds_names[background_roll]
        background_description = dwarf_backgrounds[background_name]

    elif kin == "elf":
        background_roll = random.randint(0, 7)
        from elf_info import elf_backgrounds
        from elf_info import elf_backgrounds_names
        background_name = elf_backgrounds_names[background_roll]
        background_description = elf_backgrounds[background_name]

    display_background_roll = background_roll + 1
    print(
        f"You rolled a {display_background_roll}. {background_name}. {background_description}"
    )
else:
    proper_background = False
    if kin == "human":

        from human_info import human_backgrounds_names
        from human_info import human_backgrounds
        while proper_background == False:
            try:
                background_name = input(
                    "Please type in the name of the background (remove any ' in the name): "
                )
                background_description = human_backgrounds[background_name]
            except KeyError:
                print("That isn't a recognized background.")
            else:
                proper_background = True

    elif kin == "halfling":

        from halfling_info import halfling_backgrounds

        while proper_background == False:
            try:
                background_name = input(
                    f"Please type in the name of a {kin} background: ")
                background_description = halfling_backgrounds[background_name]
            except KeyError:
                print("That isn't a recognized background.")
            else:
                proper_background = True

    elif kin == "dwarf":
        background_roll = random.randint(0, 7)
        from dwarf_info import dwarf_backgrounds

        while proper_background == False:
            try:
                background_name = input(
                    f"Please type in the name of a {kin} background: ")
                background_description = dwarf_backgrounds[background_name]
            except KeyError:
                print("That isn't a recognized background.")
            else:
                proper_background = True

    elif kin == "elf":

        from elf_info import elf_backgrounds

        while proper_background == False:
            try:
                background_name = input(
                    f"Please type in the name of an {kin} background: ")
                background_description = elf_backgrounds[background_name]
            except KeyError:
                print("That isn't a recognized background.")
            else:
                proper_background = True

time.sleep(Section_Timer)

attitude = ""
hair = ""
face = ""
eyes = ""
body = ""
quirk = ""

description_prompt = y_n_prompt('roll for your descriptors')

if description_prompt == True:
  if kin == "human":
    attitude_roll = int(random.randint(0,99))
    from human_info import human_attitude
    attitude = human_attitude[attitude_roll]

    hair_roll = int(random.randint(0,19))
    from human_info import human_hair
    hair = human_hair[hair_roll]

    face_roll = int(random.randint(0,19))
    from human_info import human_face
    face = human_face[face_roll]

    eyes_roll = int(random.randint(0,19))
    from human_info import human_eyes
    eyes = human_eyes[eyes_roll]

    body_roll = int(random.randint(0,19))
    from human_info import human_body
    body = human_body[body_roll]

    quirk_roll = int(random.randint(0,99))
    from human_info import human_quirk
    quirk = human_quirk[quirk_roll]

  elif kin == "elf":
    attitude = "elf"
    hair = "elf"
    face = "elf"
    eyes = "elf"
    body = "elf"
    quirk = "elf"
  
  elif kin == "dwarf":
    attitude = "dwarf"
    hair = "dwarf"
    face = "dwarf"
    eyes = "dwarf"
    body = "dwarf"
    quirk = "dwarf"
  
  elif kin == "halfling":
    attitude = "halfling"
    hair = "halfling"
    face = "halfling"
    eyes = "halfling"
    body = "halfling"
    quirk = "halfling"

else:
  attitude = input("Your attitude could be decribed as: ")
  hair = input("Your hair is: ")
  face = input("Your face is: ")
  eyes = input("Your eyes are: ")
  body = input("Your frame is: ")
  quirk = input("Your defining personality trait is your: ")

time.sleep(Section_Timer)

money_prompt = y_n_prompt('roll for your starting coins')

if money_prompt == True:
    starting_coins = (random.randint(1, 6) + random.randint(1, 6) +
                      random.randint(1, 6)) * 10
    print(f"You have {starting_coins} coins for your journey.")
else:
    starting_coins_check = False
    while starting_coins_check == False:
        starting_coins = int(
            input("Enter number of coins between 30 and 180: "))
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

if name_prompt == True:
    if kin == "human":
        from human_info import human_names
        name_roll = random.randint(0, 99)
        name = human_names[name_roll]

    if kin == "dwarf":
        from dwarf_info import dwarf_names
        name_roll = random.randint(0, 7)
        name = dwarf_names[name_roll]

    if kin == "elf":
        from elf_info import elf_names
        name_roll = random.randint(0, 7)
        name = elf_names[name_roll]

    if kin == "halfling":
        from halfling_info import halfling_names
        name_roll = random.randint(0, 7)
        name = halfling_names[name_roll]

else:
    name = input("So what is your name?: ")

time.sleep(Section_Timer)

print("""
Ok let's get this all together...
""")

time.sleep(Thought_Timer)

character_profile = (f"""
Your stats are the following:
  Agility:    {agility} | {stat_rating_calc(agility)}
  Charisma:   {charisma} | {stat_rating_calc(charisma)}
  Intellect:  {intellect} | {stat_rating_calc(intellect)}
  Perception: {perception} | {stat_rating_calc(perception)}
  Strength:   {strength} | {stat_rating_calc(strength)}

Your maximum HP is {max_hp}.

You can carry at most {max_heavy} heavy item(s) unaided.

Your name is {name}. You hail from the {kin} lands 

{attitude}
{hair}
{face}
{eyes}
{body}
{quirk}

You were a {background_name}. {background_description}



With {starting_coins} coins in your pocket you set off on your journey.

""")

print(f"Good Hunting {kin}!")


```