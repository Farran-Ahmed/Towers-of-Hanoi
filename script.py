from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks += [left_stack, middle_stack, right_stack]

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disks, 0, -1):
  left_stack.push(disk)

num_optmial_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optmial_moves))
#Get User Input
def get_imput():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:

    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter, name))
    user_imput = input("")

    if user_imput in choices:
      for i in range(len(stacks)):
        if user_imput == choices[i]:
          return stacks[i]
#Play the Game
num_user_moves = 0

while(right_stack.get_size() != num_disks):

  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
    
  while True:
    print("\nWhich stack do you want to move from?\n")
    form_stack = get_imput()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_imput()
    if form_stack.get_size() == 0:
      print("\n\nInvalid Move. Try Again")
    elif to_stack.get_size() == 0 or form_stack.peek() < to_stack.peek():
      disk = form_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")


print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optmial_moves))
