print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# used
prompt1 = 'You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n'

# used
prompt2 = 'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'

#used
prompt3 = "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"

# used
prompt4 = "It's a room full of fire. Game Over."

# used
prompt5 = "You found the treasure! You Win!"

# used
prompt6 = "You enter a room of beasts. Game Over."

# used
prompt7 = "You chose a door that doesn't exist. Game Over."

# used
prompt8 = "You get attacked by an angry trout. Game Over."

# used
prompt9 = "You fell into a hole. Game Over."

# used
prompt10 = "Invalid response, you are dead."

answer = input(prompt1)
answer = answer.lower()

if answer == 'left':
  answer = input(prompt2)
  answer = answer.lower()
  if answer == 'wait':
    answer = input(prompt3)
    answer = answer.lower()
    if answer == 'red':
      print(prompt4)
    elif answer == 'yellow':
      print(prompt6)
    elif answer == 'blue':
      print(prompt5)
    else:
      print(prompt7)
  elif answer == 'swim':
    print(prompt8)
  else:
    print(prompt10)
elif answer == 'right':
  print(prompt9)
else:
  print(prompt10)