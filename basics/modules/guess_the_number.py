from random import randrange as ra

def play_guess_the_number():
  print("Please enter the minimum value:")
  i=int(input())
  print("Please enter the maximum value:")
  j=int(input())
  while(j<=i):
    print("The maximum cannot be lower than or equal to the minimum. Please choose a different maximum:")
    j=int(input())
  n=ra(i,j,1)
  print("I am thinking of a number between {} and {}. Can you guess what it is?".format(i,j))
  while(1==1):
    i=int(input())
    if n==i:
      print("Congratulations! You guessed my number!")
      break
    elif n>i:
      print("Your guess is too low!")
    else:
      print("You guess is too high!")
    print("Try again:")
def run():
  play_guess_the_number()