print("Welcome to Treasure Island!")

first_fork = input("You come to a fork in the road! Do you choose LEFT or RIGHT? ")

if first_fork == "LEFT":
    lake_choice = input("You make your way down a winding road until you reach a large, gloomy lake. You see a boat in the distance making its way toward you. Do you WAIT for it or try to SWIM? ")
    if lake_choice == "WAIT":
        door_choice = input("You chose to wait for the boat and it safely escorts you across the treacherous lake. You find yourself in front of three doors: one RED, one BLUE, one YELLOW. Which door contains the treasure? You must decide! ")
        if door_choice == "YELLOW":
            print("You open the yellow door, and as you do you are almost blinded by the reflection of light on a HUGE PILE OF GOLD AND TREASURES. You WIN! Congratulations hero.")
        elif door_choice == "RED":
            print("As you open the red door fire blasts from the room scorching you to the bone! You die! Try again.")
        elif door_choice == "BLUE":
            print("As you open the blue door you feel a cold wind grip your bones. Each step you take into the room slows you more and more until you find yourself unable to move. Slowly your entire body is encased in ice! You die! Try again.")
        else:
            print("Please choose RED, BLUE, or YELLOW.")
    elif lake_choice == "SWIM":
        print("You try to swim across the lake but as you do, shadowy hands grab at your lags and drag you under. You drown! Try again.")    
    else:
        print("Please choose WAIT or SWIM.")
elif first_fork == "RIGHT":
    print("You make your way down a dark, shadowy lane. You can't see too much. After a while you trip and fall off a cliff! You died! Try again.")
else:
    print("Please choose LEFT or RIGHT.")